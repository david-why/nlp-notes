from __future__ import annotations

import typing as t
from collections import defaultdict

import numpy as np

if t.TYPE_CHECKING:
    import typing_extensions as te

__all__ = ['MarkovClassifier']

FloatArray = np.ndarray[t.Any, np.dtype[np.floating]]


class MarkovModel:
    def __init__(self, vocab, tokenizer: t.Callable[[str], t.List[str]] = str.split):
        M = len(vocab) + 1
        self.A: np.ndarray = np.ones((M, M), np.float64)
        self.pi: np.ndarray = np.ones((M,), np.float64)
        self.vocab: defaultdict[str, int] = vocab
        self.tokenizer = tokenizer

    def fit(self, documents: t.Iterable[str]) -> te.Self:
        """
        Train the Markov model with the documents.
        :param documents: The documents to learn the A and pi matrices from.
        :returns: self
        """
        M = len(self.vocab) + 1
        self.A = np.ones((M, M), np.float64)
        self.pi = np.ones((M,), np.float64)
        count = 0
        for document in documents:
            generator = filter(None, self.tokenizer(document))
            first = next(generator)
            last = self.vocab[first]
            self.pi[last] += 1
            for token in generator:
                idx = self.vocab[token]
                self.A[last, idx] += 1
                count += 1
                last = idx
        self.A = np.log(self.A / (np.array([np.sum(self.A, axis=1)]).T + M))
        self.pi = np.log(self.pi / (np.sum(self.pi) + M))
        return self

    def predict(self, documents: t.Collection[str]) -> FloatArray:
        """
        Calculate the relative probability of the document existing.
        :param document: The documents to predict.
        :returns: The log probabilities of each document.
        """
        array = np.empty(len(documents), np.float64)
        for i, document in enumerate(documents):
            array[i] = self._predict(document)
        return array

    def _predict(self, document: str) -> float:
        assert self.A is not None and self.pi is not None, 'Please fit first'
        generator = filter(None, self.tokenizer(document))
        first = next(generator)
        last = self.vocab.get(first, len(self.vocab) - 1)
        result = self.pi[last]
        for token in generator:
            idx = self.vocab.get(token, len(self.vocab) - 1)
            result += self.A[last, idx]
            last = idx
        return result


class MarkovClassifier:
    def __init__(self, tokenizer: t.Callable[[str], t.List[str]] = str.split):
        """
        Initialize the classifier.
        :param tokenizer: The tokenizer, defaults to str.split.
        """
        self.models: t.Optional[t.List[MarkovModel]] = None
        self.priors: t.Optional[FloatArray] = None
        self.vocab: defaultdict[str, int] = defaultdict(lambda: len(self.vocab))
        self.reverse: t.Dict[int, str] = {}
        self.tokenizer = tokenizer

    def fit(self, documents: t.Iterable[str], X: t.Iterable[int]) -> te.Self:
        """
        Train all of the Markov models with the documents.
        :param documents: The documents to learn the A and pi matrices from.
        :param X: The expected classes of the documents.
        :returns: self
        """
        self.vocab.clear()
        self.reverse.clear()
        for document in documents:
            for token in filter(None, self.tokenizer(document)):
                self.reverse[self.vocab[token]] = token
        self.models = [
            MarkovModel(self.vocab, self.tokenizer) for _ in range(max(X) + 1)
        ]
        for i, model in enumerate(self.models):
            model.fit([d for d, c in zip(documents, X) if c == i])
        self.priors = np.zeros(len(self.models))
        for clazz in X:
            self.priors[clazz] += 1
        self.priors = np.log(self.priors / sum(self.priors))
        return self

    def predict(self, documents: t.Collection[str]) -> FloatArray:
        """
        Predict each document's class with the Markov models.
        :param documents: The documents to classify.
        :returns: An array of the same length of documents, each representing
        the index of the class.
        """
        assert self.priors is not None and self.models is not None, 'Please fit first'
        predictions = np.array(
            [m.predict(documents) + self.priors[i] for i, m in enumerate(self.models)]
        )
        return (-predictions).argsort(axis=0)[0]

    def score(self, documents: t.Collection[str], X: t.Iterable[int]) -> np.floating:
        """
        Score the performance of the classifier with the documents.
        :param documents: The documents to score.
        :param X: The expected classes of the documents.
        :returns: The percentage of documents classified correctly, from 0 to 1.
        """
        return np.mean(self.predict(documents) == X)


if __name__ == '__main__':
    import string

    from sklearn.model_selection import train_test_split

    FILES = ['files/edgar_allan_poe.txt', 'files/robert_frost.txt']
    REMOVE_PUNC = str.maketrans('', '', string.punctuation)

    inputs = []
    labels = []
    for i, file in enumerate(FILES):
        for line in open(file):
            line = line.strip()
            if line:
                inputs.append(line.lower().translate(REMOVE_PUNC))
                labels.append(i)
    inputs_train, inputs_test, Xtrain, Xtest = train_test_split(
        inputs, labels, random_state=1234
    )
    classifier = MarkovClassifier().fit(inputs_train, Xtrain)
    print(classifier.vocab)
    print('vocab size:', len(classifier.vocab))
    print('train score:', classifier.score(inputs_train, Xtrain))
    print('test score:', classifier.score(inputs_test, Xtest))

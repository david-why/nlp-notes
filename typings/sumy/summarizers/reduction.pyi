import typing as t
from collections import defaultdict
from ..models.dom import ObjectDocumentModel, Sentence
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class ReductionSummarizer(AbstractSummarizer):
    @property
    def stop_words(self) -> frozenset[str]: ...
    @stop_words.setter
    def stop_words(self, words: t.Iterable[str]) -> None: ...
    def rate_sentences(self, document: ObjectDocumentModel) -> defaultdict[Sentence, float]: ...

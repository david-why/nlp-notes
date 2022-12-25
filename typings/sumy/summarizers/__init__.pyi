import typing as t
from ..models.dom import ObjectDocumentModel, Sentence

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class AbstractSummarizer(object):
    def __init__(self, stemmer: t.Callable[[str], str] = ...) -> None: ...
    def __call__(
        self, document: ObjectDocumentModel, sentences_count: _CountType
    ) -> tuple[Sentence, ...]: ...
    def stem_word(self, word: str) -> str: ...
    @staticmethod
    def normalize_word(word: str) -> str: ...
    def rate_sentences(
        self, document: ObjectDocumentModel
    ) -> dict[Sentence, float]: ...

del t

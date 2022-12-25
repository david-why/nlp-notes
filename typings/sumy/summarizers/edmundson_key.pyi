import typing as t
from ..models.dom import ObjectDocumentModel, Sentence
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class EdmundsonKeyMethod(AbstractSummarizer):
    def __init__(
        self, stemmer: t.Callable[[str], str], bonus_words: t.Container[str]
    ) -> None: ...
    def __call__(
        self, document: ObjectDocumentModel, sentences_count: _CountType, weight: float
    ) -> tuple[Sentence, ...]: ...
    def rate_sentences(
        self, document: ObjectDocumentModel, weight: float = 0.5
    ) -> dict[Sentence, float]: ...

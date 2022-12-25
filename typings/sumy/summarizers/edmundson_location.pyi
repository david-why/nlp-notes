import typing as t
from ..models.dom import ObjectDocumentModel, Sentence
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class EdmundsonLocationMethod(AbstractSummarizer):
    def __init__(
        self, stemmer: t.Callable[[str], str], null_words: t.Container[str]
    ) -> None: ...
    def __call__(
        self,
        document: ObjectDocumentModel,
        sentences_count: _CountType,
        w_h: float,
        w_p1: float,
        w_p2: float,
        w_s1: float,
        w_s2: float,
    ) -> tuple[Sentence, ...]: ...
    def rate_sentences(
        self,
        document: ObjectDocumentModel,
        w_h: float = 1,
        w_p1: float = 1,
        w_p2: float = 1,
        w_s1: float = 1,
        w_s2: float = 1,
    ) -> dict[Sentence, float]: ...

import typing as t
from ..models.dom import ObjectDocumentModel, Sentence
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class EdmundsonSummarizer(AbstractSummarizer):
    def __init__(
        self,
        stemmer: t.Callable[[str], str] = ...,
        cue_weight: float = 1.0,
        key_weight: float = 1.0,
        title_weight: float = 1.0,
        location_weight: float = 1.0,
    ) -> None: ...
    @property
    def bonus_words(self) -> frozenset[str]: ...
    @bonus_words.setter
    def bonus_words(self, collection: t.Iterable[str]) -> None: ...
    @property
    def stigma_words(self) -> frozenset[str]: ...
    @stigma_words.setter
    def stigma_words(self, collection: t.Iterable[str]) -> None: ...
    @property
    def null_words(self) -> frozenset[str]: ...
    @null_words.setter
    def null_words(self, collection: t.Iterable[str]) -> None: ...
    def cue_method(
        self,
        document: ObjectDocumentModel,
        sentences_count: _CountType,
        bonus_word_value: float = 1,
        stigma_word_value: float = 1,
    ) -> tuple[Sentence, ...]: ...
    def key_method(
        self,
        document: ObjectDocumentModel,
        sentences_count: _CountType,
        weight: float = 0.5,
    ) -> tuple[Sentence, ...]: ...
    def title_method(
        self, document: ObjectDocumentModel, sentences_count: _CountType
    ) -> tuple[Sentence, ...]: ...
    def location_method(
        self,
        document: ObjectDocumentModel,
        sentences_count: _CountType,
        w_h: float = 1,
        w_p1: float = 1,
        w_p2: float = 1,
        w_s1: float = 1,
        w_s2: float = 1,
    ) -> tuple[Sentence, ...]: ...

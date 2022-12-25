import typing as t
from ..models.dom import ObjectDocumentModel, Sentence
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class EdmundsonCueMethod(AbstractSummarizer):
    def __init__(
        self,
        stemmer: t.Callable[[str], str],
        bonus_words: t.Container[str],
        stigma_words: t.Container[str],
    ) -> None: ...
    def __call__(
        self,
        document: ObjectDocumentModel,
        sentences_count: _CountType,
        bonus_word_weight: float,
        stigma_word_weight: float,
    ) -> tuple[Sentence, ...]: ...
    def rate_sentences(
        self,
        document: ObjectDocumentModel,
        bonus_word_weight: float = 1,
        stigma_word_weight: float = 1,
    ) -> dict[Sentence, float]: ...

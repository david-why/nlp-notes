import typing as t
from ..models.dom import Sentence
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class LuhnSummarizer(AbstractSummarizer):
    max_gap_size: int
    significant_percentage: float
    @property
    def stop_words(self) -> frozenset[str]: ...
    @stop_words.setter
    def stop_words(self, words: t.Iterable[str]) -> None: ...
    def rate_sentence(
        self, sentence: Sentence, significant_stems: t.Container[str]
    ) -> float: ...

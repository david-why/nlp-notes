import typing as t
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class LsaSummarizer(AbstractSummarizer):
    MIN_DIMENSIONS: int
    REDUCTION_RATIO: float
    @property
    def stop_words(self) -> frozenset[str]: ...
    @stop_words.setter
    def stop_words(self, words: t.Iterable[str]) -> None: ...

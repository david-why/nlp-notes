import typing as t
import numpy
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class TextRankSummarizer(AbstractSummarizer):
    epsilon: float
    damping: float
    @property
    def stop_words(self) -> frozenset[str]: ...
    @stop_words.setter
    def stop_words(self, words: t.Iterable[str]) -> None: ...
    @staticmethod
    def power_method(
        matrix: numpy.ndarray, epsilon: float
    ) -> numpy.ndarray[t.Any, numpy.dtype[numpy.float64]]: ...

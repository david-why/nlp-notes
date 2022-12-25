import typing as t
import numpy
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class LexRankSummarizer(AbstractSummarizer):
    threshold: float
    epsilon: float
    @property
    def stop_words(self) -> frozenset[str]: ...
    @stop_words.setter
    def stop_words(self, words: t.Iterable[str]) -> None: ...
    @staticmethod
    def cosine_similarity(
        sentence1: t.Iterable[str],
        sentence2: t.Iterable[str],
        tf1: dict[str, float],
        tf2: dict[str, float],
        idf_metrics: dict[str, float],
    ) -> float: ...
    @staticmethod
    def power_method(
        matrix: numpy.ndarray, epsilon: float
    ) -> numpy.ndarray[t.Any, numpy.dtype[numpy.float64]]: ...

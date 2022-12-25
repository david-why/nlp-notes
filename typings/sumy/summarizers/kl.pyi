import typing as t
from ..models.dom import Sentence
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class KLSummarizer(AbstractSummarizer):
    stop_words: frozenset[str]
    def compute_tf(self, sentences: t.Iterable[Sentence]) -> dict[str, float]: ...

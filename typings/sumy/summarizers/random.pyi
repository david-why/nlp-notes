import typing as t
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class RandomSummarizer(AbstractSummarizer):
    pass

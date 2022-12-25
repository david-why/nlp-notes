import typing as t
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class EdmundsonTitleMethod(AbstractSummarizer):
    def __init__(self, stemmer: t.Callable[[str], str], null_words: t.Container[str]) -> None: ...

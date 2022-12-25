import typing as t
from ..models.dom import ObjectDocumentModel, Sentence
from . import AbstractSummarizer

_CountType = t.Callable[[t.Sequence[str]], t.Sequence[str]] | str | int

class SumBasicSummarizer(AbstractSummarizer):
    @property
    def stop_words(self) -> frozenset[str]: ...
    @stop_words.setter
    def stop_words(self, words: t.Iterable[str]) -> None: ...

import os
import typing as t
import typing_extensions as te
from .parser import DocumentParser
from ..models.dom import ObjectDocumentModel

__all__ = ['HtmlParser']

class _SupportsStr(t.Protocol):
    def __str__(self) -> str: ...

class _WordSentenceTokenizer(t.Protocol):
    def to_sentences(self, paragraph: _SupportsStr) -> t.Sequence[str]: ...
    def to_words(self, sentence: _SupportsStr) -> t.Sequence[str]: ...

class HtmlParser(DocumentParser):
    SIGNIFICANT_TAGS: tuple[str, ...]
    @classmethod
    def from_string(
        cls, string: str | bytes, url: str, tokenizer: _WordSentenceTokenizer
    ) -> te.Self: ...
    @classmethod
    def from_file(
        cls, file_path: os.PathLike, url: str, tokenizer: _WordSentenceTokenizer
    ) -> te.Self: ...
    @classmethod
    def from_url(cls, url: str, tokenizer: _WordSentenceTokenizer) -> te.Self: ...
    def __init__(
        self,
        html_content: str | bytes,
        tokenizer: _WordSentenceTokenizer,
        url: t.Optional[str] = None,
    ) -> None: ...
    @property
    def significant_words(self) -> tuple[str, ...]: ...
    @property
    def stigma_words(self) -> tuple[str, ...]: ...
    @property
    def document(self) -> ObjectDocumentModel: ...

del t

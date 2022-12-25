import typing as t

__all__ = ['Tokenizer']

class _Tokenizer(t.Protocol):
    def tokenize(self, text: str) -> list[str]: ...

class _SupportsStr(t.Protocol):
    def __str__(self) -> str: ...

class Tokenizer(object):
    LANGUAGE_ALIASES: dict[str, str]
    LANGUAGE_EXTRA_ABREVS: dict[str, list[str]]
    SPECIAL_SENTENCE_TOKENIZERS: dict[str, _Tokenizer]
    SPECIAL_WORD_TOKENIZERS: dict[str, _Tokenizer]
    def __init__(self, language: str) -> None: ...
    @property
    def language(self) -> str: ...
    def to_sentences(self, paragraph: _SupportsStr) -> tuple[str, ...]: ...
    def to_words(self, sentence: _SupportsStr) -> tuple[str, ...]: ...

del t

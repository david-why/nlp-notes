import typing as t

__all__ = ['null_stemmer', 'Stemmer']

class _SupportsStr(t.Protocol):
    def __str__(self) -> str: ...

def null_stemmer(object: _SupportsStr) -> str: ...

class Stemmer(object):
    SPECIAL_STEMMERS = dict[str, t.Callable[[str], str]]
    def __init__(self, language: str) -> None: ...
    def __call__(self, word: str) -> str: ...

del t

import re

WORD_PATTERN: re.Pattern[str]

def stem_word(word: str, aggressive: bool = False) -> str: ...

import typing as t
from ..models.dom import Sentence

def rouge_n(
    evaluated_sentences: t.Sequence[Sentence],
    reference_sentences: t.Sequence[Sentence],
    n: int = 2,
) -> float: ...
def rouge_1(
    evaluated_sentences: t.Sequence[Sentence], reference_sentences: t.Sequence[Sentence]
) -> float: ...
def rouge_2(
    evaluated_sentences: t.Sequence[Sentence], reference_sentences: t.Sequence[Sentence]
) -> float: ...
def rouge_l_sentence_level(
    evaluated_sentences: t.Sequence[Sentence], reference_sentences: t.Sequence[Sentence]
) -> float: ...
def rouge_l_summary_level(
    evaluated_sentences: t.Sequence[Sentence], reference_sentences: t.Sequence[Sentence]
) -> float: ...

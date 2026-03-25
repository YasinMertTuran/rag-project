from typing import List, TYPE_CHECKING
from .Hit import Hit
import re

if TYPE_CHECKING:
    from .Chunk import Chunk

def _normalize(text: str) -> str:
    if not text:
        return ''
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", ' ', text)
    return text


def retrieve_keywords(terms: List[str], corpus: List['Chunk']) -> List[Hit]:
    hits: List[Hit] = []
    norm_terms = [_normalize(t) for t in terms if t]
    for chunk in corpus:
        score = 0
        content = _normalize(chunk.text or '')
        content_words = [w for w in content.split() if w]

        for term in norm_terms:
            if not term:
                continue
            if term in content:
                score += 2
                continue
            matched = False
            for w in content_words:
                if w.startswith(term) or term.startswith(w):
                    score += 1
                    matched = True
                    break
            if matched:
                continue

        if score > 0:
            hits.append(Hit(chunk, score))

    hits.sort(key=lambda h: h.score, reverse=True)
    return hits[:5]


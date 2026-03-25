from typing import List, TYPE_CHECKING
from .Hit import Hit

if TYPE_CHECKING:
    from .Chunk import Chunk

class VectorRetriever:
    def _get_stub_vector(self, text: str) -> List[float]:
        """Ödev gereği gerçek AI modeli yerine sabit sayılar (stub) üretir[cite: 49]."""
        if not text: return [0.0, 0.0, 0.0]
        # Basit bir matematiksel hesaplama ile metni 3 boyutlu sayıya çevirir
        v1 = len(text) % 10 / 10.0
        v2 = text.count(' ') % 10 / 10.0
        v3 = sum(ord(c) for c in text[:3]) % 10 / 10.0
        return [v1, v2, v3]

    def _cosine_similarity(self, v1: List[float], v2: List[float]) -> float:
        """İki sayı dizisi arasındaki benzerliği ölçer[cite: 168]."""
        dot_product = sum(a * b for a, b in zip(v1, v2))
        mag1 = sum(a**2 for a in v1)**0.5
        mag2 = sum(b**2 for b in v2)**0.5
        return dot_product / (mag1 * mag2) if (mag1 * mag2) > 0 else 0.0

    def retrieve(self, terms: List[str], corpus: List['Chunk']) -> List[Hit]:

        query_text = " ".join(terms)
        query_vec = self._get_stub_vector(query_text)
        hits = []

        for chunk in corpus:
            chunk_vec = self._get_stub_vector(chunk.text)
            sim = self._cosine_similarity(query_vec, chunk_vec)
            # Benzerlik skoru 0'dan büyükse listeye ekle
            if sim > 0:
                hits.append(Hit(chunk, int(sim * 100)))
        
        # Skorlara göre büyükten küçüğe sırala ve ilk 5'i dön
        hits.sort(key=lambda h: h.score, reverse=True)
        return hits[:5]
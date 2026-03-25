from typing import List
from .Hit import Hit

class JaccardReranker:
    def rerank(self, terms: List[str], hits: List[Hit]) -> List[Hit]:
        if not hits:
            return []
            
        query_set = set(t.lower() for t in terms if t)
        for hit in hits:
            text_words = set(hit.chunk.text.lower().split())
            intersection = query_set.intersection(text_words)
            union = query_set.union(text_words)
            
            # Jaccard Skoru hesapla
            score = len(intersection) / len(union) if union else 0.0
            # Skoru 0-100 arasına çek (Iteration 2 standartlarına göre)
            hit.score = int(score * 100)
        
        # HOCANIN İSTEDİĞİ KRİTİK SIRALAMA (Determinism):
        # 1. Skora göre azalan (-h.score)
        # 2. docId'ye göre artan (h.chunk.docId)
        # 3. id'ye göre artan (h.chunk.id)
        hits.sort(key=lambda h: (-h.score, h.chunk.docId, h.chunk.id)) 
        return hits
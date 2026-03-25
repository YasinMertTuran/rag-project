from typing import List


class SimpleReranker:
    def rerank(self, terms: List[str], hits: List['Hit']) -> List['Hit']:
        mutable = list(hits)
        lower_terms = [t.lower() for t in terms]
        for hit in mutable:
            title = (hit.chunk.title or '').lower()
            text = (hit.chunk.text or '').lower()
            score = 0
            for term in lower_terms:
                if term and term in text:
                    score += 1
                if term and term in title:
                    score += 3
            query = ' '.join(lower_terms)
            if query and query in text:
                score += 5
            hit.score = score
        mutable.sort(key=lambda h: h.score, reverse=True)
        return mutable


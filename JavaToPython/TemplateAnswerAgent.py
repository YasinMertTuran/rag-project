from typing import List
import re


class TemplateAnswerAgent:
    def generate_answer(self, question: str, terms: List[str], hits: List['Hit']) -> str:
        if not hits:
            return "No information found for the given question."
        best = hits[0]
        chunk = best.chunk
        best_sentence = self.find_best_sentence(chunk.text, terms)
        return f"{best_sentence}\n--------------------------------------------------\nSource: {chunk.title} | Document: {chunk.docId}"

    def find_best_sentence(self, text: str, terms: List[str]) -> str:
        if not text:
            return "No relevant sentence found."
        sentences = re.split(r'(?<=[.!?])\s+', text)
        best_sentence = sentences[0]
        best_score = -1
        lower_terms = [t.lower() for t in terms if t]
        for s in sentences:
            score = 0
            lower = s.lower()
            for term in lower_terms:
                if term and term in lower:
                    score += 1
            if score > best_score:
                best_score = score
                best_sentence = s
        return best_sentence


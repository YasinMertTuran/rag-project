from typing import List
import re

class TemplateAnswerAgent:
    MAX_ANSWER_CHARS = 350

    def generate_answer(self, question: str, terms: List[str], hits: List) -> str:
        if not hits:
            return "No information found for the given question."

        best = hits[0]
        chunk = best.chunk

        # En alakalı cümleyi bulur
        best_sentence = self.find_best_sentence(chunk.text, terms)

        # Citation (Atıf) kısmını hazırlar
        # Not: JSON şemana göre 'id' veya 'chunkId' olduğundan emin ol.
        citation = f"{chunk.docId}:{chunk.chunkId if hasattr(chunk, 'chunkId') else chunk.id}"
        title = (chunk.title or "").strip()

        # Başlık çok uzunsa 80 karakterde keser (Terminal düzeni için)
        if len(title) > 80:
            title = title[:77].rstrip() + "..."

        # Tek satır profesyonel çıktı formatı
        if title:
            return f"{best_sentence} (Source: {citation} | {title})"
        return f"{best_sentence} (Source: {citation})"

    def find_best_sentence(self, text: str, terms: List[str]) -> str:
        if not text:
            return "No relevant sentence found."

        # Cümleleri bölme mantığı (Nokta, Ünlem, Soru, Alt Satır, Noktalı Virgül)
        parts = re.split(r'(?<=[.!?])\s+|[\n;]+', text)
        parts = [p.strip() for p in parts if p and p.strip()]

        if not parts:
            return "No relevant sentence found."

        lower_terms = [t.lower() for t in terms if t]
        best_sentence = parts[0]
        best_score = -1

        # Kelime eşleşmesine göre en iyi cümleyi seçme
        for s in parts:
            lower = s.lower()
            score = 0
            for term in lower_terms:
                if term and term in lower:
                    score += 1
            if score > best_score:
                best_score = score
                best_sentence = s

        return self._clip(best_sentence, self.MAX_ANSWER_CHARS)

    def _clip(self, s: str, max_chars: int) -> str:
        """Cevabı belirlenen limitin altında tutar."""
        s = (s or "").strip()
        if len(s) <= max_chars:
            return s
        cut = s[:max_chars].rstrip()
        last_space = cut.rfind(" ")
        if last_space > (max_chars * 0.7):
            cut = cut[:last_space].rstrip()
        return cut + "..."
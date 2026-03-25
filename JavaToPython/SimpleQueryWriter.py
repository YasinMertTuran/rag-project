from typing import List, Optional
import re

from .Intent import Intent


class SimpleQueryWriter:
    def __init__(self):
        self.stop_words = self._create_stop_words()
        self.intent_boosters = self._create_intent_boosters()

    def write(self, question: str, intent: Optional[Intent]) -> List[str]:
        if not question:
            return []
        clear = re.sub(r'[^a-z0-9üçğıöş\s]', ' ', question.lower())
        words = [w for w in clear.split() if len(w) > 2 and w not in self.stop_words]

        boosters = self.intent_boosters.get(intent, []) if intent is not None else []
        for b in boosters:
            if b not in words:
                words.append(b)
        return words

    def _create_stop_words(self):
        return set(["ve", "ile", "bu", "şu", "bir", "nedir", "nasıl", "hangi", "için", "ama", "fakat", "lakin", "mi", "mı", "mu", "mü"])

    def _create_intent_boosters(self):
        boosters = {}
        boosters[Intent.STAFF_LOOKUP] = ["öğretim", "hoca", "ofis", "telefon", "öğretmen", "akademisyen"]
        boosters[Intent.COURSE] = ["ders", "kredi", "önkoşul", "dönem", "müfredat"]
        boosters[Intent.POLICY_FAQ] = ["yönerge", "kural", "sınav", "not", "madde"]
        boosters[Intent.REGISTRATION] = ["kayıt", "başvuru", "öğrenci", "kabul", "belge", "ücret"]
        return boosters


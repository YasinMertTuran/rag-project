from .Intent import Intent


class RuleIntentDetector:
    def detect(self, question: str) -> Intent:
        q = (question or '').lower()
        for intent in Intent:
            if intent == Intent.UNKNOWN:
                continue
            for keyword in intent.get_keywords():
                if keyword and keyword in q:
                    return intent
        return Intent.UNKNOWN


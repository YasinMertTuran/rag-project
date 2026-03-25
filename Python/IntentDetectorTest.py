from .IntentDetector import IntentDetector
from .RuleIntentDetector import RuleIntentDetector
from .Intent import Intent


def expect(question: str, expected: Intent, detector: IntentDetector):
    found = detector.detect(question)
    if found == expected:
        print(f"PASS: {question} -> {found}")
    else:
        print(f"FAIL: {question} -> {found} (expected {expected})")


if __name__ == "__main__":
    detector = RuleIntentDetector()
    expect("Kayıt ve hoca bilgilerini nereden alabilirim?", Intent.REGISTRATION, detector)
    expect("Hoca e-posta ve yönergeler nerede?", Intent.STAFF_LOOKUP, detector)
    expect("Yönerge ve ders ile ilgili soru", Intent.POLICY_FAQ, detector)
    expect("Bu tamamen bilgilendirici bir cümle.", Intent.UNKNOWN, detector)


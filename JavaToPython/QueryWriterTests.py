from .SimpleQueryWriter import SimpleQueryWriter


def test_stopword_removal(writer: SimpleQueryWriter):
    q = "Bu ders nedir ve nasıl alınır?"
    terms = writer.write(q, None)
    stops = ["bu", "nedir", "nasıl", "ve"]
    passed = all(s not in terms for s in stops)
    print(("PASS" if passed else "FAIL") + f": Stopword removal -> {terms}")


def test_intent_boosters(writer: SimpleQueryWriter):
    q = "Bilgi"
    course_terms = writer.write(q, None)
    has_booster = "ders" in course_terms or "kredi" in course_terms
    print(("PASS" if has_booster else "FAIL") + f": Course -> {course_terms}")


def test_stemming_behavior(writer: SimpleQueryWriter):
    q = "Öğretmenleri bulmak istiyorum"
    terms = writer.write(q, None)
    contains_inflected = any("öğretmen" in t for t in terms)
    contains_booster_base = "öğretmen" in terms or "öğretim" in terms
    passed = contains_inflected and contains_booster_base
    print(("PASS" if passed else "FAIL") + f": terms={terms}")


if __name__ == "__main__":
    writer = SimpleQueryWriter()
    test_stopword_removal(writer)
    test_intent_boosters(writer)
    test_stemming_behavior(writer)


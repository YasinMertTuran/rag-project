from .SimpleReranker import SimpleReranker


def test_title_boost(reranker: SimpleReranker):
    a = Chunk("d1", 0, "OOD", "adı geçmiyor burada")
    b = Chunk("d2", 0, "Başlık", "burada OOD geçiyor")

    hits = [Hit(a, 0), Hit(b, 0)]
    terms = ["OOD", "3063"]
    out = reranker.rerank(terms, hits)
    passed = out[0].chunk == a
    print(("PASS" if passed else "FAIL") + f": Title -> top={out[0].chunk.title}")


def test_text_matches(reranker: SimpleReranker):
    a = Chunk("d3", 0, "T1", "OOD OOD OOD")
    b = Chunk("d4", 0, "T2", "OOD")
    hits = [Hit(a, 0), Hit(b, 0)]
    terms = ["OOD"]
    out = reranker.rerank(terms, hits)
    passed = out[0].chunk == a
    print(("PASS" if passed else "FAIL") + f": Text -> top text={out[0].chunk.text}")


def test_exact_phrase_boost(reranker: SimpleReranker):
    a = Chunk("d5", 0, "T1", "OOD projesi yapıyorum")
    b = Chunk("d6", 0, "T2", "O O D projesi yapıyorum")
    hits = [Hit(a, 0), Hit(b, 0)]
    terms = ["OOD", "projesi"]
    out = reranker.rerank(terms, hits)
    passed = out[0].chunk == a
    print(("PASS" if passed else "FAIL") + f": Exact phrase -> top text={out[0].chunk.text}")


if __name__ == "__main__":
    from .Chunk import Chunk
    from .Hit import Hit

    r = SimpleReranker()
    test_title_boost(r)
    test_text_matches(r)
    test_exact_phrase_boost(r)


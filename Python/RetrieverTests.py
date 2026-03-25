from .Chunk import Chunk
from .Hit import Hit
from .KeywordRetriever import retrieve_keywords


def test_ordering_and_topk():
    a = Chunk("doc1", 0, "A", "murat can murat")
    b = Chunk("doc2", 0, "B", "murat")
    c = Chunk("doc3", 0, "C", "murat can murat can")

    corpus = [a, b, c]
    terms = ["murat", "can"]

    hits = retrieve_keywords(terms, corpus)

    pass_size = len(hits) == 3
    last_is_b = hits[2].chunk == b
    top_two_have_score2 = hits[0].score == 2 and hits[1].score == 2

    print(("PASS" if (pass_size and last_is_b and top_two_have_score2) else "FAIL") + f": size={len(hits)}, order={hits[0].chunk.docId},{hits[1].chunk.docId},{hits[2].chunk.docId}, scores={hits[0].score},{hits[1].score},{hits[2].score}")


if __name__ == "__main__":
    test_ordering_and_topk()


from .JsonCorpusLoader import load_corpus
from .Chunk import Chunk
import json


def run_test():
    temp_path = "src/mu/cse/rag/clean/test_corpus.json"
    data = [
        {"docId": "doc-A", "chunkId": 0, "title": "T1", "text": "Hello world"},
        {"docId": "doc-B", "chunkId": 1, "title": "T2", "text": "Goodbye\nfriend"}
    ]
    with open(temp_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

    corpus = load_corpus(temp_path)
    passed = len(corpus) == 2 and corpus[0].docId == 'doc-A' and corpus[1].docId == 'doc-B'
    print(("PASS" if passed else "FAIL") + f": JsonCorpusLoader -> loaded={len(corpus)}")


if __name__ == "__main__":
    run_test()


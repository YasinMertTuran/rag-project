import json
from typing import List

from .Chunk import Chunk


def load_corpus(file_path: str) -> List[Chunk]:
    """Load corpus from a JSON array file where each item has docId, chunkId, title, text."""
    corpus: List[Chunk] = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for obj in data:
                doc_id = obj.get('docId')
                chunk_id = obj.get('chunkId')
                title = obj.get('title')
                text = obj.get('text')
                if doc_id is not None and chunk_id is not None:
                    try:
                        corpus.append(Chunk(doc_id, int(chunk_id), title or '', text or ''))
                    except Exception:
                        continue
    except Exception:
        return []
    return corpus


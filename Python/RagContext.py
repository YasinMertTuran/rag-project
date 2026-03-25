from typing import List, Optional, Any

class RagContext:
    def __init__(self):
        # Kullanıcının sorduğu ham soru
        self.question: str = ""
        
        # Soru analizinden gelen niyet (Intent)
        self.intent: Optional[str] = None
        
        # Arama motoru için hazırlanan anahtar kelimeler listesi
        self.terms: List[str] = []
        
        # Retrieval (Arama) aşamasından dönen ilk sonuçlar listesi
        self.hits: List[Any] = []
        
        # Reranking (Yeniden Sıralama) sonrası filtrelenmiş final sonuçlar
        self.finalHits: List[Any] = []
        
        # Agent tarafından üretilen final cevap metni
        self.answerText: str = ""
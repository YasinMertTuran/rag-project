from .TemplateAnswerAgent import TemplateAnswerAgent
from .Hit import Hit
from .Chunk import Chunk

def test_agent():
    agent = TemplateAnswerAgent()
    
    # Sahte veri oluşturarak agent'ı deniyoruz
    test_chunk = Chunk(
        docId="yonetmelik.txt",
        chunkId="42",
        title="Başarı Notu Değerlendirmesi Hakkında Uzun Bir Başlık Örneği",
        text="Öğrencinin bir dersteki başarı durumu harf notuyla belirlenir. FF notu alan öğrenciler başarısız sayılır; mazeret sınavına giremezler."
    )
    
    test_hit = Hit(chunk=test_chunk, score=0.95)
    
    # Test parametreleri
    question = "Hangi notu alanlar başarısız sayılır?"
    terms = ["notu", "başarısız"]
    hits = [test_hit]

    print("\n--- TEMPLATE AGENT TEST ---")
    answer = agent.generate_answer(question, terms, hits)
    print(f"Cevap: {answer}")
    print("---------------------------\n")

if __name__ == "__main__":
    test_agent()
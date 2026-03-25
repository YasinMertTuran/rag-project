package mu.cse.rag.clean;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RerankerTests {
    public static void main(String[] args) {
        SimpleReranker reranker = new SimpleReranker();

        testTitleBoost(reranker);
        testTextMatches(reranker);
        testExactPhraseBoost(reranker);
    }

    private static void testTitleBoost(Reranker reranker) { //Title match should boost score
        Chunk a = new Chunk("d1", 0, "OOD", "adı geçmiyor burada");
        Chunk b = new Chunk("d2", 0, "Başlık", "burada OOD geçiyor");

        List<Hit> hits = new ArrayList<>();
        hits.add(new Hit(a, 0));
        hits.add(new Hit(b, 0));
        
        List<String> terms = Arrays.asList("OOD", "3063");
        List<Hit> out = reranker.rerank(terms, hits);
        boolean pass = out.get(0).chunk == a; //Title boost should make 'a' top when query has both terms
        System.out.println((pass ? "PASS" : "FAIL") + ": Title -> top=" + out.get(0).chunk.title);
    }

    private static void testTextMatches(Reranker reranker) { //More than one occurence in text should increase score more
        Chunk a = new Chunk("d3", 0, "T1", "OOD OOD OOD");
        Chunk b = new Chunk("d4", 0, "T2", "OOD");

        List<Hit> hits = new ArrayList<>();
        hits.add(new Hit(a, 0));
        hits.add(new Hit(b, 0));

        List<String> terms = Arrays.asList("OOD");
        List<Hit> out = reranker.rerank(terms, hits);

        boolean pass = out.get(0).chunk == a;
        System.out.println((pass ? "PASS" : "FAIL") + ": Text -> top text=" + out.get(0).chunk.text);
    }

    private static void testExactPhraseBoost(Reranker reranker) { //Exact phrase should get an even more boost
        Chunk a = new Chunk("d5", 0, "T1", "OOD projesi yapıyorum");
        Chunk b = new Chunk("d6", 0, "T2", "O O D projesi yapıyorum");

        List<Hit> hits = new ArrayList<>();
        hits.add(new Hit(a, 0));
        hits.add(new Hit(b, 0));

        List<String> terms = Arrays.asList("OOD", "projesi");
        List<Hit> out = reranker.rerank(terms, hits);

        boolean pass = out.get(0).chunk == a;
        System.out.println((pass ? "PASS" : "FAIL") + ": Exact phrase -> top text=" + out.get(0).chunk.text);
    }
}

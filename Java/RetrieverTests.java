package mu.cse.rag.clean;

import java.util.Arrays;
import java.util.List;

public class RetrieverTests {
    public static void main(String[] args) {
        testOrderingAndTopK();
    }

    private static void testOrderingAndTopK() {
        Chunk a = new Chunk("doc1", 0, "A", "murat can murat");
        Chunk b = new Chunk("doc2", 0, "B", "murat" );
        Chunk c = new Chunk("doc3", 0, "C", "murat can murat can");

        List<Chunk> corpus = Arrays.asList(a, b, c);
        List<String> terms = Arrays.asList("murat", "can");

        KeywordRetriever retriever = new KeywordRetriever();
        List<Hit> hits = retriever.retrieve(terms, corpus);

        boolean passSize = hits.size() == 3;
        boolean lastIsB = hits.get(2).chunk == b;
        boolean topTwoHaveScore2 = hits.get(0).score == 2 && hits.get(1).score == 2;

        System.out.println(((passSize && lastIsB && topTwoHaveScore2) ? "PASS" : "FAIL") + ": size=" + hits.size() + ", order=" + hits.get(0).chunk.docId + "," + hits.get(1).chunk.docId + "," + hits.get(2).chunk.docId + ", scores=" + hits.get(0).score + "," + hits.get(1).score + "," + hits.get(2).score);
    }
}

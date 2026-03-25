package mu.cse.rag.clean;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class JsonCorpusLoaderTest {
    public static void main(String[] args) {
        String tempPath = "src\\mu\\cse\\rag\\clean\\test_corpus.json";
        String json = "[\n" +
                "{\"docId\":\"doc-A\",\"chunkId\":0,\"title\":\"T1\",\"text\":\"Hello world\"},\n" +
                "{\"docId\":\"doc-B\",\"chunkId\":1,\"title\":\"T2\",\"text\":\"Goodbye\\nfriend\"}\n" +
                "]";
        try (FileWriter w = new FileWriter(tempPath)) {
            w.write(json);
        } catch (IOException e) {
            System.err.println("Failed to write test corpus: " + e.getMessage());
            return;
        }

        List<Chunk> corpus = JsonCorpusLoader.loadCorpus(tempPath);
        boolean pass = corpus.size() == 2 && "doc-A".equals(corpus.get(0).docId) && "doc-B".equals(corpus.get(1).docId);
        System.out.println((pass ? "PASS" : "FAIL") + ": JsonCorpusLoader -> loaded=" + corpus.size());
    }
}

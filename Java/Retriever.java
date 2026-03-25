package mu.cse.rag.clean;
import java.util.List;

public interface Retriever {
    List<Hit> retrieve(List<String> terms, List<Chunk> corpus);
}
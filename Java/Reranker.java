package mu.cse.rag.clean;
import java.util.List;

public interface Reranker {
    List<Hit> rerank(List<String> terms, List<Hit> hits);
}
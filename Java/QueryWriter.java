package mu.cse.rag.clean;

import java.util.List;

public interface QueryWriter {
    List<String> write(String question, Intent intent);
}
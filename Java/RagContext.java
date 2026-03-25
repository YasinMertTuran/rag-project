package mu.cse.rag.clean;

import java.util.List;

public class RagContext { //Holds all context data for RAG process
    public String question;
    public Intent intent;
    public List<String> terms;
    public List<Hit> hits;
    public List<Hit> finalHits;
    public String answerText;
}

package mu.cse.rag.clean;

public class Hit {
    public Chunk chunk;
    public int score;
    
    public Hit(Chunk chunk, int score) {
        this.chunk = chunk;
        this.score = score;
    }
}
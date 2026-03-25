package mu.cse.rag.clean;

public class Chunk {
    final String docId; //Document ID
    final int id; //Chunk ID
    final String title; //Chunk title
    final String text; //Chunk text

    public Chunk(String docId, int id, String title, String text) {
        this.docId = docId;
        this.id = id;
        this.title = title;
        this.text = text;
    }
}
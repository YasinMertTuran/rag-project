package mu.cse.rag.clean;

import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;

public class JsonlTraceSink implements TraceListener {

    private final String filePath; //JSONL file path

    public JsonlTraceSink(String filePath) {
        this.filePath = filePath;
    }

    @Override
    @SuppressWarnings("CallToPrintStackTrace")
    public void onEvent(TraceEvent event) { //Overrides the method
        try (FileWriter filewriter = new FileWriter(filePath, true)) {
            String json = String.format(
                    "{\"stage\":\"%s\",\"input\":\"%s\",\"output\":\"%s\",\"durationMs\":%d,\"timestamp\":\"%s\"}",
                    escape(event.stage), //Replaces double quotes with \"
                    escape(event.inputSummary), //Replaces double quotes with \"
                    escape(event.outputSummary), //Replaces double quotes with \"
                    event.durationMs, //Time taken
                    LocalDateTime.now().toString()
            );
            filewriter.write(json + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private String escape(String s) {
        return s.replace("\"", "\\\"");
    }
}

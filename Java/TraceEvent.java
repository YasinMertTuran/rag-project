package mu.cse.rag.clean;

public class TraceEvent {
    public final String stage;
    public final String inputSummary;
    public final String outputSummary;
    public final long durationMs;

    public TraceEvent(String stage, String inputSummary, String outputSummary, long durationMs) {
        this.stage = stage;
        this.inputSummary = inputSummary;
        this.outputSummary = outputSummary;
        this.durationMs = durationMs;
    }
}

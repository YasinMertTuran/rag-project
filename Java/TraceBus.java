package mu.cse.rag.clean;

import java.util.ArrayList;
import java.util.List;

public class TraceBus {

    private final List<TraceListener> listeners = new ArrayList<>();

    public void addListener(TraceListener listener) {
        listeners.add(listener);
    }

    public void publish(TraceEvent event) {
        for (TraceListener l : listeners) {
            l.onEvent(event);
        }
    }
}

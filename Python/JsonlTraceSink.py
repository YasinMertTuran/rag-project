import json
from datetime import datetime
from typing import Any

from .TraceListener import TraceListener
from .TraceEvent import TraceEvent


class JsonlTraceSink(TraceListener):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def on_event(self, event: TraceEvent) -> None:
        record: dict[str, Any] = {
            "stage": event.stage,
            "input": event.inputSummary,
            "output": event.outputSummary,
            "durationMs": event.durationMs,
            "timestamp": datetime.now().isoformat(),
        }
        try:
            with open(self.file_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        except Exception:
            pass


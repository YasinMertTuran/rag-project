from dataclasses import dataclass


@dataclass
class TraceEvent:
    stage: str
    inputSummary: str
    outputSummary: str
    durationMs: int


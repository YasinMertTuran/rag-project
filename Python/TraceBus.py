from typing import List


class TraceBus:
    def __init__(self):
        self.listeners: List = []

    def add_listener(self, listener) -> None:
        self.listeners.append(listener)

    def publish(self, event) -> None:
        for l in self.listeners:
            if hasattr(l, 'on_event'):
                l.on_event(event)
            elif hasattr(l, 'onEvent'):
                l.onEvent(event)


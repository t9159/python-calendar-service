from typing import List
from .event import Event

class Person:
    def __init__(self, name: str):
        self.name = name
        self.events: List[Event] = []

    def add_event(self, event: Event):
        self.events.append(event)

    def __repr__(self):
        return f"Person(name='{self.name}', events_count={len(self.events)})"
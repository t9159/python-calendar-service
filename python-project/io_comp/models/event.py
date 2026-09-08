from .time_slot import TimeSlot

class Event:
    def __init__(self, subject: str, time_slot: TimeSlot):
        self.subject = subject
        self.time_slot = time_slot

    def __repr__(self):
        return f"Event(subject='{self.subject}', time_slot={self.time_slot})"
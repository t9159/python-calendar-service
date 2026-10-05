from datetime import time
from exceptions import InvalidTimeSlotError

class TimeSlot:
    def __init__(self, start_time: time, end_time: time):
        if start_time >= end_time:
            raise InvalidTimeSlotError(f"End time {end_time} must be after start time {start_time}")
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"
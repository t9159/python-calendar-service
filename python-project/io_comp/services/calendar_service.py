from typing import List
from datetime import time, datetime, timedelta
from exceptions import InvalidTimeSlotError
from repositories.base_repository import BaseRepository
from config import DAY_START, DAY_END
from typing import Tuple

class CalendarService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def find_available_slots(self, person_list: List[str], event_duration: timedelta) -> List[Tuple[time, time]]:
        """
            Returns a list of possible start times for a meeting of a requested duration
            for the specified persons, taking into account their existing schedules
            and the system's operating hours.

            :param persons: A list of participant names to check availability for.
            :param duration: The required duration for the meeting (as a timedelta).
            :return: A list of time objects representing the available start times.
        """
        if not person_list:
            return []

        base_date = datetime.today().date()
        day_start_dt = datetime.combine(base_date, DAY_START)
        day_end_dt = datetime.combine(base_date, DAY_END)
        total_day_duration = day_end_dt - day_start_dt

        if event_duration > total_day_duration:
            raise InvalidTimeSlotError("The requested meeting duration exceeds the total operating hours of the day.")

        all_persons = self.repository.get_persons()
        normalized_person_list = [name.strip().lower() for name in person_list]
        relevant_persons = [p for p in all_persons if p.name.lower() in normalized_person_list]

        busy_intervals = []
        for person in relevant_persons:
            for event in person.events:
                busy_intervals.append((event.time_slot.start_time, event.time_slot.end_time))

        busy_dt_intervals = [
            (datetime.combine(base_date, s), datetime.combine(base_date, e))
            for s, e in busy_intervals
        ]

        busy_dt_intervals.sort(key=lambda x: x[0])

        merged_busy = []
        for start, end in busy_dt_intervals:
            if not merged_busy:
                merged_busy.append((start, end))
            else:
                last_start, last_end = merged_busy[-1]
                if start <= last_end:
                    merged_busy[-1] = (last_start, max(last_end, end))
                else:
                    merged_busy.append((start, end))

        free_slots = []
        current_time = day_start_dt

        for start, end in merged_busy:
            if current_time < start:
                free_slots.append((current_time, start))
            current_time = max(current_time, end)

        if current_time < day_end_dt:
            free_slots.append((current_time, day_end_dt))

        available_slots = []
        for start, end in free_slots:
            if (end - start) >= event_duration:
                latest_start = end - event_duration
                available_slots.append((start.time(), latest_start.time()))

        return available_slots
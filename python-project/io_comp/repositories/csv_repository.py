import csv
from datetime import datetime
from typing import List

from repositories.base_repository import BaseRepository
from models.event import Event
from models.person import Person
from models.time_slot import TimeSlot

class CsvRepository(BaseRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_persons(self) -> List[Person]:
        persons_dict = {}

        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or len(row) < 4:
                    continue

                person_name = row[0].strip()
                subject = row[1].strip()
                start_time = datetime.strptime(row[2].strip(), "%H:%M").time()
                end_time = datetime.strptime(row[3].strip(), "%H:%M").time()

                time_slot = TimeSlot(start_time, end_time)
                event = Event(subject, time_slot)

                if person_name not in persons_dict:
                    persons_dict[person_name] = Person(person_name)

                persons_dict[person_name].add_event(event)

        return list(persons_dict.values())
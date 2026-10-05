from datetime import time, timedelta
from io_comp.models.person import Person
from io_comp.models.event import Event
from io_comp.models.time_slot import TimeSlot
from io_comp.services.calendar_service import CalendarService
from io_comp.repositories.base_repository import BaseRepository
import pytest
from datetime import timedelta
from io_comp.exceptions import InvalidTimeSlotError
@pytest.fixture
def calendar_service():
    repo = MockRepository()
    return CalendarService(repo)

class MockRepository(BaseRepository):

    def get_persons(self):
        person = Person("Alice")
        person.add_event(Event("Meeting", TimeSlot(time(8, 0), time(9, 30))))
        return [person]


def test_find_available_slots_basic():
    repo = MockRepository()
    service = CalendarService(repo)

    slots = service.find_available_slots(["Alice"], timedelta(minutes=60))

    assert time(9, 30) in slots


def test_no_available_slots_if_day_full():
    class FullDayRepository(BaseRepository):
        def get_persons(self):
            person = Person("Bob")
            person.add_event(Event("All Day", TimeSlot(time(7, 0), time(19, 0))))
            return [person]

    service = CalendarService(FullDayRepository())
    slots = service.find_available_slots(["Bob"], timedelta(minutes=60))

    assert len(slots) == 0


def test_exceeding_day_duration_raises_error(calendar_service):
    """
    Test that requesting a meeting duration longer than the entire working day
    raises an InvalidTimeSlotError custom exception.
    """
    participants = ["Alice"]
    too_long_duration = timedelta(hours=12,minutes=1)

    with pytest.raises(InvalidTimeSlotError):
        calendar_service.find_available_slots(participants, too_long_duration)


def test_non_existent_participant_handling(calendar_service):
    """
    Test that searching for a participant who does not exist in the repository
    handles gracefully and returns a list.
    """
    participants = ["NonExistentUser"]
    duration = timedelta(minutes=60)

    slots = calendar_service.find_available_slots(participants, duration)

    assert isinstance(slots, list)


def test_multiple_persons_overlapping_schedules():
    class MultiPersonRepo(BaseRepository):
        def get_persons(self):
            alice = Person("Alice")
            alice.add_event(Event("Meeting 1", TimeSlot(time(9, 0), time(10, 0))))
            alice.add_event(Event("Meeting 2", TimeSlot(time(13, 0), time(14, 0))))

            bob = Person("Bob")
            bob.add_event(Event("Meeting 3", TimeSlot(time(9, 30), time(11, 0))))
            bob.add_event(Event("Meeting 4", TimeSlot(time(15, 0), time(16, 0))))

            return [alice, bob]

    service = CalendarService(MultiPersonRepo())
    slots = service.find_available_slots(["Alice", "Bob"], timedelta(minutes=60))
    expected_starts = [time(7, 0), time(11, 0), time(14, 0), time(16, 0)]

    assert slots == expected_starts
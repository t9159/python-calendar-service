from datetime import time
from io_comp.models.time_slot import TimeSlot
from io_comp.models.event import Event
from io_comp.models.person import Person

def test_time_slot_repr():
    slot = TimeSlot(time(8, 0), time(9, 30))
    assert repr(slot) == "08:00 - 09:30"

def test_event_creation():
    slot = TimeSlot(time(10, 0), time(11, 0))
    event = Event("Meeting", slot)
    assert event.subject == "Meeting"
    assert event.time_slot == slot

def test_person_add_event():
    person = Person("Alice")
    slot = TimeSlot(time(13, 0), time(14, 0))
    event = Event("Lunch", slot)
    person.add_event(event)
    assert len(person.events) == 1
    assert person.events[0] == event
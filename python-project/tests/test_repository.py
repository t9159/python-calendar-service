from datetime import time
from io_comp.repositories.csv_repository import CsvRepository


def test_csv_repository_parsing(tmp_path):
    csv_file = tmp_path / "calendar.csv"
    csv_file.write_text('Alice,"Morning meeting",08:00,09:30\nAlice,"Lunch",13:00,14:00\n', encoding='utf-8')

    repo = CsvRepository(str(csv_file))
    persons = repo.get_persons()

    assert len(persons) == 1
    assert persons[0].name == "Alice"
    assert len(persons[0].events) == 2
    assert persons[0].events[0].subject == "Morning meeting"
    assert persons[0].events[0].time_slot.start_time == time(8, 0)
    assert persons[0].events[0].time_slot.end_time == time(9, 30)
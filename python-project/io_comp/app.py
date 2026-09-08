import os
from datetime import timedelta
from services.calendar_service import CalendarService
from repositories.csv_repository import CsvRepository


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'resources', 'calendar.csv')

    repository = CsvRepository(file_path)
    service = CalendarService(repository)

    # Prompt the user for participant names
    names_input = input("Who is in the meeting? (Enter names separated by commas, e.g., Alice, Jack): ")
    person_list = [name.strip() for name in names_input.split(",") if name.strip()]

    # Prompt the user for meeting duration in minutes
    try:
        minutes = int(input("Meeting duration in minutes: "))
        event_duration = timedelta(minutes=minutes)
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Execute the search and handle potential custom exceptions
    try:
        available_slots = service.find_available_slots(person_list, event_duration)

        for start_t, end_t in available_slots:
            if start_t == end_t:
                print(f"Starting Time of available slots: {start_t.strftime('%H:%M')}")
            else:
                print(f"Starting Time of available slots: {start_t.strftime('%H:%M')} - {end_t.strftime('%H:%M')}")

    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()
# Comp Calendar Application

A clean, modular Python application designed to find available meeting time slots across multiple participant schedules within a given workday.

## Project Structure

```text
python-project/
├── io_comp/                 # Main application package
│   ├── models/              # Domain models (Person, Event, TimeSlot)
│   ├── repositories/        # Data access layer (CSV repository)
│   ├── services/            # Business logic (CalendarService)
│   ├── app.py               # Application entry point
│   ├── config.py            # System configuration & operating hours
│   └── exceptions.py        # Custom exceptions
├── tests/                   # Unit tests (pytest)
├── resources/               # Data resources (calendar.csv)
├── requirements.txt         # Python dependencies
├── setup.py                 # Package configuration
└── README.md

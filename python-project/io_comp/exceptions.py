class CalendarError(Exception):
    """
    Base exception class for all custom errors in the calendar system.
    """
    pass


class InvalidTimeSlotError(CalendarError):
    """
    Raised when a time slot or meeting duration is invalid or exceeds boundaries.
    """
    pass
from enum import Enum

class ReservationStatus(Enum):
    SCHEDULED = 1
    INPROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4
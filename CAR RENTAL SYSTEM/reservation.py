from datetime import datetime
from user import User
from product.vehicle import Vehicle
from reservation_status import ReservationStatus
from reservation_type import ReservationType

class Reservation:
    def __init__(self, reservation_id: int = None, user: User = None, vehicle: Vehicle = None):
        self.reservation_id = reservation_id
        self.user = user
        self.vehicle = vehicle
        self.booking_date = datetime.now()  # Use current date and time for booking
        self.date_booked_from = None
        self.date_booked_to = None
        self.from_time_stamp = None
        self.to_time_stamp = None
        self.pick_up_location = None
        self.drop_location = None
        self.reservation_type = None
        self.reservation_status = None

    def create_reserve(self, user: User, vehicle: Vehicle) -> int:
        # Generate new reservation ID (simulate in a simple way)
        self.reservation_id = 1423
        self.user = user
        self.vehicle = vehicle
        self.reservation_type = ReservationType.DAILY
        self.reservation_status = ReservationStatus.SCHEDULED

        return self.reservation_id
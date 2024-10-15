from show import Show
from payment import Payment

class Booking:
    def __init__(self, booking_id: int = None, show: Show = None,payment : Payment=None,booked_seats:list=[]):
        self.booking_id = booking_id
        self.show = show
        self.payment = payment
        self.booked_seats = booked_seats
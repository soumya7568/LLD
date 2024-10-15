from enums import SeatType

class Seat:
    def __init__(self, seat_number, seat_type : SeatType, row) -> None:
        self._seat_id = seat_number
        self._seat_type = seat_type
        self._row = row

    @property
    def seat_id(self):
        return self._seat_id

    @seat_id.setter
    def seat_id(self, value):
        self._seat_id = value

    @property
    def seat_type(self):
        return self._seat_type

    @seat_type.setter
    def seat_type(self, value):
        self._seat_type = value

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        self._row = value
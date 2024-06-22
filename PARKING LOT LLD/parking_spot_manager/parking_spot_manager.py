class ParkingSpotManager:
    def __init__(self, spots):
        self.spots = spots

    def get_available_spot(self):
        for spot in self.spots:
            if not spot.get_is_occupied():
                return spot
        return None  # Or raise an exception if no spots are available


class TwoWheelerManager(ParkingSpotManager):
    pass


class FourWheelerManager(ParkingSpotManager):
    pass

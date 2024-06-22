from parking_spot_manager.parking_spot import TwoWheelerParkingSpot,FoorWheelerParkingSpot
from parking_spot_manager.factory import ParkingSpotManagerFactory

class ParkingLot:
    def __init__(self):
        self.two_wheeler_spots = [TwoWheelerParkingSpot(f"2W-{i}", price=10 + (i % 5)) for i in range(1, 601)]
        self.four_wheeler_spots = [FoorWheelerParkingSpot(f"4W-{i}", price=20 + (i % 10)) for i in range(1, 401)]
        self.manager_factory = ParkingSpotManagerFactory(self.two_wheeler_spots, self.four_wheeler_spots)

    def get_manager_factory(self):
        return self.manager_factory

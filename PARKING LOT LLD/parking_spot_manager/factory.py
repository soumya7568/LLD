from parking_spot_manager.parking_spot_manager import TwoWheelerManager,FourWheelerManager
class ParkingSpotManagerFactory:
    def __init__(self, two_wheeler_spots, four_wheeler_spots):
        self.two_wheeler_manager = TwoWheelerManager(two_wheeler_spots)
        self.four_wheeler_manager = FourWheelerManager(four_wheeler_spots)

    def get_manager(self, vehicle):
        if vehicle.get_type() == "TwoWheeler":
            return self.two_wheeler_manager
        else:
            return self.four_wheeler_manager

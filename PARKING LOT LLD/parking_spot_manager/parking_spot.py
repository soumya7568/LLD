class ParkingSpot:
    def __init__(self, spot_id, price=10):
        self.spot_id = spot_id
        self.is_occupied = False
        self.vehicle = None
        self.price = price

    def get_spot_id(self):
        return self.spot_id

    def get_is_occupied(self):
        return self.is_occupied

    def get_vehicle(self):
        return self.vehicle

    def get_price(self):
        return self.price

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.is_occupied = True

    def remove_vehicle(self):
        self.vehicle = None
        self.is_occupied = False

class TwoWheelerParkingSpot(ParkingSpot):
    pass

class FoorWheelerParkingSpot(ParkingSpot):
    pass

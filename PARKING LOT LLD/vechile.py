class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def get_type(self):
        return self.vehicle_type

    def get_license_plate(self):
        return self.license_plate
    

class TwoWheeler(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "TwoWheeler")


class FourWheeler(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "FourWheeler")
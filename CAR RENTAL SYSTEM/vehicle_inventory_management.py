from typing import List
from product.vehicle import Vehicle

class VehicleInventoryManagement:
    def __init__(self, vehicles: List[Vehicle]):
        self.vehicles = vehicles

    def get_vehicles(self) -> List[Vehicle]:
        # In Python, typically, no need to explicitly filter unless more complex logic is involved
        return self.vehicles

    def set_vehicles(self, vehicles: List[Vehicle]):
        self.vehicles = vehicles
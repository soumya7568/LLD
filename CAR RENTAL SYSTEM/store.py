from vehicle_inventory_management import VehicleInventoryManagement
from product.vehicle import Vehicle
from user import User
from reservation import Reservation

class Store:
    def __init__(self, store_id: int, store_location: str):
        self.store_id = store_id
        self.store_location = store_location
        self.inventory_management = None
        self.reservations = []

    def get_vehicles(self, vehicle_type: str) -> list:
        return self.inventory_management.get_vehicles(vehicle_type)

    def set_vehicles(self, vehicles: list):
        self.inventory_management = VehicleInventoryManagement(vehicles)

    def create_reservation(self, vehicle: Vehicle, user: User) -> Reservation:
        reservation = Reservation(len(self.reservations) + 1, user, vehicle)
        self.reservations.append(reservation)
        return reservation

    def complete_reservation(self, reservation_id: int) -> bool:
        return True
# Importing Store and User classes (simplified for demonstration)
from store import Store
from user import User
from location import Location  # Assuming Location class is defined

# Define VehicleRentalSystem class
class VehicleRentalSystem:
    def __init__(self, stores: list, users: list):
        self.store_list = stores
        self.user_list = users

    def get_store(self, location: Location) -> Store:
        # Simulated method to find a store based on location (simplified)
        # In a real application, this could involve searching or filtering based on location details
        return self.store_list[0]  # Returning the first store for demonstration

    def add_user(self, user: User):
        self.user_list.append(user)

    def remove_user(self, user: User):
        if user in self.user_list:
            self.user_list.remove(user)

    def add_store(self, store: Store):
        self.store_list.append(store)

    def remove_store(self, store: Store):
        if store in self.store_list:
            self.store_list.remove(store)
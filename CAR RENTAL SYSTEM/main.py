from user import User  
from location import Location 
from store import Store 
from bill import Bill  
from payment import Payment 
from product.car import Car 
from product.vehicle_type import VehicleType
from vehicel_rental_system import VehicleRentalSystem


def main():
    users = add_users()
    vehicles = add_vehicles()
    stores = add_stores(vehicles)

    rental_system = VehicleRentalSystem(stores, users)

    # 0. User comes
    user = users[0]

    # 1. User searches store based on location
    location = Location(pincode=403012, city="Bangalore", state="Karnataka", country="India")
    store = rental_system.get_store(location)

    # 2. Get all vehicles user is interested in (based on different filters)
    store_vehicles = store.get_vehicles(VehicleType.CAR)

    # 3. Reserving a particular vehicle
    reservation = store.create_reservation(store_vehicles[0], user)

    # 4. Generate the bill
    bill = Bill(reservation)

    # 5. Make payment
    payment = Payment()
    payment.pay_bill(bill)

    # 6. Trip completed, submit the vehicle and close the reservation
    store.complete_reservation(reservation.reservation_id)

def add_vehicles():
    vehicles = []

    # Adding vehicles (assuming Car class with necessary methods)
    vehicle1 = Car()
    vehicle1.set_vehicle_id(1)
    vehicle1.set_vehicle_type(VehicleType.CAR)

    vehicle2 = Car()
    vehicle2.set_vehicle_id(2)
    vehicle2.set_vehicle_type(VehicleType.CAR)

    vehicles.append(vehicle1)
    vehicles.append(vehicle2)

    return vehicles

def add_users():
    users = []

    # Adding users (assuming User class with necessary methods)
    user1 = User()
    user1.set_user_id(1)
    user1.set_user_name("Tiaban")

    users.append(user1)

    return users

def add_stores(vehicles):
    stores = []

    # Adding stores (assuming Store class with necessary methods)
    store1 = Store()
    store1.store_id = 1
    store1.set_vehicles(vehicles)

    stores.append(store1)

    return stores

main()

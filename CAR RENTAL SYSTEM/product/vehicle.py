from datetime import datetime
from product.status import Status
from product.vehicle_type import VehicleType


class Vehicle:
    def __init__(self, vehicle_id: int, vehicle_number: int, vehicle_type: VehicleType, company_name: str, 
                 model_name: str, km_driven: int, manufacturing_date: datetime, average: int, cc: int, 
                 daily_rental_cost: int, hourly_rental_cost: int, no_of_seat: int, status: Status):
        self.vehicle_id = vehicle_id
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.company_name = company_name
        self.model_name = model_name
        self.km_driven = km_driven
        self.manufacturing_date = manufacturing_date
        self.average = average
        self.cc = cc
        self.daily_rental_cost = daily_rental_cost
        self.hourly_rental_cost = hourly_rental_cost
        self.no_of_seat = no_of_seat
        self.status = status

    # Getters and setters
    def get_vehicle_id(self):
        return self.vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def get_vehicle_number(self):
        return self.vehicle_number

    def set_vehicle_number(self, vehicle_number):
        self.vehicle_number = vehicle_number

    def get_vehicle_type(self):
        return self.vehicle_type

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def get_company_name(self):
        return self.company_name

    def set_company_name(self, company_name):
        self.company_name = company_name

    def get_model_name(self):
        return self.model_name

    def set_model_name(self, model_name):
        self.model_name = model_name

    def get_km_driven(self):
        return self.km_driven

    def set_km_driven(self, km_driven):
        self.km_driven = km_driven

    def get_manufacturing_date(self):
        return self.manufacturing_date

    def set_manufacturing_date(self, manufacturing_date):
        self.manufacturing_date = manufacturing_date

    def get_average(self):
        return self.average

    def set_average(self, average):
        self.average = average

    def get_cc(self):
        return self.cc

    def set_cc(self, cc):
        self.cc = cc

    def get_daily_rental_cost(self):
        return self.daily_rental_cost

    def set_daily_rental_cost(self, daily_rental_cost):
        self.daily_rental_cost = daily_rental_cost

    def get_hourly_rental_cost(self):
        return self.hourly_rental_cost

    def set_hourly_rental_cost(self, hourly_rental_cost):
        self.hourly_rental_cost = hourly_rental_cost

    def get_no_of_seat(self):
        return self.no_of_seat

    def set_no_of_seat(self, no_of_seat):
        self.no_of_seat = no_of_seat

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
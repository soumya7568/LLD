from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, vehicle, entry_time, parking_spot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.entry_time = entry_time
        self.parking_spot = parking_spot

    def get_ticket_id(self):
        return self.ticket_id

    def get_vehicle(self):
        return self.vehicle

    def get_entry_time(self):
        return self.entry_time

    def get_parking_spot(self):
        return self.parking_spot

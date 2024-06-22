import uuid
from ticket import Ticket

class EntryGate:
    def __init__(self, gate_id, manager_factory):
        self.gate_id = gate_id
        self.manager_factory = manager_factory

    def generate_ticket(self, vehicle):
        from datetime import datetime
        entry_time = datetime.now()
        manager = self.manager_factory.get_manager(vehicle)
        parking_spot = manager.get_available_spot()
        parking_spot.park_vehicle(vehicle)
        ticket_id = f"TICKET-{uuid.uuid4()}"
        return Ticket(ticket_id, vehicle, entry_time, parking_spot)

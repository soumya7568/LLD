
from cost_computation.factory import *
class ExitGate:
    def __init__(self, gate_id):
        self.gate_id = gate_id

    def process_exit(self, ticket):
        from datetime import datetime
        exit_time = datetime.now()
        duration = (exit_time - ticket.get_entry_time()).total_seconds() / 3600
        cost_computation = CostComputationFactory.get_cost_computation(ticket.get_vehicle())
        cost = cost_computation.compute_cost(ticket, duration)
        ticket.get_parking_spot().remove_vehicle()
        return cost

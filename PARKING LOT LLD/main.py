from parkinglot import ParkingLot
from entry_gate import EntryGate
from exit_gate import ExitGate
from vechile import FourWheeler

# Create the parking lot
parking_lot = ParkingLot()
manager_factory = parking_lot.get_manager_factory()

# Create entry and exit gates
entry_gate = EntryGate("E1", manager_factory)
exit_gate = ExitGate("X1")

# Create a vehicle
vehicle = FourWheeler("ABC-123")

# Generate a ticket at entry gate
ticket = entry_gate.generate_ticket(vehicle)

# Simulate some parking duration
import time
time.sleep(10)  # Simulating a short parking duration

# Process exit at exit gate
cost = exit_gate.process_exit(ticket)

print(f"Total cost for parking: ${cost:.2f}")

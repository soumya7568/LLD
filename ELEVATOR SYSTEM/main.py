# Elevator System LLD

class Elevator:
    def __init__(self, id, total_floors):
        self.id = id
        self.current_floor = 0
        self.direction = None  # None, 'UP', or 'DOWN'
        self.total_floors = total_floors
        self.requests = []  # List of requested floors

    def move_to_floor(self, floor):
        if 0 <= floor < self.total_floors:
            self.current_floor = floor
            print(f"Elevator {self.id} moving to floor {floor}.")
        else:
            raise ValueError("Invalid floor.")

    def add_request(self, floor):
        if floor not in self.requests:
            self.requests.append(floor)
            self.requests.sort()  # Sort requests in ascending order
            print(f"Request added for elevator {self.id} to floor {floor}.")

    def clear_requests(self):
        self.requests.clear()
        print(f"Requests cleared for elevator {self.id}.")

    def serve_requests(self):
        # Move to each requested floor
        while self.requests:
            next_floor = self.requests.pop(0)
            self.move_to_floor(next_floor)
            print(f"Elevator {self.id} served request for floor {next_floor}.")


class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.up_button = Button(floor_number)
        self.down_button = Button(floor_number)

    def press_up_button(self):
        self.up_button.press()
        print(f"Up button pressed on floor {self.floor_number}.")

    def press_down_button(self):
        self.down_button.press()
        print(f"Down button pressed on floor {self.floor_number}.")

    def call_elevator(self, elevator_controller):
        if self.up_button.pressed:
            print(f"Calling elevator from floor {self.floor_number} to go up.")
            elevator_controller.request_elevator(self.floor_number, 'UP')
        if self.down_button.pressed:
            print(f"Calling elevator from floor {self.floor_number} to go down.")
            elevator_controller.request_elevator(self.floor_number, 'DOWN')


class Button:
    def __init__(self, floor):
        self.floor = floor
        self.pressed = False

    def press(self):
        self.pressed = True
        print(f"Button for floor {self.floor} pressed.")


class ElevatorController:
    def __init__(self, number_of_elevators, total_floors):
        self.elevators = [Elevator(i, total_floors) for i in range(number_of_elevators)]
        self.floors = [Floor(i) for i in range(total_floors)]

    def request_elevator(self, requested_floor, direction):
        # Simple logic to assign the nearest elevator
        closest_elevator = min(self.elevators, key=lambda e: abs(e.current_floor - requested_floor))
        closest_elevator.add_request(requested_floor)
        print(f"Elevator {closest_elevator.id} assigned to floor {requested_floor}.")

    def elevator_arrived(self, elevator_id, floor):
        print(f"Elevator {elevator_id} has arrived at floor {floor}.")



# Driver Code (Main Execution)
if __name__ == "__main__":
    # Create an elevator controller for 2 elevators and 10 floors
    elevator_controller = ElevatorController(2, 10)

    # Simulate pressing buttons on various floors
    elevator_controller.floors[3].press_up_button()  # Press up button on floor 3
    elevator_controller.floors[5].press_down_button()  # Press down button on floor 5
    elevator_controller.floors[1].press_up_button()  # Press up button on floor 1

    # Simulate calling the elevator
    elevator_controller.floors[3].call_elevator(elevator_controller)  # Call elevator from floor 3
    elevator_controller.floors[5].call_elevator(elevator_controller)  # Call elevator from floor 5
    elevator_controller.floors[1].call_elevator(elevator_controller)  # Call elevator from floor 1

    # Serve requests for elevators
    for elevator in elevator_controller.elevators:
        elevator.serve_requests()

from reservation import Reservation

# Define Bill class
class Bill:
    def __init__(self, reservation: Reservation):
        self.reservation = reservation
        self.total_bill_amount = self.compute_bill_amount()
        self.is_bill_paid = False

    def compute_bill_amount(self) -> float:
        # Simulated bill computation (replace with actual logic)
        return 100.0
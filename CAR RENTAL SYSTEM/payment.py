from bill import Bill

# Define Payment class
class Payment:
    def pay_bill(self, bill: Bill):
        # Simulate payment processing
        # In a real application, this would involve actual payment processing logic
        print(f"Processing payment for Reservation ID: {bill.reservation.reservation_id}")
        bill.is_bill_paid = True
        print("Payment successful.")
        print(f"Bill status updated: Is Bill Paid = {bill.is_bill_paid}")
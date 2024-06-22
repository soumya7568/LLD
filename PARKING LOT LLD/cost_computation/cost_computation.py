class CostComputation:
    def compute_cost(self, ticket, duration):
        raise NotImplementedError


class TwoWheelerCC(CostComputation):
    def compute_cost(self, ticket, duration):
        # Example rate based on parking spot price
        return duration * ticket.get_parking_spot().get_price()


class FourWheelerCC(CostComputation):
    def compute_cost(self, ticket, duration):
        # Example rate based on parking spot price
        return duration * ticket.get_parking_spot().get_price()

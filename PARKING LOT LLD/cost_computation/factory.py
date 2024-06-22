from cost_computation.cost_computation import *

class CostComputationFactory:
    @staticmethod
    def get_cost_computation(vehicle):
        if vehicle.get_type() == "TwoWheeler":
            return TwoWheelerCC()
        else:
            return FourWheelerCC()

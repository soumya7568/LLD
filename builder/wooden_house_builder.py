from house_builder import HouseBuilder
from house import House

class WoodenHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "wooden walls"

    def build_roof(self):
        self.house.roof = "wooden roof"

    def build_windows(self):
        self.house.windows = "glass windows"

    def build_doors(self):
        self.house.doors = "wooden door"

    def get_house(self) -> House:
        return self.house
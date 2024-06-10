from house_builder import HouseBuilder
from house import House

class IglooBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "ice blocks"

    def build_roof(self):
        self.house.roof = "ice dome"

    def build_windows(self):
        self.house.windows = "ice windows"

    def build_doors(self):
        self.house.doors = "ice door"

    def get_house(self) -> House:
        return self.house
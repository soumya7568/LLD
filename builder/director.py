from house_builder import HouseBuilder

class Director:
    def __init__(self, builder: HouseBuilder):
        self._builder = builder

    def construct_house(self):
        self._builder.build_walls()
        self._builder.build_roof()
        self._builder.build_windows()
        self._builder.build_doors()

    def get_house(self):
        return self._builder.get_house()

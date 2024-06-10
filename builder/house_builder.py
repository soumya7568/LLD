from abc import ABC, abstractmethod
from house import House

class HouseBuilder(ABC):
    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def get_house(self) -> House:
        pass

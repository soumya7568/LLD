from igloo_builder import IglooBuilder
from castle_builder import CastleBuilder
from wooden_house_builder import WoodenHouseBuilder
from director import Director

def client_code(builder):
    director = Director(builder)
    director.construct_house()
    house = director.get_house()
    print(house)

if __name__ == "__main__":
    print("Building an Igloo:")
    client_code(IglooBuilder())

    print("\nBuilding a Castle:")
    client_code(CastleBuilder())

    print("\nBuilding a Wooden House:")
    client_code(WoodenHouseBuilder())

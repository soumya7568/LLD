from factory import AnimalFactory
def main():
    factory = AnimalFactory()
    
    animal_type = input("Enter animal type (Dog/Cat): ")
    try:
        animal = factory.create_animal(animal_type)
        print(animal.speak())
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

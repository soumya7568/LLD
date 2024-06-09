from abc import abstractmethod,ABC

class Vechile(ABC):

    @abstractmethod
    def engine(self,name):
        pass

    @abstractmethod
    def speed(self,speed):
        pass

class Car(Vechile):

    def engine(self,name):
        self.engine = name
        print(self.engine)

    def speed(self,speed):
        self.speed = speed
        print(self.speed)

    def color(self,color):
        self.color = color
        print(self.color)


if __name__ == "__main__":
    
    new = Car()
    new.color("red")
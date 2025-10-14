# Create an abstract class called Vehicle.

# Add an abstract method called start_engine().

# Add another abstract method called stop_engine().

# Create two child classes: Car and Motorcycle.

# Each class should implement the start_engine() and stop_engine() methods with their own print statements.

# Create an object of each subclass and call their methods to test.

from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass
class car(vehicle):
    def start_engine(self):
        print("car engine starting")
    def stop_engine(self):
        print("car engine stoped")
class motorcycle(vehicle):
    def start_engine(self):
        print("bike engine starting")
    def stop_engine(self):
        print("bike engine stoped")
benz=car()
benz.start_engine()
benz.stop_engine()

yamaha=motorcycle()
yamaha.start_engine()
yamaha.stop_engine()
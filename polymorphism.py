# Activity 2: Polymorphism Challenge! 

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class (inherits from Vehicle)
class Boat(Vehicle):
    def move(self):
        print("Sailing")

    def test_vehicles():
    # Create instances of different vehicles
    car = Car()
    plane = Plane()
    boat = Boat()

    # Call the move() method on each instance
    vehicles = [car, plane, boat]
    for vehicle in vehicles:
        vehicle.move()

# Run the test
if __name__ == "__main__":
    test_vehicles()


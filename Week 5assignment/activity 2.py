class Car:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        return f"{self.model} is driving 🚗"


class Plane:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        return f"{self.model} is flying ✈️"


class Boat:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        return f"{self.model} is sailing ⛵"


# Create vehicle instances
vehicles = [
    Car("Tesla"),
    Plane("Boeing"),
    Boat("Yacht")
]

# Demonstrate polymorphism
for vehicle in vehicles:
    print(vehicle.move())
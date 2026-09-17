class CarInventory:
    default_color = "white"
    default_seating_capacity = 4 
    def __init__(self, make, model, color = None, seating_capacity = None, maximum_speed = 180, mileage = 20):
        self.make = make
        self.model = model
        self.color = color or self.default_color
        self.maximum_speed = maximum_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity or self.default_seating_capacity
    def printAll(self):
        print(f"The car maker is:{self.make},\nModel is:{self.model},\nSeating capacity is:{self.seating_capacity}, \nMaximum permissible speed is:{self.maximum_speed},\nMileage is:{self.mileage}.")


ob1 = CarInventory("Honda", "Civic", "Black", maximum_speed=340, mileage=5)
ob2 = CarInventory("BMW", "M5 Competition", maximum_speed=400, mileage=3)

ob1.printAll()
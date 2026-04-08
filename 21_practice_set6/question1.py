class car:
    def __init__(self, car):
        self.car = car

    def drive(self):
        print(f"Car {self.car} is moving")

car = car("Honda Civic")
car.drive()
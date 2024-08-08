# car.py

class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.started = False
        self.speed = 0
        self.max_speed = 200

    
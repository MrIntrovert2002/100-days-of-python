from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager():
    def __init__(self, no_of_cars):
        super().__init__()
        self.cars = []
        self.create_cars(no_of_cars)
        self.moving_speed = STARTING_MOVE_DISTANCE

    def new_car_init(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(1,2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        return new_car
    
    def create_cars(self, no_of_cars):
        for i in range(no_of_cars):
            new_car = self.new_car_init()
            new_car.goto(random.randint(-250, 350), random.randint(-240,240))
            self.cars.append(new_car)

    def add_cars(self, no_of_cars):
        for i in range(no_of_cars):
            new_car = self.new_car_init()
            new_car.goto(random.randint(250, 400), random.randint(-240,240))
            self.cars.append(new_car)

    def increase_car_speed(self):
        self.moving_speed += MOVE_INCREMENT

    def move_cars(self):
        for i in self.cars:
            i.forward(self.moving_speed)

    def replace_cars(self):
        for i in range(len(self.cars)):
            if self.cars[i].xcor() < -340:
                self.cars[i] = self.new_car_init()
                self.cars[i].goto(random.randint(250, 400), random.randint(-240,240))

    def check_coll(self, player):
        for i in self.cars:
            if i.distance(player) <= 25:
                return True
        return False
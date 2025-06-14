import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")

def start_game():
    screen.clear()
    screen.tracer(0)
    player1 = Player()
    carM = CarManager(15)
    writer = Scoreboard()
    screen.listen()
    screen.onkeypress(player1.move, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        carM.move_cars()
        carM.replace_cars()

        if carM.check_coll(player1):    
            screen.update()
            time.sleep(1)
            game_is_on = False
            screen.clear()
            writer.game_over()
            screen.onkey(start_game, "space")

        if player1.check_finish():
            player1.refresh()
            carM.add_cars(1)
            carM.increase_car_speed()
            writer.increase_level()

start_game()
screen.exitonclick()
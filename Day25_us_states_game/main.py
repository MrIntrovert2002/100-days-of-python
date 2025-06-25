import turtle
import pandas

FONT = ("Arial", 8, "normal")
PR = "Guess the name of any state!"

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

# Get click location
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

def print_state(state_data):
    state_name = state_data["state"].item()
    x = state_data["x"].item()
    y = state_data["y"].item()
    tim.goto(x,y)
    tim.write(state_name, False, "left", FONT)

correct_gusses = []
while len(correct_gusses) < 50:
    answer_state = screen.textinput(title=f"Guess the State - {len(correct_gusses)}/50", prompt=PR).title()
    if answer_state == "Exit":
        break
    elif answer_state in correct_gusses:
        print("Already Guessed!")
        PR = "Already Guessed! Try again."
    elif answer_state in data.state.to_list():
        correct_gusses.append(answer_state)
        print_state(data[data.state == answer_state])
        PR = "What's another state's name?"
    else:
        PR = "Wrong Guess! Try again."

remaining_states = data.state.to_list()
for i in correct_gusses:
    remaining_states.pop(remaining_states.index(i))
new_dict = {"State": remaining_states}
new_data = pandas.DataFrame(new_dict)
new_data.to_csv("states_to_learn.csv")
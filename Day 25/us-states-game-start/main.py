import turtle
import pandas as pd

FONT = ("Courier", 12, "normal")
img = "Day 25/us-states-game-start/blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(img)
turtle.shape(img)

# Getting the 50 states names and screen coordinates
states_data = pd.read_csv("Day 25/us-states-game-start/50_states.csv")
states = states_data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    #Ask the user to guess a state
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    #the title method returns the string with the 1st letter capitalized
    if answer_state in states:
        display_state = turtle.Turtle()
        display_state.ht()
        display_state.penup() 
        display_state.goto(int(states_data[states_data.state == answer_state].x), int(states_data[states_data.state == answer_state].y))
        display_state.write(answer_state,  align="center", font= FONT)
        # the score won't go up if the state is duplicated
        guessed_states.append(answer_state)
        states.remove(answer_state)
    if answer_state == "Exit":
        break 

new_data = pd.DataFrame(states)
new_data.to_csv("Day 25/us-states-game-start/states_to_learn.csv")
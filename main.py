import os
import turtle
import pandas

screen = turtle.Screen()
screen.title("Guessing the regions of Finland")
img = "Regions_of_Finland_blank_map.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("Finland_regions.csv")
states = data.state.tolist()

guesses = []
correctGuesses = 0
game_on = True

while game_on:
    answer = screen.textinput(title=f"{correctGuesses}/19 Regions correct", prompt="Guess another region")
    answer = answer.title()

    print(answer)
    if answer == "Exit":
        missing_states = []
        for state in states:
            if state not in guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing.csv")
        break
    if answer in states and answer not in guesses:
        correctGuesses += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

    guesses.append(answer)

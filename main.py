import pandas
from turtle import Turtle,Screen

cur = Turtle()
screen = Screen()
point_state = Turtle()
point_state.hideturtle()
point_state.penup()
point_state.speed("fastest")

screen.title("US State guessing game")
screen.addshape("Map recognising/day-25-us-states-game-start/blank_states_img.gif")
cur.shape("Map recognising/day-25-us-states-game-start/blank_states_img.gif")


data = pandas.read_csv("Map recognising/day-25-us-states-game-start/50_states.csv")
game = True
data_state_list = data.state.tolist()
 

guessed_answer = []

user_name =screen.textinput("Information","Whats your name?")

with open("Map recognising/day-25-us-states-game-start/data.txt",mode="a") as file:
    file.write(f"\n{user_name} started the game:-\n->User knows this much states:-\n")

no_of_guesses = 0

while game:
    user_guess = screen.textinput("State Game","Guess the state in US.").title()
    if user_guess in data_state_list:
        part_state = data[data.state == user_guess]
        point_state.goto(int(part_state.x),int(part_state.y))
        point_state.write(user_guess)
        guessed_answer.append(user_guess)
        no_of_guesses += 1
        with open("Map recognising/day-25-us-states-game-start/data.txt",mode="a") as file:
            file.write(f"{no_of_guesses}. {user_guess}\n")

    elif user_guess == "Exit":
        game = False

    else:
        print("wrong")
        print(type(user_guess))





screen.exitonclick()
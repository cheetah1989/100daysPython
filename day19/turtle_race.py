from turtle import Turtle, Screen, TK
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
is_raceON = False
user_input = screen.textinput(title="Make your choice:", prompt="Select the color of Turtle you're betting on: ")
colors = ["red","green","blue","orange","purple","yellow"]
y_cordinates = [-70,-40,-10,20,50,80]
turtles = []

for turt in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turt])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cordinates[turt])
    turtles.append(new_turtle)


if user_input:
    is_raceON = True 

while is_raceON:
    for t in turtles:
        if t.xcor() > 230:
          is_raceON = False
          winner = t.pencolor()
          if winner == user_input:
             TK.messagebox.showinfo(title="Game status", message="You've Won!!")
          else:
                TK.messagebox.showinfo(title="Game status", message="You've Lost!!")

        rand_dist = randint(0,10)
        t.forward(rand_dist)

screen.exitonclick()
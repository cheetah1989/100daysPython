from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle() 
screen.colormode(255)
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tup = (r,g,b)
    return tup

directions = [0,90,180,270]
tim.pensize(10)
tim.speed(10)

for i in range(100):
    tim.color(rand_color())
    tim.setheading(random.choice(directions))
    tim.forward(30)


screen.exitonclick()
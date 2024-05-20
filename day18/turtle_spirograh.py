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

tim.speed(30)
def spirograh(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(rand_color())
        current_heading= tim.heading()
        tim.circle(100)
        tim.setheading(tim.heading() + 5)

spirograh(5)

screen.exitonclick()
from turtle import Turtle, Screen
import random


screen = Screen()
screen.colormode(255)
tim = Turtle()

#colors = ['dark orange','red','dark red','sienna','dark goldenrod','green','dark green','indigo',
#'blue violet','gold','yellow']

def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tup = (r,g,b)
    return tup

def draw_shape(num_sides):
    angle = int(360 / num_sides)
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(rand_color())
    draw_shape(shape_side)
    #print(shape_side)


screen.exitonclick()

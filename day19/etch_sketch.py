from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



def move_forward():
    tim.forward(100)

def move_backward():
    tim.backward(100)

def turn_left():
    tim.left(100)

def turn_right():
    tim.right(100)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def move_backward():
    tim.left(100)
    tim.left(100)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right,"d")
screen.onkey(turn_left,"a")
screen.onkey(clear,"c")
screen.exitonclick()

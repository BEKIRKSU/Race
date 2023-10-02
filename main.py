from turtle import Turtle, Screen

shell = Turtle()
screen = Screen()
# this controls the screen when it is run ^

def move_forward():
    shell.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
# we don't add the parantheses to the end when the function is called as an argument because
# the parantheses trigger the function there and then. What we want is for the method 'onkey' to
# listen for when the spacebar is pressed and only when that happens to trigger the move forward
# function.
screen.exitonclick()
# this is added so the screen doesn't disappear when we run it and only disappears when we click off.

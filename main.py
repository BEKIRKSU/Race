from turtle import Turtle, Screen

shell = Turtle()
screen = Screen()
# this controls the screen when it is run ^

def move_forwards():
    shell.forward(10)

def move_backwards():
    shell.backward(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
# we don't add the parentheses to the end when the function is called as an argument because
# the parentheses trigger the function there and then. What we want is for the method 'onkey' to
# listen for when the space-bar is pressed and only when that happens to trigger the move forward
# function. We're basically using a function as an input.
# we can actually pass a function inside a function like: def function_a(function_b): you only
# pass the name of the function without the parentheses at the end. Such as:
# def calculator(n1, n2, func):
#     return func(n1, n2).
# a higher order function is a function that can take and work with another function.
# It's really useful when we want to listen for events and then trigger a function.
# Also use keyword arguments rather than positional inside the parentheses for methods you didn't make
# such as 'onkey'.
screen.exitonclick()
# this is added so the screen doesn't disappear when we run it and only disappears when we click off.

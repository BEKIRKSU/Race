from turtle import Turtle, Screen

shell = Turtle()
screen = Screen()
# this controls the screen when it is run ^

def move_forwards():
    shell.forward(10)

def move_backwards():
    shell.backward(10)

def turn_left():
    new_heading = shell.heading() + 10
    shell.setheading(new_heading)
#     Could also just use shell.left(10)
def turn_right():
    new_heading = shell.heading() - 10
    shell.setheading(new_heading)

def clear():
    shell.clear()
    shell.penup()
    shell.home()
# Find the relevant methods in the documentation. Patience + play around with the code.
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
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

# we can create as many turtles just like we created Shell above. Even tho they'll all be tutle objects
# they function completely independent of each other, in programming we would say that they are
# each a separate 'instance'. They each an example of the turtle object. Just like real life.
# Two turtles with different attributes, doing different things. These objects can
# have different attributes and can be performing different methods at any one time, is called
# their 'state'. The state of one objects Color attribute can be green and the other red.
# So they have different states in terms of their attributes or appearance. They can also have different
# state in terms of what they are doing. One goes forward, whilst one doesn't etc.
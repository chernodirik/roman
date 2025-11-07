import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
spiral = turtle.Turtle()
spiral.speed(0)  # Fastest drawing

# Constants
golden_ratio = (1 + math.sqrt(5)) / 2
num_steps = 500
angle_increment = 10  # degrees
length = 2  # initial length of each segment
def drawT(myTurtle):
 for _ in range(3):
    myTurtle.right(120)
    myTurtle.forward(20)
 
# Draw the logarithmic spiral
for i in range(num_steps):
    # Increase the length roughly according to the golden ratio
    length *= golden_ratio ** (angle_increment / 360)
    # Turn the turtle
    spiral.forward(length)
    spiral.left(angle_increment)
    drawT(spiral)

# Hide the turtle and display the window
spiral.hideturtle()
turtle.done()

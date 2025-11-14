import turtle
import math
screen = turtle.Screen()
def drawSquare(myTurtle):
   for _ in range (4):
      myTurtle.color("pink")
      myTurtle.right(90)
      myTurtle.forward(20)
      #myTurtle.down(120)
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
 myTurtle.width(15)
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
    if i<num_steps/6:
       drawT(spiral)
    else:
       drawSquare(spiral)

# Hide the turtle and display the window
spiral.hideturtle()
turtle.done()

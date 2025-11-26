import turtle
import math
import random
screen = turtle.Screen()
screen.colormode(255)  
def drawHexagon(myTurtle):
   for _ in range(6):
      myTurtle.color((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
      def randint(green, blue, ):
       green: int
      blue: int
   myTurtle.right(360/6)
   myTurtle.forward(20)
   num_steps = 1000
def drawPentagon(myTurtle):
   for _ in range(5):
    myTurtle.color((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
   myTurtle.right(360/5)
   myTurtle.forward(20)
   num_steps = 350
def drawSquare(myTurtle):
   for _ in range (4):
    myTurtle.color((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
    myTurtle.right(90)
    myTurtle.forward(20)
    num_steps = 450
      #myTurtle.down(120)
# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

spiral = [drawSquare, drawPentagon, drawHexagon]
# Create a turtle
spiral = turtle.Turtle()
spiral.speed(0)  # Fastest drawing
# Constants
golden_ratio = (1 + math.sqrt(5)) / 2
num_steps = 350
angle_increment = 10  # degrees
length = 2  # initial length of each segment
spiral.color((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
def drawT(myTurtle):
 myTurtle.width(1)
 myTurtle.color((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
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
   elif i<num_steps/4:
       drawSquare(spiral)
   elif i<num_steps/2:
      drawPentagon(spiral)
   else:
       drawHexagon(spiral)

# Hide the turtle and display the window
spiral.hideturtle()
turtle.done()

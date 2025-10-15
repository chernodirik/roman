import turtle

#image = "C:/Python27/PythonProgramming/picture.gif"
screenr = turtle.Screen()

Lewi = turtle.Turtle()

#screenr.addshape(image)
#Lewi.shape(image)

#Lewi.penup()
Lewi.left(90)

Lewi.speed('fastest')

def up():
    Lewi.forward(10)

def down():
    Lewi.forward(-10)

def left():
    Lewi.left(10)
    

def right():
    Lewi.right(10)

def space():
    Lewi.clear()



screenr.onkey(up, "Up")
screenr.onkey(down, "Down")
screenr.onkey(right, "Right")
screenr.onkey(left, "Left")
screenr.onkey(space, " ")
screenr.listen()

turtle.mainloop()

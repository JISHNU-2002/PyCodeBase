import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw the first line
t.pencolor("red")
t.forward(100)

# Move without drawing
t.penup()
t.goto(0, -50)
t.pendown()

# Draw the second line
t.pencolor("blue")
t.forward(100)

# Finish the drawing
turtle.done()


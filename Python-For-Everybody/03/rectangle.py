import turtle

# Create a turtle object
t = turtle.Turtle()

# Set fill color
t.fillcolor("green")

# Start filling
t.begin_fill()

# Draw a rectangle
for _ in range(2):
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)

# End filling
t.end_fill()

# Finish the drawing
turtle.done()


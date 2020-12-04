# Turtle exercise
from turtle import *
wn = turtle.Screen()

alex = turtle.Turtle()
boom = turtle.Turtle()

color("yellow")
begin_fill()
# Draw a square
for x in range(5):
    alex.forward(50)
    alex.left(90)
end_fill()

# Draw an equilateral triangle
for y in range(4):
    boom.forward(80) 
    boom.left(120)
boom.fillcolor("yellow")

wn.mainloop()

from turtle import *

colours = ["red", "orange", "yellow", "blue", "green", "purple", "red", "orange", "yellow", "blue", "green", "purple", "red", "orange", "yellow", "blue", "green", "purple", "red", "orange"]
speed(0)
for j in range(20):
    k=10*j
    color(colours[j])
    for i in range(30):
        begin_fill()
        circle(200-k, 120)
        left(5)
        left(60)
        circle(200-k, 120)
        end_fill()
        right(50)
    right(5)
exitonclick()
hideturtle()

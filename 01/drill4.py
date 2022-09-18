import turtle

count = 0

while (count < 6):
    turtle.forward(500)
    turtle.penup()
    count += 1
    turtle.goto(0,100*count)
    turtle.pendown()

turtle.penup()
turtle.home()
turtle.pendown()

turtle.left(90)

count = 0

while (count < 6):
    turtle.forward(500)
    turtle.penup()
    count += 1
    turtle.goto(100*count, 0)
    turtle.pendown()

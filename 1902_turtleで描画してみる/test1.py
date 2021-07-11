import turtle

turtle.color('red', 'yellow')

turtle.begin_fill()
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.done()

import turtle

turtle.color('red', 'yellow')

turtle.begin_fill()
for i in range(5 * 3):
    turtle.forward(100 + i * 10)
    turtle.right(360 / 5 * 2)
turtle.end_fill()

turtle.done()

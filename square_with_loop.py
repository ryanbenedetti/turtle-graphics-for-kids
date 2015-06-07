import turtle
turtle.bgcolor("black")
toby = turtle.Pen()
toby.pencolor("green")
toby.width(2)

#Can we make it shorter with a loop?
for x in range(4):
  toby.forward(200)
  toby.left(90)



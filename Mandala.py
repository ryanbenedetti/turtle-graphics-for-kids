import turtle
turtle.bgcolor("black")
t = turtle.Pen()
t.pencolor("white")
sides = 4
colors = ["red", "green", "yellow", "purple", "blue", "orange"]

for y in range(100):
  for x in range(24):
    t.pencolor(colors[x%sides])
    t.forward(x)
    t.left(x + 5)
  t.right(180)
  for x in range(24):
    t.pencolor(colors[x%sides])
    t.forward(x)
    t.left(x + 5)

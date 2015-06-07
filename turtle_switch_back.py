import turtle
turtle.bgcolor("black")
tony = turtle.Pen()

tony.pencolor("blue")
for i in range(25):
 tony.goto(i * 4, 100)
 tony.goto(100, i * i)

tony.pencolor("yellow")
for n in range(25):
 tony.goto(n * n, 100)
 tony.goto(100, n - 100)

tony.pencolor("green")
for n in range(100):
 tony.goto(n * n, 100)
 tony.goto(100, n - 100)

#set tony at x = 0
##tony.setx(100)
##tony.sety(-100)
##
##tony.goto(200, 100)
##tony.goto(100, 200)

#draw a "switch back" pattern 
##for x in range(25):
##  tony.forward(200)
##  tony.left(90)
##  tony.forward(20)
##  tony.left(90)
##  tony.forward(200)  
##  tony.right(90) 
##  tony.forward(20)
##  tony.right(90)

  
 
  

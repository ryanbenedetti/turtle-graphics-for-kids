import turtle

#Crazy bug eyes pattern by Ryan Benedetti,6/7/2015

turtle.bgcolor("black")
tony = turtle.Pen()
tony.pencolor("green")
for i in range(360):
 #as the loop repeats, i will count up and the circles will grow
 tony.circle(i)

 #if the current number is odd, turn left
 if i%2 > 0:
  tony.left(i * 10)
  #if the current number is even, turn right
 else:
  tony.right(i * 10)
 

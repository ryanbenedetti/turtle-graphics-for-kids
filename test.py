import turtle

#Circles into 3D-ish objects by Ryan Benedetti, 6/7/2015

turtle.bgcolor("black")

tony = turtle.Pen()
tony.shape("turtle")
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
 

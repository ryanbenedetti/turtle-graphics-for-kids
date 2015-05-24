import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def draw_better(times, color_start=0, forw=95):
    for i in range(times):
        t.pencolor(colors[i + color_start])
        t.forward(forw)
       
def draw_tight(times):
    draw_better(1, 0, 10)
    t.left(90)
    last_right = 0
    for i in range(times):
        draw_better(2, 1, 80)
        if last_right == 0:
            t.right(90)
            last_right = 1
        else:
            t.left(90)
            last_right = 0
        draw_better(1, 4, 10)
        if last_right == 1:
            t.right(90)
            last_right = 1
        else:
            t.left(90)
            last_right = 0     

def draw_stairs(times):
    for i in range(times):
        t.left(90)
        draw_better(1, 3, 10)
        t.right(90)
        draw_better(1, 3, 10)

draw_tight(14)

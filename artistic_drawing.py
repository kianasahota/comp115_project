# set up turtle and screen and random module 
import turtle
import random
screen = turtle.Screen()
screen.bgcolor("light blue")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# rectangle function
def draw_rectangle(width, height, color, x,y):
    pen.setheading(0)
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# triangle function 
def draw_triangle(length, color, x, y):
    pen.setheading(0)
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(length)
        pen.left(120)
    pen.end_fill()

# non equilateral triangle function 
def draw_tall_triangle(width, height, color, x, y):
    pen.setheading(0)
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    pen.forward(width)
    pen.left(140)
    pen.forward(height)
    pen.left(80)
    pen.forward(height)
    pen.end_fill()

# circle function 
def draw_circle(radius, color, x, y):
    pen.setheading(0)
    pen.up()
    pen.goto(x, y-radius)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# tree function 
def draw_tree(trees,x,y): 
    pen.setheading(0) 
    
    for i in range(trees): 
        draw_rectangle(20, 70, "brown", x, y) 
        draw_triangle(80, "dark green", x-30,y+ 50) 
        draw_triangle(50, "forest green", x-15,y+80) 
        draw_triangle(30, "dark green", x-5,y+110) 
        x+= 50 

# mountain function 
def draw_mountain(mountains):
    x= -350
    for i in range(mountains):
        draw_tall_triangle(50, 200, "grey",x,-150)
        draw_tall_triangle(50, 170, "dark grey", x+10, -150)
        x+= 120

# cloud function 
def draw_cloud(x, y):
    draw_circle(20, "white", x, y)
    draw_circle(25, "white", x + 20, y + 10)
    draw_circle(20, "white", x + 40, y)
    draw_circle(15, "white", x + 20, y - 10)

# bird function 
def draw_bird(x,y):
    pen.setheading(0)
    pen.pensize(7)
    pen.up()
    pen.goto(x,y)
    pen.color("black")
    pen.down()
    pen.right(45) 
    pen.forward(20)
    pen.left(60)
    pen.forward(20)

# for number of birds, draw birds randomly
def draw_birds(birds):
    for i in range(birds):
        x = random.randint(-200, 200)
        y = random.randint(0, 200)
        draw_bird(x,y)

# draw mountain 
draw_mountain(7)

# draw grass
draw_rectangle(800, 200, "mediumseagreen", -400, -350)

# draw sun 
draw_circle(50, "yellow", 200, 300)

# draw trees 
draw_tree(14,-350, -200)
draw_tree(13, -325,-225)
draw_tree(14, -350, -265)

# draw clouds
draw_cloud(-260,35)
draw_cloud(-200, 300)
draw_cloud(-100, 230)
draw_cloud(-270, 190)
draw_cloud(230,230)
draw_cloud(100, 100)
draw_cloud(260,40)
draw_cloud(-130, 140)

# draw birds
draw_birds(8)

#screen closes on user click
screen.exitonclick()
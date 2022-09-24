# this is Turtle Lab #1 from week 3 due on week 5.

# create a python program where I will use simple commands to make a
# short program that uses turtle to draws shapes and add color.

# import turtle library
from turtle import *

# screen and turtle setup
speed(3) # setup speed of turtle
setup(800,800) # setup the window size

shape("turtle") # create drawing turtle 
showturtle()
fillcolor("green")
pencolor("blue")

# move to circle position
penup()
goto(200,100)

# draw a blue circle with yellow filling
pendown()
pensize(10)
fillcolor('purple')
begin_fill()
circle(100)
end_fill()

# turn turtle back to green
fillcolor('green')
pencolor('green')

# move to square position
penup()
goto(-200,-200)

# draw magenta square with orange filling
pendown()
pencolor('magenta')
fillcolor('black')
pensize(5)
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

# turn turtle back to green
fillcolor('green')
pencolor('green')

# move to triangle postion
penup()
goto(-250,175)
left(90)

# draw triangle position
pendown()
pencolor('red')
fillcolor('gray')
pensize(2)
begin_fill()
forward(160)
left (120)
forward(160)
left(120)
forward(160)
end_fill()


# turn turtle back to green
fillcolor('green')
pencolor('green')

# relocate turtle to center
penup()
goto(0,0)
right(90)

# this is here to stop the window from closing
done()
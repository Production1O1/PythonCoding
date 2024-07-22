#this ping pong game will be made using the turtle module.

import turtle 

wn = turtle.Screen()
wn.title("Ping Pong by Smarty Anvay!")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)
#This line of code allows the window pop up of the base of, PING PONG TABLE

#paddle A (Silver Warriors)
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B (Golden Hawks)
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)

#Function
def paddle_a_up():
     y = paddle_a.ycor()
     y += 20
     paddle_a.sety(y)

#keybord binding
wn.listen()
wn.onkey



#main game loop
while True:
    wn.update()

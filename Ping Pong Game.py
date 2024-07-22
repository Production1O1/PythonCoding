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
Ball.dx = 0.10
Ball.dy = 0.10

#Function Paddle A
def paddle_a_up():
     y = paddle_a.ycor()
     y += 20
     paddle_a.sety(y)

def paddle_a_down():
     y = paddle_a.ycor()
     y -= 20
     paddle_a.sety(y)
#Function Paddle B
def paddle_b_up():
     y = paddle_b.ycor()  # Use paddle_b.ycor() here
     y += 20
     paddle_b.sety(y)

def paddle_b_down():
     y = paddle_b.ycor()  # Use paddle_b.ycor() here
     y -= 20
     paddle_b.sety(y)


#keybord binding Paddle A
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
#Keybodr binding Paddle B
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    #move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border Checking (Bounce of border)
    if Ball.ycor() > 290:
         Ball.sety(290)
         Ball.dy *= -1

    #if Ball.ycor() > -290:
              #Ball.sety(-290)
              #Ball.dy *= -1

    #Update the screen
    wn.update()

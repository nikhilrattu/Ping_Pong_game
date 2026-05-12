from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen= Screen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


screen.listen()
screen.onkey(r_paddle.move_up,'Up')
screen.onkey(r_paddle.move_down,'Down')
screen.onkey(l_paddle.move_up,'w')
screen.onkey(l_paddle.move_down,'s')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.velocity)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_ball_x()

    if  ball.xcor() > 400 :
        ball.reset_ball()
        scoreboard.l_point()        

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()

        
screen.exitonclick()



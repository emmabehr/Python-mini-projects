import turtle

window = turtle.Screen()
window.title("CFG/Zopa Pong")
window.bgcolor("aquamarine")
# x -960 / 960 y -540/540
window_height = 1080
window_width = 1920
window.setup(width = window_width, height = window_height)
window.tracer(0)

score_pl1 = 0
score_pl2 = 0

#default Turtle size is 20px
bar_default_size = 20
bar_height = 80
bar_width = 20
bar_stretch_width = bar_height / bar_default_size
bar_stretch_length = bar_width / bar_default_size
bar_x = 900
bar_y = 0

initial_start_speed = 0

left_bar = turtle.Turtle()
left_bar.speed(initial_start_speed)
left_bar.shape("square")
left_bar.shapesize(stretch_wid = bar_stretch_width, stretch_len = bar_stretch_length)
left_bar.color("white")
left_bar.penup()
left_bar.goto(-bar_x, bar_y)

right_bar = turtle.Turtle()
right_bar.speed(initial_start_speed)
right_bar.shape("square")
right_bar.shapesize(stretch_wid = bar_stretch_width, stretch_len = bar_stretch_length)
right_bar.color("white")
right_bar.penup()
right_bar.goto(bar_x, bar_y)

ball_size = 10
ball_initialx = 0 
ball_initialy = 0
ball_initial_direction = 3
ball = turtle.Turtle()
ball.speed = (initial_start_speed)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(ball_initialx, ball_initialy)
ball.directionx = ball_initial_direction
ball.directiony = ball_initial_direction

score_x = 0 
score_y = 500
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(score_x, score_y)

def write_score():
    pen.clear()
    pen.write("Player 1: {}  Player 2: {}".format(score_pl1, score_pl2), align="center", font=("Arial", 28, "normal"))

game_speedx = 0
game_speedy = 0
game_speed_increase = 0.6

paddle_speed = 70 
def left_bar_upwards():
    y = left_bar.ycor()
    y += paddle_speed
    left_bar.sety(y)

def left_bar_down():
    y = left_bar.ycor()
    y -= paddle_speed
    left_bar.sety(y)

def right_bar_upwards():
    y = right_bar.ycor()
    y += paddle_speed
    right_bar.sety(y)

def right_bar_down():
    y = right_bar.ycor()
    y -= paddle_speed
    right_bar.sety(y)

increase_speed_time = 1500
def increase_ball_speed():
    global game_speedx, game_speedy, increase_speed_time
    game_speedx = game_speedx + game_speed_increase
    game_speedy = game_speedy + game_speed_increase
    turtle.ontimer(increase_ball_speed, t = increase_speed_time)

def reset_game_position():
    global game_speedx, game_speedy
    game_speedx = 0
    game_speedy = 0
    ball.goto(0,0)
    ball.directionx = ball.directionx * -1
    write_score()

window.listen()
window.onkeypress(left_bar_upwards, "w")
window.onkeypress(left_bar_down, "a")
window.onkeypress(right_bar_upwards, "Up")
window.onkeypress(right_bar_down, "Down")

bound_y = (window_height / 2) - ball_size
bound_x = (window_width / 2) - ball_size

write_score()
turtle.ontimer(increase_ball_speed, t = increase_speed_time)

   
while True:
    window.update()

    if ball.directiony > 0:
        ball.sety(ball.ycor() + ball.directiony + game_speedy)
    else:
        ball.sety(ball.ycor() + ball.directiony - game_speedy)

    if ball.directionx > 0:
        ball.setx(ball.xcor() + ball.directionx + game_speedx)
    else:
        ball.setx(ball.xcor() + ball.directionx - game_speedx)

    if ball.ycor() > bound_y:
        ball.sety(bound_y)
        ball.directiony = ball.directiony * -1

    if ball.ycor() < -bound_y:
        ball.sety(-bound_y)
        ball.directiony = ball.directiony * -1

    if ball.xcor() > bound_x:
        score_pl1 = score_pl1 + 1
        reset_game_position()
        
    if ball.xcor() < -bound_x:
        score_pl2 = score_pl2 + 1
        reset_game_position()

    if (ball.xcor() > bar_x - ball_size and ball.xcor() < bar_x) and (ball.ycor() < right_bar.ycor() + (bar_height / 2) and ball.ycor() > right_bar.ycor() - (bar_height / 2)):
        ball.directionx = ball.directionx * -1

    if (ball.xcor() < -bar_x + ball_size and ball.xcor() > -bar_x) and (ball.ycor() < left_bar.ycor() + (bar_height / 2)  and ball.ycor() > left_bar.ycor() - (bar_height / 2) ):
        ball.directionx = ball.directionx * -1 


    
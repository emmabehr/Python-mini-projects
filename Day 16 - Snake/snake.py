import turtle
import random
import time 

window = turtle.Screen()
window.title("3210 Snake")
window.bgcolor("black")
window_height = 640
window_width = 540
window.setup(width = window_width, height = window_height)
window.cv._rootwindow.resizable(False, False)
window.tracer(0)

snake_speed = 15

snake = turtle.Turtle()
snake.shape("square")
snake.speed(0)
snake.color("white")
snake.penup()
snake.goto(0,0)
snake.direction = "none"

score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,0)

def game_over():
    pen.clear()
    pen.write("Game Over - Score: {}".format(score))


def snake_upwards():
    if snake.direction != "Down":
        snake.direction = "Up"

def snake_downwards():
    if snake.direction != "Up":
        snake.direction = "Down"

def snake_right():
    if snake.direction != "Left":
        snake.direction = "Right"

def snake_left():
    if snake.direction != "Right":
        snake.direction = "Left"
        
def move():
    if snake.direction == "Up":
        snake.sety(snake.ycor() + snake_speed)
    elif snake.direction == "Down":
        snake.sety(snake.ycor() - snake_speed)
    elif snake.direction == "Right":
        snake.setx(snake.xcor() + snake_speed)
    elif snake.direction == "Left":
        snake.setx(snake.xcor() - snake_speed)

def generate_apple_location():
    apple_x = random.randrange(0 - (window_width / 2) + 20, (window_width / 2) - 20)
    apple_y = random.randrange(0 - (window_height / 2) + 20, (window_height / 2) - 20)
    apple.goto(apple_x, apple_y)

apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
generate_apple_location()


window.listen()
window.onkeypress(snake_upwards, "Up")
window.onkeypress(snake_downwards, "Down")
window.onkeypress(snake_left, "Left")
window.onkeypress(snake_right, "Right")



while True:
    window.update()

    time.sleep(0.1)
    move()

    if (snake.xcor() >= window_width / 2) or (snake.xcor() <= 0 - (window_width / 2)):
        game_over()

    if (snake.ycor() >= window_height / 2) or (snake.ycor() <= 0 - (window_height / 2)):
        game_over() 

    if snake.distance(apple) < 20:
        generate_apple_location() 
        score += 1
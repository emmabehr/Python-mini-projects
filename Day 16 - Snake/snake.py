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

cubes = []

score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,0)

game_over = False
def game_over():
    global cubes
    
    game_over = True
    pen.clear()
    pen.write("Game Over - Score: {}".format(score), align="center", font=("Arial", 28, "normal"))
    snake.hideturtle()
    for cube in cubes:
        cube.hideturtle()
    cubes = []
    apple.hideturtle()
    


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
    global game_over

    if game_over != False:
        index = len(cubes) - 1
        while index > 0:
            cubes[index].setx(cubes[index - 1].xcor())
            cubes[index].sety(cubes[index - 1].ycor())
            index = index - 1
        if index == 0:
            cubes[index].setx(snake.xcor())
            cubes[index].sety(snake.ycor())

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

def new_cube():
    cube = turtle.Turtle()
    cube.shape("square")
    cube.speed(0)
    cube.color("grey")
    cube.penup()
    cube.goto(window_height,window_width)
    return cube
    
    #cube.direction = "none"

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

    if game_over != False:
        move()

        if (snake.xcor() >= window_width / 2) or (snake.xcor() <= 0 - (window_width / 2)):
            game_over()

        if (snake.ycor() >= window_height / 2) or (snake.ycor() <= 0 - (window_height / 2)):
            game_over() 

        if snake.distance(apple) < 20:
            generate_apple_location() 
            score += 1
            cube = new_cube()
            cubes.append(cube)

        index = 0
        while index < len(cubes):
            if snake.distance(cube) <= 20 and index != 0:
                game_over()

            index = index + 1
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score = Score()
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

is_game_On = True
while is_game_On:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    # food collision
    if my_snake.all_snake[0].distance(my_food) < 15:
        my_food.new_location()
        my_snake.extend()
        my_score.update_score()
    # wall collision
    if my_snake.all_snake[0].xcor() > 299 or my_snake.all_snake[0].xcor() < -299 or my_snake.all_snake[
        0].ycor() > 299 or my_snake.all_snake[0].ycor() < -299:
        my_score.game_over()
        is_game_On = False
    # tail collision
    for i in my_snake.all_snake[1:]:
        if my_snake.all_snake[0].distance(i) < 10:
            my_score.game_over()
            is_game_On = False

screen.exitonclick()

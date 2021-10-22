from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor("black")

screen.tracer(0)
score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.down, key="Down")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segment[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        score.score_update()
        snake.extend()

    if (snake.segment[0].xcor() > 280) or (snake.segment[0].xcor() < -300) or (snake.segment[0].ycor() > 300) or \
            (snake.segment[0].ycor() < -280):
        score.reset()
        snake.reset()


    for seg in snake.segment[1:]:
        if snake.segment[0].distance(seg) < 15:
            score.reset()
            snake.reset()


























screen.exitonclick()
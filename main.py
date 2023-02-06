from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SnakeX23")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset_score()
        snake.reset_snake()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()

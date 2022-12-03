from turtle import Screen
from scoreBoard import Scoreboard
from snake import Snake
from  food import Food
import time

screen=Screen()
screen.setup(600,600)   #width and height of screen
screen.bgcolor("black")
screen.title("Snake Game by BharadwajStudios")
screen.tracer(0)

snake=Snake()
food=Food()
score_board=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#moving the snake
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    #distance is a prebuild method

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increse_score()

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score_board.reset()
        snake.reset()

    #detect collision of tail  and   detect collision of tail

    for segments in snake.segments[1:]:
        if segments==snake.head:
            pass
        elif snake.head.distance(segments)<10:
            score_board.reset()



screen.exitonclick()

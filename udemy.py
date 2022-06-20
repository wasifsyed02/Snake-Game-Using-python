import time
from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from  food import Food
screen=Screen()
screen.setup(width=600,height=700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

food=Food()

scoreboard=ScoreBoard()

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move_snake()
    #Detects collision with food.
    if snake.head.distance(food)<15:
        snake.extend()
        food.refresh()
        scoreboard.increaseScore()
    #Detects collision with wall.
    if  snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()
    #Detects collision with tail or body of sanke.
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            game_is_on=False
            scoreboard.game_over()
        
screen.exitonclick()
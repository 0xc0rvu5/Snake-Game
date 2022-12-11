import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from snake import Snake


#initialize global variables
FOOD = Food()
PLAY = True
SCOREBOARD = Scoreboard()
SCREEN = Screen()
SNAKE = Snake()


#create game window
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor('black')
SCREEN.title('My SNAKE Game')
SCREEN.tracer(0)


#connect keyboard strokes to snake movements
SCREEN.listen()
SCREEN.onkey(SNAKE.up, 'Up')
SCREEN.onkey(SNAKE.up, 'w')
SCREEN.onkey(SNAKE.down, 'Down')
SCREEN.onkey(SNAKE.down, 's')
SCREEN.onkey(SNAKE.left, 'Left')
SCREEN.onkey(SNAKE.left, 'a')
SCREEN.onkey(SNAKE.right, 'Right')
SCREEN.onkey(SNAKE.right, 'd')


#initiate game loop
try:
    while PLAY:
        SCREEN.update()
        time.sleep(.1)
        SNAKE.move()
        

        # detect collision with food
        if SNAKE.segments[0].distance(FOOD) < 15:
            FOOD.refresh()
            SNAKE.extend()
            SCOREBOARD.increase_score()


        # detect collision with wall
        if SNAKE.segments[0].xcor() > 280 or SNAKE.segments[0].xcor() < -280 or \
                SNAKE.segments[0].ycor() > 280 or SNAKE.segments[0].ycor() < -280:
            SCOREBOARD.game_over()
            PLAY = False
            

        # detect collision with tail
        for segment in SNAKE.segments[1:]:
            if SNAKE.segments[0].distance(segment) < 10:
                SCOREBOARD.game_over()
                PLAY = False

except KeyboardInterrupt:
    print('\nSee you later.')

SCREEN.exitonclick()
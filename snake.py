from turtle import Turtle


#initialize global variables
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        '''Creates initial snake.'''
        for i in STARTING_POSITIONS:
            self.add_segment(i)


    def add_segment(self, i):
        '''Add segment to snake when objective is achieved.'''
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(i)
        self.segments.append(new_segment)


    def extend(self):
        '''Special functionality as an extension to add_segment(i).'''
        self.add_segment(self.segments[-1].position())


    def move(self):
        '''Allow the snake to move.'''
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_FORWARD)


    def up(self):
        '''Move the snake up.'''
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)


    def down(self):
        '''Move the snake down.'''
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)


    def left(self):
        '''Move the snake left.'''
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)


    def right(self):
        '''Move the snake right.'''
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
from turtle import Turtle


#initialize global variables
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write(f'Score = {self.score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        '''Updates game scoreboard.'''
        self.write(f'Score = {self.score}', align=ALIGNMENT, font=FONT)


    def game_over(self):
        '''Displays "Game over."'''
        self.goto(0, 0)
        self.write('Game over.', align=ALIGNMENT, font=FONT)


    def increase_score(self):
        '''Add 1 to score then update_scoreboard().'''
        self.score += 1
        self.clear()
        self.update_scoreboard()
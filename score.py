from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(340, -410)
        self.write(f"Score: {self.score}", align='center', font=("Counier", 18, 'normal'))

    def add_score(self, point):
        self.score = point

from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier",18,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
    def update_scorebord(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w")as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scorebord()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.clear()
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def increse_score(self):
        self.score+=1
        self.update_scorebord()


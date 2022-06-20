from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,290)
        self.color("white")
        self.write(f"Score: {self.score}",align="center",font=("Ariel",24,"bold"))
        self.hideturtle()
    def increaseScore(self):
        self.score+=1;
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Ariel",24,"bold"))
    def game_over(self):
        self.goto(0,0)
        self.write("Gave Over!",align="center",font=("Ariel",24,"bold"))
       
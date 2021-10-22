from turtle import Turtle




class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(x=0, y=265)
        self.score_update()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.current_score}  High Score: {self.high_score}", False, align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.current_score += 1


    # def game_over(self):
    #     self.color("White")
    #     self.goto(x=0, y=0)
    #     self.write("Game over", False, align="center", font=("Arial", 18, "normal"))






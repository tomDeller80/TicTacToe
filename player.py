class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.score = 0
        self.won = False

    def add_point(self):
        self.score = self.score + 1
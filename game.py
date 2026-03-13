from matrix import Matrix as mtx
from player import Player as plr

class Game:

    def __init__(self):
        self.board = mtx()
        self.players = list()
        self.round = 1
        self.game_state = None

    def add_player(self, name, token):
        player = plr(name, token)
        self.players.append(player)
        return player

    def get_player(self, num):
        return self.players[(num - 1)]

    def get_winner(self):
        for player in self.players:
            if player.won:
                return player

    def display_token(self, token):
        if token == "X":
            return "❌"
        elif token == "O":
            return "⭕"
        else:
            return f"{token} "

    def get_board(self):
        board = "\n"
        tokens = self.board.matrix.flatten()
        for i in range(3):
            display = [tokens[j] if tokens[j] != " " else (j + 1) for j in range(i * 3, i * 3 + 3)]
            board += (f" {self.display_token(display[0])} | {self.display_token(display[1])} |"
                      f" {self.display_token(display[2])} \n")
            if i < 2:
                board+=("----+----+----\n")
        return board

    def available_cells(self):
        tokens = self.board.matrix.flatten()
        cells = [str(j + 1) for j in range(0, len(tokens)) if tokens[j] == " " ]
        return cells

    def make_move(self, token, num):
        if self.board.get_token(num) != " ":
            return False

        self.board.add_token(token=token, num=num)
        return True


    def check_win(self):
        if self.board.check_diag() or self.board.check_axis():
            self.game_state = 'win'
            self.round += 1
            return True

        return False

    def check_draw(self):
        if len(self.available_cells()) == 0:
            self.game_state = 'draw'
            self.round += 1
            return True

        return False

    def reset_game(self):
        self.game_state = None
        self.board.reset()


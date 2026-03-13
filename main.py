from rich.console import Console
from rich.panel import Panel, Text
from rich.align import Align
from rich.prompt import Prompt, IntPrompt
from game import Game
from art import *

console = Console()
tictactoe = Game()

def setup_game():

    tokens = ["X", "O"]

    for num in range(1,3):

        name = Prompt.ask(f"\nPlayer {num}, may I have your name?")

        if (num == 1):

            p1_token = Prompt.ask(
                prompt=f"\nPlayer 1, choose your side",
                choices=tokens,
                case_sensitive=False).upper()

            tokens.remove(p1_token)

            tictactoe.add_player(name,p1_token)

        else:

            tictactoe.add_player(name, tokens[0])

    console.print("\n")

    player1 = tictactoe.get_player(1)
    player2 = tictactoe.get_player(2)

    player1_token = tictactoe.display_token(player1.token)
    player2_token = tictactoe.display_token(player2.token)

    console.print(Panel(Text(text=f"{player1.name.title()} is {player1_token}. "
                        f"{player2.name.title()} is {player2_token}.", justify="center"
                        ),title="Setup Complete"))


def end_of_game(game_state):

    if game_state == 'win':
        winner = tictactoe.get_winner()
        console.print(Align.center(f"\n{winner.name.title()} has won!"))
        console.print(Align.center(trophy))

        winner.won = False #Reset

    elif game_state == 'draw':
        console.print(Align.center(draw))

    # Display score board
    player1 = tictactoe.get_player(1)
    player2 = tictactoe.get_player(2)

    player1_token = tictactoe.display_token(player1.token)
    player2_token = tictactoe.display_token(player2.token)

    console.print(Panel(Text(
        text=f"{player1.name.title()} ({player1_token}): {player1.score}. "
             f"{player2.name.title()} ({player2_token}): {player2.score}.",
        justify="center"),
        title="Score Board")
    )

    another_round = Prompt.ask(
        prompt="\nWould you like to play another round? (Y on N)",
        choices=['Y', 'N'],
        case_sensitive=False,
        show_choices=True).upper()

    if another_round == 'Y':
        tictactoe.reset_game()
        return False

    # End of game
    return True


def play_tictactoe():

   # Display Intro
   console.print(logo)
   console.rule("Welcome to Tic-Tac-Toe!")
   console.print(Panel("🎮 How to Play: To place your mark, "
               "simply type the number corresponding to the square you want to claim."))

   # Get player details
   setup_game()

   # Display Round
   console.rule(f"\nRound {tictactoe.round}")

   # Display Board
   console.print(Align.center(tictactoe.get_board()))

   # Play Game
   while True:

       for num in range(1, 3):

           player = tictactoe.get_player(num)

           display_token = tictactoe.display_token(player.token)

           available_cells = tictactoe.available_cells()

           # Request position selection
           position = IntPrompt.ask(
               prompt=f"\n{player.name.title()} ({display_token}), enter a position",
               choices=available_cells,
               show_choices=True)

           tictactoe.make_move(player.token, position)

           # Display Board
           console.print(Align.center(tictactoe.get_board()))

           # Check for win
           if tictactoe.check_win():
               player.score += 1
               player.won = True
               break

           # Check for draw
           elif tictactoe.check_draw():
               break

       # Check game state
       game_state = tictactoe.game_state

       if tictactoe.game_state:

           console.rule(f"\nEnd of round {tictactoe.round}")

           if not end_of_game(game_state):
               console.print("\n\n")
               console.rule(f"Round {tictactoe.round}")

               # Display Board
               console.print(Align.center(tictactoe.get_board()))
           else:
               break


# Initialise game
play_tictactoe()
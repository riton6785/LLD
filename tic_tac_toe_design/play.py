"""
===============================================================================
PlayGame  (Entry Point)
===============================================================================

Purpose
-------
play.py starts a game on the console and prints the result.

Workflow
--------
1. Create a TicTacToeGame.
2. initialize_game()  -> Player1 = X, Player2 = O, empty 3 x 3 board.
3. start_game()       -> players take turns until WIN or DRAW.
4. Print who won, or that it was a draw.

Example Session
---------------

===>>> TicTacToe Game

     |      |      |
     |      |      |
     |      |      |
Player: Player1 - Please enter [row, column]: 0,0
...
Player: Player1 - Please enter [row, column]: 0,2
X    | X    | X    |
O    | O    |      |
     |      |      |

===>>> GAME OVER: Player1 won the game

How to Run
----------
From the tic_tac_toe_design/ folder (the one containing this file):

    python3 play.py

Do not run the other files directly; they are modules meant to be
imported, and their imports only resolve from here.
===============================================================================
"""

from game import TicTacToeGame
from game_status import GameStatus


class PlayGame:
    """
    Console front end for TicTacToeGame.
    """

    @staticmethod
    def main():
        """
        Application entry point.
        """

        print("\n===>>> TicTacToe Game\n")

        game = TicTacToeGame()

        game.initialize_game()

        status = game.start_game()

        print("\n===>>> GAME OVER: ", end="")

        if status == GameStatus.WIN:
            print(
                game.winner.get_name()
                + " won the game"
            )

        elif status == GameStatus.DRAW:
            print("Its a Draw!")

        else:
            print("Game Ends")


if __name__ == "__main__":
    PlayGame.main()

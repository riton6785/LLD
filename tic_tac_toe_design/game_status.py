"""
===============================================================================
GameStatus (Enum)
===============================================================================

Purpose
-------
The result that TicTacToeGame.start_game() returns when the game ends:

    WIN   -> a player completed a row, column or diagonal
             (the player is stored in game.winner)
    DRAW  -> the board is full and nobody won

Why an Enum?
------------
The caller (PlayGame) decides what to print based on the result.
Returning True / False would lose meaning ("True" = win? = game over?),
and returning strings invites typos ("WON" vs "WIN").

    status = game.start_game()
    if status == GameStatus.WIN:
        ...

Extending
---------
A new ending (e.g. RESIGNED, TIMEOUT) is a new member here plus one
new branch in PlayGame.main().
===============================================================================
"""

from enum import Enum


class GameStatus(Enum):
    """
    How a finished game ended.
    """

    DRAW = "DRAW"
    WIN = "WIN"

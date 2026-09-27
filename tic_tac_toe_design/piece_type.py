"""
===============================================================================
PieceType (Enum)
===============================================================================

Purpose
-------
Every mark placed on the board is exactly one of two symbols:

    X  -> placed by PlayingPieceX
    O  -> placed by PlayingPieceO

The winner check compares these values: a line wins only if every cell
on it holds a piece with the SAME PieceType.

Problem Statement
-----------------
Suppose symbols were plain strings:

    PlayingPiece("x")      # lower-case!
    PlayingPiece("X")

"x" != "X", so a row of three crosses would never be seen as a win,
and nothing would report an error.

Solution
--------
An Enum defines a closed set of allowed values:

    PlayingPiece(PieceType.X)

Benefits
--------
1. Typos Fail Immediately
   PieceType.Y raises AttributeError right away.

2. Safe Comparisons
   check_for_winner() compares enum members, never raw strings.

3. Printable Symbol
   PieceType.X.value == "X" is what Board.print_board() shows.

Extending
---------
To support a third symbol (e.g. a 3-player variant with "Z"):

1. Add a member here.
2. Create PlayingPieceZ.
3. Add a third Player in TicTacToeGame.initialize_game().

The winner check itself does not change -> Open/Closed Principle.
===============================================================================
"""

from enum import Enum


class PieceType(Enum):
    """
    The closed set of symbols a piece can carry.
    """

    X = "X"
    O = "O"

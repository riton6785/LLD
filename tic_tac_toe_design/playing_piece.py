"""
===============================================================================
PlayingPiece  (Abstract Base Class)
===============================================================================

Purpose
-------
A PlayingPiece is the mark a player puts on the board. It only knows
its PieceType (X or O).

Hierarchy
---------

            PlayingPiece (abstract)
              /               \\
     PlayingPieceX       PlayingPieceO
     (PieceType.X)       (PieceType.O)

Why a Base Class?
-----------------
Board, Player and TicTacToeGame are written against PlayingPiece only.
They never check "is this an X or an O?" themselves; they just ask:

    piece.get_piece_type()

So a new kind of piece is a new subclass, and none of those classes
change.

Why Subclasses at All?
----------------------
PlayingPieceX() reads better than PlayingPiece(PieceType.X), and it is
the natural place to add per-piece behaviour later (a colour, an
image, a special move in a variant).
===============================================================================
"""

from abc import ABC

from piece_type import PieceType


class PlayingPiece(ABC):
    """
    Abstract base for every piece that can be placed on the board.
    """

    def __init__(self, piece_type: PieceType):
        """
        Args:
            piece_type (PieceType): Symbol this piece carries.
        """
        self.piece_type = piece_type

    def get_piece_type(self) -> PieceType:
        """
        Returns:
            PieceType: Symbol of this piece, used by the winner check.
        """
        return self.piece_type

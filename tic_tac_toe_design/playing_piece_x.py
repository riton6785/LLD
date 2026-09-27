"""
===============================================================================
PlayingPieceX  (Concrete Piece)
===============================================================================

Purpose
-------
The cross piece. Always carries PieceType.X.

    PlayingPieceX().get_piece_type()  ->  PieceType.X

Player1 is given this piece in TicTacToeGame.initialize_game().
===============================================================================
"""

from piece_type import PieceType
from playing_piece import PlayingPiece


class PlayingPieceX(PlayingPiece):
    """
    Concrete piece marked "X".
    """

    def __init__(self):
        super().__init__(PieceType.X)

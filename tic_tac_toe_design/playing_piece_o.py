"""
===============================================================================
PlayingPieceO  (Concrete Piece)
===============================================================================

Purpose
-------
The noughts piece. Always carries PieceType.O.

    PlayingPieceO().get_piece_type()  ->  PieceType.O

Player2 is given this piece in TicTacToeGame.initialize_game().
===============================================================================
"""

from piece_type import PieceType
from playing_piece import PlayingPiece


class PlayingPieceO(PlayingPiece):
    """
    Concrete piece marked "O".
    """

    def __init__(self):
        super().__init__(PieceType.O)

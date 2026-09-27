"""
===============================================================================
Player  (Entity)
===============================================================================

Purpose
-------
A Player is a name plus the piece they place on every turn.

    Player("Player1", PlayingPieceX())

Design Note
-----------
Player holds a PlayingPiece, not a PieceType or a raw "X". This is
composition: the player HAS a piece. Swapping sides is simply:

    player.set_playing_piece(PlayingPieceO())

The player has no game logic. Turn order and move validation belong
to TicTacToeGame; placing pieces belongs to Board.
===============================================================================
"""

from playing_piece import PlayingPiece


class Player:
    """
    A participant in the game and the piece they play with.
    """

    def __init__(self, name, playing_piece: PlayingPiece):
        """
        Args:
            name (str): Shown in prompts and in the final result.
            playing_piece (PlayingPiece): Piece placed on every move.
        """
        self.name = name
        self.playing_piece = playing_piece

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_playing_piece(self):
        return self.playing_piece

    def set_playing_piece(self, playing_piece: PlayingPiece):
        self.playing_piece = playing_piece

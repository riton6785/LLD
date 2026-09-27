"""
===============================================================================
Board
===============================================================================

Purpose
-------
The Board is an N x N grid. Each cell is either empty (None) or holds
one PlayingPiece.

    size = 3

          col 0   col 1   col 2
    row 0 [ X   ] [ None] [ None]
    row 1 [ None] [ O   ] [ None]
    row 2 [ None] [ None] [ None]

Responsibilities
----------------
1. Place a piece, refusing cells that are already taken  -> add_piece()
2. Report which cells are still empty                    -> get_free_cells()
3. Draw itself on the console                            -> print_board()

Not Its Responsibility
----------------------
The Board does NOT know about players, turns or winning. Those rules
live in TicTacToeGame. Keeping the board "dumb" means the same Board
could be reused for a different game on a grid (e.g. Connect Four).

Size
----
size is a constructor argument, so a 4 x 4 or 5 x 5 game only needs
Board(4) / Board(5) in TicTacToeGame.initialize_game().
===============================================================================
"""

from playing_piece import PlayingPiece


class Board:
    """
    N x N grid of cells, each empty (None) or holding a PlayingPiece.
    """

    def __init__(self, size):
        """
        Args:
            size (int): Number of rows (and columns).
        """
        self.size = size
        self.board: list[list[PlayingPiece | None]] = [
            [None] * size for _ in range(size)
        ]


    def add_piece(self, row, column, playing_piece: PlayingPiece):
        """
        Places a piece on an empty cell.

        Args:
            row (int): 0-based row index.
            column (int): 0-based column index.
            playing_piece (PlayingPiece): Piece to place.

        Returns:
            bool: True if placed, False if the cell was already taken.
        """

        if self.board[row][column] is not None:
            return False

        self.board[row][column] = playing_piece
        return True

    def get_free_cells(self):
        """
        Returns:
            list[tuple[int, int]]: (row, column) of every empty cell.
            An empty list means the board is full.
        """

        free_cells = []

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    free_cells.append((i, j))

        return free_cells

    def print_board(self):
        """
        Prints the grid, one row per line, cells separated by " | ".
        """

        for i in range(self.size):
            for j in range(self.size):

                if self.board[i][j] is not None:
                    print(
                        self.board[i][j].piece_type.value,
                        end="   "
                    )
                else:
                    print("    ", end="")

                print(" | ", end="")

            print()

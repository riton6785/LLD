"""
===============================================================================
TicTacToeGame  (Game Controller)
===============================================================================

Purpose
-------
TicTacToeGame owns the RULES of the game:

    - who plays next            (turn order)
    - whether a move is legal   (cell exists and is empty)
    - whether a move wins       (row, column, diagonal, anti-diagonal)
    - when the game is a draw   (board full, no winner)

Board only stores pieces; Player only holds a name and a piece.
Everything that makes it "tic-tac-toe" lives here.

Turn Order with a Queue
-----------------------
Players sit in a deque. Each turn:

    1. popleft()      -> the player whose turn it is
    2. try the move
    3. valid move     -> append()      (goes to the back of the line)
       invalid move   -> appendleft()  (same player tries again)

    [P1, P2]  -> P1 plays  -> [P2, P1]  -> P2 plays  -> [P1, P2] ...

This works unchanged for 3 or more players.

Winner Check in O(n)
--------------------
Only the LAST move can create a win, so only the lines through that
cell are checked, not the whole board:

    move at (row, col)
      -> row `row`                       n cells
      -> column `col`                    n cells
      -> main diagonal   (i, i)          n cells
      -> anti-diagonal   (i, n - 1 - i)  n cells

At most 4n comparisons per move instead of scanning every line.

Note: the diagonals are checked even when the move is not on them.
That is still correct: a diagonal the move is not on cannot be full of
the current player's pieces without having already won on an earlier
turn, which would have ended the game.

Input Format
------------
Players type "row,column" with 0-based indexes, e.g. "1,2".
Anything else (wrong format, out of range, taken cell) prints a
message and the same player is asked again.
===============================================================================
"""

from collections import deque

from board import Board
from game_status import GameStatus
from piece_type import PieceType
from player import Player
from playing_piece_o import PlayingPieceO
from playing_piece_x import PlayingPieceX


class TicTacToeGame:
    """
    Sets up the players and board, runs the turn loop and decides the result.
    """

    def __init__(self):
        self.players = deque()
        self.game_board = None
        self.winner = None

    def initialize_game(self):
        """
        Creates two players (X and O) and an empty 3 x 3 board.
        """

        # Creating 2 Players
        self.players = deque()

        cross_piece = PlayingPieceX()
        player1 = Player("Player1", cross_piece)

        noughts_piece = PlayingPieceO()
        player2 = Player("Player2", noughts_piece)

        self.players.append(player1)
        self.players.append(player2)

        # Initialize Board of size 3
        self.game_board = Board(3)

    def start_game(self):
        """
        Runs turns until someone wins or the board is full.

        Returns:
            GameStatus: WIN (winner stored in self.winner) or DRAW.
        """

        no_winner = True

        while no_winner:

            # Remove the player whose turn it is
            # and put the player back later
            current_player = self.players.popleft()

            # Get the free spaces from the board
            self.game_board.print_board()

            free_spaces = self.game_board.get_free_cells()

            if not free_spaces:
                no_winner = False
                continue

            # Read the user input
            print(
                f"Player: {current_player.get_name()} "
                f"- Please enter [row, column]: ",
                end=""
            )

            user_input = input()

            move = self.parse_move(user_input)

            if move is None:
                print(
                    f"Invalid input, enter row,column between "
                    f"0 and {self.game_board.size - 1} (e.g. 1,2)"
                )

                # Same player tries again
                self.players.appendleft(current_player)

                continue

            input_row, input_column = move

            # Place the piece in the board
            valid_move = self.game_board.add_piece(
                input_row,
                input_column,
                current_player.get_playing_piece()
            )

            if not valid_move:

                # Invalid Move
                print("Incorrect position chosen, try again!")

                # Add player back to the front of the queue
                self.players.appendleft(current_player)

                continue

            # Add player to the end of the queue
            self.players.append(current_player)

            # Check if the valid move is a winning move
            is_winner = self.check_for_winner(
                input_row,
                input_column,
                current_player.get_playing_piece().get_piece_type()
            )

            if is_winner:

                self.game_board.print_board()

                self.winner = current_player

                return GameStatus.WIN

        return GameStatus.DRAW

    def parse_move(self, user_input):
        """
        Turns "row,column" into a pair of in-range indexes.

        Negative indexes are rejected on purpose: Python would accept
        board[-1] and silently place the piece on the last row.

        Args:
            user_input (str): Raw text typed by the player.

        Returns:
            tuple[int, int] | None: (row, column), or None if invalid.
        """

        values = user_input.split(",")

        if len(values) != 2:
            return None

        try:
            row = int(values[0])
            column = int(values[1])
        except ValueError:
            return None

        size = self.game_board.size

        if not (0 <= row < size and 0 <= column < size):
            return None

        return row, column

    def check_for_winner(self, row, column, piece_type: PieceType):
        """
        Checks the lines through the last move.

        Args:
            row (int): Row of the last move.
            column (int): Column of the last move.
            piece_type (PieceType): Symbol of the player who moved.

        Returns:
            bool: True if any of the four lines is full of piece_type.
        """

        row_match = True
        column_match = True
        diagonal_match = True
        anti_diagonal_match = True

        # Check Row
        for i in range(self.game_board.size):

            piece = self.game_board.board[row][i]

            if piece is None or piece.get_piece_type() != piece_type:
                row_match = False
                break

        # Check Column
        for i in range(self.game_board.size):

            piece = self.game_board.board[i][column]

            if piece is None or piece.get_piece_type() != piece_type:
                column_match = False
                break

        # Check Diagonally
        for i in range(self.game_board.size):

            piece = self.game_board.board[i][i]

            if piece is None or piece.get_piece_type() != piece_type:
                diagonal_match = False
                break

        # Check Anti-Diagonally
        for i in range(self.game_board.size):

            j = self.game_board.size - 1 - i

            piece = self.game_board.board[i][j]

            if piece is None or piece.get_piece_type() != piece_type:
                anti_diagonal_match = False
                break

        return (
            row_match
            or column_match
            or diagonal_match
            or anti_diagonal_match
        )

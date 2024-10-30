.. tictactoe_fc2786 documentation master file, created by
   sphinx-quickstart on Tue Oct 29 20:38:26 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

tictactoe_fc2786 documentation
==============================

Welcome to the documentation for the `tictactoe_fc2786` package, a toolset for managing Tic-Tac-Toe gameplay functions.

Getting Started
---------------
To begin using the `tictactoe_fc2786` package, import the functions and initialize a game board. Here’s a simple example:

.. code-block:: python

   from tictactoe_fc2786 import initialize_board, make_move, check_winner, reset_game

   # Initialize the game board
   board = initialize_board()

   # Make example moves
   make_move(board, 0, 0, 'X')
   make_move(board, 1, 1, 'O')

   # Check for a winner
   winner = check_winner(board)
   if winner:
       print(f"Winner: {winner}")
   else:
       print("No winner yet.")

Function Overview
-----------------
- **initialize_board()**: Creates a 3x3 Tic-Tac-Toe board initialized with empty spaces.
- **make_move(board, row, col, player)**: Places the player's symbol ('X' or 'O') on the board at the specified position.
- **check_winner(board)**: Checks the board for a winner or if it’s a draw.
- **reset_game()**: Resets the game by reinitializing the board.
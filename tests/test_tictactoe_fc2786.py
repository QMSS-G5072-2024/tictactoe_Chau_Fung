from tictactoe_fc2786 import initialize_board, make_move

def test_initialize_board():
    """Verify the `initialize_board` function creates an empty 3x3 board."""
    board = initialize_board()
    assert len(board) == 3  # Check if number of rows = 3
    assert all(len(row) == 3 for row in board)  # Check the number of columns in each row
    assert all(cell == ' ' for row in board for cell in row)  # Check if all cells are empty

def test_make_move_valid():
    """Check whether make_move successfully places a player’s symbol on an empty cell."""
    board = initialize_board()
    assert make_move(board, 0, 0, 'X')  # Make a valid move with X
    assert board[0][0] == 'X'  # Check that 'X' is placed correctly
    assert make_move(board, 1, 1, 'O')  # Make another valid move with O
    assert board[1][1] == 'O'  # Check that 'O' is placed correctly

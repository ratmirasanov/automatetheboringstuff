def print_board(board):

    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


THE_BOARD = {"top-L": " ", "top-M": " ", "top-R": " ",
             "mid-L": " ", "mid-M": " ", "mid-R": " ",
             "low-L": " ", "low-M": " ", "low-R": " "}

TURN = "X"

for i in range(9):

    print_board(THE_BOARD)
    print("Turn for " + TURN + ". Move on which space?")
    move = input()
    THE_BOARD[move] = TURN

    if TURN == "X":

        TURN = "O"

    else:

        TURN = "X"

print_board(THE_BOARD)

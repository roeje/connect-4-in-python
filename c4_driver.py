from c4_engine import *

g1 = Game(6, 8, 3)
g1.board[0][0] = 1
g1.board[1][1] = 1
g1.board[2][1] = 1


print type(g1.board)

g1.print_formated()

print g1.check_full_board()


# g1.print_formated()
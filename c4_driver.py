from c4_engine import *

g1 = Game(6, 8, 3)
g1.board[0][0] = 1
g1.board[0][1] = 1
g1.board[1][1] = 1
g1.board[2][1] = 1
# g1.board[3][1] = 1
# g1.board[4][1] = 1
# g1.board[5][1] = 1

print g1.place_token(1, 1)
print g1.place_token(1, 1)
print g1.place_token(1, 1)
print g1.place_token(1, 2)

print g1.place_token(1, 7)



print type(g1.board)

g1.print_formated()

print g1.check_full_board()
print g1.check_for_col_height(1)

# g1.print_formated()
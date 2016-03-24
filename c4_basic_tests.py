g1 = Game(6, 8, 3)
g1.board[0][0] = 1
g1.board[0][1] = 0
g1.board[1][1] = 0
g1.board[2][1] = 0
# g1.board[3][1] = 1
# g1.board[4][1] = 1
# g1.board[5][1] = 1

# print g1.place_token(1, 1)
# print g1.place_token(1, 2)
# print g1.place_token(1, 7)
# print g1.place_token(1, 0)
# print g1.place_token(1, 0)
# print g1.place_token(1, 2)
# print g1.place_token(1, 2)
# print g1.place_token(1, 2)

print "checking for the height of col 1"
print g1.check_for_col_height(1)

print "checking for full board"
print g1.check_full_board()

print "Testing Hor:"
print g1.check_hor()
print "Testing Vert:"
print g1.check_ver()
print "Testing Diag Right"
print g1.check_diag_right()
print "Testing Diag Left"
print g1.check_diag_left()

print "checking winner"
print g1.check_winner()

print type(g1.board)

g1.print_formated()


print "Testing IO:"

io = IO()

io.save_obj(g1, "testFile.txt", "w")

g2 = io.load_obj("testFile.txt")

print g2

g2.print_formated()


print test
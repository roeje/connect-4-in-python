
# from prettytable import PrettyTable

class Game:	
	board = 0
	height = 0
	width = 0
	row_len = 0
	def __init__ ( self, height, width, row_len ):
		Game.height = height
		Game.width = width
		Game.row_len = row_len		

		b = lambda h, w: [[-1] * w for i in range(h)]		
		Game.board = b(height, width)


	def print_formated (self):
		# x = lambda b: for row in b: print row		

		print "--------------------------------------------"

		for row in reversed(range(self.height)):
			for cell in range(self.width):
				if (self.board[row][cell] == 1 or self.board[row][cell] == 0):
					print "|  %d" % (self.board[row][cell]),
				else:	
					print "| %d" % (self.board[row][cell]),
			print "|"	

		print "--------------------------------------------"

	def check_full_board (self):
		for row in self.board:
			for cell in row:
				if (cell == -1):
					return False
		return True		
					
	def check_for_col_height (self, col):
		for row in reversed(range(self.height)):
			if (board[row][col] == -1):
				return row
		return -1

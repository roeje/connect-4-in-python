

class Game:	

	# board = 0
	# height = 0
	# width = 0
	# row_len = 0

	def __init__ ( self, height, width, row_len ):
		self.height = height
		self.width = width
		self.row_len = row_len	
		b = lambda h, w: [[-1] * w for i in range(h)]		
		self.board = b(height, width)

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
		for row in range(self.height):
			if (self.board[row][col] == -1):
				return row
		return -1

	def place_token (self, player, col):
		if (col > (self.width - 1) or col < 0 or player > 1 or player < 0):
			return False
		open_row = self.check_for_col_height(col)
		if (open_row == -1):
			return False
		else:
			self.board[open_row][col] = player
			return True

	def check_hor (self):
		for row in range(self.height):	
			for cell in range(self.width - (self.row_len - 1)):				
				series = 0
				for i in range(self.row_len):
					if (self.board[row][cell] != -1 and self.board[row][cell] != self.board[row][cell + i]):
						 series += 1					
				if (series == (self.row_len - 1)):
					return self.board[row][cell]
		return -1		

	def check_ver (self):
		for row in range(self.height):
			print row
			for cell in range(self.width - (self.row_len - 1)):
				print cell
				series = 0
				for i in range(self.row_len):
					if (self.board[row][cell] != -1 and self.board[row][cell] != self.board[row][cell + i]):
						 series += 1					
				if (series == (self.row_len - 1)):
					return self.board[row][cell]
		return -1			

	
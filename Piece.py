class Piece:
	def __init__(self, piece_type, color, position):
		'''A position is a string of 2 numbers. The first number is the row, the second is a column.
		For example, the black rooks' positions would be "00" and "07" '''
		self.piece_type = piece_type
		self.color = color
		self.position = position
		self.up_two = False #pawns only. If a pawn moves up two, under the right conditions it can be en passanted
		self.en_passant = False #pawns only
	
	def print_piece(self):
		print(str(self.color) + " " + str(self.piece_type), end = "")

	def enemy_in_check(self, curr_Board, pos, king_position): #TODO: 180+ line function ... might want to break pieces up into different classes
		'''pass in position and king_position as a string of two numbers, representing 
			where the pieces are on the board. Checks to see if enemy is in check'''
		row = (int(pos[0]))
		col = (int(pos[1]))
		king_row = int(king_position[0])
		king_col = int(king_position[1])
		
		if (self.piece_type == "Bish"):

			sight_line_back_left = [(row + x, col - x) for x in range(8)]
			''' checks all spots on the diagonal behind and to the left. Worse case scanario,
			king on A1 and Bishop on H8, which is 7 spots. That's why it is in range(8) '''

			sight_line_forward_right = [(row - x, col + x) for x in range(8)]
			'''Checks diagonal forward and right. Worse case, King on H8, Bishop on A1 '''

			sight_line_back_right = [(row + x, col + x) for x in range(8)]
			''' Worst case, King H1, Bishop A8 '''

			sight_line_forward_left =[(row - x, col - x) for x in range(8)]
			''' Worst case, Bishop H1, King A8 '''


			for p in sight_line_back_left:
				if (p == (king_row, king_col)): # if a possible position is equal to the king position
					for x in range(1, col - king_col): #checks to see if a piece is in the way
						if (curr_Board.pieces[king_row - x][king_col + x] != 0):
							return False
					return True 

			for p in sight_line_forward_right:
				if (p == (king_row, king_col)):
					for x in range(1, king_col - col):
						if (curr_Board.pieces[king_row + x][king_col - x] != 0):
							return False
					return True
			
			for p in sight_line_back_right:
				if (p == (king_row, king_col)):
					for x in range(1, row - king_row):
						if (curr_Board.pieces[king_row - x][king_col - x] != 0):
							return False
					return True
			
			for p in sight_line_forward_left:
				if (p == (king_row, king_col)):
					for x in range(1, col - king_col):
						if (curr_Board.pieces[king_row + x][king_col + x] != 0):
							return False
					return True

			return False #King is not in any sightline.

		if (self.piece_type == "Rook"):
			
			sight_line_back = [(row + x, col) for x in range(8)]
			''' Checks spots in front of rook. Worst case, Rook on 1st row and King on 8th,
			which is 7 spots. That is why it is range(8) '''

			sight_line_front = [(row - x, col) for x in range(8)]
			'''Worst case, Rook on 8th row, King on 1st '''

			sight_line_right = [(row, col + x) for x in range(8)]
			'''Worst case, Rook on A file and King on H file '''

			sight_line_left = [(row, col - x) for x in range(8)]
			'''Worst case, Rook on H file, King on A file '''


			for p in sight_line_front:
				if (p == (king_row, king_col)):
					for x in range(1, row - king_row): #checks to see if a piece is in the way
						if (curr_Board.pieces[king_row + x][king_col] != 0):
							return False
					return True 

			for p in sight_line_back:
				if (p == (king_row, king_col)):
					for x in range(1, king_row - row): 
						if (curr_Board.pieces[king_row - x][king_col] != 0):
							return False
					return True 

			for p in sight_line_right:
				if (p == (king_row, king_col)):
					for x in range(1, king_col - col): 
						if (curr_Board.pieces[king_row][king_col - x] != 0):
							return False
					return True

			for p in sight_line_left:
				if (p == (king_row, king_col)):
					for x in range(1, col - king_col): 
						if (curr_Board.pieces[king_row][king_col + x] != 0):
							return False
					return True
			
			return False

		if (self.piece_type == "Quen"): #Literally just copy and paste code from bishop + rook
			
			sight_line_back_left = [(row + x, col - x) for x in range(8)]
			sight_line_forward_right = [(row - x, col + x) for x in range(8)]
			sight_line_back_right = [(row + x, col + x) for x in range(8)]
			sight_line_forward_left =[(row - x, col - x) for x in range(8)]
			sight_line_back = [(row + x, col) for x in range(8)]
			sight_line_front = [(row - x, col) for x in range(8)]
			sight_line_right = [(row, col + x) for x in range(8)]
			sight_line_left = [(row, col - x) for x in range(8)]

			for p in sight_line_back_left:
				if (p == (king_row, king_col)): # if a possible position is equal to the king position
					for x in range(1, col - king_col): #checks to see if a piece is in the way
						if (curr_Board.pieces[king_row - x][king_col + x] != 0):
							return False
					return True 

			for p in sight_line_forward_right:
				if (p == (king_row, king_col)):
					for x in range(1, king_col - col):
						if (curr_Board.pieces[king_row + x][king_col - x] != 0):
							return False
					return True
			
			for p in sight_line_back_right:
				if (p == (king_row, king_col)):
					for x in range(1, row - king_row):
						if (curr_Board.pieces[king_row - x][king_col - x] != 0):
							return False
					return True
			
			for p in sight_line_forward_left:
				if (p == (king_row, king_col)):
					for x in range(1, col - king_col):
						if (curr_Board.pieces[king_row + x][king_col + x] != 0):
							return False
					return True
			for p in sight_line_front:
				if (p == (king_row, king_col)):
					for x in range(1, row - king_row): #checks to see if a piece is in the way
						if (curr_Board.pieces[king_row + x][king_col] != 0):
							return False
					return True 

			for p in sight_line_back:
				if (p == (king_row, king_col)):
					for x in range(1, king_row - row): 
						if (curr_Board.pieces[king_row - x][king_col] != 0):
							return False
					return True 

			for p in sight_line_right:
				if (p == (king_row, king_col)):
					for x in range(1, king_col - col): 
						if (curr_Board.pieces[king_row][king_col - x] != 0):
							return False
					return True

			for p in sight_line_left:
				if (p == (king_row, king_col)):
					for x in range(1, col - king_col): 
						if (curr_Board.pieces[king_row][king_col + x] != 0):
							return False
					return True

			return False
					
		if (self.piece_type == "Pawn"):	
			if (self.color == "W"): #checking "in front of" pawn works differently based on color
				if ((king_position == (str(row - 1) + str(col + 1))) \
				 or (king_position == (str(row - 1) + str(col- 1)))):
					return True
				else:
					return False

			if (self.color == "B"):
				if ((king_position == (str(row + 1) + str(col + 1))) \
				 or (king_position == (str(row + 1) + str(col - 1)))):
					return True
				else:
					return False

			return False
		
		if (self.piece_type == "King"): # a king will never give check, but I use this for checking move legality
			
			sight_line = [(row, col + 1), (row + 1, col + 1),(row - 1, col + 1), # bad coding practice alert
			(row + 1, col),(row - 1, col), (row, col - 1),(row + 1, col - 1), (row - 1, col - 1) ]

			for p in sight_line:
				if (p == (king_row, king_col)):
					return True
			
			return False

		if (self.piece_type == "Nite"):
			sight_line = [(row + 2, col + 1), (row - 2, col + 1), (row + 2, col - 1), (row - 2, col - 1),
			(row + 1, col + 2), (row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)]

			for p in sight_line:
				if (p == (king_row, king_col)):
					return True
			
			return False 

	
	def legal(self, curr_Board, old, new):
		'''Checks to see if a move is legal in terms of piece collisions and squares the piece wants to move to.
		Checking whether a king is moving into check or if a piece is pinned is a separate function. This 
		function takes in a board, the old position of the moving piece as a 2 number string, the first
		number being the row and the second being the column, and finally the new square the piece will
		be moving to represented as a two number string, like the old parameter.'''

		old_row = int(old[0])
		old_col = int(old[1])
		new_row = int(new[0])
		new_col = int(new[1])
		
		if (self.piece_type == "Pawn"): #TODO: en passant
			if (self.color == "B"):
				if (old_col == new_col and (old_row == new_row - 1)): #can move forward one space
					if (curr_Board.pieces[new_row][new_col]) == 0: #only move if empty square
						return True
				if (old_col + 1 == new_col and (old_row == new_row - 1)): #take up and right
					if ((curr_Board.pieces[new_row][new_col]) != 0): #can only take if a piece is there
						if ((curr_Board.pieces[new_row][new_col].color) == "W"): # must be other color piece
							return True
				if (old_col + 1 == new_col and (old_row == new_row - 1)): #En passant. Didn't want to make other
					if (curr_Board.pieces[old_row][old_col + 1] != 0):
						if (curr_Board.pieces[old_row][old_col + 1].up_two == True): #expression too long with 
							if ((curr_Board.pieces[old_row][old_col + 1].color) == "W"): # an 'or'
								curr_Board.pieces[old_row][old_col].en_passant = True #the pawn is performing an 
								return True												#en passant
				if ((old_col - 1 == new_col) and (old_row == new_row - 1)): #take up and left
					if ((curr_Board.pieces[new_row][new_col]) != 0): #can only take if a piece is there
						if ((curr_Board.pieces[new_row][new_col]).color == "W"):
							return True
				if (old_col - 1 == new_col and (old_row == new_row - 1)): #En passant up left
					if (curr_Board.pieces[old_row][old_col - 1] != 0):
						if (curr_Board.pieces[old_row][old_col - 1].up_two == True): 
							if ((curr_Board.pieces[new_row][new_col].color) == "W"): 
								curr_Board.pieces[old_row][old_col].en_passant = True
								return True
				if ((old[0] == "1") and (old_col == new_col) and (old_row == new_row - 2)): #can move up two if on original row
					if ((curr_Board.pieces[new_row][new_col]) == 0):
						if ((curr_Board.pieces[new_row - 1][new_col]) == 0):
							return True
				
				return False

			if (self.color == "W"):
				if (old_col == new_col) and (old_row == new_row + 1): #can move forward one space
					if ((curr_Board.pieces[new_row][new_col]) == 0): #only move if empty square
						return True
				if (old_col + 1 == new_col) and (old_row == new_row + 1): #take up and right
					if ((curr_Board.pieces[new_row][new_col]) != 0): #can only take if a piece is there
						if ((curr_Board.pieces[new_row][new_col]).color == "B"):
							return True
				if (old_col + 1 == new_col) and (old_row == new_row + 1): #en passant up right
					if (curr_Board.pieces[old_row][old_col + 1] != 0):
						if (curr_Board.pieces[old_row][old_col + 1].up_two):
							if ((curr_Board.pieces[old_row][old_col + 1]).color == "B"):
								curr_Board.pieces[old_row][old_col].en_passant = True
								return True
				if (old_col - 1 == new_col) and (old_row == new_row + 1): #take up and left
					if ((curr_Board.pieces[new_row][new_col]) != 0): #can only take if a piece is there
						if ((curr_Board.pieces[new_row][new_col]).color == "B"):
							return True
				if (old_col - 1 == new_col) and (old_row == new_row + 1): #en passant up left
					if (curr_Board.pieces[old_row][old_col - 1] != 0):
						if (curr_Board.pieces[old_row][old_col - 1].up_two):
							if ((curr_Board.pieces[old_row][old_col - 1]).color == "B"):
								curr_Board.pieces[old_row][old_col].en_passant = True
								return True
				if ((old[0] == "6") and (old_col == new_col) and (old_row == new_row + 2)): #can move up two if on original row
					if ((curr_Board.pieces[new_row][new_col]) == 0): #both rows inbetween must be empty
						if ((curr_Board.pieces[new_row + 1][new_col]) == 0):
							return True
				return False
		
		if (self.piece_type == "Bish"):
			sight_line_back_left = [(old_row + x, old_col - x) for x in range(8)] # copied from check method
			sight_line_forward_right = [(old_row - x, old_col + x) for x in range(8)]
			sight_line_back_right = [(old_row + x, old_col + x) for x in range(8)]
			sight_line_forward_left =[(old_row - x, old_col - x) for x in range(8)]


			if (new_row, new_col) not in sight_line_back_left and (new_row, new_col) not in sight_line_forward_right \
				and (new_row, new_col) not in sight_line_forward_left and (new_row, new_col) not in sight_line_back_right:
				return False  # if move not in sight line, it is illegal

			if ((curr_Board.pieces[new_row][new_col]) != 0 and (curr_Board.pieces[new_row][new_col].color \
				== self.color)): #cannot take your own piece
				return False


			for p in sight_line_back_left:
				if (p == (new_row, new_col)):
					for x in range(1, old_col - new_col): #checks to see if a piece is in the way
						if (curr_Board.pieces[new_row - x][new_col + x] != 0):
							return False
					return True 

			for p in sight_line_forward_right:
				if (p == (new_row, new_col)):
					for x in range(1, new_col - old_col):
						if (curr_Board.pieces[new_row + x][new_col - x] != 0):
							return False
					return True
			
			for p in sight_line_back_right:
				if (p == (new_row, new_col)):
					for x in range(1, new_col - old_col):
						if (curr_Board.pieces[new_row - x][new_col - x] != 0):
							return False
					return True

			for p in sight_line_forward_left:
				if (p == (new_row, new_col)):
					for x in range(1, old_col - new_col):
						if (curr_Board.pieces[new_row + x][new_col + x] != 0):
							return False
					return True
		
		if (self.piece_type == "Rook"):
			sight_line_back = [(old_row + x, old_col) for x in range(8)] #taken from check function
			sight_line_front = [(old_row - x, old_col) for x in range(8)]
			sight_line_right = [(old_row, old_col + x) for x in range(8)]
			sight_line_left = [(old_row, old_col - x) for x in range(8)]


			if ((new_row, new_col) not in sight_line_back and (new_row, new_col) not in sight_line_front \
				and (new_row, new_col) not in sight_line_right and (new_row, new_col) not in sight_line_left):
				return False  # if move not in sight line, it is illegal

			if ((curr_Board.pieces[new_row][new_col]) != 0 and (curr_Board.pieces[new_row][new_col].color \
				== self.color)): #cannot take your own piece
				return False

			for p in sight_line_front:
				if (p == (new_row, new_col)):
					for x in range(1, old_row - new_row): #checks to see if a piece is in the way
						if (curr_Board.pieces[new_row + x][new_col] != 0):
							return False
					return True 

			for p in sight_line_back:
				if (p == (new_row, new_col)):
					for x in range(1, new_row - old_row): 
						if (curr_Board.pieces[new_row - x][new_col] != 0):
							return False
					return True 

			for p in sight_line_right:
				if (p == (new_row, new_col)):
					for x in range(1, new_col - old_col): 
						if (curr_Board.pieces[new_row][new_col - x] != 0):
							return False
					return True

			for p in sight_line_left:
				if (p == (new_row, new_col)):
					for x in range(1, old_col - new_col): 
						if (curr_Board.pieces[new_row][new_col + x] != 0):
							return False
					return True
		
		if (self.piece_type == "Quen"): #again, just bishop + rook
			sight_line_back = [(old_row + x, old_col) for x in range(8)] 
			sight_line_front = [(old_row - x, old_col) for x in range(8)]
			sight_line_right = [(old_row, old_col + x) for x in range(8)]
			sight_line_left = [(old_row, old_col - x) for x in range(8)]
			sight_line_back_left = [(old_row + x, old_col - x) for x in range(8)] # copied from check method
			sight_line_forward_right = [(old_row - x, old_col + x) for x in range(8)]
			sight_line_back_right = [(old_row + x, old_col + x) for x in range(8)]
			sight_line_forward_left =[(old_row - x, old_col - x) for x in range(8)]


			if (new_row, new_col) not in sight_line_back and (new_row, new_col) not in sight_line_right \
				and (new_row, new_col) not in sight_line_left and (new_row, new_col) not in sight_line_front:
				if (new_row, new_col) not in sight_line_back_left and (new_row, new_col) not in sight_line_forward_right \
				and (new_row, new_col) not in sight_line_forward_left and (new_row, new_col) not in sight_line_back_right:
					return False  # if move not in sight line, it is illegal
				

			if ((curr_Board.pieces[new_row][new_col]) != 0 and (curr_Board.pieces[new_row][new_col].color \
				== self.color)): #cannot take your own piece
				return False

			for p in sight_line_front:
				if (p == (new_row, new_col)):
					for x in range(1, old_row - new_row): #checks to see if a piece is in the way
						if (curr_Board.pieces[new_row + x][new_col] != 0):
							return False
					return True 

			for p in sight_line_back:
				if (p == (new_row, new_col)):
					for x in range(1, new_row - old_row): 
						if (curr_Board.pieces[new_row - x][new_col] != 0):
							return False
					return True 

			for p in sight_line_right:
				if (p == (new_row, new_col)):
					for x in range(1, new_col - old_col): 
						if (curr_Board.pieces[new_row][new_col - x] != 0):
							return False
					return True

			for p in sight_line_left:
				if (p == (new_row, new_col)):
					for x in range(1, old_col - new_col): 
						if (curr_Board.pieces[new_row][new_col + x] != 0):
							return False
					return True
			for p in sight_line_back_left:
				if (p == (new_row, new_col)):
					for x in range(1, old_col - new_col): #checks to see if a piece is in the way
						if (curr_Board.pieces[new_row - x][new_col + x] != 0):
							return False
					return True 

			for p in sight_line_forward_right:
				if (p == (new_row, new_col)):
					for x in range(1, new_col - old_col):
						if (curr_Board.pieces[new_row + x][new_col - x] != 0):
							return False
					return True
			
			for p in sight_line_back_right:
				if (p == (new_row, new_col)):
					for x in range(1, new_col - old_col):
						if (curr_Board.pieces[new_row - x][new_col - x] != 0):
							return False
					return True

			for p in sight_line_forward_left:
				if (p == (new_row, new_col)):
					for x in range(1, old_col - new_col):
						if (curr_Board.pieces[new_row + x][new_col + x] != 0):
							return False
					return True

		if (self.piece_type == "Nite"):
			
			sight_line = [(old_row + 2, old_col + 1), (old_row - 2, old_col + 1), (old_row + 2, old_col - 1), (old_row - 2, old_col - 1),
			(old_row + 1, old_col + 2), (old_row + 1, old_col - 2), (old_row - 1, old_col + 2), (old_row - 1, old_col - 2)]

			if (new_row, new_col) not in sight_line:
				return False
			if ((curr_Board.pieces[new_row][new_col] != 0) and curr_Board.pieces[new_row][new_col].color == self.color):
				return False #if the square is occupied by one of your pieces, can't move there
			return True

		if (self.piece_type == "King"):
			sight_line = [(old_row, old_col + 1), (old_row + 1, old_col + 1),(old_row - 1, old_col + 1), # bad coding practice alert
			(old_row + 1, old_col),(old_row - 1, old_col), (old_row, old_col - 1),(old_row + 1, old_col - 1), (old_row - 1, old_col - 1) ]

			if (self.color == "W"): #castling
				if ((not curr_Board.wt_king_moved) and (not curr_Board.wt_lf_rook_moved)): # castling long for white, so rook and king have not moved
					if (curr_Board.pieces[7][1] == 0 and curr_Board.pieces[7][2] == 0 and curr_Board.pieces[7][3] == 0): # no pieces in the way
						if (new_row == old_row and new_col == old_col - 2): # if attempting the castle
							if (not curr_Board.player2.check(curr_Board)): #player 2 not giving check
								curr_Board.move("E1", "D1")
								if (curr_Board.player2.check(curr_Board)): #player 2 giving check one over, so would be castling through check
									curr_Board.move("D1", "E1")
									return False
								curr_Board.move("D1", "E1")	
								return True
				if ((not curr_Board.wt_king_moved) and (not curr_Board.wt_rt_rook_moved)): # castling short for white, so rook and king have not moved
					if (curr_Board.pieces[7][5] == 0 and curr_Board.pieces[7][6] == 0): # no pieces in the way
						if (new_row == old_row and new_col == old_col + 2): # if attempting the castle
							if (not curr_Board.player2.check(curr_Board)): #player 2 not giving check
								curr_Board.move("E1", "F1")
								if (curr_Board.player2.check(curr_Board)): #player 2 giving check one over, so would be castling through check
									curr_Board.move("F1", "E1")
									return False
								curr_Board.move("F1", "E1")	
								return True

			if (self.color == "B"):
				if ((not curr_Board.bl_king_moved) and (not curr_Board.bl_lf_rook_moved)): # castling long for black, so rook and king have not moved
					if (curr_Board.pieces[0][1] == 0 and curr_Board.pieces[0][2] == 0 and curr_Board.pieces[0][3] == 0): # no pieces in the way
						if (new_row == old_row and new_col == old_col - 2): # if attempting the castle
							if (not curr_Board.player1.check(curr_Board)): #player 1 not giving check
								curr_Board.move("E8", "D8")
								if (curr_Board.player2.check(curr_Board)): #player 2 giving check one over, so would be castling through check
									curr_Board.move("D8", "E8")
									return False
								curr_Board.move("D8", "E8")	
								return True
				if ((not curr_Board.bl_king_moved) and (not curr_Board.bl_rt_rook_moved)): # castling short for white, so rook and king have not moved
					if (curr_Board.pieces[0][5] == 0 and curr_Board.pieces[0][6] == 0): # no pieces in the way
						if (new_row == old_row and new_col == old_col + 2): # if attempting the castle
							if (not curr_Board.player1.check(curr_Board)): #player 2 not giving check
								curr_Board.move("E8", "F8")
								if (curr_Board.player2.check(curr_Board)): #player 2 giving check one over, so would be castling through check
									curr_Board.move("F8", "E8")
									return False
								curr_Board.move("F8", "E8")	
								return True
			
			if (new_row, new_col) not in sight_line:
				return False
			
			if ((curr_Board.pieces[new_row][new_col] != 0) and curr_Board.pieces[new_row][new_col].color == self.color):
				return False #if the square is occupied by one of your pieces, can't move there
			return True
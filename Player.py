
class Player:
	def __init__(self, color):
		self.color = color


	def make_move(self, curr_board, old, new):
		old_row = old[0]
		old_col = old[1]
		new_row = new[0]
		new_col = new[1]

		if (curr_board.pieces[old_row][old_col] == 0 or curr_board.pieces[old_row][old_col].color != self.color):
			return False #cannot make a move if no piece, or if piece is not your color

	def check(self, curr_board): #before wreck(self)
		'''Returns true iff any piece is giving the opposing king check '''
		if (self.color == "W"):
			enemy_king_pos = curr_board.bl_king_pos
		else:
			enemy_king_pos = curr_board.wt_king_pos

		for p in curr_board.pieces:
			for q in p:
				if (q != 0 and q.color == self.color): 
					if (q.enemy_in_check(curr_board, q.position, enemy_king_pos)): 
						return True
		return False

	def not_in_check_after_move(self, curr_board, old, new):
		'''When a player makes a move, their king cannot be in check. This function makes a new
		board, initialized to the current board's position. This new board then makes the 
		requested move, and if the player would be in check, it returns false, which would signify
		and illegal move. '''
		new_board = Board(curr_board.pieces, curr_board.bl_king_pos, curr_board.wt_king_pos)
		if (new_board[old[0]][old[1]].piece_type == "King"):
			if (new_board[old[0]][old[1]].color == "W"):
				new_board.wt_king_pos = new
			if (new_board[old[0]][old[1]].color == "B"):
				new_board.bl_king_pos = new
        
		new_board.move(old, new)
        
		if (self.color == "W"): #if I am white, I want to make sure the black pieces are not giving check
			if new_board.player2.check(new_board):
				return False
			else:
				return True
		else: 
			if new_board.player1.check(new_board):
				return False
			else:
				return True

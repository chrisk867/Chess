from Piece import * 
from copy import deepcopy

class Player:
    def __init__(self, color):
        self.color = color

    def check(self, curr_board): #before wreck(self, curr_board)
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

    def print_player(self):
        if (self.color == "W"):
            return ("Player 1")
        else: 
            return ("Player 2")

    def not_in_check_after_move(self, curr_board, old, new):
        '''When a player makes a move, their king cannot be in check. This function makes a new
        board, initialized to the current board's position. This new board then makes the 
        requested move, and if the player would be in check, it returns false, which would signify
        and illegal move. '''
        old_row = int(curr_board.moves_to_pos[old][0])
        old_col = int(curr_board.moves_to_pos[old][1])
        new_row = int(curr_board.moves_to_pos[new][0])
        new_col = int(curr_board.moves_to_pos[new][1])

        new_board = Board(curr_board.player1, curr_board.player2, deepcopy(curr_board.pieces), curr_board.bl_king_pos, curr_board.wt_king_pos)
        
        new_board.wt_king_moved = curr_board.wt_king_moved #instead of making the constructor extremely long, I do this
        new_board.bl_king_moved = curr_board.bl_king_moved
        new_board.wt_lf_rook_moved = curr_board.wt_lf_rook_moved
        new_board.wt_rt_rook_moved = curr_board.wt_rt_rook_moved
        new_board.bl_lf_rook_moved = curr_board.bl_lf_rook_moved
        new_board.bl_rt_rook_moved = curr_board.bl_rt_rook_moved

        if (new_board.pieces[old_row][old_col].legal(new_board, new_board.moves_to_pos[old], new_board.moves_to_pos[new])):
            if (new_board.pieces[old_row][old_col].piece_type == "King"): #if the king is moving, update the king position
                if (new_board.pieces[old_row][old_col].color == "W"):
                        new_board.wt_king_pos = str(new_row) + str(new_col)
                if (new_board.pieces[old_row][old_col].color == "B"):
                        new_board.bl_king_pos = str(new_row) + str(new_col)
            
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
        else:
            return False

class Board:
    """The pieces are represented by a list of lists, where each single list is a
    row. If a list of pieces is not passed in, then the board will create the initial
    set up. The black pieces are at the beginning of the list and the white pieces at
    the end so that board looks more like a traditional board. If a square is empty, 
    the value at that square is 0. Else, the value will be a string of the name
    of the piece."""
    def __init__(self, player1 = Player("W"), player2 = Player("B"), pieces = None, bl_king_pos = None, wt_king_pos = None):
        if pieces == None:
            nb1, bb1 = Piece("Nite", "B", "01"), Piece("Bish", "B", "02") 
            nb2, bb2 = Piece("Nite", "B", "06"), Piece("Bish", "B", "05")
            nw1, bw1 = Piece("Nite", "W", "71"), Piece("Bish", "W", "72")
            nw2, bw2 = Piece("Nite", "W", "76"), Piece("Bish", "W", "75")                    
            rb1, rw1 = Piece("Rook", "B", "00"), Piece("Rook", "W", "70")
            rb2, rw2 = Piece("Rook", "B", "07"), Piece("Rook", "W", "77")
            qb, qw = Piece("Quen", "B", "03"), Piece("Quen", "W", "73")                      
            kb, kw = Piece("King", "B", "04"), Piece("King", "W", "74")
            pb1, pw1 = Piece("Pawn", "B", "10"), Piece("Pawn", "W", "60")
            pb2, pw2 = Piece("Pawn", "B", "11"), Piece("Pawn", "W", "61")
            pb3, pw3 = Piece("Pawn", "B", "12"), Piece("Pawn", "W", "62")
            pb4, pw4 = Piece("Pawn", "B", "13"), Piece("Pawn", "W", "63")
            pb5, pw5 = Piece("Pawn", "B", "14"), Piece("Pawn", "W", "64")
            pb6, pw6 = Piece("Pawn", "B", "15"), Piece("Pawn", "W", "65")
            pb7, pw7 = Piece("Pawn", "B", "16"), Piece("Pawn", "W", "66")
            pb8, pw8 = Piece("Pawn", "B", "17"), Piece("Pawn", "W", "67")                  
            self.pieces = [[rb1, nb1, bb1, qb, kb, bb2, nb2, rb2], \
                        [pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8], \
                        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],\
                        [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], \
                        [pw1, pw2, pw3, pw4, pw5, pw6, pw7, pw8], \
                        [rw1, nw1, bw1, qw, kw, bw2, nw2, rw2]]
            self.bl_king_pos = "04" # start position of black king
            self.wt_king_pos = "74" # start position of white king
            self.wt_king_moved = False
            self.bl_king_moved = False
            self.wt_lf_rook_moved = False
            self.wt_rt_rook_moved = False
            self.bl_lf_rook_moved = False
            self.bl_rt_rook_moved = False

        else:
            self.pieces = pieces
            self.bl_king_pos = bl_king_pos
            self.wt_king_pos = wt_king_pos

        self.player1 = player1
        self.player2 = player2
        
        self.temp_moves_to_pos = [{'A' + str(x) : str(7-x+1) + "0" for x in range(1,9)}, #creates a list of dictionaries that translates
                           {'B' + str(x) : str(7-x+1) + "1" for x in range(1,9)}, #moves (such as A1, B5) into list indicies. Will
                           {'C' + str(x) : str(7-x+1) + "2" for x in range(1,9)}, #be used for the move function further down.
                           {'D' + str(x) : str(7-x+1) + "3" for x in range(1,9)}, #I could not get dictionary generator expressions
                           {'E' + str(x) : str(7-x+1) + "4" for x in range(1,9)}, #to all fit into one dictionary, so I make a list
                           {'F' + str(x) : str(7-x+1) + "5" for x in range(1,9)}, #of dictionaries and merge them all into the 
                           {'G' + str(x) : str(7-x+1) + "6" for x in range(1,9)}, #actual moves dictionary.
                           {'H' + str(x) : str(7-x+1) + "7" for x in range(1,9)}]

        self.temp_pos_to_moves = [{str(7-x+1) + "0" : 'A' + str(x) for x in range(1,9)}, 
                           {str(7-x+1) + "1" : 'B' + str(x) for x in range(1,9)}, 
                           {str(7-x+1) + "2" : 'C' + str(x) for x in range(1,9)}, 
                           {str(7-x+1) + "3" : 'D' + str(x) for x in range(1,9)}, 
                           {str(7-x+1) + "4" : 'E' + str(x) for x in range(1,9)}, 
                           {str(7-x+1) + "5" : 'F' + str(x) for x in range(1,9)},  
                           {str(7-x+1) + "6" : 'G' + str(x) for x in range(1,9)}, 
                           {str(7-x+1) + "7" : 'H' + str(x) for x in range(1,9)}]

        def merge_dicts(*dict_args): #taken from https://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-in-a-single-expression
            '''
            Given any number of dicts, shallow copy and merge into a new dict,
            precedence goes to key value pairs in latter dicts.
            '''
            result = {}
            for dictionary in dict_args:
                result.update(dictionary)
            return result

        self.moves_to_pos = merge_dicts(self.temp_moves_to_pos[0], self.temp_moves_to_pos[1], self.temp_moves_to_pos[2], \
            self.temp_moves_to_pos[3], self.temp_moves_to_pos[4], self.temp_moves_to_pos[5], self.temp_moves_to_pos[6], \
            self.temp_moves_to_pos[7]) #should be a cleaner way to do this, look into it in future

        self.pos_to_moves = merge_dicts(self.temp_pos_to_moves[0], self.temp_pos_to_moves[1], self.temp_pos_to_moves[2], \
            self.temp_pos_to_moves[3], self.temp_pos_to_moves[4], self.temp_pos_to_moves[5], self.temp_pos_to_moves[6], \
            self.temp_pos_to_moves[7])
        ''' moves_to_pos translates a move (such as "A1, F5") to a position (such as "00", "54"). pos_to_moves does the
        reverse. '''
    
    def print_board(self): #prints a correctly formatted board in cmd (on Windows)
    	for p in self.pieces:
    		print(" ")
    		for _ in range(56):
    			print('-', end = "")
    		print('-')
    		print('|', end = "")
    		for q in p:
    			if (q == 0):
    				print("   ", end="")
    				print(q, end ="")
    				print("  ", end="")
    				print('|', end = "")
    			else:
    				q.print_piece()
    				print('|', end = "")
    	print(" ")
    
    def move(self, old, new): # moves a piece from old position to new position
        old_row = int(self.moves_to_pos[old][0])
        old_col = int(self.moves_to_pos[old][1])
        new_row = int(self.moves_to_pos[new][0])
        new_col = int(self.moves_to_pos[new][1])

        moving_piece = self.pieces[old_row][old_col]

        moving_piece.legal(self, self.moves_to_pos[old], self.moves_to_pos[new]) # read below
        '''Okay this is really dumb, but en passant was teh last thing I did and I didn't want to have
        to restructure a ton of code. In legal, if the pawn did an en passant, it changes the attribute of
        the pawn. However, before, I was only ever using legal in not_in_check_after_move, which checks
        legal moves in a new board. So, the pawn on the actual board was never having its en_passant
        value set to true. So, even though the move function will only ever be called on a legal move, 
        I still need to call legal here to remove the piece correctly if an en passant occurs. En 
        passant is a stupid rule. '''
        
        if (moving_piece.piece_type == "King"):
            if (moving_piece.color == "W"):
                self.wt_king_pos = str(self.moves_to_pos[new]) # for keeping track of check
                self.wt_king_moved = True # for castling, can't have moved king

                if (old == "E1" and new == "C1"): #move rook when castle long
                    self.pieces[7][3] = self.pieces[7][0]
                    self.pieces[7][3].position =  "73"
                    self.pieces[7][0] = 0
                if (old == "E1" and new == "G1"): # castle short, move rook
                    self.pieces[7][5] = self.pieces[7][7]
                    self.pieces[7][5].position = "75"
                    self.pieces[7][7] = 0
            else:
                self.bl_king_pos = str(self.moves_to_pos[new])
                self.bl_king_moved = True
                if (old == "E8" and new == "C8"): #move rook when castle long
                    self.pieces[0][3] = self.pieces[0][0]
                    self.pieces[0][3].position =  "03"
                    self.pieces[0][0] = 0
                if (old == "E8" and new == "G8"): # castle short, move rook
                    self.pieces[0][5] = self.pieces[0][7]
                    self.pieces[0][5].position = "05"
                    self.pieces[0][7] = 0

        if (moving_piece.piece_type == "Rook"): #for castling. Can't have moved rook
            if (moving_piece.position == "00"):
                self.bl_lf_rook_moved = True
            if (moving_piece.position == "07"):
                self.bl_wt_rook_moved = True
            if (moving_piece.position == "70"):
                self.wt_lf_rook_moved = True
            if (moving_piece.position == "77"):
                self.wt_rt_rook_moved = True

        if (moving_piece.piece_type == "Pawn"):
            if (moving_piece.color == "W" and old[1] == "2" and new[1] == "4"):
                self.pieces[old_row][old_col].up_two = True
            if (moving_piece.color == "B" and old[1] == "7" and new[1] == "5"):
                self.pieces[old_row][old_col].up_two = True
            if (moving_piece.en_passant and moving_piece.color == "B"):
                self.pieces[new_row - 1][new_col] = 0 # if en passanting, remove en passanted pawn
            if (moving_piece.en_passant and moving_piece.color == "W"):
                self.pieces[new_row + 1][new_col] = 0

        self.pieces[new_row][new_col] = self.pieces[old_row][old_col] #moves piece
        self.pieces[new_row][new_col].position = str(self.moves_to_pos[new]) #changes moved piece's position attribute
        self.pieces[old_row][old_col] = 0 #sets old spot to 0

    def checkmate(self):
        possible_moves = [(x,y) for x in range(8) for y in range(8)] # every possible move on the board

        if (self.player1.check(self)): #black is in check
            for p in self.pieces:
                for q in p:
                    if (q != 0 and q.color == "B"): # check all black pieces
                        for m in possible_moves: # if any possible moves ends in black not being in check, then it is not checkmate
                            if self.player2.not_in_check_after_move(self, self.pos_to_moves[q.position], self.pos_to_moves[str(m[0]) + str(m[1])]):
                                return False
            return True # is in check mate
        
        if (self.player2.check(self)): #white is in check
            for p in self.pieces:
                for q in p:
                    if (q != 0 and q.color == "W"):
                        for m in possible_moves:
                            if self.player1.not_in_check_after_move(self, self.pos_to_moves[q.position], self.pos_to_moves[str(m[0]) + str(m[1])]):
                                return False
            return True # is in check mate

        return False #no one in check, game not over
from Board import Board

def play_game():
    game = Board()
    player_turn = game.player1
    opponenet = game.player2
    while (not game.checkmate()):
        game.print_board()
        moved = False
        while (not moved):
            p_move = input(player_turn.print_player() + " please make a move of the form: from, to    ")
            #try:
            if (game.pieces[int(game.moves_to_pos[p_move[0:2]][0])][int(game.moves_to_pos[p_move[0:2]][1])] == 0):
                print ("There's not piece in that spot!")
                continue
            if (player_turn.not_in_check_after_move(game, p_move[0:2], p_move[4:]) \
            and game.pieces[int(game.moves_to_pos[p_move[0:2]][0])][int(game.moves_to_pos[p_move[0:2]][1])].color == player_turn.color): #same color
                game.move(p_move[0:2], p_move[4:])
                moved = True
            else :
                print ("Not a valid move")
            # except:
            #     print ("Please input moves in the form: to, from. For example: A1, A2")
        
        for p in game.pieces: # Pawn promotion
            for q in p:
                if (q != 0 and q.piece_type == "Pawn"):
                    if ((q.color == "W" and q.position[0] == '0') or (q.color == "B" and q.position[0] == '7')):
                        promoted = False
                        while (not promoted):
                            promote_to = input("Please pick a piece to promote to: Quen, Bish, Nite, or Rook     ")
                            if (promote_to == "Quen" or promote_to == "Rook" or promote_to == "Nite" or promote_to == "Bish"):
                                game.pieces[int(q.position[0])][int(q.position[1])].piece_type = promote_to
                                promoted = True
                            else:
                                print("Please pick a valid piece to promote to  ")

        if (player_turn == game.player1):
            player_turn, opponent = game.player2, game.player1
        else:
            player_turn, opponent = game.player1, game.player2
    game.print_board()
    print ("Congratulations! " + opponent.print_player() + " has won!") # player turn switches beforegame is checked to be over

if __name__ == '__main__':
    play_game()
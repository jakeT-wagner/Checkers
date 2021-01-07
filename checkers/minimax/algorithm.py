from copy import deepcopy #we will copy the board many times within the algorithm
import pygame
'''
x = []
y = deepcopy(x)
now when we change one of the variables it will only change that one, wherease it would normally change both since the variable is 
passed by reference in python
'''
RED = (255,0,0)
WHITE = (255,255,255)

def minimax(position, depth, max_player, game):
    #based on a given board, make the best possible move
    #position == the board
    #depth == how many moves are we checking. recursive until 0
    #max_player = boolean for maximize or minimize the player's scores. true = maximize false = minimize
    #game == game object we will be passed. Irrelevant at this point
    if depth == 0 or position.winner() != None: #board has a winner method
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf') #have to initialize the value
        best_move = None #initialize to none
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0] # we only return the actual best_move when returned to caller
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move 
    else:
        minEval = float('inf') #have to initialize the value
        best_move = None #initialize to none
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0] # we only return the actual best_move when returned to caller
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move 

def get_all_moves(board, color, game):
    moves = [] #[board, other board]
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece) #(row,col) : [pieces]
        for move, skip in valid_moves.items(): #skip is the pieces that must be removed 
            draw_moves(game, board, piece)
            temp_board = deepcopy(board) #should do this in chess.
            temp_piece = temp_board.get_piece(piece.row,piece.col) #it was breaking at first due to an issue of copying the board but not the piece. It was changing the piece, even tho the original board was fine
            new_board = simulate_move(temp_piece,move, temp_board, game, skip) #going to take the piece, move it, make that move, and then return the new board
            moves.append(new_board)
    return moves

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1]) #move is currently a tuple of (row,col)
    if skip:
        board.remove(skip)
    
    return board 

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x,piece.y), 50,5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)









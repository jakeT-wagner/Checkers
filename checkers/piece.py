import pygame

from .constants import GRAY,RED, WHITE, SQUARE_SIZE, CROWN

class Piece:
    PADDING = 12
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x, self.y = 0,0
        self.calc_pos() #to call another member method in an object, have to use the self. This may be why it has to be passed

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2 # get the pixel location and then add half a square for center
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2) )
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self): #representation of the piece for debugging
        return str(self.color)
    


    

    
import pygame

WIDTH, HEIGHT = 640,640
ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH//COLS

#rgb, defining colors for easier use
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GRAY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (36,28))

import sys
import pygame
from constants import *
import numpy as np


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

class Board:
    def __init__(self):
        self.squares = np.zeros ( (ROWS, COLS))
        
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

class Game:
    
    def __init__(self):
        self.board = Board()
        self.show_lines()
    
    
    def show_lines(self):
        pygame.draw.line(screen, LINE_COLOR, (SQ_SIZE, 0), (SQ_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQ_SIZE, 0), (WIDTH - SQ_SIZE, HEIGHT), LINE_WIDTH)
        
        pygame.draw.line(screen, LINE_COLOR, (0, SQ_SIZE), (WIDTH, SQ_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQ_SIZE), (WIDTH, HEIGHT - SQ_SIZE), LINE_WIDTH)
        
        

    
    
def main():
    
    game = Game()
    board = game.board
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQ_SIZE
                col = pos[0] // SQ_SIZE
                print(row, col)
                
                board.mark_sqr(row, col, 1)
                print(game.board.squares)
                
        pygame.display.update()
        
                
main()
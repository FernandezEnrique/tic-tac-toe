import pygame
from pygame.locals import *
from colors import *
from popup import show_message
from win_checker import main as win_checker

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.running = True
        self.playing = True
        self.active_player = 1 # 1 is X and 2 is O
        self.background = WHITE
        self.screen.fill(self.background)
        self.define_board()
        pygame.display.set_caption('Tic Tac Toe')
        pygame.display.update()
    
    def define_board(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.squares = []
        x = 0
        y = 0
        id = 0
        for i in range(3):
            for j in range(3):
                rect = Rect(x,y,200,200)
                pygame.draw.rect(self.screen, BLACK, rect, 2)
                self.squares.append([rect, x, x+200, y, y+200, id])
                x += 200
                id += 1
            y += 200
            x = 0
            
    def click(self, pos, player):
        cell = None
        for _c in self.squares:
            if (pos[0] > _c[1]) and(pos[0] < _c[2]) and (pos[1] > _c[3]) and (pos[1] < _c[4]):
                cell = _c
                
        if self.board[int(cell[5]/3)][cell[5]%3] == 0:
            if player == 1:
                img = pygame.image.load('img/x.png').convert()
            else:
                img = pygame.image.load('img/o.png').convert()
                
            rect = img.get_rect()
            rect.center = cell[1]+100, cell[3]+100
            self.screen.blit(img, rect)
            pygame.draw.rect(self.screen, WHITE, rect, 1)
            pygame.display.update()
            self.change_board(cell[5], player)
            self.active_player = (1,2)[self.active_player == 1]
        else:
            show_message("Error","This cell is taken","Ok")
    
    def change_board(self, id, player):
        self.board[int(id/3)][id%3] = player
        result = win_checker(self.board)
        if result != 0:
            self.playing = False
            show_message("Error",f"Player {result} is the winner","Ok")
        

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.playing == True:
                    self.click(pygame.mouse.get_pos(), self.active_player)
                    
        pygame.quit()   
    
    
if __name__ == '__main__':
    Game().run()
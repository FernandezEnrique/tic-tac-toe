import pygame
from pygame.locals import *
from colors import *

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.running = True
        self.active_player = 1 # 1 is X and 2 is O
        self.background = WHITE
        self.screen.fill(self.background)
        self.define_board()
        pygame.display.set_caption('Tic Tac Toe')
        pygame.display.update()
    
    def define_board(self):
        self.board = [[],[],[]]
        self.squares = []
        x = 0
        y = 0
        id = 0
        for i in range(3):
            for j in range(3):
                rect = Rect(x,y,200,200)
                pygame.draw.rect(self.screen, RED, rect, 2)
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
                print(_c[5])
                
        if player == 1:
            img = pygame.image.load('img/x.png').convert()
        else:
            img = pygame.image.load('img/o.png').convert()
            
        rect = img.get_rect()
        rect.center = cell[1]+100, cell[3]+100
        self.screen.blit(img, rect)
        pygame.draw.rect(self.screen, WHITE, rect, 1)
        pygame.display.update()
    
    def change_board(self):
        pass
            
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.click(pygame.mouse.get_pos(), self.active_player)
                    self.active_player = (1,2)[self.active_player == 1]
        pygame.quit()   
    
    
if __name__ == '__main__':
    Game().run()
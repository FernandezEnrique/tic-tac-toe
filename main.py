import pygame
from pygame.locals import *
from colors import *

class Game:

    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        self.screen = pygame.display.set_mode((600, 600), flags)
        self.running = True
        self.background = WHITE
        self.screen.fill(self.background)
        pygame.display.set_caption('Tic Tac Toe')
        pygame.display.update()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False       
        pygame.quit()
        
        
    
if __name__ == '__main__':
    Game().run()
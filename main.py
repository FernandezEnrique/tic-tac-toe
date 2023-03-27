import pygame
from pygame.locals import *
from colors import *
from popup import show_message
from win_checker import main as win_checker
from menu import Menu
from machine import get_machine_position, get_cell
import time

class Game:

    def __init__(self, mode):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.running = True
        self.playing = True
        self.active_player = 1 # 1 is X and 2 is O
        self.mode = mode
        self.machine_player = 2
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
        for cell in self.squares:
            if (pos[0] > cell[1]) and(pos[0] < cell[2]) and (pos[1] > cell[3]) and (pos[1] < cell[4]):
                # Checks the box the click was on
                row = cell[5]//3
                column = cell[5]%3
                x_position = cell[1]+100
                y_position = cell[3]+100
                updated = self.update_game(cell[5], row, column, x_position, y_position, player)
                if updated and self.mode == "local":
                    self.active_player = (1,2)[self.active_player == 1]

    def update_game(self, cell, row, column, x_position, y_position, player):          
        if self.board[row][column] == 0:
            if player == 1:
                img = pygame.image.load('img/x.png').convert()
            else:
                img = pygame.image.load('img/o.png').convert()
                
            rect = img.get_rect()
            rect.center = x_position, y_position
            self.screen.blit(img, rect)
            pygame.draw.rect(self.screen, WHITE, rect, 1)
            pygame.display.update()
            self.change_board(cell, player)
            return True
        else:
            show_message("Error","This cell is taken","Ok")
            return False
    
    def change_board(self, id, player):
        self.board[int(id/3)][id%3] = player
        result = win_checker(self.board)
        if result != 0:
            self.playing = False
            self.running = False
            response = Menu("Winner",f"Player {result} is the winner. Play again?", "Yes", "No", "Back to Menu")
            if (response.selection == "Yes"):
                Game(self.mode).run()

            elif (response.selection == "Back to Menu"): 
                mode = Menu("Menu", "Choose game mode", "Local", "Machine")
                if ( mode.selection == "Local"):
                    Game("local").run()
                else:
                    Game("machine").run()
            else:
                self.running = False                

    def is_tie(self):
        tie = True
        for i in range(9):
            if self.board[i//3][i%3] == 0:
                tie = False
        return tie

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.playing == True:
                    self.click(pygame.mouse.get_pos(), self.active_player)
                    if self.is_tie():
                        self.playing = False

                    if self.mode == "machine" and self.playing:
                        machine_pos = get_machine_position(self.board)
                        cell = get_cell(self.squares, machine_pos)
                        time.sleep(0.5)
                        self.update_game(cell['cell'], 
                                            cell['row'], 
                                            cell['column'], 
                                            cell['x_position'], 
                                            cell['y_position'], 
                                            self.machine_player)
                
                        
        pygame.quit()   
    
    
if __name__ == '__main__':
    mode = Menu("Menu", "Choose game mode", "Local", "Machine")
    if ( mode.selection == "Local"):
        Game("local").run()

    else:
        Game("machine").run()
import pygame
from screen import Screen
from map import GameMap

class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = GameMap(self.screen)

    def run(self):
        while self.running:
            self.map.update()
            self.screen.update()
            
    

if __name__ == "__main__":
    pygame.init()
    game_instance = Game()
    game_instance.run()


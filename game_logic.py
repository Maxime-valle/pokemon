import pygame
from screen import Screen
from map import GameMap
from entity import Entity
from kelistener import KeyListener
from game import Game


class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = GameMap(self.screen)
        self.keylistener = KeyListener()
        self.entity = Entity(self.keylistener)
        self.map.add_player(self.entity)
    
    def run(self):
        def run(self):
         while self.running:
            self.handle_input() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            for player in self.players:  # Change here
                player.update()

            self.map.update()
            self.screen.update()
            
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN: 
                self.keylistener.add_key(event.ke)
            elif event.type == pygame.KEYUP: 
                self.keylistener.remove_key(event.key)
                
        

        
            if __name__ == "__main__":
                pygame.init()
    game_instance = Game()
    game_instance.run()



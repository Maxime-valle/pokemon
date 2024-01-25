import pygame
from tool import Tool
from kelistener import KeyListener

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spritesheet = pygame.image.load("img55/sprit2.png")
        self.image = Tool.split_image(self.spritesheet, x=0, y=0, width=24, height=32)
        self.position = [15, 0]
        self.rect = pygame.Rect(0, 0, 32, 32)
        self._layer = 10

    def update(self):
        self.check_move()
        self.rect.topleft = self.position

    def check_move(self):
        pass

    def move_left(self):
        self.position[0] -= 1

    def move_right(self):
        self.position[0] += 1

    def move_up(self):
        self.position[1] -= 1

    def move_down(self):
        self.position[1] += 1
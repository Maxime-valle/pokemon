import pygame

class Tool:
    @staticmethod
    def split_image(spritesheet, x, y, width, height):
        return spritesheet.subsurface(pygame.Rect(x, y, width, height))

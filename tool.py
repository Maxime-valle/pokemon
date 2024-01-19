import pygame

class tool:
    @staticmethod
    def split_image(spritesheet: pygame.surface, x: int, y: int, width: int, height: int):
        return spritesheet.subsurface(pygame.Rect(x, y, width, height))
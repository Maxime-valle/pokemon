import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((640, 480))

personnage = pygame.image.load('sprit2.png').convert_alpha()
carte = pygame.image.load('Map.tmx').convert()



def deplacerPersonnage(keys, rect):
    if keys[K_UP]: rect.move_ip(0, -3)
    if keys[K_DOWN]: rect.move_ip(0, 3)
    if keys[K_LEFT]: rect.move_ip(-3, 0)
    if keys[K_RIGHT]: rect.move_ip(3, 0)
    return rect.clamp(pygame.Rect(0, 0, 640, 480))  # Restreint le personnage à la fenêtre
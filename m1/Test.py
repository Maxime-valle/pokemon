import pygame
import sys
import os
import pygame_gui
import cv2



class ImageButton(pygame.sprite.Sprite):
    def __init__(self, image_path, position, size=(100, 100), rotation_angle=-5):  # l'angle de rotation
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)  # R
        self.image = pygame.transform.rotate(self.image, rotation_angle)  # R 
        self.rect = self.image.get_rect()
        self.rect.center = position  # Centrer le bouton

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

pygame.init()

# Fenêtre
largeur_fenetre, hauteur_fenetre = 800, 800 
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))


gestionnaire = pygame_gui.UIManager((largeur_fenetre, hauteur_fenetre))


button_size = (150,150)  
button = ImageButton('img55/bouton1.png', (largeur_fenetre//2, hauteur_fenetre//2 -250), button_size)  # Déplacer l'image légèrement vers le haut

#  opencv
chemin_video = os.path.join('img55/Menu55.mp4')
cap = cv2.VideoCapture(chemin_video)

# Variables 
en_cours = True
aller_a_pendu = False
aller_a_niveau = False

# Bande son
pygame.mixer.music.load("img55/musicp.mp3")
pygame.mixer.music.set_volume(3)
pygame.mixer.music.play(1)  

clock = pygame.time.Clock()

while en_cours:
    delta_temps = clock.tick(50) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
            if button.is_clicked(event):
                print('Commencer')

        gestionnaire.process_events(event)

    gestionnaire.update(delta_temps)

    # Frame de la vidéo  OpenCV
    ret, frame = cap.read()
    if not ret:
        # revenir au début
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue


    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Redimensionner l'image à la taille de la fenêtre Pygame
    frame = cv2.resize(frame, (largeur_fenetre, hauteur_fenetre))

    # Convertir l'image OpenCV en surface Pygame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = pygame.surfarray.make_surface(frame)
    fenetre.blit(frame, (0, 0))

    # dessiner le bouton
    fenetre.blit(button.image, button.rect.topleft)

    gestionnaire.draw_ui(fenetre)
    pygame.display.update()
    
    
cap.release()
cv2.destroyAllWindows()

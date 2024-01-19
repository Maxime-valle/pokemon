import pygame
import sys
import os
import pygame_gui
import cv2
from moviepy.editor import VideoFileClip

#  classe pour le bouton personnalisé
class ImageButton(pygame.sprite.Sprite):
    def __init__(self, image_path, position, size=(100, 100), rotation_angle=-5):  # l'angle de rotation
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)  # R
        self.image = pygame.transform.rotate(self.image, rotation_angle)  # Rotation 
        self.rect = self.image.get_rect()
        self.rect.center = position  # Centrer le bouton

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

pygame.init()

# Fenetre
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))

# Ajouter un titre à la fenêtre
pygame.display.set_caption("Pokemon omnipotens")

# Manager pour pygame_gui
manager = pygame_gui.UIManager((win_width, win_height))

# Bouton
button_size = (150,150)  
button = ImageButton('img55/bouton1.png', (win_width//2, win_height//2 + 75), button_size)  # Déplacer l'image légèrement vers le haut

# fond ecran opencv
chemin_video = os.path.join('img55/Menu55.mp4')
cap = cv2.VideoCapture(chemin_video)


# Bande son
pygame.mixer.music.load("img55/musicp.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1)

# Initialisation de l'horloge
clock = pygame.time.Clock()

# Boucle principale
running = True
while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if button.is_clicked(event):
            print('Commencer')

    manager.update(time_delta)

    # Dessiner le fond d'écran
    win.blit(cap, (0, 0))
    
    # dessiner le bouton
    win.blit(button.image, button.rect.topleft)

   #mettre a jours image
    pygame.display.flip()
    
    # Frame de la vidéo avec OpenCV
    ret, frame = cap.read()
    if not ret:
          # revenir au début
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        #  pivoter l'image
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Redimensionner l'image à la taille de la fenêtre Pygame
    frame = cv2.resize(frame, (largeur_fenetre, hauteur_fenetre))

        # Convertir l'image OpenCV en  Pygame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = pygame.surfarray.make_surface(frame)
    fenetre.blit(frame, (0, 0))

    gestionnaire.draw_ui(fenetre)
    pygame.display.update()


#  les ressources
cap.release()
cv2.destroyAllWindows()

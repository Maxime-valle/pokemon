import pygame
import sys
import os
import pygame_gui
import cv2





pygame.init()

# Fenêtre
largeur_fenetre, hauteur_fenetre = 800, 800 
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))


gestionnaire = pygame_gui.UIManager((largeur_fenetre, hauteur_fenetre))


#  opencv
chemin_video = os.path.join('img55/histoire nar.mp4')
cap = cv2.VideoCapture(chemin_video)

# Variables 
en_cours = True
aller_a_pendu = False
aller_a_niveau = False

# Bande son
pygame.mixer.music.load("img55/narration.mp3")
pygame.mixer.music.set_volume(3)
pygame.mixer.music.play(1)  

clock = pygame.time.Clock()

while en_cours:
    delta_temps = clock.tick(50) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

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


    gestionnaire.draw_ui(fenetre)
    pygame.display.update()
    
    
cap.release()
cv2.destroyAllWindows()

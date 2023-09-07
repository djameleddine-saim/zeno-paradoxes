import pygame
import sys

pygame.init()

largeur_fenetre = 400
hauteur_fenetre = 400

blanc = (255, 255, 255)

distance = 110.0  # en mètres 
vitesse_fleche = 5.0  # en mètres par seconde

position_fleche = 0.0
temps_debut = pygame.time.get_ticks()  # Temps en millisecondes au début

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Simulation de la flèche en vol")

# Chargez l'image de la flèche
fleche_image = pygame.image.load("fleche.png")
fleche_image = pygame.transform.scale(fleche_image, (50, 50))  # Redimensionnez l'image

# Chargez l'image de la cible
cible_image = pygame.image.load("cible.png")
cible_image = pygame.transform.scale(cible_image, (100, 100))  # Redimensionnez l'image

# Positionnez la cible à l'emplacement souhaité
cible_x = 100
cible_y = hauteur_fenetre // 2 - cible_image.get_height() // 2


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fenetre.fill(blanc)

    temps_actuel = pygame.time.get_ticks()  # Temps actuel en millisecondes
    temps_ecoule = (temps_actuel - temps_debut) / 1000.0  # Convertissez en secondes

    position_fleche = vitesse_fleche * temps_ecoule  # Met à jour la position de la flèche

    # Dessinez la cible à sa position
    fenetre.blit(cible_image, (cible_x, cible_y))

    # Dessinez la flèche à sa position actuelle
    fenetre.blit(fleche_image, (int(position_fleche), hauteur_fenetre // 2 - 25))

    pygame.display.flip()

    if position_fleche >= distance:
        running = False


pygame.quit()
sys.exit()

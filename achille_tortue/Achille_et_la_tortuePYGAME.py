import pygame
import sys
import time

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 400

blanc = (255, 255, 255)

vitesse_achille = 10
vitesse_tortue = 1

position_achille = 0
position_tortue = 300

# Charger les images des personnages
achille_image = pygame.image.load('achille.png')
tortue_image = pygame.image.load('tortue.png')

# Redimensionner les images si nécessaire
achille_image = pygame.transform.scale(achille_image, (100, 100))
tortue_image = pygame.transform.scale(tortue_image, (100, 100))

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Course entre Achille et la Tortue")

clock = pygame.time.Clock()

while position_achille < position_tortue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    position_achille += vitesse_achille
    position_tortue += vitesse_tortue

    fenetre.fill(blanc)

    # Afficher les images des personnages
    fenetre.blit(achille_image, (position_achille, 150))
    fenetre.blit(tortue_image, (position_tortue, 250))

    font = pygame.font.Font(None, 36)
    achille_texte = font.render(f"Achille: {position_achille}", True, (0, 0, 255))
    tortue_texte = font.render(f"Tortue: {position_tortue}", True, (255, 0, 0))
    fenetre.blit(achille_texte, (50, 50))
    fenetre.blit(tortue_texte, (50, 100))

    pygame.display.flip()

    time.sleep(0.5)
    clock.tick(60)

pygame.quit()
sys.exit()

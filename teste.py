import pygame

# Initialiser pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 600, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Rejouer Partie d'Echecs")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Boucle principale du jeu
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Remplir la fenêtre avec une couleur
    fenetre.fill(blanc)

    # Actualiser l'affichage
    pygame.display.flip()

# Quitter pygame
pygame.quit()
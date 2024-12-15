from accueil import PageAccueil
from choix_pion import ChoixPion
from jeux_plateau import JeuxPlateau
import pygame

def main():
    pygame.init()  
    fenetre = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jeux de Plateau")

    accueil = PageAccueil(fenetre)
    choix_pion = ChoixPion(fenetre)
    jeu_plateau = None

    running = True
    while running:
        if accueil.run():
            pion_choisi = choix_pion.run()
            if pion_choisi:
                jeu_plateau = JeuxPlateau(
                    pion_1_selectionne=(pion_choisi == 'pion_1'),
                    pion_2_selectionne=(pion_choisi == 'pion_2'),
                    pion_3_selectionne=(pion_choisi == 'pion_3'),
                    pion_4_selectionne=(pion_choisi == 'pion_4'),
                )
                if not jeu_plateau.run(): 
                    accueil = PageAccueil(fenetre)  
        else:
            running = False 

    pygame.quit()


if __name__ == "__main__":
    main()

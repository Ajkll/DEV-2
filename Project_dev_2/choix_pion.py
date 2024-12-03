import pygame
from pion import Pion
from de import De
from animation import Animation
from board_map import Map
from deplacement import Deplacement
from choix_pion import ChoixPion

class JeuxPlateau:
    def __init__(self, pion_1_selectionne=False, pion_2_selectionne=False, pion_3_selectionne=False, pion_4_selectionne=False):
        self.largeur = 800
        self.hauteur = 600
        pygame.init()
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Jeux de Plateau")

        self.map = Map()
        self.map.load_map()

        self.cases_deplacement = self.map.cases_deplacement

        if len(self.cases_deplacement) > 0:
            self.pions = {
                1: Pion(self.cases_deplacement[0].x, self.cases_deplacement[0].y, "img/mario.png", "pion_1", self.cases_deplacement),
                2: Pion(self.cases_deplacement[0].x, self.cases_deplacement[0].y, "img/luigi.png", "pion_2", self.cases_deplacement),
                3: Pion(self.cases_deplacement[0].x, self.cases_deplacement[0].y, "img/peach.png", "pion_3", self.cases_deplacement),
                4: Pion(self.cases_deplacement[0].x, self.cases_deplacement[0].y, "img/yoshi.png", "pion_4", self.cases_deplacement),
            }

        self.deplacement = None  # Initialisez une référence vide pour le déplacement
        self.animation = Animation()

        try:
            self.son_lancer_de = pygame.mixer.Sound("mp3/cube.mp3")
            self.son_piece = pygame.mixer.Sound("mp3/coin.mp3")
        except pygame.error as e:
            print(f"Erreur lors du chargement des sons : {e}")

        self.bouton_active = True
        self.nombre_clic = 0

    def bouton_retour(self):
        self.bouton_exit = pygame.image.load("img/bouton_exit.png").convert_alpha()
        self.bouton_exit = pygame.transform.scale(self.bouton_exit, (106, 50))
        self.bouton_exit_rect = self.bouton_exit.get_rect(topleft=(10, 10))
        self.fenetre.blit(self.bouton_exit, self.bouton_exit_rect)

    def run(self):
        choix_pion = ChoixPion(self.fenetre)
        pion_selectionne = choix_pion.run()

        if pion_selectionne:
            pion_instance = self.pions[int(pion_selectionne[-1])]  # Récupère le pion sélectionné
            self.de = De(self.fenetre, self.pions, pion_choisi=pion_instance)
            self.deplacement = Deplacement(pion_choisi=pion_instance, de=self.de, cases_reculer=self.map.cases_reculer, cases_map = self.map.cases_map)
        else:
            print("Aucun pion n'a été sélectionné. Fin du jeu.")
            return False

        clock = pygame.time.Clock()  
        running = True
        while running:
            self.map.draw(self.fenetre)
            self.de.afficher_bouton()
            self.bouton_retour()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.de.verifier_clic_bouton(event.pos):
                        if self.deplacement:
                            self.deplacement.lancer_deplacement()

                    if self.bouton_exit_rect.collidepoint(event.pos):
                        return 

            if self.deplacement:
                self.deplacement.update()

            # Afficher uniquement le pion choisi
            self.fenetre.blit(pion_instance.image, (pion_instance.x, pion_instance.y))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        return False

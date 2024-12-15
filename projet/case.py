import random
import pygame

class Case:
    def __init__(self, fenetre, pions, pion_choisi):
        self.fenetre = fenetre
        self.largeur, self.hauteur = self.fenetre.get_size()
        self.pions = pions
        self.pion_choisi = pion_choisi

        # Charger les faces du dé
        self.faces = [pygame.image.load(f"img/case_extra_malchance.png").convert_alpha() for i in range(1, 7)]  # 6 faces du dé
        self.faces = [pygame.transform.scale(face, (100, 100)) for face in self.faces]

        # Charger le bouton de jeu
        self.bouton_play = pygame.image.load("img/bouton_commencer.png").convert_alpha()
        self.bouton_play = pygame.transform.scale(self.bouton_play, (107, 32))
        self.bouton_rect = pygame.Rect(self.largeur // 2 - 53, 50, 107, 32)  # Position du bouton

        self.son_lancer_de = pygame.mixer.Sound("mp3/cube.mp3")
        self.font = pygame.font.Font(None, 36)

    def afficher_bouton(self):
        self.fenetre.blit(self.bouton_play, self.bouton_rect)

    def verifier_clic_bouton(self, pos_souris):
        if self.bouton_rect.collidepoint(pos_souris):
            return True
        return False

    def lancer_de(self):
        self.son_lancer_de.play()
        temps_debut_animation = pygame.time.get_ticks()
        duree_animation = 4000

        while pygame.time.get_ticks() - temps_debut_animation < duree_animation:

            self.fenetre.blit(self.pion_choisi.image, (self.pion_choisi.x, self.pion_choisi.y))

            indice_face_choisie = random.randint(0, 5)
            face_choisie = self.faces[indice_face_choisie]
            self.fenetre.blit(face_choisie, (self.largeur // 2 - 50, self.hauteur // 2 - 50))

            self.afficher_bouton()  # Afficher le bouton pendant l'animation

            pygame.display.flip()
            pygame.time.Clock().tick(60)

        pygame.time.wait(2000)

        return indice_face_choisie + 1

from plateau import Plateau

class ChangerMap:
    def __init__(self, taille_new_map):
        self.taille_new_map = taille_new_map

    def changement_map_active(self, jeu):
        new_map = Plateau(self.taille_new_map)
        jeu.plateau = new_map

        for pion in jeu.pions:
            pion.position = 0

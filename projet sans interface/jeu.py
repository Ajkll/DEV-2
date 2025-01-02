import random
from pion import Pion
from plateau import Plateau
from changement_map import ChangerMap

class Jeu:
    def __init__(self, nom_joueurs, length_plateau=15, cases_speciales=None):
        self.plateau = Plateau(length_plateau, cases_speciales)
        self.pions = [Pion(nom) for nom in nom_joueurs]
        self.joueur_actuel = 0
        self.case_victoire = length_plateau - 1
        self.changement_map = ChangerMap(taille_new_map=15)
        self.questions = [
            {"question": "Quelle est la capitale de la Belgique ?", "options": ["1. Bruxelles", "2. Londres", "3. Berlin"], "reponse": 1},
            {"question": "Combien font 6 x 6 ?", "options": ["1. 6", "2. 36", "3. 12"], "reponse": 2},
            {"question": "Comment s'appelle le local TI ?", "options": ["1. openLab", "2. L221", "3. Ephec Ti"], "reponse": 1},
        ]

    def lancer_de(self):
        return random.randint(1, 6)

    def avancer_pion(self, pion, resultalt):
        pion.deplacer(resultalt)
        effet = self.plateau.obtenir_effet_case(pion.position)

        if effet == "changement_map":
            self.changement_map.changement_map_active(self)

        return effet

    def reculer_pion(self, pion, resultalt):
        pion.reculer(resultalt)

    def poser_question(self):
        return random.choice(self.questions)

    def verif_reponse(self, reponse, question):
        return reponse == question["reponse"]

    def est_win(self, pion):
        return pion.position >= self.case_victoire

    def tour_suivant(self):
        self.joueur_actuel = (self.joueur_actuel + 1) % len(self.pions)

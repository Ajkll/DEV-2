class Deplacement:
    """Class représentant le mouvement d'un pion dans le jeu et ses interactions avec le plateau.
    """

    def __init__(self, pion_choisi=None, de=None, cases_reculer=None, cases_map=None, cases_question=None):
        """Initialises la class Deplacement avec un pion, des dés.

        PRE: pion_choisi est un objet representant le pion.
        POST: Initialise les attributs de la classe avec les valeurs par défaut ou bien les valeurs données.
        """

    def lancer_deplacement(self):
        """Déclenches les mouvements en demarrant le dé.

        PRE: self.de et self.pion_choisi sont initialisés.
        POST: Initialise le mouvement vers la destination si possible.
        RAISES: si le dé ou le pion n'est pas initialisé, ou si le pion est sur une case invalide on a ValueError.
        """

    def update(self):
        """Mettre à jour la position du pion.

        PRE: Le déplacement est vers l'avant ou reculer.
        POST: Mets a jour la position du pion et gestion des effets des cases spéciales.
        """

    def _effectuer_recul(self):
        """Gérer le retour en arriere du pion.

        PRE: self.recul_en_cours est True et self.case_recul est initialisée.
        POST: Le pion recule jusqu'à la case determinée.
        """

    def question_reponse(self):
        """Posez une question aléatoire et vérifiez la réponse du joueur.

        PRE: self.questions contient au moins une question.
        POST: Une question est posée et ca vérifie la réponse et affiche un message en fonction.
        RAISES: Si la reponse de l'utilisateur est invalide = ValueError.
        """
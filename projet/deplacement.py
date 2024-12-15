import random

class Deplacement:
    def __init__(self, pion_choisi=None, de=None, cases_reculer=None, cases_map = None, cases_question = None):
        self.pion_choisi = pion_choisi
        self.de = de
        self.vitesse = 3
        self.case_destination = 0
        self.en_cours = False  # Indique si un déplacement est en cours
        self.cases_a_parcourir = []

        self.cases_reculer = cases_reculer
        self.cases_map = cases_map
        self.cases_question = cases_question

        self.recul_en_cours = False
        self.case_recul = None 

        self.questions = [
            {
                "question": "Quelle est la capitale de la France ?",
                "options": ["1. Paris", "2. Londres", "3. Berlin"],
                "answer": 1 
            },
            {
                "question": "Combien font 5 x 5 ?",
                "options": ["1. 20", "2. 25", "3. 30"],
                "answer": 2
            },
            {
                "question": "Quelle est la couleur du ciel par temps clair ?",
                "options": ["1. Rouge", "2. Bleu", "3. Vert"],
                "answer": 2
            }
        ]

    def lancer_deplacement(self):
        if not self.de or not self.pion_choisi:
            print("Erreur : Dé ou Pion non initialisé.")
            return

        # Lancer le dé
        de_resultat = self.de.lancer_de()
        case_actuelle = self.pion_choisi.get_case()

        if case_actuelle is None:
            print("Erreur : Le pion n'est pas sur une case valide.")
            return

        self.case_destination = case_actuelle + de_resultat

        if self.case_destination < len(self.pion_choisi.cases_deplacement):
            self.cases_a_parcourir = self.pion_choisi.cases_deplacement[case_actuelle + 1:self.case_destination + 1]
            self.en_cours = True
        else: 
            print("Erreur : La case destination est hors des limites.")

    def update(self):
        if self.recul_en_cours:
            self._effectuer_recul()
            return

        if not self.en_cours or not self.cases_a_parcourir:
            return

        case_suivante = self.cases_a_parcourir[0] 

        if self.pion_choisi.x < case_suivante.x:
            self.pion_choisi.x = min(self.pion_choisi.x + self.vitesse, case_suivante.x)
        elif self.pion_choisi.x > case_suivante.x:
            self.pion_choisi.x = max(self.pion_choisi.x - self.vitesse, case_suivante.x)

        if self.pion_choisi.y < case_suivante.y:
            self.pion_choisi.y = min(self.pion_choisi.y + self.vitesse, case_suivante.y)
        elif self.pion_choisi.y > case_suivante.y:
            self.pion_choisi.y = max(self.pion_choisi.y - self.vitesse, case_suivante.y)


        if self.pion_choisi.x == case_suivante.x and self.pion_choisi.y == case_suivante.y:
            case_numero = self.pion_choisi.cases_deplacement.index(case_suivante)
            print(f"Le pion {self.pion_choisi.nom} est à la case n° {case_numero}.")
            self.cases_a_parcourir.pop(0)

            if not self.cases_a_parcourir:
                self.en_cours = False # si le pion atteint sa destination le déplacement en cours est remis à faux

                for case in self.cases_reculer:
                    if case.collidepoint(self.pion_choisi.x, self.pion_choisi.y):
                        print(f"{self.pion_choisi.nom} est sur une case 'reculer'. Il recule !") # on detecte que le joueur se trouve sur une casse recule

                        case_numero = max(case_numero - 1, 0) 

                        self.case_recul = self.pion_choisi.cases_deplacement[case_numero]

                        self.recul_en_cours = True  
                        break

                for case in self.cases_map:
                    if case.collidepoint(self.pion_choisi.x, self.pion_choisi.y):
                        print(f"{self.pion_choisi.nom} est sur une case changement de map !")

                for case in self.cases_question:
                    if case.collidepoint(self.pion_choisi.x, self.pion_choisi.y):
                        print(f"{self.pion_choisi.nom} est sur une case question !")
                        self.question_reponse()

    def _effectuer_recul(self):

        if self.pion_choisi.x < self.case_recul.x:
            self.pion_choisi.x = min(self.pion_choisi.x + self.vitesse, self.case_recul.x)
        elif self.pion_choisi.x > self.case_recul.x:
            self.pion_choisi.x = max(self.pion_choisi.x - self.vitesse, self.case_recul.x)

        if self.pion_choisi.y < self.case_recul.y:
            self.pion_choisi.y = min(self.pion_choisi.y + self.vitesse, self.case_recul.y)
        elif self.pion_choisi.y > self.case_recul.y:
            self.pion_choisi.y = max(self.pion_choisi.y - self.vitesse, self.case_recul.y)


        if self.pion_choisi.x == self.case_recul.x and self.pion_choisi.y == self.case_recul.y:
            print(f"{self.pion_choisi.nom} recule à la case précédente.")
            self.recul_en_cours = False


    def question_reponse(self):
        # Tirer une question au hasard
        question = random.choice(self.questions)
        print(f"Question : {question['question']}")
        print("Options :")
        for option in question["options"]:
            print(option)

        try:
            user_input = int(input("Votre réponse (entrez le numéro de l'option) : "))
            if user_input == question["answer"]:
                print("Bonne réponse ! Vous continuez votre chemin.")
            else:
                print("Mauvaise réponse. Essayez de nouveau la prochaine fois.")
        except ValueError:
            print("Entrée invalide. Assurez-vous d'entrer un numéro correspondant à une option.")

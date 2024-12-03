class Deplacement:
    def __init__(self, pion_choisi=None, de=None, cases_reculer=None, cases_map = None):
        self.pion_choisi = pion_choisi
        self.de = de
        self.vitesse = 3
        self.case_destination = 0
        self.en_cours = False  # Indique si un déplacement est en cours
        self.cases_a_parcourir = []
        self.cases_reculer = cases_reculer
        self.cases_map = cases_map
        self.recul_en_cours = False
        self.case_recul = None 

    def lancer_deplacement(self):
        if not self.de or not self.pion_choisi:
            print("Erreur : Dé ou Pion non initialisé.")
            return

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
                self.en_cours = False 

                for case in self.cases_reculer:
                    if case.collidepoint(self.pion_choisi.x, self.pion_choisi.y):
                        print(f"{self.pion_choisi.nom} est sur une case 'reculer'. Il recule !") 

                        case_numero = max(case_numero - 1, 0) 

                        self.case_recul = self.pion_choisi.cases_deplacement[case_numero]

                        self.recul_en_cours = True  
                        break

                for case in self.cases_map:
                    if case.collidepoint(self.pion_choisi.x, self.pion_choisi.y):
                        print(f"{self.pion_choisi.nom} est sur une case changement de map !")

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
            self.recul_en_cours = False  # Fin du mode de recul



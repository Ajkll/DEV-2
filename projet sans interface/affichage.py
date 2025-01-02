class Affichage:
    def afficher_message(self, message):
        print(message)

    def affichage_pion(self, pion):
        print(f"{pion.nom} est maintenant sur la case {pion.position}.")

    def affichage_plateau(self, plateau):
        print("\nVoici le plateau de jeu :")
        print(plateau)

    def demander_action(self, pion):
        choix = input(f"{pion.nom}, voulez-vous lancer le dé ? (y/n) : ").strip().lower()
        return choix == 'y'

    def annoncer_vainqueur(self, pion):
        print(f"Félicitations, {pion.nom}, vous gagnez la partie !")

    def affichage_effet_case(self, effet, pion):
        if effet == "reculer":
            print(f"Attention ! {pion.nom}, vous devez reculer de 2 cases.")
        elif effet == "question":
            print(f"{pion.nom}, vous êtes sur une case Question !")
        elif effet == "changement_map":
            print(f"{pion.nom}, vous avez déclenché un changement de map ! Le plateau est réinitialisé, vous êtes à la case départ")

    def poser_question(self, question):
        print(f"Question : {question['question']}")
        for option in question["options"]:
            print(option)

        while True:  # while pour verifier le numero
            reponse = input("Votre réponse (entrez le numéro de l'option) : ").strip()
            if reponse.isdigit():
                return int(reponse)
            else:
                print("Choix de réponse invalide. Veuillez entrer un numéro de réponses.")

    def affichage_resultat_question(self, correct, pion):
        if correct:
            print(f"Bonne réponse ! {pion.nom}, vous avancez d'une case.")
        else:
            print(f"Mauvaise réponse ! {pion.nom}, vous reculez d'une case.")

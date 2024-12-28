class Affichage:
    @staticmethod
    def afficher_message(message):
        print(message)

    @staticmethod
    def affichage_pion(pion):
        print(f"{pion.nom} est maintenant sur la case {pion.position}.")

    @staticmethod
    def affichage_plateau(plateau):
        print("\nVoici le plateau de jeu :")
        print(plateau)

    @staticmethod
    def demander_action(pion):
        choix = input(f"{pion.nom}, voulez-vous lancer le dé ? (y/n) : ").strip().lower()
        return choix == 'y'

    @staticmethod
    def annoncer_vainqueur(pion):
        print(f"Félicitations, {pion.nom}, vous gagnez la partie !")

    @staticmethod
    def affichage_effet_case(effet, pion):
        if effet == "reculer":
            print(f"Attention ! {pion.nom}, vous devez reculer de 2 cases.")
        elif effet == "question":
            print(f"{pion.nom}, vous etes sur une case Question !")
        elif effet == "changement_map":
            print(f"{pion.nom}, vous avez déclenché un changement de map ! Le plateau est réinitialisé, vous etes a la case départ")

    @staticmethod
    def poser_question(question):
        print(f"Question : {question['question']}")
        for option in question["options"]:
            print(option)

        while True:  # Boucle pour demander une entrée valide
            reponse = input("Votre réponse (entrez le numéro de l'option) : ").strip()
            if reponse.isdigit():  # Vérifie que l'entrée est un nombre
                return int(reponse)
            else:
                print("Choix de réponse invalide. Veuillez entrer un numéro de réponses.")

    @staticmethod
    def affichage_resultat_question(correct, pion):
        if correct:
            print(f"Bonne réponse ! {pion.nom} , vous avancez d'une case.")
        else:
            print(f"Mauvaise réponse ! {pion.nom}, vous reculez d'une case.")

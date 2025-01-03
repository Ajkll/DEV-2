from jeu import Jeu
from affichage import Affichage

def main():
    affichage = Affichage()

    # Initialisation du jeu
    noms_joueurs = ["Pion 1", "Pion 2"]
    cases_speciales = {
        2: "question",
        5: "reculer",
        8: "question",
        10: "changement_map",
        12: "changement_map",
        13: "question"
    }
    jeu = Jeu(noms_joueurs, length_plateau=15, cases_speciales=cases_speciales)

    affichage.afficher_message("Démarrage du jeu de plateau !")
    affichage.affichage_plateau(jeu.plateau)

    winn = False
    while not winn:
        pion_actuel = jeu.pions[jeu.joueur_actuel]

        if affichage.demander_action(pion_actuel):
            valeur_de = jeu.lancer_de()
            affichage.afficher_message(f"{pion_actuel.nom} a lancé le dé et a obtenu un {valeur_de}.")

            effet = jeu.avancer_pion(pion_actuel, valeur_de)
            affichage.affichage_pion(pion_actuel)

            if effet == "reculer":
                affichage.affichage_effet_case(effet, pion_actuel)
                jeu.reculer_pion(pion_actuel, 2)

            elif effet == "question":
                affichage.affichage_effet_case(effet, pion_actuel)
                question = jeu.poser_question()
                reponse = affichage.poser_question(question)
                correct = jeu.verif_reponse(reponse, question)
                affichage.affichage_resultat_question(correct, pion_actuel)
                if correct:
                    jeu.avancer_pion(pion_actuel, 1)
                else:
                    jeu.reculer_pion(pion_actuel, 1)

            elif effet == "changement_map":
                affichage.affichage_effet_case(effet, pion_actuel)
                affichage.affichage_plateau(jeu.plateau)

            if jeu.est_win(pion_actuel):
                affichage.annoncer_vainqueur(pion_actuel)
                winn = True
            else:
                jeu.tour_suivant()

if __name__ == "__main__":
    main()

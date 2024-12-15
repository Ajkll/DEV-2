import pygame
import os
from board_map import Map

class Pion:
    def __init__(self, x, y, image_path, nom ,cases_deplacement = None):
        self.x = x
        self.y = y
        self.selectionne = False
        self.image = self.load_image(image_path)
        self.cases_deplacement = cases_deplacement
        self.nom = nom

    def load_image(self, path):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            full_path = os.path.join(script_dir, path)
            
            if not os.path.exists(full_path):
                print(f"Erreur : Le fichier image '{full_path}' n'existe pas.")
                return None

            image = pygame.image.load(full_path).convert_alpha()
            return image
        except pygame.error as e:
            print(f"Erreur Pygame lors du chargement de l'image {path}: {e}")
            return None

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_case(self):
        if not self.cases_deplacement:
            print("Erreur : Aucune case de déplacement définie.")
            return None

        for index, case in enumerate(self.cases_deplacement):
            
            if isinstance(case, pygame.Rect) and case.collidepoint(self.x, self.y):
                print(f"Pion sur la case {index}")
                return index
            else:
                print(f"Case {index} non valide ou le pion n'est pas sur cette case.")
        
        print("Erreur : Le pion n'est pas sur une case valide.")
        return None




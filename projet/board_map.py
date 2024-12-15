import pytmx
import random
import pygame

class Map:
    def __init__(self):
        self.liste_map = []  # Liste pour stocker les différentes cartes
        self.map_au_hasard = None  # Carte sélectionnée au hasard
        self.cases_deplacement = []  # Cases de déplacement
        self.cases_reculer = []  # Cases où le joueur recule
        self.cases_pieces = []  # (Non utilisé, mais gardé si nécessaire)
        self.cases_map = []  # Cases pour changer de carte
        self.cases_question = []  # Cases pour poser des questions

    def load_map(self):
        try:
            # Charger les cartes dans la liste
            for i in range(2):
                self.liste_map.append(pytmx.load_pygame(f"tileset/map_{i}.tmx"))  # Ajouter chaque carte tmx

            # Sélectionner une carte au hasard
            self.map_au_hasard = random.choice(self.liste_map) 

            # Charger les cases spécifiques à partir des objets de la carte
            for obj in self.map_au_hasard.objects:
                if obj.type == "roto": 
                    self.cases_deplacement.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height)) 

                elif obj.type == "cases_reculer":
                    self.cases_reculer.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

                elif obj.type == "changement_map":
                    self.cases_map.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

                elif obj.type == "cases_question":
                    self.cases_question.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

            print(f"Cases de déplacement : {len(self.cases_deplacement)}")
            print(f"Cases reculer : {len(self.cases_reculer)}")
            print(f"Cases changement de map : {len(self.cases_map)}")
            print(f"Cases questions : {len(self.cases_question)}")

        except pygame.error as e:
            print(f"Erreur lors du chargement de la carte : {e}")

    def draw(self, surface):
        # Vérifie si une carte est chargée avant de dessiner
        if self.map_au_hasard is None:
            print("Aucune carte chargée.")
            return

        # Dessiner chaque calque visible de la carte
        for layer in self.map_au_hasard.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):  # Vérifie si le calque est un calque de tuiles
                for x, y, gid in layer:
                    tile = self.map_au_hasard.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.map_au_hasard.tilewidth, y * self.map_au_hasard.tileheight))

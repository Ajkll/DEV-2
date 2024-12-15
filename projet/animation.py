import pygame

class Animation:
    def __init__(self):
        self.animations = {
            "mario_droite": [],
            "mario_gauche": [],
            "mario_devant": [],
            "mario_win": [],
            "luigi_droite": []
        }

    def charger_animation(self, prefix, count, liste_animation):
        for i in range(count):
            image = pygame.image.load(f"sprites/{prefix}_{i}.png").convert_alpha()
            liste_animation.append(image)
            print(self.animations["mario_droite"])

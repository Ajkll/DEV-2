import pygame
import time


class ChoixPion:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.largeur = fenetre.get_width()
        self.hauteur = fenetre.get_height()

        # Charger les images (ajustez les chemins en fonction de votre projet)
        try:
            self.background = pygame.image.load("img/background_2.jpg")
            self.background = pygame.transform.scale(self.background, (self.largeur, self.hauteur))

            self.bouton_exit = pygame.image.load("img/bouton_exit.png").convert_alpha()
            self.bouton_exit = pygame.transform.scale(self.bouton_exit, (106, 50))
            self.bouton_exit_rect = self.bouton_exit.get_rect(topleft=(10, 10))

            self.image_pion_1 = pygame.image.load("img/mario.png").convert_alpha()
            self.image_pion_1 = pygame.transform.scale(self.image_pion_1, (80, 120))
            self.pion_1_rect = pygame.Rect((self.largeur // 3 - 40, self.hauteur // 2 - 200, 80, 120))

            self.image_pion_2 = pygame.image.load("img/luigi.png").convert_alpha()
            self.image_pion_2 = pygame.transform.scale(self.image_pion_2, (64, 136))
            self.pion_2_rect = pygame.Rect((self.largeur // 2 + 32, self.hauteur // 2 - 200, 64, 136))

            self.image_pion_3 = pygame.image.load("img/peach.png").convert_alpha()
            self.image_pion_3 = pygame.transform.scale(self.image_pion_3, (80, 148))
            self.pion_3_rect = pygame.Rect((self.largeur // 2 + 32, self.hauteur // 2, 80, 148))

            self.image_pion_4 = pygame.image.load("img/yoshi.png").convert_alpha()
            self.image_pion_4 = pygame.transform.scale(self.image_pion_4, (64, 124))
            self.pion_4_rect = pygame.Rect((self.largeur // 3 - 40, self.hauteur // 2, 64, 124))

            self.default_cursor = pygame.SYSTEM_CURSOR_ARROW
            self.hand_cursor = pygame.SYSTEM_CURSOR_HAND

            self.mario_dance = []
            self.peach_dance = []
            
            for i in range(24): 
                image = pygame.image.load(f"sprites/mario_animation/dance/mario_dance_{i}.png")
                image_resized = pygame.transform.scale(image, (80, 120))  # Redimensionner chaque image
                self.mario_dance.append(image_resized) # avant d'ajouter a la liste

            for i in range(24):
                image = pygame.image.load(f"sprites/peach_animation/dance/peach_dance_{i}.png") # on charge tous les image de dance de peach
                image_resized = pygame.transform.scale(image, (80, 148))  # Redimensionner l'image de danse ici
                self.peach_dance.append(image_resized) # avant de les ajouter aussi a la liste
                
            self.mario_animation_frame = 0
            self.peach_animation_frame = 0 
            self.last_update_time = pygame.time.get_ticks()  

            self.animation_delay = 100 # cela permet de determiner la vitesse de notre animation
            
        except pygame.error as e:
            print("Erreur lors du chargement des ressources de ChoixPion :", e)

    def draw(self):
        # Dessiner l'arrière-plan, le bouton exit et les personnages
        self.fenetre.blit(self.background, (0, 0))
        self.fenetre.blit(self.bouton_exit, self.bouton_exit_rect)
        self.fenetre.blit(self.image_pion_1, self.pion_1_rect.topleft)
        self.fenetre.blit(self.image_pion_2, self.pion_2_rect.topleft)
        self.fenetre.blit(self.image_pion_3, self.pion_3_rect.topleft)
        self.fenetre.blit(self.image_pion_4, self.pion_4_rect.topleft)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pion_1_rect.collidepoint(event.pos):
                        return 'pion_1'
                    if self.pion_2_rect.collidepoint(event.pos):
                        return 'pion_2'
                    if self.pion_3_rect.collidepoint(event.pos):
                        return 'pion_3'
                    if self.pion_4_rect.collidepoint(event.pos):
                        return 'pion_4'
                    if self.bouton_exit_rect.collidepoint(event.pos):
                        return False

            #animation mario au sruvol de la souris
            if self.pion_1_rect.collidepoint(pygame.mouse.get_pos()):
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update_time > self.animation_delay:
                    self.mario_animation_frame += 1
                    if self.mario_animation_frame >= len(self.mario_dance):
                        self.mario_animation_frame = 0  
                    self.image_pion_1 = self.mario_dance[self.mario_animation_frame]
                    self.last_update_time = current_time

            elif self.pion_2_rect.collidepoint(pygame.mouse.get_pos()):
                print("Souris sur le pion 2")

            # animation peach au survol de la souris
            elif self.pion_3_rect.collidepoint(pygame.mouse.get_pos()): 
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update_time > self.animation_delay:
                    self.peach_animation_frame += 1
                    if self.peach_animation_frame >= len(self.peach_dance):
                        self.peach_animation_frame = 0  
                    self.image_pion_3 = self.peach_dance[self.peach_animation_frame]
                    self.last_update_time = current_time
                    
            elif self.pion_4_rect.collidepoint(pygame.mouse.get_pos()):
                print("Souris sur le pion 4")


            # Mettre à jour l'écran
            pygame.display.update()

            # Changer le curseur selon la souris
            if any(rect.collidepoint(pygame.mouse.get_pos()) for rect in [self.bouton_exit_rect, self.pion_1_rect, self.pion_2_rect, self.pion_3_rect, self.pion_4_rect]):
                pygame.mouse.set_cursor(self.hand_cursor)
            else:
                pygame.mouse.set_cursor(self.default_cursor)

            self.draw()

        return False

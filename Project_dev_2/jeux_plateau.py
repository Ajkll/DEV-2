import pygame
import random
import time
import pytmx

class JeuxPlateau:
    def __init__(self, pion_1_selectionne=False, pion_2_selectionne=False, pion_3_selectionne=False, pion_4_selectionne=False):
        self.en_cours = True
        self.largeur = 800
        self.hauteur = 600

        # Initialize pygame and window
        pygame.init()
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Jeux de Plateau")

        self.cases_deplacement = []
        self.cases_reculer = []
        self.cases_pieces = []
        self.cases_map = []
        
        self.mario_deplacement_droite = []
        
        self.case_actuelle = 0
        self.case_actuelle_2 = 0
        self.case_actuelle_3 = 0
        self.case_actuelle_4 = 0
        
        self.case_destination = 0
        self.case_destination_2 = 0
        self.case_destination_3 = 0
        self.case_destination_4 = 0

        self.vitesse_deplacement = 1
        self.en_recul = False

        self.piece_1 = 0
        self.piece_2 = 0
        self.piece_3 = 0
        self.piece_4 = 0

        font_mario = "font/SuperMario256.ttf"
        font = pygame.font.Font(font_mario, 24)
        self.text_piece = font.render('Piece Mario: ' + str(self.piece_1), True, (255, 255, 255))

        self.liste_map = []

        try:
            for i in range(2):
                self.liste_map.append(pytmx.load_pygame(f"tileset/map_{i}.tmx"))

            self.map_au_hasard = random.choice(self.liste_map)
                
            self.pion_1_selectionne = pion_1_selectionne
            self.pion_2_selectionne = pion_2_selectionne
            self.pion_3_selectionne = pion_3_selectionne
            self.pion_4_selectionne = pion_4_selectionne

            self.image_pion_1 = pygame.image.load("img/mario.png").convert_alpha()
            self.image_pion_1 = pygame.transform.scale(self.image_pion_1, (20, 30))
            self.pion_1_rect = self.image_pion_1.get_rect()

            self.son_lancer_de = pygame.mixer.Sound("mp3/cube.mp3")
            self.son_piece = pygame.mixer.Sound("mp3/coin.mp3")

            # Pions supplémentaires
            self.image_pion_2 = pygame.image.load("img/luigi.png").convert_alpha()
            self.image_pion_2 = pygame.transform.scale(self.image_pion_2, (16, 34))

            self.image_pion_3 = pygame.image.load("img/peach.png").convert_alpha()
            self.image_pion_3 = pygame.transform.scale(self.image_pion_3, (20, 37))

            self.image_pion_4 = pygame.image.load("img/yoshi.png").convert_alpha()
            self.image_pion_4 = pygame.transform.scale(self.image_pion_4, (16, 31))

            # Charger les images d'animation (pour exemple pour pion 1
            self.animation_mario_droite = []
            self.animation_mario_devant = []
            self.animation_mario_gauche = []
            self.animation_mario_win = []
            
            self.animation_luigi_droite = []
            
            self.mario_animation_frame_droite = 0
            self.mario_animation_frame_devant = 0
            self.mario_animation_frame_gauche = 0
            self.mario_animation_frame_win = 0

            self.luigi_animation_frame_droite = 0

            for i in range(10):
                image_mario_droite = pygame.image.load(f"sprites/mario_animation/droite/mario_droite_{i}.png").convert_alpha()
                self.animation_mario_droite.append(image_mario_droite)

            for i in range(10):
                image_mario_gauche = pygame.image.load(f"sprites/mario_animation/gauche/mario_gauche_{i}.png").convert_alpha()
                self.animation_mario_gauche.append(image_mario_gauche)

            for i in range(10):
                image_mario_devant = pygame.image.load(f"sprites/mario_animation/devant/mario_devant_{i}.png").convert_alpha()
                self.animation_mario_devant.append(image_mario_devant)

            for i in range(4): 
                image_mario_win = pygame.image.load(f"sprites/mario_animation/win/mario_win_{i}.png").convert_alpha()
                self.animation_mario_win.append(image_mario_win)

            for i in range(10):
                image_luigi_droite = pygame.image.load(f"sprites/luigi_animation/droite/luigi_droite_{i}.png").convert_alpha()
                self.animation_luigi_droite.append(image_luigi_droite)

            self.last_update_time = pygame.time.get_ticks()
            self.last_update_time_luigi = pygame.time.get_ticks()  
            self.animation_delay = 100
                
            #############################################

            # Faces de dé
            self.faces = [pygame.image.load(f"img/face_{i}.png").convert_alpha() for i in range(1, 7)]
            self.faces = [pygame.transform.scale(face, (100, 100)) for face in self.faces]
            self.bouton_active = True
            self.nombre_clic = 0
            
            # Paramètres d'animation du dé
            self.face_choisie = None
            self.duree_animation = 4
            self.temps_initial = None

            # Boutons
            self.bouton_play = pygame.image.load("img/bouton_commencer.png").convert_alpha()
            self.bouton_play = pygame.transform.scale(self.bouton_play, (107, 32))
            self.bouton_rect = pygame.Rect((self.largeur // 2 - 53, 60, 107, 32))

            self.bouton_exit = pygame.image.load("img/bouton_exit.png").convert_alpha()
            self.bouton_exit = pygame.transform.scale(self.bouton_exit, (106, 50))
            self.bouton_exit_rect = self.bouton_exit.get_rect(topleft=(10, 10))

            # Charger les cases de déplacement
            for obj in self.map_au_hasard.objects:
                if obj.type == "roto":
                    self.cases_deplacement.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

            for obj in self.map_au_hasard.objects:
                if obj.type == "cases_reculer":
                    self.cases_reculer.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

            for obj in self.map_au_hasard.objects:
                if obj.type == "gagner_pieces":
                    self.cases_pieces.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

            for obj in self.map_au_hasard.objects:
                if obj.type == "changement_map":
                    self.cases_map.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

            # Initialiser les positions des pions
            if self.cases_deplacement:
                self.pion_1_x, self.pion_1_y = self.cases_deplacement[0].topleft
                self.pion_2_x, self.pion_2_y = self.cases_deplacement[0].topleft
                self.pion_3_x, self.pion_3_y = self.cases_deplacement[0].topleft
                self.pion_4_x, self.pion_4_y = self.cases_deplacement[0].topleft

        except pygame.error as e:
            print("Erreur lors du chargement des ressources de JeuxPlateau :", e)

    def draw_background(self):
        for layer in self.map_au_hasard.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.map_au_hasard.get_tile_image_by_gid(gid)
                    if tile:
                        self.fenetre.blit(tile, (x * self.map_au_hasard.tilewidth, y * self.map_au_hasard.tileheight))

    def draw(self):
        self.draw_background()
        self.fenetre.blit(self.bouton_play, self.bouton_rect.topleft)

        # Dessiner le pion 1
        if self.pion_1_selectionne:
            self.fenetre.blit(self.image_pion_1, (self.pion_1_x, self.pion_1_y))
            self.fenetre.blit(self.text_piece, (16, 16))

        # Dessiner le pion 2
        if self.pion_2_selectionne:
            self.fenetre.blit(self.image_pion_2, (self.pion_2_x, self.pion_2_y))

        # Dessiner le pion 3
        if self.pion_3_selectionne:
            self.fenetre.blit(self.image_pion_3, (self.pion_3_x, self.pion_3_y))

         # Dessiner le pion 4
        if self.pion_4_selectionne:
            self.fenetre.blit(self.image_pion_4, (self.pion_4_x, self.pion_4_y))

        # Mise à jour du texte (à chaque frame)
        font_mario = "font/SuperMario256.ttf"
        font = pygame.font.Font(font_mario, 24)
        self.text_piece = font.render('Piece Mario: ' + str(self.piece_1), True, (255, 255, 255))
        self.fenetre.blit(self.text_piece, (16, 16))

        self.texte_cases = font.render('case n° : ' + str(self.case_actuelle), True, (255, 255, 255))
        self.fenetre.blit(self.texte_cases, (300, 16))


        # Lancer de dé et animation
        if self.temps_initial is not None:
            elapsed_time = time.time() - self.temps_initial
            if elapsed_time < self.duree_animation:
                self.face_choisie = random.choice(self.faces)
            else:
                self.face_choisie = random.choice(self.faces)
                self.temps_initial = None
                self.valeur_de = self.faces.index(self.face_choisie) + 1
                self.case_destination = self.case_actuelle + self.valeur_de
                self.case_destination_2 = self.case_actuelle_2 + self.valeur_de

                # Assurez-vous de ne pas dépasser les cases disponibles
                if self.case_destination >= len(self.cases_deplacement):
                    self.case_destination = len(self.cases_deplacement) - 1

                if self.case_destination_2 >= len(self.cases_deplacement):
                    self.case_destination_2 = len(self.cases_deplacement) - 1

        # Déplacement du pion 1 ########################################################################################################"""
        if not self.en_recul and self.case_actuelle < self.case_destination: 
            destination_rect = self.cases_deplacement[self.case_actuelle + 1]

            if self.pion_1_x < destination_rect.x:
                self.pion_1_x += self.vitesse_deplacement
                self.bouton_active = False 

                # Animation du déplacement vers la droite 
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update_time > self.animation_delay:
                    self.mario_animation_frame_droite += 1
                    if self.mario_animation_frame_droite >= len(self.animation_mario_droite):
                        self.mario_animation_frame_droite = 0  # Revenir à la première image

                    self.image_pion_1 = self.animation_mario_droite[self.mario_animation_frame_droite]
                    self.last_update_time = current_time
                    
            # déplacer le pion vers le haut 
            elif self.pion_1_y > destination_rect.y:
                self.pion_1_y -= self.vitesse_deplacement
                self.bouton_active = False 

                #animation déplacement vers le haut
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update_time > self.animation_delay:
                    self.mario_animation_frame_devant += 1
                    if self.mario_animation_frame_devant >= len(self.animation_mario_devant):
                        self.mario_animation_frame_devant = 0  # Revenir à la première image

                    self.image_pion_1 = self.animation_mario_devant[self.mario_animation_frame_devant]
                    self.last_update_time = current_time

            # déplacer le pion vers le bas 
            elif self.pion_1_y < destination_rect.y:
                self.pion_1_y += self.vitesse_deplacement
                self.bouton_active = False 

            elif self.pion_1_x > destination_rect.x:
                self.pion_1_x -= self.vitesse_deplacement
                self.bouton_active = False

                #animation déplacement vers la gauche
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update_time > self.animation_delay:
                    self.mario_animation_frame_gauche += 1
                    if self.mario_animation_frame_gauche >= len(self.animation_mario_gauche):
                        self.mario_animation_frame_gauche = 0  # Revenir à la première image

                    self.image_pion_1 = self.animation_mario_gauche[self.mario_animation_frame_gauche]
                    self.last_update_time = current_time
                    
                    
            else:
                if self.case_actuelle + 1 < len(self.cases_deplacement):
                    self.case_actuelle += 1
                    self.image_pion_1 = pygame.image.load("sprites/mario_animation/dance/mario_dance_0.png").convert_alpha()

                    if self.case_actuelle == self.case_destination: #si mon pion est arrivé à destination
                        self.bouton_active = True
                        self.nombre_clic = 0 
                        for case in self.cases_reculer: # pour les cases présent dans la liste des cases recul
                            if case.collidepoint(self.pion_1_x, self.pion_1_y): # si l'un de mes cases recul touch mon pion
                                print("case reculer")
                                self.case_destination = max(0, self.case_actuelle - 1)  # Reculer d'une case sans sortir de la grille
                                self.en_recul = True  # Activer l'état de recul
                                    
                                
                        for case in self.cases_pieces: 
                            if case.collidepoint(self.pion_1_x, self.pion_1_y): 
                                self.piece_1 += 5
                                self.son_piece.play()

                        for case in self.cases_map:
                            if case.collidepoint(self.pion_1_x, self.pion_1_y):
                                nouvelle_map = random.choice(self.liste_map) 
                                while nouvelle_map == self.map_au_hasard:
                                    nouvelle_map = random.choice(self.liste_map)

                                self.map_au_hasard = nouvelle_map

                                self.cases_deplacement = [
                                    pygame.Rect(obj.x, obj.y, obj.width, obj.height) 
                                    for obj in self.map_au_hasard.objects if obj.type == "roto"
                                ]

                                self.cases_reculer = [
                                    pygame.Rect(obj.x, obj.y, obj.width, obj.height) 
                                    for obj in self.map_au_hasard.objects if obj.type == "cases_reculer"
                                ]
                                self.cases_pieces = [
                                    pygame.Rect(obj.x, obj.y, obj.width, obj.height) 
                                    for obj in self.map_au_hasard.objects if obj.type == "gagner_pieces"
                                ]
                                self.cases_map = [
                                    pygame.Rect(obj.x, obj.y, obj.width, obj.height) 
                                    for obj in self.map_au_hasard.objects if obj.type == "changement_map"
                                ]

                                if self.cases_deplacement:
                                    self.pion_1_x, self.pion_1_y = self.cases_deplacement[self.case_actuelle].topleft

                                self.draw_background()



        elif self.en_recul and self.case_actuelle > self.case_destination:
            destination_rect = self.cases_deplacement[self.case_actuelle - 1]

            if self.pion_1_x > destination_rect.x:
                self.pion_1_x -= self.vitesse_deplacement
                self.bouton_active = False 
                self.nombre_clic = 0
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update_time > self.animation_delay:
                    self.mario_animation_frame_gauche += 1
                    if self.mario_animation_frame_gauche >= len(self.animation_mario_gauche):
                        self.mario_animation_frame_gauche = 0

                    self.image_pion_1 = self.animation_mario_gauche[self.mario_animation_frame_gauche]
                    self.last_update_time = current_time

            else:
                self.case_actuelle -= 1
                if self.case_actuelle == self.case_destination:
                    self.bouton_active = True 
                    self.en_recul = False
                    self.image_pion_1 = pygame.image.load("sprites/mario_animation/dance/mario_dance_0.png").convert_alpha()

                    for case in self.cases_pieces:
                        if case.collidepoint(self.pion_1_x, self.pion_1_y): 
                            self.piece_1 += 5
                            self.son_piece.play()
                        

        # Déplacement du pion 2 ###############################################################################################################"
        if self.case_actuelle_2 < self.case_destination_2:
            destination_rect_2 = self.cases_deplacement[self.case_actuelle_2 + 1]
            if self.pion_2_x < destination_rect_2.x:
                self.pion_2_x += self.vitesse_deplacement

                current_time = pygame.time.get_ticks()
                if current_time - self.last_update_time_luigi > self.animation_delay:
                    self.luigi_animation_frame_droite += 1
                    if self.luigi_animation_frame_droite >= len(self.animation_luigi_droite):
                        self.luigi_animation_frame_droite = 0  # Revenir à la première image

                    self.image_pion_2 = self.animation_luigi_droite[self.luigi_animation_frame_droite]
                    self.last_update_time_luigi = current_time
                    
            elif self.pion_2_y > destination_rect_2.y:
                self.pion_2_y -= self.vitesse_deplacement

            elif self.pion_2_x > destination_rect_2.x:
                self.pion_2_x -= self.vitesse_deplacement
                
            else:
                if self.case_actuelle_2 + 1 < len(self.cases_deplacement):
                    self.case_actuelle_2 += 1
                    self.luigi_animation_frame_droite = 0  # Réinitialisation de l'animation à la première image
                    self.image_pion_2 = self.animation_luigi_droite[self.luigi_animation_frame_droite]  # Mettre à jour l'image

        # Déplacement du pion 3
        if self.case_actuelle_3 < self.case_destination_3:
            destination_rect_3 = self.cases_deplacement[self.case_actuelle_3 + 1]
            if self.pion_3_x < destination_rect_3.x:
                self.pion_3_x += self.vitesse_deplacement
            elif self.pion_3_y < destination_rect_3.y:
                self.pion_3_y += self.vitesse_deplacement
            else:
                if self.case_actuelle_3 + 1 < len(self.cases_deplacement):
                    self.case_actuelle_3 += 1

        # Déplacement du pion 4
        if self.case_actuelle_4 < self.case_destination_4:
            destination_rect_4 = self.cases_deplacement[self.case_actuelle_4 + 1]
            if self.pion_4_x < destination_rect_4.x:
                self.pion_4_x += self.vitesse_deplacement
            elif self.pion_4_y < destination_rect_4.y:
                self.pion_4_y += self.vitesse_deplacement
            else:
                if self.case_actuelle_4 + 1 < len(self.cases_deplacement):
                    self.case_actuelle_4 += 1

        # Afficher le visage du dé
        if self.face_choisie:
            image_rect = self.face_choisie.get_rect(center=(self.largeur // 2, self.hauteur // 2))
            self.fenetre.blit(self.face_choisie, image_rect.topleft)

        pygame.display.flip()

    def run(self):
        while self.en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.en_cours = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.bouton_active:
                    if self.bouton_rect.collidepoint(event.pos):
                        self.nombre_clic += 1
                        if self.nombre_clic == 1:
                            self.temps_initial = time.time()
                            self.son_lancer_de.play()  # Joue le son quand le bouton est cliqué

                    if self.bouton_exit_rect.collidepoint(event.pos):
                        return False

            self.draw()
        return True

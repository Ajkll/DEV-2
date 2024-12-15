import pygame

class PageAccueil:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.largeur = fenetre.get_width()
        self.hauteur = fenetre.get_height()

        try: 
            self.background = pygame.image.load("img/background.png").convert_alpha() # on importe une image de fond 
            self.background = pygame.transform.scale(self.background, (self.largeur, self.hauteur)) # on vient recadrer l'imager

            self.bouton_play = pygame.image.load("img/bouton_commencer.png").convert_alpha() # on ajoute l'image du bouton commencer
            self.bouton_play = pygame.transform.scale(self.bouton_play, (429, 129)) # on viens changer sa taille 
            self.bouton_rect = pygame.Rect((self.largeur // 2 - 214, self.hauteur // 2 - 64, 429, 129))

            # Cursor settings
            self.default_cursor = pygame.SYSTEM_CURSOR_ARROW
            self.hand_cursor = pygame.SYSTEM_CURSOR_HAND

            self.button_start_sound = pygame.mixer.Sound("mp3/start_sound.mp3")
            
        except pygame.error as e:
            print("Erreur lors du chargement des ressources de PageAccueil :", e)

    def draw(self):
        self.fenetre.blit(self.background, (0, 0)) # on vient mettre l'image de fond sur la fenetre
        self.fenetre.blit(self.bouton_play, self.bouton_rect.topleft) # on vient mettre le bouton commencer sur le background
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return False

                if self.bouton_rect.collidepoint(pygame.mouse.get_pos()): # si la souris survole le rectangle du bouton commencer
                    pygame.mouse.set_cursor(self.hand_cursor) # le curseur pointe
                    if event.type == pygame.MOUSEBUTTONDOWN: # et si fait un clique gauche
                        if self.bouton_rect.collidepoint(event.pos): # et que le clique gauche a lieu dans le rectangle 
                            self.button_start_sound.play() # alors on joue le mp3
                            return True  
                else:
                    pygame.mouse.set_cursor(self.default_cursor) # si on n'est pas dans le rectangle le curseur reste normal

            self.draw() # on appelle la fonction qui vient dessiner le fond d'écran ansi que le bouton commencer
        return False

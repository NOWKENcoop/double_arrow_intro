import pygame
import os
import time
import random
import math
# Initialisation de Pygame
pygame.init()

# Charger et définir l'icône de l'application
# Définir le chemin absolu de l'icône
icon_path = os.path.join(os.path.dirname(__file__), "../image/imd.png")



# Constantes
WIDTH, HEIGHT = 800, 600
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GREEN = (50, 200, 50)
YELLOW = (255, 215, 0)
DARK_GRAY = (100, 100, 100)
# Définition des couleurs (du dégradé CSS donné)
color1 = (5, 2, 54)     # rgba(5,2,54,1) à 9%
color2 = (48, 48, 208)  # rgba(48,48,208,1) à 51%
color3 = (26, 95, 176)  # rgba(26,95,176,1) à 93%
PLAYER_SPEED = 5
BULLET_SPEED = 7
HEALTH_BAR_WIDTH = 200
HEALTH_BAR_HEIGHT = 20
MAX_HEALTH = 100
SHOOT_COOLDOWN =500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Double Arrows")
clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 36)

background_image = pygame.image.load("../image/img.jpg")  # Remplace par le chemin de ton image de fond
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Redimensionner l'image pour qu'elle couvre l'écran


# Charger l'image que tu veux afficher en haut
image_path = "../image/S11.png"  # Remplace par le chemin de ton image
image = pygame.image.load(image_path)  # Charger l'image

image_path_1= "../image/1.jpg"  # Remplace par le chemin de ton image
image_1 = pygame.image.load(image_path_1)  # Charger l'image

image_path_2= "../image/S11.png"  # Remplace par le chemin de ton image
image_2 = pygame.image.load(image_path_2)  # Charger l'image

image_path_3= pygame.image.load("../image/c2.png")  # Remplace par le chemin de ton image
image_3 = pygame.transform.scale(image_path_3, (300, 200))  # Charger l'image

image_path_4= "../image/1.png"  # Remplace par le chemin de ton image
image_4 = pygame.image.load(image_path_4)  # Charger l'image

image_path_5= pygame.image.load("../image/imd1.png")  # Remplace par le chemin de ton image
image_5 = pygame.transform.scale(image_path_5, (300, 300))  # Charger l'image

# Redimensionner l'image si nécessaire
image = pygame.transform.scale(image, (50, 50))  # Ajuste la taille de l'image 
image_1 = pygame.transform.scale(image_1, (WIDTH, 100))  # Ajuste la taille de l'image 
image_2 = pygame.transform.scale(image_2, (50, 50))  # Ajuste la taille de l'image
image_3 = pygame.transform.scale(image_3, (500, 500))  # Ajuste la taille de l'image
image_4 = pygame.transform.scale(image_4, (WIDTH, 100))  # Ajuste la taille de l'image
image_5 = pygame.transform.scale(image_5, (500, 500))  # Ajuste la taille de l'image


# Charger les images
loading_screen = pygame.image.load("../image/imd.png")  # Image de chargement
loading_screen = pygame.transform.scale(loading_screen, (WIDTH, HEIGHT))

# Charger les images des personnages
character_images = [
    pygame.image.load("../image/4.png"),
    pygame.image.load("../image/3.png"),
    pygame.image.load("../image/5.png"),
    pygame.image.load("../image/9.png"),
    pygame.image.load("../image/2.png"),
    pygame.image.load("../image/6.png"),
    pygame.image.load("../image/7.png"),
    pygame.image.load("../image/8.png")
]

# Redimensionner les images
character_images = [pygame.transform.scale(img, (100, 100)) for img in character_images]

# Vitesses par difficulté
SPEED_MULTIPLIERS = {
    "amateur": 2,
    "normal": 8,
    "professionel": 15,
    "extra": 22
}



if os.path.exists(icon_path):
    try:
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
        print("✅ Icône chargée avec succès !")
    except pygame.error as e:
        print(f"⚠️ Impossible de charger l'icône : {e}")
else:
    print("⚠️ Erreur : L'icône 'imd.png' est introuvable !")


class Player:
    def __init__(self, x, color, up_key, down_key, shoot_key, image):
        self.x = x
        self.y = HEIGHT // 2
        self.color = color
        self.speed = PLAYER_SPEED
        self.up_key = up_key
        self.down_key = down_key
        self.shoot_key = shoot_key
        self.bullets = []
        self.health_stages = [(GREEN, 100), (YELLOW, 100), (RED, 100)]
        self.current_stage = 0
        self.image = pygame.transform.scale(image, (100, 100))  # Redimensionne l'image correctement

    def draw(self):
        screen.blit(self.image, (self.x - 25, self.y - 25))

    def move(self, keys):
        if keys[self.up_key] and self.y > 25:
            self.y -= self.speed
        if keys[self.down_key] and self.y < HEIGHT - 25:
            self.y += self.speed
    def shoot(self, keys):
        if keys[self.shoot_key]:
            self.bullets.append(Bullet(self.x, self.y, self.color))

    def shoot_training(self):
            bullet = Bullet(self.x, self.y, self.color)
            self.bullets.append(bullet)
            self.can_shoot = False
            self.shoot_timer = SHOOT_COOLDOWN  # Temps avant le prochain tir

    def update(self, keys):
        self.move(keys)

    def take_damage(self):
        if self.current_stage == 0:
            damage = 2
        elif self.current_stage == 1:
            damage = 5
        else:
            damage = 10

        self.health_stages[self.current_stage] = (self.health_stages[self.current_stage][0], 
                                                  self.health_stages[self.current_stage][1] - damage)

        if self.health_stages[self.current_stage][1] <= 0 and self.current_stage < 2:
            self.current_stage += 1  # Passe à la jauge suivante

    def is_dead(self):
        return self.current_stage == 2 and self.health_stages[self.current_stage][1] <= 0

# Classe Flèche (projectile sous forme de triangle)
class Bullet:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = BULLET_SPEED if color == RED else -BULLET_SPEED  # Droite pour rouge, gauche pour bleu

    def move(self):
        self.x += self.speed  # Déplacer la flèche uniquement en X

    def draw(self):
        points = [(self.x, self.y), (self.x - 5, self.y - 5), (self.x + 5, self.y - 5)]
        pygame.draw.polygon(screen, self.color, points)



# Fonction d'affichage de l'écran de chargement
def show_loading_screen():
    screen.blit(loading_screen, (0, 0))
    pygame.display.flip()
    time.sleep(3)  # Attendre 3 secondes avant d'afficher le menu principal


# Affichage de la barre de vie
def draw_health_bar(player, x, y):
    pygame.draw.rect(screen, DARK_GRAY, (x, y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    health_width = (player.health_stages[player.current_stage][1] / MAX_HEALTH) * HEALTH_BAR_WIDTH
    pygame.draw.rect(screen, player.health_stages[player.current_stage][0], (x, y, health_width, HEALTH_BAR_HEIGHT))

def draw_linear_gradient():
    """Dessine un dégradé horizontal avec interpolation de couleurs."""
    for x in range(WIDTH):
        t = x / WIDTH  # Normalisation entre 0 et 1

        # Interpolation entre color1 -> color2 -> color3
        if t < 0.31:  # Transition de color1 à color2
            ratio = t / 0.31
            r = int(color1[0] + ratio * (color2[0] - color1[0]))
            g = int(color1[1] + ratio * (color2[1] - color1[1]))
            b = int(color1[2] + ratio * (color2[2] - color1[2]))
        else:  # Transition de color2 à color3
            ratio = (t - 0.51) / (1 - 0.51)
            r = int(color2[0] + ratio * (color3[0] - color2[0]))
            g = int(color2[1] + ratio * (color3[1] - color2[1]))
            b = int(color2[2] + ratio * (color3[2] - color2[2]))

        pygame.draw.line(screen, (r, g, b), (x, 0), (x, HEIGHT))


# Fonction pour dessiner un dégradé vertical
def draw_gradient_2(surface, color1, color2):
    """Dessine un dégradé linéaire vertical du haut (color1) vers le bas (color2)."""
    for y in range(HEIGHT):
        # Calcul de la couleur intermédiaire pour chaque ligne
        ratio = y / HEIGHT
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)

        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))

# Couleurs du dégradé (correspondant à ton CSS)
start_color = (34, 98, 195)  # Bleu (rgba(34,98,195,0.8))
end_color = (215, 253, 45)   # Vert-jaune (rgba(215,253,45,0.7))


def training_mode():
    def start_training(difficulty):
        game_loop(training_mode=True, difficulty=difficulty)

    running = True
    while running:
        screen.fill(WHITE)
        title = FONT.render("Sélection de la difficulté", True, BLACK)
        screen.blit(title, (WIDTH // 4, 50))

        # Créer des boutons pour chaque niveau de difficulté
        draw_button("Amateur", 300, 200, 200, 50, GREEN, lambda: start_training("amateur"))
        draw_button("Normal", 300, 300, 200, 50, YELLOW, lambda: start_training("normal"))
        draw_button("Pro", 300, 400, 200, 50, BLUE, lambda: start_training("professionel"))
        draw_button("Extra", 300, 500, 200, 50, RED, lambda: start_training("extra"))
        draw_button("Retour", 300, 600, 200, 50, DARK_GRAY, main_menu)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def draw_radial_gradient(surface, color1, color2):
    """Dessine un dégradé radial de color1 au centre vers color2 sur les bords."""
    center_x, center_y = surface.get_width() // 2, surface.get_height() // 2
    max_radius = math.sqrt(center_x**2 + center_y**2)

    for y in range(surface.get_height()):
        for x in range(surface.get_width()):
            # Calcul de la distance au centre
            distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
            ratio = distance / max_radius  # Normaliser entre 0 et 1

            # Interpolation des couleurs
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)

            surface.set_at((x, y), (r, g, b))

# Définition des couleurs en (R, G, B)
color_start_help = (174, 238, 231)  # rgba(174,238,231,0.96) → Opacité ignorée en Pygame
color_end_help = (102, 97, 17)  


def help_screen():
    running = True
    while running:
        #screen.fill(WHITE)
        draw_radial_gradient(screen, color_start_help, color_end_help)
        title = FONT.render("AIDE - Commandes du jeu", True, BLACK)
        
        screen.blit(title, (WIDTH // 4, 50))

        help_text = [
            "Joueur 1: W (haut), S (bas), O(tirer)",
            "                                       ",
            "Joueur 2: Haut (UP), Bas (DOWN), 8 (tirer)",
            "                                       ",
            "Mode entraînement: Adversaire automatique",
            "                                       ",
            "Objectif: Éliminez votre adversaire avec les flèches !"
        ]

        for i, line in enumerate(help_text):
            text = FONT.render(line, True, BLACK)
            screen.blit(text, (100, 150 + i * 50))

        draw_button("Retour", 300, 530, 200, 50,RED, main_menu)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


# Fonction d'affichage du menu principal
def main_menu():
    running = True
    while running:
        #screen.fill(WHITE)
        draw_linear_gradient()
        screen.blit(image_5, (0, 0))
        title = FONT.render("Double Arrows - Menu Principal", True, BLACK)
        screen.blit(title, (WIDTH // 3, 50))
        draw_button("1 VS 1", 300, 220, 200, 50, (45,55,106), game_loop)
        draw_button("Entraînement", 300, 300, 200, 50, (213, 130, 30), training_mode)
        draw_button("Aide", 300, 400, 200, 50, (102, 73, 17), help_screen)
        draw_button("Quitter", 300, 500, 200, 50, (124, 50, 65), quit_game)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()
    exit()

# Fonction pour dessiner un bouton interactif
def draw_button(text, x, y, w, h, color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    current_color = DARK_GRAY if x < mouse[0] < x + w and y < mouse[1] < y + h else color
    pygame.draw.rect(screen, current_color, (x, y, w, h))
    text_surf = FONT.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text_surf, text_rect)
    
    if x < mouse[0] < x + w and y < mouse[1] < y + h and click[0] == 1 and action:
        pygame.time.delay(200)
        action()

# Fonction pour quitter le jeu proprement
def quit_game():
    pygame.quit()
    exit()

# Détection des collisions entre flèches et joueurs
def check_collisions(player1, player2):
    for bullet in player1.bullets:
        if player2.x - 20 < bullet.x < player2.x + 20 and player2.y - 20 < bullet.y < player2.y + 20:
            player2.take_damage()
            player1.bullets.remove(bullet)

    for bullet in player2.bullets:
        if player1.x - 20 < bullet.x < player1.x + 20 and player1.y - 20 < bullet.y < player1.y + 20:
            player1.take_damage()
            player2.bullets.remove(bullet)

# Fonction pour dessiner un dégradé linéaire
def draw_linear_gradient_1(surface, color1, color2):
    for x in range(WIDTH):
        # Calculer l'interpolation entre color1 et color2
        r = int(color1[0] + (color2[0] - color1[0]) * (x / WIDTH))
        g = int(color1[1] + (color2[1] - color1[1]) * (x / WIDTH))
        b = int(color1[2] + (color2[2] - color1[2]) * (x / WIDTH))
        pygame.draw.line(surface, (r, g, b), (x, 0), (x, HEIGHT))

# Définition des couleurs du gradient
color_start = (174, 209, 238)  # rgba(174,209,238,0.87) sans alpha
color_end = (22, 63, 161)  # rgba(22,63,161,0.73) sans alpha


# Écran de victoire
def victory_screen(winner_color):
    running = True
    while running:
        #screen.fill(WHITE)
        draw_linear_gradient_1(screen,color_start,color_end)
        text = FONT.render(f"Félicitations ! {winner_color} gagne !", True, winner_color)
        screen.blit(text, (WIDTH // 3, HEIGHT // 2))
        screen.blit(image_3, (0, 10)) 
        screen.blit(image_4, (0, 10))
        draw_button("FERMER", 300, 500, 200, 50, BLUE, main_menu)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    main_menu()


# Fonction de sélection des personnages
# Fonction pour générer une couleur aléatoire
def get_random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

# Fonction de sélection des personnages
def select_character():
    selected = [None, None]
    running = True

    # Générer des couleurs aléatoires pour les cadres des personnages
    character_colors = [get_random_color() for _ in range(len(character_images))]

    while running:
        #screen.fill(WHITE)
        draw_gradient_2(screen, start_color, end_color)
        title = FONT.render("Sélection des personnages", True, BLACK)
        screen.blit(title, (WIDTH // 4, 50))

        positions = []
        player1_text = FONT.render("JOUEUR 1", True, (200, 50, 50))
        player2_text = FONT.render("JOUEUR 2", True, (50, 50, 200))
        screen.blit(player1_text, (100, 150))
        screen.blit(player2_text, (100, 350))

        for i in range(4):  # Joueur 1 (Groupe du haut)
            x, y = 100 + i * 150, 200
            pygame.draw.rect(screen, character_colors[i], (x - 5, y - 5, 110, 110))  # Cadre coloré
            screen.blit(character_images[i], (x, y))
            positions.append((x, y, i, 0))

        for i in range(4, 8):  # Joueur 2 (Groupe du bas)
            x, y = 100 + (i - 4) * 150, 400
            pygame.draw.rect(screen, character_colors[i], (x - 5, y - 5, 110, 110))  # Cadre coloré
            screen.blit(character_images[i], (x, y))
            positions.append((x, y, i, 1))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for x, y, idx, group in positions:
                    if x < mx < x + 100 and y < my < y + 100:
                        if group == 0 and selected[0] is None:
                            selected[0] = character_images[idx]
                        elif group == 1 and selected[1] is None:
                            selected[1] = character_images[idx]

                        if selected[0] and selected[1]:
                            return selected  # Retourner les choix des joueurs
# Boucle du jeu
# Boucle principale du jeu
def game_loop(training_mode=False, difficulty="professionel"):
   
    player_images = select_character()
    player1 = Player(100, RED, pygame.K_w, pygame.K_s, pygame.K_o, player_images[0])
    player2 = Player(WIDTH - 100, BLUE, pygame.K_UP, pygame.K_DOWN, pygame.K_KP_8, player_images[1])
    speed_multiplier = SPEED_MULTIPLIERS[difficulty]
    running=True

    #show_loading_screen()  # Afficher l'écran de chargement avant le menu principal
    
    
    while running:
        # Afficher le fond
        screen.blit(background_image, (0, 0))


        # Afficher l'image en haut de la fenêtre
        screen.blit(image, (0, 10))  # L'image est positionnée à (0, 0), soit en haut à gauche
        screen.blit(image_1, (0, HEIGHT-100)) 
        screen.blit(image_2, (WIDTH-50, 10)) 

    # Mettre à jour l'affichage
        keys = pygame.key.get_pressed()
        player1.update(keys)
        player2.update(keys)
        player1.shoot(keys)
        player2.shoot(keys)

        check_collisions(player1, player2)
        if training_mode:
            player2.y += speed_multiplier
            if player2.y >= HEIGHT - 50 or player2.y <= 50:
                speed_multiplier = -speed_multiplier
            if random.randint(1,20)==2 or random.randint(10,100)==50:
                player2.shoot_training()


        if player1.is_dead():
            victory_screen(BLUE)
            return
        if player2.is_dead():
            victory_screen(RED)
            return

        player1.draw()
        player2.draw()
        draw_health_bar(player1, 50, 20)
        draw_health_bar(player2, WIDTH - 250, 20)

        for bullet in player1.bullets + player2.bullets:
            bullet.move()
            bullet.draw()
        
        else:
            player2.move(keys)
            player2.shoot(keys)

        draw_button("Retour", 300, 550, 200, 50, BLUE, main_menu)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()
        clock.tick(60)

    main_menu()

# Lancer le menu principal
main_menu()
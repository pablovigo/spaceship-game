import pygame
import random

# Inicialitza Pygame
pygame.init()

# Configuració de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Ship")

# Colors
white = (255, 255, 255)

# Rellotje
clock = pygame.time.Clock()

# Carrega les imatges
#background_image = pygame.image.load("images/background.png")
player_image = pygame.image.load("images/player_ship.png")
enemy_image = pygame.image.load("images/enemy_ship.png")

# Classe del jugador (nau)
class Player:
    def __init__(self):
        self.image = player_image
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 60))

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

# Classe de les naus enemigues
class EnemyShip:
    def __init__(self):
        self.image = enemy_image
        self.rect = self.image.get_rect(x=random.randint(0, screen_width - 50), y=0)
        self.speed = random.randint(3, 8)

    def fall(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Dibuixa la nau enemiga

# Funció principal del joc
def game_loop():
    player = Player()
    enemy_ships = []
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5)
        if keys[pygame.K_RIGHT]:
            player.move(5)

        if random.randint(1, 20) == 1:  # Crea una nau enemiga aleatòria
            enemy_ships.append(EnemyShip())

        # Dibuixa el fons
        #screen.blit(background_image, (0, 0))
        screen.fill((160, 160, 160))  # valors RGB

        for enemy in enemy_ships:
            enemy.fall()
            if enemy.rect.y > screen_height:
                enemy_ships.remove(enemy)
                score += 1
            enemy.draw(screen)  # Dibuixa la nau enemiga
            if enemy.rect.colliderect(player.rect):  # Col·lisió
                running = False

        # Dibuixa la nau del jugador
        screen.blit(player.image, player.rect)

        # Mostrar marcador
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Executa el joc
game_loop()

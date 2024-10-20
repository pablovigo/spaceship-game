import pygame
import random

# Inicialitza Pygame
pygame.init()

# Configuració de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Relotje
clock = pygame.time.Clock()

# Classe del jugador
class Player:
    def __init__(self):
        self.rect = pygame.Rect(screen_width // 2, screen_height - 50, 50, 50)
    
    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

# Classe dels blocs
class Block:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, screen_width - 50), 0, 50, 50)
        self.speed = random.randint(3, 8)

    def fall(self):
        self.rect.y += self.speed

# Funció principal del joc
def game_loop():
    player = Player()
    blocks = []
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

        if random.randint(1, 20) == 1:  # Crea un bloc de forma aleatoria
            blocks.append(Block())

        screen.fill(white)
        
        for block in blocks:
            block.fall()
            if block.rect.y > screen_height:
                blocks.remove(block)
                score += 1
            pygame.draw.rect(screen, red, block.rect)
            if block.rect.colliderect(player.rect):  # Colisió
                running = False

        pygame.draw.rect(screen, black, player.rect)

        # Mostrar marcador
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, black)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Executa el joc
game_loop()


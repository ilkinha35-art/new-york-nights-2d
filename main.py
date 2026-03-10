import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New York Nights 2D")

# Cores
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)

# Carregar sprites (substitua pelos seus arquivos reais)
player_img = pygame.Surface((40, 40))
player_img.fill((0, 0, 255))  # Azul para o jogador

car_img = pygame.Surface((50, 30))
car_img.fill((255, 0, 0))  # Vermelho para carros

# Posição inicial do jogador
player_x, player_y = 400, 300
player_speed = 5

# Lista de carros
cars = [
    {"x": 100, "y": 200, "speed": 2},
    {"x": 300, "y": 400, "speed": 3},
    {"x": 600, "y": 250, "speed": 1}
]

clock = pygame.time.Clock()

# Loop principal
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Atualizar carros
    for car in cars:
        car["x"] += car["speed"]
        if car["x"] > WIDTH:
            car["x"] = -50  # Reinicia fora da tela

    # Desenhar fundo (Central Park verde)
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (100, 100, 600, 400))  # Central Park

    # Desenhar jogador
    screen.blit(player_img, (player_x, player_y))

    # Desenhar carros
    for car in cars:
        screen.blit(car_img, (car["x"], car["y"]))

    pygame.display.flip()

pygame.quit()
sys.exit()

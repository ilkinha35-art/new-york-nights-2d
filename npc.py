import pygame
import random

class NPC:
    def __init__(self, x, y, color=(200,200,200), size=(30,30), speed=2):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = speed
        self.direction = random.choice(["left","right","up","down"])

    def update(self):
        # Movimento simples aleatório
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed

        # Troca direção aleatoriamente
        if random.randint(0,100) < 2:
            self.direction = random.choice(["left","right","up","down"])

        # Mantém dentro da tela
        if self.rect.x < 0: self.rect.x = 0
        if self.rect.y < 0: self.rect.y = 0
        if self.rect.x > 770: self.rect.x = 770
        if self.rect.y > 570: self.rect.y = 570

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def interact(self, player_rect):
        if self.rect.colliderect(player_rect):
            return "Olá, bem-vindo a Nova York!"
        return None

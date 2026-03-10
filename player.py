import pygame

class Player:
    def __init__(self, x, y, color=(0,0,255), size=(40,40), speed=5):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = speed

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def update(self):
        self.handle_input()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

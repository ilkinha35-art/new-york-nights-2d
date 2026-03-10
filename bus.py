import pygame

class Bus:
    def __init__(self, sprite, path, speed=1.5):
        self.sprite = sprite
        self.path = path  # lista de pontos [(x1,y1), (x2,y2), ...]
        self.speed = speed
        self.current_point = 0
        self.x, self.y = self.path[0]

    def update(self):
        target_x, target_y = self.path[self.current_point]
        dx = target_x - self.x
        dy = target_y - self.y
        dist = (dx**2 + dy**2) ** 0.5

        if dist > 0:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist

        if dist < 3:  # chegou ao ponto
            self.current_point += 1
            if self.current_point >= len(self.path):
                self.current_point = 0  # loop infinito

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

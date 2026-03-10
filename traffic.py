import pygame
import json

class Car:
    def __init__(self, sprite, path, speed=2):
        self.sprite = sprite
        self.path = path  # lista de pontos [(x1,y1), (x2,y2), ...]
        self.speed = speed
        self.current_point = 0
        self.x, self.y = self.path[0]

    def update(self):
        # Ponto alvo
        target_x, target_y = self.path[self.current_point]

        # Movimento em direção ao alvo
        dx = target_x - self.x
        dy = target_y - self.y
        dist = (dx**2 + dy**2) ** 0.5

        if dist > 0:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist

        # Se chegou ao ponto alvo, passa para o próximo
        if dist < 2:
            self.current_point += 1
            if self.current_point >= len(self.path):
                self.current_point = 0  # loop infinito

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))


def load_traffic(map_file, car_sprite):
    with open(map_file, "r") as f:
        map_data = json.load(f)

    cars = []
    # Criar carros em cada rua
    for street in map_data["streets"]:
        path = street["path"]
        car = Car(car_sprite, path, speed=2)
        cars.append(car)

    return cars

import pygame
import time

class Flight:
    def __init__(self, origin, destination, departure_time):
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.active = True

class FlightSystem:
    def __init__(self, flights):
        self.flights = flights
        self.font = pygame.font.SysFont(None, 24)
        self.selected_index = 0
        self.active_menu = False

    def open_menu(self):
        self.active_menu = True

    def close_menu(self):
        self.active_menu = False

    def draw_menu(self, screen):
        if self.active_menu:
            y = 120
            for i, flight in enumerate(self.flights):
                text = f"{flight.origin} -> {flight.destination} às {flight.departure_time}"
                color = (255,255,0) if i == self.selected_index else (255,255,255)
                rendered = self.font.render(text, True, color)
                screen.blit(rendered, (20, y))
                y += 30

    def handle_input(self, keys):
        if self.active_menu:
            if keys[pygame.K_UP]:
                self.selected_index = max(0, self.selected_index - 1)
            if keys[pygame.K_DOWN]:
                self.selected_index = min(len(self.flights)-1, self.selected_index + 1)

    def confirm_flight(self, player):
        if self.active_menu and self.flights:
            flight = self.flights[self.selected_index]
            # Teleporta jogador para destino (simulação)
            if flight.destination == "Miami":
                player.rect.topleft = (100,100)
            elif flight.destination == "Los Angeles":
                player.rect.topleft = (600,400)
            elif flight.destination == "São Paulo":
                player.rect.topleft = (300,300)
            self.close_menu()

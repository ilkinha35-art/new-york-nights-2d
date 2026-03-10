import pygame
import json
from player import Player
from traffic import load_traffic
from npc import NPC
from bus import Bus
from airport import Airport
from flights import Flight, FlightSystem

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New York Nights 2D")

clock = pygame.time.Clock()

# Carregar mapa
with open("maps/manhattan_map.json", "r") as f:
    map_data = json.load(f)

# Criar jogador
player = Player(400, 300)

# Criar carros
car_img = pygame.Surface((40,20))
car_img.fill((255,0,0))
cars = load_traffic("maps/manhattan_map.json", car_img)

# Criar ônibus
bus_img = pygame.Surface((70,30))
bus_img.fill((0,255,255))
bus_routes = [
    [(100,100), (700,100), (700,500), (100,500)],  # loop quadrado
    [(50,300), (750,300)]  # linha reta
]
buses = [Bus(bus_img, route) for route in bus_routes]

# Criar NPCs
npcs = [
    NPC(200,200, ["Oi turista!", "Times Square é incrível à noite."]),
    NPC(500,400, ["Bem-vindo ao Central Park!", "Você sabia que ele é enorme?"]),
    NPC(300,150, ["Cuidado com o trânsito!", "Os carros nunca param aqui."])
]

# Criar aeroportos
airports = [
    Airport("JFK Airport", (50, 50)),
    Airport("LaGuardia Airport", (600, 100)),
    Airport("Newark Airport", (300, 500))
]

# Criar voos
flights = [
    Flight("JFK Airport", "Miami", "21:00"),
    Flight("LaGuardia Airport", "Los Angeles", "22:30"),
    Flight("Newark Airport", "São Paulo", "23:15")
]
flight_system = FlightSystem(flights)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizações
    player.update()
    for car in cars: car.update()
    for bus in buses: bus.update()
    for npc in npcs: npc.update()

    # Desenhar fundo
    screen.fill((0,0,0))

    # Desenhar pontos de interesse
    for poi in map_data["points_of_interest"]:
        rect = pygame.Rect(poi["position"][0], poi["position"][1],
                           poi["size"][0], poi["size"][1])
        pygame.draw.rect(screen, poi["color"], rect)

    # Desenhar jogador
    player.draw(screen)

    # Desenhar carros e ônibus
    for car in cars: car.draw(screen)
    for bus in buses: bus.draw(screen)

    # Desenhar NPCs
    for npc in npcs: npc.draw(screen)

    # Aeroportos
    message = None
    for airport in airports:
        airport.draw(screen)
        msg = airport.interact(player.rect)
        if msg:
            message = msg
            flight_system.open_menu()

    if message:
        font = pygame.font.SysFont(None, 28)
        text = font.render(message, True, (255,255,255))
        screen.blit(text, (20, 80))

    # Controle do menu de voos
    keys = pygame.key.get_pressed()
    flight_system.handle_input(keys)
    if keys[pygame.K_RETURN]:
        flight_system.confirm_flight(player)

    # Desenhar menu de voos
    flight_system.draw_menu(screen)

    pygame.display.flip()

pygame.quit()

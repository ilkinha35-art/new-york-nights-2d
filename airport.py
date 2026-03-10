from airport import Airport

# Criar aeroportos
airports = [
    Airport("JFK Airport", (50, 50)),
    Airport("LaGuardia Airport", (600, 100)),
    Airport("Newark Airport", (300, 500))
]

# Dentro do loop principal:
for airport in airports:
    airport.draw(screen)
    message = airport.interact(player.rect)
    if message:
        font = pygame.font.SysFont(None, 28)
        text = font.render(message, True, (255,255,255))
        screen.blit(text, (20, 80))

import pygame


pygame.init()
pygame.display.set_caption('YandexMaps')
size = width, height = 900, 900

running = True
clock = pygame.time.Clock()

app = YandexMap()
get_map(lon, lat)
sc
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                pass
            if event.key == pygame.K_PAGEDOWN:
                pass
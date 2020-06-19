import pygame
import sys


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
delta = 0.0
max_fps = 20.0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("SPACE CLICKED")
    
    
    delta += clock.tick() / 1000.0
    while delta > 1 / max_fps:
        delta -= 1 / max_fps

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            print("d")
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 150, 255), pygame.Rect(100, 100, 200, 200))
    pygame.display.flip()


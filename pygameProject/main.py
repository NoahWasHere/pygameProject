#Import and init modules
import pygame
import sys
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()

#Constants
WINDOW_SIZE = (700, 400)
DISPLAY_SIZE = (350, 200)

#Images/world items
player = pygame.image.load('img/player.png')
player_rect = pygame.Rect(50, 50, 8, 16)

#Create the display
pygame.display.set_caption('Python Game')
window = pygame.display.set_mode(WINDOW_SIZE)
display = pygame.Surface(DISPLAY_SIZE)

#Movement variables
moving_right = False
moving_left = False

#Game Loop
while True:

    display.fill((0, 100, 255))

    pygame.draw.rect(display, (0, 0, 0), player_rect)
    display.blit(player, player_rect)

    if moving_left:
        player_rect.x -= 5
    if moving_right:
        player_rect.x += 5

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                moving_right = True
            if event.key == K_a:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    window.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(60)

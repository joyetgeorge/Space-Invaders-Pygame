import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

playerImg = pygame.image.load('battleship.png')
playerX = 370
playerY = 480
playerX_change = 0
# playerY_change = 0

alienImg = pygame.image.load('space-ship.png')
alienX = random.randint(0, 738)
alienY = random.randint(0, 150)


def player(x, y):
    screen.blit(playerImg, (x, y))

def alien(x, y):
    screen.blit(alienImg, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            # if event.key == pygame.K_UP:
            #     playerY_change = -0.2
            # if event.key == pygame.K_DOWN:
            #     playerY_change = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
                playerY_change = 0

    screen.fill((46, 52, 64))

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 738:
        playerX = 738
    
    # print(playerX)
    player(playerX, playerY)
    alien(alienX, alienY)
    pygame.display.update()

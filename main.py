import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

bg = pygame.image.load('background.jpg')
bg = pygame.transform.scale(bg, (800, 600))


playerImg = pygame.image.load('battleship.png')
playerX = 370
playerY = 480
playerX_change = 0

alienImg = pygame.image.load('space-ship.png')
alienImg = pygame.transform.scale(alienImg, (45, 45))
alienX = random.randint(0, 738)
alienY = 10
alienX_change = 0.1

bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (20, 20))
bulletX = 0
bulletY = 480
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y):
    screen.blit(alienImg, (x, y))
    # print(y)


def bulletFire(x):
    global bulletY
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x+22, bulletY))
    bulletY -= 0.5
    if bulletY < 0:
        bullet_state = "ready"
        bulletY = 480


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.4
            # print(playerX)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bulletFire(bulletX)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
                playerY_change = 0

    screen.blit(bg, (0, 0))

    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    elif playerX > 738:
        playerX = 738

    alienX += alienX_change

    if alienX >= 738:
        alienX_change = -0.2
        alienY += 20
    if alienX <= 0:
        alienX_change = 0.2
        alienY += 20
    if alienY > playerY - 30:
        print("Game over")

    if bullet_state is "fire":
        bulletFire(bulletX)

    player(playerX, playerY)
    alien(alienX, alienY)
    pygame.display.update()

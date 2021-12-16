import pygame
import random
import math

from pygame import mixer

score_file = open('score.txt', 'r+', encoding="utf8", errors='ignore')
high_score = score_file.read()
print(high_score)

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True

bg = pygame.image.load('background.jpg')
bg = pygame.transform.scale(bg, (800, 600))


playerImg = pygame.image.load('battleship.png')
playerX = 370
playerY = 480
playerX_change = 0

alienImg = []
alienImg = []
alienX = []
alienY = []
explo = []
alienX_change = []
no_of_alien = 6

for i in range(no_of_alien):
    # alienImg.append()
    alienImg.append(pygame.transform.scale(
        pygame.image.load('space-ship.png'), (45, 45)))
    alienX.append(random.randint(0, 738))
    alienY.append(10)
    alienX_change.append(0.1)
    explo.append(pygame.image.load('explosion.png'))

bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (20, 20))
bulletX = 0
bulletY = 480
bullet_state = "ready"

score_value = 0
scoreX = 695
scoreY = 10
font = pygame.font.Font('freesansbold.ttf', 20)
high_score_font = pygame.font.Font('freesansbold.ttf', 12)
high_score_render = font.render("Score : " + str(score_value), True, (118, 118, 118))
screen.blit(high_score_render, (695, 15))

def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y, i):
    screen.blit(alienImg[i], (x, y))


def bulletFire(x):
    global bulletY
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x+22, bulletY))
    bulletY -= 0.5
    if bulletY < 0:
        bullet_state = "ready"
        bulletY = 480


def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt((math.pow(alienX-bulletX, 2) +
                         (math.pow(alienY-bulletY, 2))))
    if distance < 27:
        return True
    else:
        return False


def isScore(x, y):
    score = font.render("Score : " + str(score_value), True, (118, 118, 118))
    screen.blit(score, (x, y))


def explosion(x, y, i):
    screen.blit(explo[i], (x, y))

mixer.music.load('background.wav')
mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if str(score_value) > high_score:
                score_file.truncate(0)
                score_file.write(str(score_value))
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.4
            # print(playerX)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    laser_sound = mixer.Sound('laser.wav')
                    laser_sound.play()
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

    for i in range(no_of_alien):
        alienX[i] += alienX_change[i]

        if alienX[i] >= 738:
            alienX_change[i] = -0.2
            alienY[i] += 20
        if alienX[i] <= 0:
            alienX_change[i] = 0.2
            alienY[i] += 20
        if alienY[i] > playerY - 30:
            print("Game over")

        collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)

        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            explosion(alienX[i], alienY[i], i)
            bullet_state = "ready"
            bulletY = 480
            score_value += 1
            # print(score)
            alienX[i] = random.randint(0, 738)
            alienY[i] = random.randint(0, alienY[i])

        alien(alienX[i], alienY[i], i)

    if bullet_state == "fire":
        bulletFire(bulletX)

    
    isScore(scoreX, scoreY)
    player(playerX, playerY)
    pygame.display.update()

import math

import pygame
from pygame import mixer
import random
# Initialization of pygame
pygame.init()
# creating the Screen
screen = pygame.display.set_mode((800, 600))
# Background
background = pygame.image.load("Background.png")
running = True
# background sound
mixer.music.load("background.wav")
mixer.music.play(-1)
# Title and the icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerChange = 0
# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXChange = []
enemyYChange = []
num_of_enemy = 6
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyXChange.append(3)
    enemyYChange.append(40)
# bullet
# fire bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletXChange = 0
bulletYChange = 8
bulletState = "ready"

#score
score_value =  0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
#Game over Font
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("Score: "+ str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200, 250))
def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))
def enemy(enemyX, enemyY, i):
    screen.blit(enemyImg[i], (enemyX, enemyY))
def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
# game loop
while running:
    # RGB color
    screen.fill((0, 0, 64))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange = -5
            if event.key == pygame.K_RIGHT:
                playerChange = 5
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletSound=mixer.Sound("laser.wav")
                    bulletSound.play()
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChange = 0
# player movement
    playerX += playerChange
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
# enemy movement
    for i in range (num_of_enemy):

        # Game over
        if enemyY[i]>400:
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyXChange[i]
        if enemyX[i] <= 0:
            enemyXChange[i] = 3
            enemyY[i] += enemyYChange[i]
        elif enemyX[i] >= 736:
            enemyXChange[i] = -3
            enemyY[i] += enemyYChange[i]
        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collisionSound = mixer.Sound("explosion.wav")
            collisionSound.play()
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
# bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = 'ready'
    if bulletState == "fire":
        fire_bullet(bulletX , bulletY)
        bulletY -= bulletYChange

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()


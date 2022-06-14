import pygame
import random
# Initialization of pygame
pygame.init()
# creating the Screen
screen = pygame.display.set_mode((800, 600))
# Background
background = pygame.image.load("Background.png")
running = True
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
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyXChange = 2
enemyYChange = 40
# bullet
# fire bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletXChange = 0
bulletYChange = 6
bulletState = "ready"
def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))
def enemy(enemyX, enemyY):
    screen.blit(enemyImg, (enemyX, enemyY))
def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
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
                playerChange = -3
            if event.key == pygame.K_RIGHT:
                playerChange = 3
            if event.key == pygame.K_SPACE:
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
    enemyX += enemyXChange
    if enemyX <= 0:
        enemyXChange = 2
        enemyY += enemyYChange
    elif enemyX >= 736:
        enemyXChange = -2
        enemyY += enemyYChange
# bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = 'ready'
    if bulletState == "fire":
        fire_bullet(bulletXcd , bulletY)
        bulletY -= bulletYChange
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()


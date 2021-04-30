#import 
import pygame


#init pygame
pygame.init

#main window
screen = pygame.display.set_mode((800,600))
#title and icon
pygame.display.set_caption("q q fazai")
icon=pygame.image.load("123.gif")
pygame.display.set_icon(icon)
#player
playerX_change=0
playerImg=pygame.image.load('spaceship.png')
playerX=370
playerY=540
def player(playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))
#enemy
enemyX_change=0
enemyImg=pygame.image.load('enemy.png')
enemyX=370
enemyY=50
def player(playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))
def enemy(enemyX,enemyY):
    screen.blit(enemyImg,(enemyX, enemyY))
#game loop
ruuing = True
while ruuing:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
         ruuing=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.3
            if event.key==pygame.K_RIGHT:
                playerX_change=0.3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                playerX_change=0
    
    playerX+=playerX_change
    if playerX<=0:
        playerX= 0
    elif playerX>=763:
        playerX=763
    player(playerX,playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
      
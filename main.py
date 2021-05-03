#import 
import pygame
import math
import random

#init pygame
pygame.init

#main window
screen = pygame.display.set_mode((800,600))
background=pygame.image.load('b.png')
#title and icon
pygame.display.set_caption("q q fazai")
icon=pygame.image.load("123.gif")
pygame.display.set_icon(icon)
#player
playerX_change=0
playerImg=pygame.image.load('spaceship.png')
playerX=370
playerY=540
#miisle
missileY_change=15
missileImg=pygame.image.load('missile.png')
missileX=playerX
missileY=playerY
missile_state='ready'
def fire_missile(missileX,missileY):
    global missile_state
    missile_state='fire'
    screen.blit(missileImg,(missileX-4,missileY-30))
#enemy
enemyX_change=3
enemyY_change=15
enemyImg=pygame.image.load('enemy.png')
enemyX=random.randint(0,800)
enemyY=random.randint(25, 150)
def player(playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))
def enemy(enemyX,enemyY):
    screen.blit(enemyImg,(enemyX, enemyY))
#game loop
ruuing = True
while ruuing:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
         ruuing=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-3
            if event.key==pygame.K_RIGHT:
                playerX_change=3
            if event.key==pygame.K_SPACE:
                fire_missile(playerX,missileY)
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                playerX_change=0
    
    playerX+=playerX_change
    if playerX<=0:
        playerX= 0
    elif playerX>=763:
        playerX=763
    enemyX+=enemyX_change
    if enemyX<=0:
        enemyX_change= 4
        enemyY+=enemyY_change
    elif enemyX>=763:
        enemyX_change=-4
        enemyY+=enemyY_change
    
    if missileY<=0 :
        missileY=540
        missile_state='ready'
    if missile_state is 'fire':
        
        fire_missile(playerX, missileY)
        missileY-=missileY_change
    player(playerX,playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
      
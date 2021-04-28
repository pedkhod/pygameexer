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
#game loop
ruuing = True
while ruuing:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
         ruuing=False
    #background color
    screen.fill((255,0,0))
    
    pygame.display.update()
#import 
import pygame


#init pygame
pygame.init

#main window
screen = pygame.display.set_mode((800,600))

#game loop
ruuing = True
while ruuing:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
         ruuing=False


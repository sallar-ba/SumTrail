import pygame
from sys import exit
import random
import math

#Initializing the PyGame
pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SumTrail')
icon = pygame.image.load("graphics\logo.jpg")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.Font('font\pixeltype.ttf', 50)


sky_surface = pygame.image.load("graphics\sky.jpg").convert()
text_surface = font.render("Sum: ", False, 'White')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(text_surface, (450, 50))
    
    pygame.display.update()
    clock.tick(60)
        
import pygame
from sys import exit
import random
import math
from button import Button

#Initializing the PyGame
pygame.init()

WIDTH = 1280
HEIGHT = 720

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SumTrail')
icon = pygame.image.load("assets\imgs\logo.jpg")
pygame.display.set_icon(icon)

BG = pygame.image.load("assets\imgs\Background.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets\\font\\font.ttf", size)

def play():
    
    clock = pygame.time.Clock()
    font = pygame.font.Font("assets\\font\\pixeltype.ttf", 50)


    sky_surface = pygame.image.load("assets\imgs\sky.jpg").convert()
    text_surface = font.render("Sum: ", False, 'White')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        SCREEN.blit(sky_surface, (0, 0))
        SCREEN.blit(text_surface, (450, 50))
        
        pygame.display.update()
        clock.tick(60)


def levels():
    while True:
        SCREEN.blit(BG, (0,0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("LEVEL", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        LEVEL_3 = Button(image=pygame.image.load("assets\imgs\Options Rect.png"), pos=(640, 250), 
                            text_input="3", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL_5 = Button(image=pygame.image.load("assets\imgs\Options Rect.png"), pos=(640, 400), 
                            text_input="5", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL_7 = Button(image=pygame.image.load("assets\imgs\Options Rect.png"), pos=(640, 550), 
                            text_input="7", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [LEVEL_3, LEVEL_5, LEVEL_7]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_3.checkForInput(MENU_MOUSE_POS):
                    play()
                if LEVEL_5.checkForInput(MENU_MOUSE_POS):
                    play()
                if LEVEL_7.checkForInput(MENU_MOUSE_POS):
                    play()

        pygame.display.update()
        

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets\imgs\Play Rect.png"), pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets\imgs\Quit Rect.png"), pos=(640, 450), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    levels()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
import pygame
import sys
import random
import math
from button import Button

#Initializing the PyGame
pygame.init()

WIDTH = 1280
HEIGHT = 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SumTrail')
icon = pygame.image.load("assets\imgs\logo.jpg")
pygame.display.set_icon(icon)

BG = pygame.image.load("assets\imgs\Background.png")

def get_font(name, size): 
    return pygame.font.Font("assets\\font\\" + name + ".ttf", size)

def play(level):
    
    clock = pygame.time.Clock()
    font = get_font("pixeltype", 75)
    triangle = makeTriangle(level)
    buttons = create_buttons(triangle)
    sky_surface = pygame.image.load("assets\imgs\Background.png").convert()
    
    global sum
    sum = 0
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    handle_click(pygame.mouse.get_pos(), buttons)
        
        SCREEN.blit(sky_surface, (0, 0))
        SCREEN.blit(font.render("Sum: " + str(sum), True, 'White'), (1050, 50))
        draw_triangle(buttons)
        pygame.display.update()
        clock.tick(60)
               
def handle_click(click_pos, buttons):
    for button_row in buttons:
        for button in button_row:
            if button.checkForInput(click_pos):
                # Custom action when a number is clicked
                global sum
                sum += int(button.text_input)
                return sum

def makeTriangle(level):
    triangle = []
    for i in range(level):
        row = []
        for j in range(i + 1):
            number = random.randint(1, 9)  # Generate a random number between 1 and 100
            row.append(number)
        triangle.append(row)
    return triangle

def create_buttons(triangle):
    
    font = get_font("font", 50) 
    buttons = []
    triangle_height = len(triangle)
    max_row_width = max([len(row) for row in triangle]) 
    x = WIDTH // 2
    y = HEIGHT // 2 - (triangle_height // 2) * 100 
    for i in range(triangle_height):
        row = triangle[i]
        row_width = len(row)
        button_row = []
        for j in range(row_width):
            number = row[j]
            text_input = str(number)
            text_surface = font.render(text_input, True, BLACK) 
            button_x = x - (row_width // 2) * 100 + j * 100
            if i % 2 == 1:
                button_x += 50
            button = Button(None, (button_x, y), text_input, font, WHITE, RED)
            button.image = text_surface  
            button.rect = button.image.get_rect(center=(button_x, y)) 
            button_row.append(button)
        buttons.append(button_row)
        y += 100 
    return buttons

def draw_triangle(buttons):
    for button_row in buttons:
        for button in button_row:
            button.update(SCREEN)

def levels():
    while True:
        SCREEN.blit(BG, (0,0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font("font", 100).render("LEVEL", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        LEVEL_3 = Button(image=pygame.image.load("assets\imgs\Options Rect.png"), pos=(640, 250), 
                            text_input="3", font=get_font("font", 75), base_color="#d7fcd4", hovering_color="White")
        LEVEL_5 = Button(image=pygame.image.load("assets\imgs\Options Rect.png"), pos=(640, 400), 
                            text_input="5", font=get_font("font", 75), base_color="#d7fcd4", hovering_color="White")
        LEVEL_7 = Button(image=pygame.image.load("assets\imgs\Options Rect.png"), pos=(640, 550), 
                            text_input="7", font=get_font("font", 75), base_color="#d7fcd4", hovering_color="White")
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
                    play(3)
                if LEVEL_5.checkForInput(MENU_MOUSE_POS):
                    play(5)
                if LEVEL_7.checkForInput(MENU_MOUSE_POS):
                    play(7)

        pygame.display.update()    

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font("font", 100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets\imgs\Play Rect.png"), pos=(640, 300), 
                            text_input="PLAY", font=get_font("font", 75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets\imgs\Quit Rect.png"), pos=(640, 450), 
                            text_input="QUIT", font=get_font("font", 75), base_color="#d7fcd4", hovering_color="White")

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

if __name__ == "__main__":
    main_menu()
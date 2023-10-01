import pygame
import sys
import random
from scripts.button import Button
import time

# Initializing PyGame
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

global selected_numbers, level, last_selected_index
selected_numbers = []
level = 0
last_selected_index = 0


#-------------------    GET FONT FUNCTION    ---------------------------
def get_font(name, size):
    return pygame.font.Font("assets\\font\\" + name + ".ttf", size)




#-------------------    MAXIMUM SUM    ---------------------------
def calculate_max_sum_descent(triangle):
    triangle_height = len(triangle)
    for i in range(triangle_height - 2, -1, -1):
        row = triangle[i]
        next_row = triangle[i + 1]
        for j in range(len(row)):
            row[j] += max(next_row[j], next_row[j + 1])
    return triangle[0][0]



#-------------------    CREATE BUTTONS    ---------------------------
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


#-------------------    HANDLE CLICKS    ---------------------------
def handle_click(click_pos, buttons):
    global level, selected_numbers, total_sum, last_selected_index

    for i, button_row in enumerate(buttons):
        for j, button in enumerate(button_row):
            if button.checkForInput(click_pos):
                selected_number = int(button.text_input)
                if len(selected_numbers) == 0 or (i == len(selected_numbers) and j in [last_selected_index, last_selected_index + 1]):
                    selected_numbers.append(selected_number)
                    button.changeColor(click_pos)
                    total_sum += selected_number  # Update the sum
                    last_selected_index = j
                    if len(selected_numbers) < level:
                        if i < len(buttons) - 1:
                            buttons[i + 1][j].changeColor(click_pos)
                            buttons[i + 1][j + 1].changeColor(click_pos)
                    return selected_number, total_sum
    return None, total_sum


#-------------------    DRAW TRIANGLES    ---------------------------
def draw_triangle(buttons):
    for button_row in buttons:
        for button in button_row:
            button.update(SCREEN)


#-------------------    MAKE TRIANGLES    ---------------------------
def makeTriangle(level):
    triangle = []
    for i in range(level):
        row = []
        for j in range(i + 1):
            number = random.randint(1, 9)  # Generate a random number between 1 and 9
            row.append(number)
        triangle.append(row)
    return triangle


#-------------------    MAIN MENU    ---------------------------
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font("font", 100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets\imgs\Play Rect.png"), pos=(640, 300),
                             text_input="PLAY", font=get_font("font", 75), base_color="#d7fcd4",
                             hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets\imgs\Quit Rect.png"), pos=(640, 450),
                             text_input="QUIT", font=get_font("font", 75), base_color="#d7fcd4",
                             hovering_color="White")
        SCREEN.blit(get_font("pixeltype", 50).render("v0.3", True, WHITE), (600, 650))
        SCREEN.blit(get_font("pixeltype", 20).render("Powered By: Sallar & Co.", True, WHITE), (1111, 680))


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
                    instructions()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


#-------------------    INSTRUCTIONS FUNCTION       ---------------------------
def instructions():
    font = get_font("pixeltype", 75)



    while True:
        SCREEN.blit(BG, (0, 0))

        INST_MOUSE_POS = pygame.mouse.get_pos()

        INST_TEXT = get_font("font", 100).render("Instructions", True, "#b68f40")
        INST_RECT = INST_TEXT.get_rect(center=(640, 100))


        CONTINUE_BUTTON = Button(image=pygame.image.load("assets\imgs\Play Rect.png"), pos=(640, 600),
                             text_input="LETS GO!", font=get_font("font", 40), base_color="#d7fcd4",
                             hovering_color="White")

        SCREEN.blit(INST_TEXT, INST_RECT)


        SCREEN.blit(font.render("There is a Timer on Each Level.", True, WHITE), (40, 200))
        SCREEN.blit(font.render("You can only select numbers that are directly below", True, WHITE), (40, 300))
        SCREEN.blit(font.render("the current number you have selected", True, WHITE), (40, 350))

        # the current number you have selected
        SCREEN.blit(font.render("You can only select one number at each level of triangle", True, WHITE), (40, 450))



        CONTINUE_BUTTON.changeColor(INST_MOUSE_POS)
        CONTINUE_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE_BUTTON.checkForInput(INST_MOUSE_POS):
                    levels()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()



#-------------------    PLAY LEVELS    ---------------------------
def play_level(level):  # New function to start a level
    # Reset the game state
    global selected_numbers, total_sum, last_selected_index
    selected_numbers = []
    total_sum = 0
    last_selected_index = 0

    play(level)  # Call the play function with the selected level
    


#-------------------    LEVELS    ---------------------------
def levels():
    while True:
        SCREEN.blit(BG, (0, 0))

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
        global level
        level = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_3.checkForInput(MENU_MOUSE_POS):
                    level = 3
                    play_level(level)
                if LEVEL_5.checkForInput(MENU_MOUSE_POS):
                    level = 5
                    play_level(level)
                if LEVEL_7.checkForInput(MENU_MOUSE_POS):
                    level = 7
                    play_level(7)

        pygame.display.update()


#-------------------    PLAY   ---------------------------
def play(level):
    clock = pygame.time.Clock()
    font = get_font("pixeltype", 75)
    fontMed = get_font("pixeltype", 40)
    fontSmall = get_font("pixeltype", 20)
    global triangle, last_selected_index
    triangle = makeTriangle(level)
    print(triangle)
    buttons = create_buttons(triangle)
    global total_sum
    total_sum = 0
    last_selected_index = 0

    time_limit = level * 1150
    start_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    handle_click(pygame.mouse.get_pos(), buttons)

        SCREEN.blit(BG, (0, 0))

        # Calculate elapsed time
        elapsed_time = pygame.time.get_ticks() - start_time

        # Check if the time limit is reached
        if elapsed_time >= time_limit:
            TimeUp()

        if len(selected_numbers) == level:
            check_win(selected_numbers)

        SCREEN.blit(font.render("Sum: " + str(total_sum), True, WHITE), (1050, 50))
        SCREEN.blit(font.render("Time: " + str((time_limit - elapsed_time) // 1000) + "s", True, WHITE), (50, 50))
        draw_triangle(buttons)
        pygame.display.update()
        clock.tick(60)



#-------------------    CHECK WIN    ---------------------------
def check_win(selected_numbers):
    font = get_font("pixeltype", 175)
    clock = pygame.time.Clock()

    global total_sum, triangle

    maxSumDescent = calculate_max_sum_descent(triangle)
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        RESET = Button(image=pygame.image.load("assets\imgs\Options Rect.png"), pos=(660, 600),
                         text_input="RESET", font=get_font("font", 75), base_color="#d7fcd4", hovering_color="White")
    
        if total_sum == maxSumDescent:
            SCREEN.blit(font.render("WINNER", True, WHITE), (500, 50))
            SCREEN.blit(font.render("Your Sum : " + str(total_sum), True, WHITE), (350, 200))
            SCREEN.blit(font.render("Max Sum : " + str(maxSumDescent), True, WHITE), (350, 375))
            
            RESET.changeColor(MENU_MOUSE_POS)
            RESET.update(SCREEN)
            
        else:
            SCREEN.blit(font.render("LOSER", True, WHITE), (500, 50))
            SCREEN.blit(font.render("Your Sum : " + str(total_sum), True, WHITE), (350, 200))
            SCREEN.blit(font.render("Max Sum : " + str(maxSumDescent), True, WHITE), (350, 375))
            
            RESET.changeColor(MENU_MOUSE_POS)
            RESET.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESET.checkForInput(MENU_MOUSE_POS):
                    main_menu()
        pygame.display.update()
        clock.tick(60)


#-------------------    TIME UP    ---------------------------
def TimeUp():
    font = get_font("pixeltype", 175)
    while True:
        SCREEN.blit(BG, (0, 0))
        TRY_AGAIN_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(font.render("TIME'S UP", True, "#b68f40"), (430, 100))

        TRY_AGAIN = Button(image=pygame.image.load("assets\imgs\Options Rect.png"), pos=(660, 400),
                         text_input="TRY AGAIN", font=get_font("font", 45), base_color="#d7fcd4", hovering_color="White")
        
        
        TRY_AGAIN.changeColor(TRY_AGAIN_MOUSE_POS)
        TRY_AGAIN.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TRY_AGAIN.checkForInput(TRY_AGAIN_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#-------------------    END    ---------------------------
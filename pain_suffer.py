
def button(button, image, pos, text_input, font, base_color, hovering_color):
    button.image = image
    button.x_pos = pos[0]
    button.y_pos = pos[1]
    button.font = font
    button.base_color, button.hovering_color = base_color, hovering_color
    button.text_input = text_input
    button.text = button.font.render(button.text_input, True, button.base_color)
    if button.image is None:
        button.image = button.text
    button.rect = button.image.get_rect(center=(button.x_pos, button.y_pos))
    button.text_rect = button.text.get_rect(center=(button.x_pos, button.y_pos))

def update(button, screen):
    if button.image is not None:
        screen.blit(button.image, button.rect)
    screen.blit(button.text, button.text_rect)

def checkForInput(button, position):
    if position[0] in range(button.rect.left, button.rect.right) and position[1] in range(button.rect.top, button.rect.bottom):
        return True
    return False

def changeColor(button, position):
    if position[0] in range(button.rect.left, button.rect.right) and position[1] in range(button.rect.top, button.rect.bottom):
        button.text = button.font.render(button.text_input, True, button.hovering_color)
    else:
        button.text = button.font.render(button.text_input, True, button.base_color)



import pygame, sys, os
from subprocess import call

# initializing the constructor
pygame.init()


font = "font.otf"
clock = pygame.time.Clock()


# screen resolution
res = (1366,768)
width = 1366
height = 768

# opens up a window
screen = pygame.display.set_mode(res)

# background
bg_img = pygame.image.load("bg.jpg")
bg_img = pygame.transform.scale(bg_img,(1366,768))

# define the RGB value for white,
# green, yellow, orange colour
color = (255,255,255)
white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)
black = (0,0,0)
done = False

menu_font = pygame.font.Font(font, 132)
small_menu_font = pygame.font.Font(font, 100)
 

def play():
    call(["python", "test_video.py"])
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = menu_font.render('This is the play screen', True, white)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(690, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_BACK = Button(image=None, pos=(700, 460), text_input="BACK", font=small_menu_font, base_color="White", hovering_color="Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                main_menu()

        pygame.display.update()
    

def main_menu():
    while True:
        screen.blit(bg_img, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = menu_font.render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 100))
        #(button, image, pos, text_input, font, base_color, hovering_color)
        LESSON_BUTTON = button(image=pygame.image.load("Options Rect.png"), pos=(700, 250), text_input="Lesson", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(700, 400), text_input="Play", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        QUIZ_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(700, 550), text_input="Quiz", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        RESULTS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(400, 700), text_input="Results", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(1000, 700), text_input="EXIT", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [LESSON_BUTTON, PLAY_BUTTON, QUIZ_BUTTON, RESULTS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LESSON_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

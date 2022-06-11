import pygame
import sys

# initializing the constructor
pygame.init()


font = "font.otf"
clock = pygame.time.Clock()
gui_font = pygame.font.Font(font,30)


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
white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)
black = (0,0,0)
done = False

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font("font.otf", 132)
 
# create a text surface object,
# on which text is drawn on it.
text2 = font.render('Survive', True, black)
 
# create a rectangular object for the
# text surface object
textRect = text2.get_rect()
 
# set the center of the rectangular object.
textRect.center = (width//2, 100)

# mouse pos
mouse = pygame.mouse.get_pos()

# white color
color = (255,255,255)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()
def button(msg, x, y, w, h, inactive_colour, active_colour, action, fontsize):

    #Defines mouse, as the coodinates of the mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
  
    #checks if the mouse is within the coordinates of the button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        #draws the button in the active colour
        pygame.draw.rect(screen, active_colour, (x, y, w, h))
        #checks if the mouse is pressed
        if click[0] == 1:
            #performs action based on the button's said function

            if action == "quit":
                pygame.quit()

    #inactive and active button color
    else:
        pygame.draw.rect(screen, inactive_colour, (x, y, w, h))
   
    textSurf, textRect = text_objects(msg, font)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

    
# rendering a text written in
# this font


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = font.render('THis is the play screen', True, white)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_BACK = button('BACK',200,45,(width//2.78, 220),5)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()


LESSON_BUTTON = button("Play", 100, 100, 50, 50, yellow, white, quit, 132)


def main_menu():
    while True:
        
        screen.blit(bg_img, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font.render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        
        

        screen.blit(MENU_TEXT, MENU_RECT)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LESSON_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

                if LESSON_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
button1 = Button(image=None, pos=(100, 100), text_input="PLAY", font=font, base_color="Black", hovering_color="Green")
while True:
    screen.blit(bg_img,(0,0))
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    
    screen.blit(text2, textRect)    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
    
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # superimposing the text onto our button
    # updates the frames of the game
    #button1.draw()
    pygame.display.update()
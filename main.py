import pygame, sys, os
from subprocess import call

score = 0
quiz_started = False

# initializing the constructor
pygame.init()


jungle_font = "font.otf"
debug_font = "debug_font.otf"
conflict_font = "conflict_font.ttf"
sf_display = "SFUI-Heavy.otf"
clock = pygame.time.Clock()


# screen resolution
res = (1366,768)
width = 1366
height = 768

# opens up a window
screen = pygame.display.set_mode(res)

# background
bg_img = pygame.image.load("abc.jpg")
bg_img = pygame.transform.scale(bg_img,(1366,768))
bg2 = pygame.image.load("bg2.jpg")
bg2 = pygame.transform.scale(bg2,(1366,768))
death = pygame.image.load("death.jpg")
death = pygame.transform.scale(death,(1366,768))
slide1 = pygame.image.load("Slide1.jpg")
slide1 = pygame.transform.scale(slide1,(1366,768))
slide2 = pygame.image.load("Slide2.jpg")
slide2 = pygame.transform.scale(slide2,(1366,768))
slide3 = pygame.image.load("Slide3.jpg")
slide3 = pygame.transform.scale(slide3,(1366,768))
slide4 = pygame.image.load("Slide4.jpg")
slide4 = pygame.transform.scale(slide4,(1366,768))
slide5 = pygame.image.load("Slide5.jpg")
slide5 = pygame.transform.scale(slide5,(1366,768))

# define the RGB value for white,
# green, yellow, orange colour
color = (255,255,255)
white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)
black = (0,0,0)
red = (255, 49, 49)
done = False

menu_font = pygame.font.Font(jungle_font, 132)
small_menu_font = pygame.font.Font(jungle_font, 100)
back_button_font = pygame.font.Font(sf_display, 50)
button_font = pygame.font.Font(debug_font, 80)
death_font = pygame.font.Font(conflict_font, 80)
ui_font = pygame.font.Font(sf_display, 80)
title_font = pygame.font.Font(sf_display, 120)
hehe_font = pygame.font.Font(sf_display, 20)



 
class Button():
    #prepares and renders the button in the specified place
	def __init__(button, image, pos, text_input, font, base_color, hovering_color):
		button.image = image
		button.x_pos = pos[0]
		button.y_pos = pos[1]
		button.font = font
		button.base_color, button.hovering_color = base_color, hovering_color
		button.text_input = text_input
		button.text = button.font.render(button.text_input, True, button.base_color)
        #if we don't set an image as the bg, this will cause the text to be standalone
		if button.image is None:
			button.image = button.text
		button.rect = button.image.get_rect(center=(button.x_pos, button.y_pos))
		button.text_rect = button.text.get_rect(center=(button.x_pos, button.y_pos))

	def update(button, screen):
		if button.image is not None:
			screen.blit(button.image, button.rect)
		screen.blit(button.text, button.text_rect)
    
    #checks to see if the position of your mouse is in the x and y range of the button
	def checkForInput(button, position):
		if position[0] in range(button.rect.left, button.rect.right) and position[1] in range(button.rect.top, button.rect.bottom):
			return True
		return False
    
    #if the position if your mouse is over the button, it will change the colour
	def changeColor(button, position):
		if position[0] in range(button.rect.left, button.rect.right) and position[1] in range(button.rect.top, button.rect.bottom):
			button.text = button.font.render(button.text_input, True, button.hovering_color)
		else:
			button.text = button.font.render(button.text_input, True, button.base_color)


def main_menu():
    while True:
        screen.blit(bg_img, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = title_font.render("MAIN    MENU", True, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 100))

        LESSON_BUTTON = Button(image=pygame.image.load("Large_Rect.png"), pos=(700, 250), text_input="Lesson", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        PLAY_BUTTON = Button(image=pygame.image.load("Small_Rect.png"), pos=(700, 400), text_input="Play", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        QUIZ_BUTTON = Button(image=pygame.image.load("Small_Rect.png"), pos=(700, 550), text_input="Quiz", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        RESULTS_BUTTON = Button(image=pygame.image.load("Large_Rect.png"), pos=(400, 700), text_input="Results", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit_Rect.png"), pos=(1000, 700), text_input="EXIT", font=small_menu_font, base_color="#d7fcd4", hovering_color="red")

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
                    lesson1()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIZ_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quiz()
                if RESULTS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    results()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



def lesson1():
    while True:
        screen.blit(slide1, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        NEXT = Button(image=None, pos=(1200, 700), text_input="NEXT", font=back_button_font, base_color="White", hovering_color="Green")
        
        NEXT.changeColor(MOUSE_POS)
        NEXT.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if NEXT.checkForInput(MOUSE_POS):
                lesson2()
        pygame.display.update()

def lesson2():
    while True:
        screen.blit(slide2, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        NEXT = Button(image=None, pos=(1200, 700), text_input="NEXT", font=back_button_font, base_color="White", hovering_color="Green")
        
        NEXT.changeColor(MOUSE_POS)
        NEXT.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if NEXT.checkForInput(MOUSE_POS):
                lesson3()
        pygame.display.update()

def lesson3():
    while True:
        screen.blit(slide3, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        NEXT = Button(image=None, pos=(1200, 700), text_input="NEXT", font=back_button_font, base_color="White", hovering_color="Green")
        
        NEXT.changeColor(MOUSE_POS)
        NEXT.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if NEXT.checkForInput(MOUSE_POS):
                lesson4()
        pygame.display.update()

def lesson4():
    while True:
        screen.blit(slide4, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        NEXT = Button(image=None, pos=(1200, 700), text_input="NEXT", font=back_button_font, base_color="White", hovering_color="Green")
        
        NEXT.changeColor(MOUSE_POS)
        NEXT.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if NEXT.checkForInput(MOUSE_POS):
                lesson5()
        pygame.display.update()

def lesson5():
    while True:
        screen.blit(slide5, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        MENU = Button(image=None, pos=(1200, 700), text_input="MAIN MENU", font=back_button_font, base_color="White", hovering_color="Green")
        
        MENU.changeColor(MOUSE_POS)
        MENU.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if MENU.checkForInput(MOUSE_POS):
                main_menu()
        pygame.display.update()

def play():
    call(["python", "lore_video.py"])
    while True:
        screen.blit(bg2, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()


        TEXT = small_menu_font.render('what  will  you  do', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)
        WALK = Button(image=None, pos=(700, 400), text_input="Keep Walking", font=button_font, base_color="#d7fcd4", hovering_color="white")
        MOMENT = Button(image=None, pos=(700, 600), text_input="Take a Moment to Collect your Thoughts", font=button_font, base_color="#d7fcd4", hovering_color="white")

        
        WALK.changeColor(MOUSE_POS)
        WALK.update(screen)
        MOMENT.changeColor(MOUSE_POS)
        MOMENT.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if WALK.checkForInput(MOUSE_POS):
                walking1()
              if MOMENT.checkForInput(MOUSE_POS):
                main_menu()

        pygame.display.update()

def walking1():
      while True:
        screen.blit(bg2, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()


        TEXT = small_menu_font.render('choose   wisely', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)
        CAVE = Button(image=None, pos=(700, 400), text_input="Take Shelter in a Nearby Cave", font=button_font, base_color="#d7fcd4", hovering_color="white")
        WALK = Button(image=None, pos=(700, 600), text_input="Try to Find your Way Back", font=button_font, base_color="#d7fcd4", hovering_color="white")

        
        CAVE.changeColor(MOUSE_POS)
        CAVE.update(screen)
        WALK.changeColor(MOUSE_POS)
        WALK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if CAVE.checkForInput(MOUSE_POS):
                death_spider()
              if WALK.checkForInput(MOUSE_POS):
                death_tiger()

        pygame.display.update()


    
def death_spider():
  #call(["python", "test_video.py"])
      while True:
        screen.blit(death, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()


        TEXT = death_font.render('YOU WERE BITTEN BY A SPIDER', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)
        DEATH_MENU = Button(image=None, pos=(700, 400), text_input="Main Menu", font=button_font, base_color="green", hovering_color="white")
        
        DEATH_MENU.changeColor(MOUSE_POS)
        DEATH_MENU.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if DEATH_MENU.checkForInput(MOUSE_POS):
                main_menu()

        pygame.display.update()

def death_tiger():
  #call(["python", "test_video.py"])
      while True:
        screen.blit(death, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()


        TEXT = death_font.render('YOU WERE KILLED BY A TIGER', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)
        DEATH_MENU = Button(image=None, pos=(700, 400), text_input="Main Menu", font=button_font, base_color="green", hovering_color="white")
        
        DEATH_MENU.changeColor(MOUSE_POS)
        DEATH_MENU.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if DEATH_MENU.checkForInput(MOUSE_POS):
                main_menu()

        pygame.display.update()


def quiz():
    #call(["python", "test_video.py"])
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        TEXT = menu_font.render('READY    TO    BEGIN?', True, white)
        RECT = TEXT.get_rect(center=(690, 260))
        screen.blit(TEXT, RECT)
        MENU = Button(image=None, pos=(500, 500), text_input="MAIN MENU", font=back_button_font, base_color="red", hovering_color="white")
        READY = Button(image=None, pos=(900, 500), text_input="READY", font=back_button_font, base_color="White", hovering_color="Green")
        
        MENU.changeColor(MOUSE_POS)
        MENU.update(screen)
        READY.changeColor(MOUSE_POS)
        READY.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if MENU.checkForInput(MOUSE_POS):
                main_menu()
              if READY.checkForInput(MOUSE_POS):
                question1()

        pygame.display.update()

def question1():
  global score
  global quiz_started
  quiz_started = True
  while True:
      MOUSE_POS = pygame.mouse.get_pos()

      screen.fill("black")

      TEXT = ui_font.render('What is the MOST Reliable', True, white)
      RECT = TEXT.get_rect(center=(690, 150))
      TEXT2 = ui_font.render('Source of Body Heat?', True, white)
      RECT2 = TEXT.get_rect(center=(750, 240))
      screen.blit(TEXT, RECT)
      screen.blit(TEXT2, RECT2)
      OPT1 = Button(image=None, pos=(500, 450), text_input="Fire", font=back_button_font, base_color="red", hovering_color="white")
      OPT2 = Button(image=None, pos=(900, 450), text_input="Lighter", font=back_button_font, base_color="red", hovering_color="white")
      OPT3 = Button(image=None, pos=(500, 650), text_input="Body Heat", font=back_button_font, base_color="red", hovering_color="white")
      OPT4 = Button(image=None, pos=(900, 650), text_input="Shelter", font=back_button_font, base_color="red", hovering_color="white")
      
      OPT1.changeColor(MOUSE_POS)
      OPT1.update(screen)
      OPT2.changeColor(MOUSE_POS)
      OPT2.update(screen)
      OPT3.changeColor(MOUSE_POS)
      OPT3.update(screen)
      OPT4.changeColor(MOUSE_POS)
      OPT4.update(screen)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if OPT1.checkForInput(MOUSE_POS):
              question2()
            if OPT2.checkForInput(MOUSE_POS):
              question2()
            if OPT3.checkForInput(MOUSE_POS):
              score += 1
              question2()
            if OPT4.checkForInput(MOUSE_POS):
              question2()    
      pygame.display.update()



def question2():
  global score

  while True:
      MOUSE_POS = pygame.mouse.get_pos()

      screen.fill("black")

      TEXT = ui_font.render('How do you Make Sure that', True, white)
      RECT = TEXT.get_rect(center=(690, 150))
      TEXT2 = ui_font.render('Your Water is Safe?', True, white)
      RECT2 = TEXT.get_rect(center=(850, 240))
      screen.blit(TEXT, RECT)
      screen.blit(TEXT2, RECT2)
      OPT1 = Button(image=None, pos=(500, 450), text_input="Drink Clear", font=back_button_font, base_color="red", hovering_color="white")
      OPT1B = Button(image=None, pos=(500, 500), text_input="Pond Water", font=back_button_font, base_color="white", hovering_color="white")
      OPT2 = Button(image=None, pos=(900, 450), text_input="Drink Green", font=back_button_font, base_color="red", hovering_color="white")
      OPT2B = Button(image=None, pos=(900, 500), text_input="River Water", font=back_button_font, base_color="white", hovering_color="white")
      OPT3 = Button(image=None, pos=(500, 650), text_input="Boil Water", font=back_button_font, base_color="red", hovering_color="white")
      OPT3B = Button(image=None, pos=(500, 700), text_input="with Heat Vision", font=back_button_font, base_color="white", hovering_color="white")
      OPT4 = Button(image=None, pos=(900, 650), text_input="Boil Water", font=back_button_font, base_color="red", hovering_color="white")
      OPT4B = Button(image=None, pos=(900, 700), text_input="with a Fire", font=back_button_font, base_color="white", hovering_color="white")
      
      OPT1.changeColor(MOUSE_POS)
      OPT1.update(screen)
      #OPT1B.changeColor(MOUSE_POS)
      OPT1B.update(screen)
      OPT2.changeColor(MOUSE_POS)
      OPT2.update(screen)
      #OPT2B.changeColor(MOUSE_POS)
      OPT2B.update(screen)
      OPT3.changeColor(MOUSE_POS)
      OPT3.update(screen)
      #OPT3B.changeColor(MOUSE_POS)
      OPT3B.update(screen)
      OPT4.changeColor(MOUSE_POS)
      OPT4.update(screen)
      #OPT4B.changeColor(MOUSE_POS)
      OPT4B.update(screen)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if OPT1.checkForInput(MOUSE_POS) or OPT1B.checkForInput(MOUSE_POS):
              question3()
            if OPT2.checkForInput(MOUSE_POS) or OPT2B.checkForInput(MOUSE_POS):
              question3()
            if OPT3.checkForInput(MOUSE_POS) or OPT3B.checkForInput(MOUSE_POS):
              question3()
            if OPT4.checkForInput(MOUSE_POS) or OPT4B.checkForInput(MOUSE_POS):
              score += 1
              question3()    
      pygame.display.update()

def question3():
  global score
  while True:
      MOUSE_POS = pygame.mouse.get_pos()

      screen.fill("black")

      TEXT = ui_font.render('Is it Sensible to Make Camp', True, white)
      RECT = TEXT.get_rect(center=(690, 100))
      TEXT2 = ui_font.render('Near a Tree with Lots ', True, white)
      RECT2 = TEXT.get_rect(center=(810, 190))
      TEXT3 = ui_font.render('of Old Scratch Marks?', True, white)
      RECT3 = TEXT.get_rect(center=(795, 280))
      screen.blit(TEXT, RECT)
      screen.blit(TEXT2, RECT2)
      screen.blit(TEXT3, RECT3)
      OPT1 = Button(image=None, pos=(500, 450), text_input="Yes", font=back_button_font, base_color="red", hovering_color="white")
      OPT2 = Button(image=None, pos=(900, 450), text_input="No", font=back_button_font, base_color="red", hovering_color="white")
      OPT3 = Button(image=None, pos=(500, 650), text_input="Not Sure", font=back_button_font, base_color="red", hovering_color="white")
      OPT4 = Button(image=None, pos=(900, 650), text_input="Rick Astley", font=back_button_font, base_color="red", hovering_color="white")
      
      OPT1.changeColor(MOUSE_POS)
      OPT1.update(screen)
      OPT2.changeColor(MOUSE_POS)
      OPT2.update(screen)
      OPT3.changeColor(MOUSE_POS)
      OPT3.update(screen)
      OPT4.changeColor(MOUSE_POS)
      OPT4.update(screen)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if OPT1.checkForInput(MOUSE_POS):
              question4()
            if OPT2.checkForInput(MOUSE_POS):
              score += 1
              question4()
            if OPT3.checkForInput(MOUSE_POS):
              question4()
            if OPT4.checkForInput(MOUSE_POS):
              question4()    
      pygame.display.update()

def question4():
  global score
  while True:
      MOUSE_POS = pygame.mouse.get_pos()

      screen.fill("black")

      TEXT = ui_font.render("The Best Way to Remember These", True, white)
      RECT = TEXT.get_rect(center=(680, 150))
      TEXT2 = ui_font.render("Tips is Through the Acronym:", True, white)
      RECT2 = TEXT.get_rect(center=(800, 240))
      screen.blit(TEXT, RECT)
      screen.blit(TEXT2, RECT2)
      OPT1 = Button(image=None, pos=(500, 450), text_input="SHOP", font=back_button_font, base_color="red", hovering_color="white")
      OPT2 = Button(image=None, pos=(900, 450), text_input="STOP", font=back_button_font, base_color="red", hovering_color="white")
      OPT3 = Button(image=None, pos=(500, 650), text_input="RICK ASTLEY", font=back_button_font, base_color="red", hovering_color="white")
      OPT4 = Button(image=None, pos=(900, 650), text_input="WATER", font=back_button_font, base_color="red", hovering_color="white")
      
      OPT1.changeColor(MOUSE_POS)
      OPT1.update(screen)
      OPT2.changeColor(MOUSE_POS)
      OPT2.update(screen)
      OPT3.changeColor(MOUSE_POS)
      OPT3.update(screen)
      OPT4.changeColor(MOUSE_POS)
      OPT4.update(screen)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if OPT1.checkForInput(MOUSE_POS):
              question5()
            if OPT2.checkForInput(MOUSE_POS):
              score += 1
              question5()
            if OPT3.checkForInput(MOUSE_POS):
              question5()
            if OPT4.checkForInput(MOUSE_POS):
              question5()    
      pygame.display.update()

def question5():
  global score
  while True:
      MOUSE_POS = pygame.mouse.get_pos()

      screen.fill("black")

      TEXT = ui_font.render('It is Okay to use ______ to Make', True, white)
      RECT = TEXT.get_rect(center=(690, 150))
      TEXT2 = ui_font.render('an Insulation Layer', True, white)
      RECT2 = TEXT.get_rect(center=(850, 240))
      TEXT3 = ui_font.render('When Making Your Tent?', True, white)
      RECT3 = TEXT.get_rect(center=(760, 330))
      screen.blit(TEXT, RECT)
      screen.blit(TEXT2, RECT2)
      screen.blit(TEXT3, RECT3)
      OPT1 = Button(image=None, pos=(500, 450), text_input="Leaves", font=back_button_font, base_color="red", hovering_color="white")
      OPT2 = Button(image=None, pos=(900, 450), text_input="Branches", font=back_button_font, base_color="red", hovering_color="white")
      OPT3 = Button(image=None, pos=(440, 650), text_input="Twigs", font=back_button_font, base_color="red", hovering_color="white")
      OPT4 = Button(image=None, pos=(900, 650), text_input="A Fire Inside Your Tent", font=back_button_font, base_color="red", hovering_color="white")
      
      OPT1.changeColor(MOUSE_POS)
      OPT1.update(screen)
      OPT2.changeColor(MOUSE_POS)
      OPT2.update(screen)
      OPT3.changeColor(MOUSE_POS)
      OPT3.update(screen)
      OPT4.changeColor(MOUSE_POS)
      OPT4.update(screen)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if OPT1.checkForInput(MOUSE_POS):
              score += 1
              results()
            if OPT2.checkForInput(MOUSE_POS):
              results()
            if OPT3.checkForInput(MOUSE_POS):
              results()
            if OPT4.checkForInput(MOUSE_POS):
              results()    
      pygame.display.update()


def results():
    global score
    global quiz_started
    #call(["python", "test_video.py"])
    while True:
      screen.fill("black")
      MOUSE_POS = pygame.mouse.get_pos()
      if not quiz_started:
        TEXT = ui_font.render("You didn't Begin the Quiz Yet!", True, white)
        RECT = TEXT.get_rect(center=(720, 150))
        screen.blit(TEXT, RECT)

      else:
    
        if score <= 2:
          TEXT = ui_font.render("You scored a " + str(score) + " out of 5", True, white)
          RECT = TEXT.get_rect(center=(720, 150))
          TEXT2 = ui_font.render("YOU DID TERRIBLE!", True, white)
          RECT2 = TEXT.get_rect(center=(775, 300))
        elif score == 3:
          TEXT = ui_font.render("You scored a " + str(score) + " out of 5", True, white)
          RECT = TEXT.get_rect(center=(720, 150))
          TEXT2 = ui_font.render("YOU DID DECENT!", True, white)
          RECT2 = TEXT.get_rect(center=(820, 300))
        elif score == 4:
          TEXT = ui_font.render("You scored a " + str(score) + " out of 5", True, white)
          RECT = TEXT.get_rect(center=(720, 150))
          TEXT2 = ui_font.render("SO CLOSE!!!", True, white)
          RECT2 = TEXT.get_rect(center=(925, 300))
        else: 
          TEXT = ui_font.render("You scored a " + str(score) + " out of 5", True, white)
          RECT = TEXT.get_rect(center=(720, 150))
          TEXT2 = ui_font.render("YOU ARE THE EMBODIMENT", True, white)
          RECT2 = TEXT.get_rect(center=(600, 300))
          TEXT3 = ui_font.render("OF PERFECTION", True, white)
          RECT3 = TEXT.get_rect(center=(850, 400))
          TEXT4 = hehe_font.render("like Sujay!!", True, white)
          RECT4 = TEXT.get_rect(center=(1700, 775))
          screen.blit(TEXT3, RECT3)
          screen.blit(TEXT4, RECT4)
        
        screen.blit(TEXT, RECT)
        screen.blit(TEXT2, RECT2)
      
      BACK = Button(image=None, pos=(720, 700), text_input="MAIN MENU", font=back_button_font, base_color="White", hovering_color="Green")
      TRY_AGAIN = Button(image=None, pos=(720, 600), text_input="BACK TO THE QUIZ", font=back_button_font, base_color="White", hovering_color="Green")
      
      BACK.changeColor(MOUSE_POS)
      BACK.update(screen)
      TRY_AGAIN.changeColor(MOUSE_POS)
      TRY_AGAIN.update(screen)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if BACK.checkForInput(MOUSE_POS):
              main_menu()
            if TRY_AGAIN.checkForInput(MOUSE_POS):
              score = 0
              quiz()
      
      pygame.display.update()

main_menu()


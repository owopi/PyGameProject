import pygame, sys, os, time
from subprocess import call

score = 0
quiz_started = False
water_visited = False
pond_drank = False

# initializing the constructor
pygame.init()

#declare paths
jungle_font = "font.otf"
debug_font = "debug_font.otf"
conflict_font = "conflict_font.ttf"
sf_display = "SFUI-Heavy.otf"
reactive_font = "ReactiveAnchor.ttf"
clock = pygame.time.Clock()


# screen resolution
res = (1366,768)
width = 1366
height = 768

# opens up a window
screen = pygame.display.set_mode(res)

# backgrounds
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
compass_bg = pygame.image.load("compass.jpg")
compass_bg = pygame.transform.scale(compass_bg,(1366,768))
jaguar_death = pygame.image.load("jaguar1.jpg")
jaguar_death = pygame.transform.scale(jaguar_death,(1366,768))
web_death = pygame.image.load("web.jpg")
web_death = pygame.transform.scale(web_death,(1366,768))


# define the RGB values
color = (255,255,255)
white=(255, 255, 255)
yellow=(255, 255, 0)
green=(0, 255, 255)
orange=(255, 100, 0)
black = (0,0,0)
red = (255, 49, 49)

# declare fonts
menu_font = pygame.font.Font(jungle_font, 132)
small_menu_font = pygame.font.Font(jungle_font, 100)
back_button_font = pygame.font.Font(sf_display, 50)
button_font = pygame.font.Font(debug_font, 80)
death_font = pygame.font.Font(conflict_font, 80)
ui_font = pygame.font.Font(sf_display, 80)
title_font = pygame.font.Font(reactive_font, 166)
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
        MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = title_font.render("MAIN", True, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 300))
        MENU_TEXT2 = title_font.render("MENU", True, "#ffffff")
        MENU_RECT2 = MENU_TEXT2.get_rect(center=(400, 500))
        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(MENU_TEXT2,MENU_RECT2)

        LESSON_BUTTON = Button(image=pygame.image.load("Large_Rect.png"), pos=(1000, 100), text_input="Lesson", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        PLAY_BUTTON = Button(image=pygame.image.load("Small_Rect.png"), pos=(1000, 250), text_input="Play", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        QUIZ_BUTTON = Button(image=pygame.image.load("Small_Rect.png"), pos=(1000, 400), text_input="Quiz", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        RESULTS_BUTTON = Button(image=pygame.image.load("Large_Rect.png"), pos=(1000, 550), text_input="Results", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit_Rect.png"), pos=(1000, 700), text_input="EXIT", font=small_menu_font, base_color="#d7fcd4", hovering_color="red")

        for button in [LESSON_BUTTON, PLAY_BUTTON, QUIZ_BUTTON, RESULTS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LESSON_BUTTON.checkForInput(MOUSE_POS):
                    lesson1()
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    play()
                if QUIZ_BUTTON.checkForInput(MOUSE_POS):
                    quiz()
                if RESULTS_BUTTON.checkForInput(MOUSE_POS):
                    results()
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

"""LESSON CODE"""

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

"""GAME CODE"""

def play():
    #call(["python", "lore_video.py"])
    while True:
        screen.blit(bg2, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        TEXT = ui_font.render("You're Lost, What do you do?", True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)

        WALK = Button(image=None, pos=(700, 400), text_input="Explore your Surroundings", font=button_font, base_color="#d7fcd4", hovering_color="white")
        MOMENT = Button(image=None, pos=(700, 600), text_input="Take a Moment to Collect your Thoughts", font=button_font, base_color="#d7fcd4", hovering_color="white")
        
        for button in [WALK, MOMENT]:
          button.changeColor(MOUSE_POS)
          button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if WALK.checkForInput(MOUSE_POS):
                walking1()
              if MOMENT.checkForInput(MOUSE_POS):
                camp()
        pygame.display.update()

def camp():
    global water_visited
    #call(["python", "lore_video.py"])
    while True:
        screen.blit(bg2, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        TEXT = ui_font.render('Choose Wisely!', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)

        COMPASS = Button(image=None, pos=(700, 300), text_input="Use Your Compass and Map", font=button_font, base_color="#d7fcd4", hovering_color="white")
        WALK = Button(image=None, pos=(700, 500), text_input="Keep Walking", font=button_font, base_color="#d7fcd4", hovering_color="white")
        if not water_visited:
          WATER = Button(image=None, pos=(700, 700), text_input="Search for Water", font=button_font, base_color="#d7fcd4", hovering_color="white")
          WATER.changeColor(MOUSE_POS)
          WATER.update(screen)
        
        for button in [COMPASS, WALK]:
          button.changeColor(MOUSE_POS)
          button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if COMPASS.checkForInput(MOUSE_POS):
                compass()
              if WATER.checkForInput(MOUSE_POS):
                water_collect()
              if WALK.checkForInput(MOUSE_POS):
                death_jaguar()
                #need to add extra 
        pygame.display.update()

def compass():
    #call(["python", "lore_video.py"])
    while True:
        screen.blit(compass_bg, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        TEXT = ui_font.render('Night is Approaching Fast', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)

        RUN = Button(image=None, pos=(700, 400), text_input="Run Through the Forest to the Exit", font=button_font, base_color="#d7fcd4", hovering_color="white")
        SHELTER = Button(image=None, pos=(700, 600), text_input="Build a Shelter to Spend the Night", font=button_font, base_color="#d7fcd4", hovering_color="white")

        for button in [RUN, SHELTER]:
          button.changeColor(MOUSE_POS)
          button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if RUN.checkForInput(MOUSE_POS):
                death_jaguar()
                #need to add extra
              if SHELTER.checkForInput(MOUSE_POS):
                shelter()
        pygame.display.update()

def water_collect():
    global water_visited
    global pond_drank
    water_visited = True
    #call(["python", "lore_video.py"])
    while True:
        screen.blit(bg2, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        TEXT = ui_font.render('Think Carefully!', True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)

        POND = Button(image=None, pos=(700, 400), text_input="Collect Water from a Clear Water Pond", font=button_font, base_color="#d7fcd4", hovering_color="white")
        RIVER = Button(image=None, pos=(700, 600), text_input="Collect Water from a Free Flowing River", font=button_font, base_color="#d7fcd4", hovering_color="white")
        
        
        for button in [POND, RIVER]:
          button.changeColor(MOUSE_POS)
          button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if POND.checkForInput(MOUSE_POS):
                pond_drank = True
                camp()
                #add info aaaaaaaa
              if RIVER.checkForInput(MOUSE_POS):
                camp()
        pygame.display.update()


def shelter():
    #call(["python", "lore_video.py"])
    while True:
        screen.blit(bg2, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        TEXT = ui_font.render("It's a Simple Choice", True, white)
        RECT = TEXT.get_rect(center=(690, 100))
        screen.blit(TEXT, RECT)

        TARP = Button(image=None, pos=(700, 350), text_input="Build a Tent with the Tarp ", font=button_font, base_color="#d7fcd4", hovering_color="white")
        BRANCHES = Button(image=None, pos=(700, 475), text_input="Build a Shelter with", font=button_font, base_color="#d7fcd4", hovering_color="white")
        BRANCHES_B = Button(image=None, pos=(700, 525), text_input=" Branches, Leaves, Debris, and Tarp", font=button_font, base_color="white", hovering_color="white")
        BRICKS = Button(image=None, pos=(700, 650), text_input="Build a shelter with Bricks", font=button_font, base_color="#d7fcd4", hovering_color="white")

        BRANCHES_B.update(screen)
        for button in [TARP, BRANCHES, BRICKS]:
          button.changeColor(MOUSE_POS)
          button.update(screen)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if TARP.checkForInput(MOUSE_POS):
                tarp_death()
              if BRANCHES.checkForInput(MOUSE_POS):
                escape()
              if BRICKS.checkForInput(MOUSE_POS):
                call(["python", "brick_video.py"])
        pygame.display.update()

def escape():
    global pond_drank
    #call(["python", "lore_video.py"])
    while True:
        screen.blit(bg2, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        if not pond_drank:
          TEXT = ui_font.render("You Sucessfully Survived and Escaped!", True, white)
          RECT = TEXT.get_rect(center=(690, 100))
          screen.blit(TEXT, RECT)
        else:
          TEXT = death_font.render('You Drank Pond Water', True, white)
          RECT = TEXT.get_rect(center=(690, 100))
          TEXT2 = death_font.render('Yesterday and Died from the Bacteria', True, white)
          RECT2 = TEXT.get_rect(center=(690, 200))
          TEXT3 = death_font.render('How Unfortunate', True, white)
          RECT3 = TEXT.get_rect(center=(690, 300))
          screen.blit(TEXT, RECT)
          screen.blit(TEXT2, RECT2)
          screen.blit(TEXT3, RECT3)

        MENU = Button(image=None, pos=(700, 400), text_input="MAIN MENU", font=button_font, base_color="#d7fcd4", hovering_color="white")
        
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


def tarp_death():
  #call(["python", "test_video.py"])
      while True:
        screen.blit(death, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()


        TEXT = ui_font.render('Your Tarp Flew Away!', True, white)
        RECT = TEXT.get_rect(center=(700, 50))
        TEXT2 = back_button_font.render('The Temperature at Night Dropped Rapidly and', True, white)
        RECT2 = TEXT.get_rect(center=(550, 150))
        TEXT3 = back_button_font.render('You Died of Hypothermia!', True, red)
        RECT3 = TEXT.get_rect(center=(810, 240))
        screen.blit(TEXT, RECT)
        screen.blit(TEXT2, RECT2)
        screen.blit(TEXT3, RECT3)
        DEATH_MENU = Button(image=None, pos=(1175, 725), text_input="Main Menu", font=button_font, base_color="red", hovering_color="white")
        
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

#in testing
"""
text_list = ["a", "bcd", "cd"]

#function to render textt
def render_animation(text, colour, type):
  text = type.render(str(text), True, colour)
  return text
  
def scene_6():
  #draws the background and images
  screen.fill (white)
  #question writing
  ypos = 35
  for i in text_list:
    time.sleep(1)
    pygame.display.update()
    text = render_animation(i, (0, 0, 0), ui_font)
    screen.blit (text, (35, ypos))
    ypos = ypos + 80
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
    pygame.display.update()"""

#path 3
def walking1():
  while True:
    screen.blit(bg2, (0,0))
    MOUSE_POS = pygame.mouse.get_pos()

    TEXT = small_menu_font.render('ABC', True, white)
    RECT = TEXT.get_rect(center=(690, 100))
    screen.blit(TEXT, RECT)
    CAVE = Button(image=None, pos=(700, 400), text_input="Take Shelter in a Nearby Cave", font=button_font, base_color="#d7fcd4", hovering_color="white")
    WALK = Button(image=None, pos=(700, 600), text_input="Try to Find your Way Back", font=button_font, base_color="#d7fcd4", hovering_color="white")

    for button in [CAVE, WALK]:
      button.changeColor(MOUSE_POS)
      button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if CAVE.checkForInput(MOUSE_POS):
            death_spider()
          if WALK.checkForInput(MOUSE_POS):
            death_jaguar()
    pygame.display.update()


def death_spider():
  #call(["python", "spider_death.py"])
  while True:
    screen.blit(web_death, (0,0))
    MOUSE_POS = pygame.mouse.get_pos()

    TEXT = ui_font.render('You were bitten by a spider!', True, white)
    RECT = TEXT.get_rect(center=(690, 100))
    screen.blit(TEXT, RECT)
    DEATH_MENU = Button(image=None, pos=(1175, 725), text_input="Main Menu", font=button_font, base_color="red", hovering_color="white")
    
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

def death_jaguar():
  #call(["python", "test_video.py"])
  while True:
    screen.blit(jaguar_death, (0,0))
    MOUSE_POS = pygame.mouse.get_pos()


    TEXT = ui_font.render('You were Jumped by a Jaguar!', True, white)
    RECT = TEXT.get_rect(center=(690, 80))
    screen.blit(TEXT, RECT)
    DEATH_MENU = Button(image=None, pos=(200, 700), text_input="Main Menu", font=button_font, base_color="red", hovering_color="white")
    
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



"""QUIZ STARTS HERE"""

def quiz():
  #call(["python", "test_video.py"])
  while True:
    MOUSE_POS = pygame.mouse.get_pos()

    screen.fill("black")

    TEXT = title_font.render('READY TO BEGIN?', True, white)
    RECT = TEXT.get_rect(center=(690, 260))
    screen.blit(TEXT, RECT)
    MENU = Button(image=None, pos=(500, 500), text_input="MAIN MENU", font=back_button_font, base_color="red", hovering_color="white")
    READY = Button(image=None, pos=(900, 500), text_input="READY", font=back_button_font, base_color="White", hovering_color="Green")
    
    for button in [MENU, READY]:
      button.changeColor(MOUSE_POS)
      button.update(screen)
    
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
    
    for button in [OPT1, OPT2, OPT3, OPT4]:
      button.changeColor(MOUSE_POS)
      button.update(screen)

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
      
      for button in [OPT1, OPT2, OPT3, OPT4]:
        button.changeColor(MOUSE_POS)
        button.update(screen)
      for button in [OPT1B, OPT2B, OPT3B, OPT4B]:
        button.update(screen)

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
      
      for button in [OPT1, OPT2, OPT3, OPT4]:
        button.changeColor(MOUSE_POS)
        button.update(screen)

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
      
      for button in [OPT1, OPT2, OPT3, OPT4]:
        button.changeColor(MOUSE_POS)
        button.update(screen)
    
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
      
      for button in [OPT1, OPT2, OPT3, OPT4]:
        button.changeColor(MOUSE_POS)
        button.update(screen)

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
      
      for button in [BACK, TRY_AGAIN]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

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
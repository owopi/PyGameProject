# importing modules
import pygame, sys, os, time
from subprocess import call

# initialize/declare
score = 0
quiz_started = False
water_visited = False
pond_drank = False

# initializing the constructor
pygame.init()

#declare paths
jungle_font = "Fonts/font.otf"
debug_font = "Fonts/debug_font.otf"
sf_display = "Fonts/SFUI-Heavy.otf"
reactive_font = "Fonts/ReactiveAnchor.ttf"
clock = pygame.time.Clock()


# screen resolution
res = (1366,768)
width = 1366
height = 768

# opens up a window
screen = pygame.display.set_mode(res)

# all backgrounds and images
bg_img = pygame.image.load("Images/abc.jpg")
bg_img = pygame.transform.scale(bg_img,(1366,768))
bg2 = pygame.image.load("Images/bg2.jpg")
bg2 = pygame.transform.scale(bg2,(1366,768))
slide1 = pygame.image.load("Images/Slide1.jpg")
slide1 = pygame.transform.scale(slide1,(1366,768))
slide2 = pygame.image.load("Images/Slide2.jpg")
slide2 = pygame.transform.scale(slide2,(1366,768))
slide3 = pygame.image.load("Images/Slide3.jpg")
slide3 = pygame.transform.scale(slide3,(1366,768))
slide4 = pygame.image.load("Images/Slide4.jpg")
slide4 = pygame.transform.scale(slide4,(1366,768))
slide5 = pygame.image.load("Images/Slide5.jpg")
slide5 = pygame.transform.scale(slide5,(1366,768))
compass_bg = pygame.image.load("Images/compass.jpg")
compass_bg = pygame.transform.scale(compass_bg,(1366,768))
jaguar_death = pygame.image.load("Images/jaguar1.jpg")
jaguar_death = pygame.transform.scale(jaguar_death,(1366,768))
web_death = pygame.image.load("Images/web.jpg")
web_death = pygame.transform.scale(web_death,(1366,768))
tarp_death_img = pygame.image.load("tarp.png")
tarp_death_img = pygame.transform.scale(tarp_death_img,(1366,768))
scratch = pygame.image.load("Images/scratch_marks.png")
scratch = pygame.transform.scale(scratch, (1366,768))
heat = pygame.image.load("Images/heat_src.jpg")
heat = pygame.transform.scale(heat,(1366,768))
water = pygame.image.load("Images/water.jpg")
water = pygame.transform.scale(water,(1366,768))
shelter_bg = pygame.image.load("Images/shelter.jpg")
shelter_bg = pygame.transform.scale(shelter_bg,(1366,768))
acronym = pygame.image.load("Images/acronym_q.jpg")
acronym = pygame.transform.scale(acronym,(1366,768))
path = pygame.image.load("Images/path.jpg")
path = pygame.transform.scale(path,(1366,768))
forest = pygame.image.load("Images/forest.jpg")
forest = pygame.transform.scale(forest,(1366,768))
river = pygame.image.load("Images/river.jpg")
river = pygame.transform.scale(river,(1366,768))
clear_area = pygame.image.load("Images/area.jpg")
clear_area = pygame.transform.scale(clear_area,(1366,768))
escaped = pygame.image.load("Images/escaped.jpg")
escaped = pygame.transform.scale(escaped,(1366,768))
cit1 = pygame.image.load("Images/cit1.png")
cit1 = pygame.transform.scale(cit1,(1366,768))
cit2 = pygame.image.load("Images/cit2.png")
cit2 = pygame.transform.scale(cit2,(1366,768))
cit3 = pygame.image.load("Images/cit3.png")
cit3 = pygame.transform.scale(cit3,(1366,768))


# define the RGB values
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
ui_font = pygame.font.Font(sf_display, 80)
title_font = pygame.font.Font(reactive_font, 166)
hehe_font = pygame.font.Font(sf_display, 20)


# First Button 
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

	#****************************************************************
# Program Name: Landing Page
# Program Author(s): Surya T.
# Revision Date: 2022-06-16
# Description: renders and blits the text needed for the animated text in the landing page
#*****************************************************************
def write_message(char, x, y):
	# first render the value as text so it can be drawn on the screen using screen.blit
	message_text = ui_font.render(char, True, (255, 255, 255))
	screen.blit(message_text, (x, y))

	#****************************************************************
# Program Name: Landing Page
# Program Author(s): Surya T.
# Revision Date: 2022-06-16
# Description: Code for landing page and Button to main menu 
#*****************************************************************
def landing():
	# Backgrounds + messages 
	message = ""
	xpos = 20
	ypos = -70
	message_text_speed = 45
	lines = ["Survive the Night", "Developed by:", "Surya and Sri", "15/06/2022", "ICS2O7", "Ms.Keras"]
	for line in lines:
		message = ""
		ypos += 110
		for char in line:
			message += char
			write_message(message, xpos, ypos)
			pygame.event.pump() #decrease likelihood of program freezing by handling internal events
			pygame.time.delay(message_text_speed)
			pygame.display.update()
			clock.tick(60)
	clock.tick(0.50)
	# Game loop  for the Landing page
	while True:
		screen.fill("Black")
		MOUSE_POS = pygame.mouse.get_pos()

		MAIN_MENU = Button(image=None, pos=(700, 300), text_input="BEGIN", font=title_font, base_color="#d7fcd4", hovering_color="Green")
		MAIN_MENU.changeColor(MOUSE_POS)
		MAIN_MENU.update(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if MAIN_MENU.checkForInput(MOUSE_POS):
					main_menu()
		pygame.display.update()
# Main Menu Page
	#****************************************************************
# Program Name: Main Menu
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Code for the main menu along with buttons and mouse position properties to see if the button has been clicked 
#*****************************************************************
def main_menu():
	#Blits backgrounds and buttons along with code to know if the button has been pressed
	while True:
		screen.blit(bg_img, (0, 0))
		MOUSE_POS = pygame.mouse.get_pos()
	# declares and renders the text and buttons onto the screen
		MENU_TEXT = title_font.render("MAIN", True, "#ffffff")
		MENU_RECT = MENU_TEXT.get_rect(center=(400, 300))
		MENU_TEXT2 = title_font.render("MENU", True, "#ffffff")
		MENU_RECT2 = MENU_TEXT2.get_rect(center=(400, 500))
		screen.blit(MENU_TEXT, MENU_RECT)
		screen.blit(MENU_TEXT2,MENU_RECT2)
	# assigns each button its attribtues and calls it
		LESSON_BUTTON = Button(image=pygame.image.load("Images/Large_Rect.png"), pos=(1000, 100), text_input="Lesson", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
		PLAY_BUTTON = Button(image=pygame.image.load("Images/Small_Rect.png"), pos=(1000, 250), text_input="Play", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
		QUIZ_BUTTON = Button(image=pygame.image.load("Images/Small_Rect.png"), pos=(1000, 400), text_input="Quiz", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
		RESULTS_BUTTON = Button(image=pygame.image.load("Images/Large_Rect.png"), pos=(1000, 550), text_input="Results", font=small_menu_font, base_color="#d7fcd4", hovering_color="White")
		QUIT_BUTTON = Button(image=pygame.image.load("Images/Quit_Rect.png"), pos=(1000, 700), text_input="EXIT", font=small_menu_font, base_color="#d7fcd4", hovering_color="red")
	# adds the colour changing effect upon hovering
		for button in [LESSON_BUTTON, PLAY_BUTTON, QUIZ_BUTTON, RESULTS_BUTTON, QUIT_BUTTON]:
			button.changeColor(MOUSE_POS)
			button.update(screen)
		#checks if the button has been clicked on and defines what to do when clicked
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
					exit()
		pygame.display.update()

	#****************************************************************
# Program Name: Lesson
# Program Author(s): Surya T. 
# Revision Date: 2022-06-16
# Description: displays the biblography and exists
#*****************************************************************
def exit():
	biblography = [cit1, cit2, cit3] 
	while True:
		for image in biblography:
			screen.blit(image, (0,0))
			pygame.event.pump()    #decrease likelihood of program freezing by handling internal events
			pygame.display.update()
			pygame.time.delay(750)
		pygame.quit() # quits the program right after
		sys.exit()

"""LESSON CODE"""

	#****************************************************************
# Program Name: Lesson
# Program Author(s): Srivathsan Prasanna, Surya T. 
# Revision Date: 2022-06-16
# Description: Blits lesson pages 1 - 5
#*****************************************************************


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

#****************************************************************
# Program Name: Play
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Code for the the animation and buttons on it 
#*****************************************************************
def play():
	#call(["python", "lore_video.py"])
	while True:
		screen.blit(bg2, (0,0))
		MOUSE_POS = pygame.mouse.get_pos()

		TEXT = ui_font.render("You're Lost, What do you do?", True, white)
		RECT = TEXT.get_rect(center=(690, 100))
		TEXT2 = back_button_font.render("You have a tarp, compass and map, first-aid, and food.", True, white)
		RECT2 = TEXT.get_rect(center=(600, 200))
		screen.blit(TEXT, RECT)
		screen.blit(TEXT2, RECT2)

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

#****************************************************************
# Program Name: Camp
# Program Author(s): Surya T.
# Revision Date: 2022-06-16
# Description: Options Page for the Camp question
#*****************************************************************

def camp():
	global water_visited
	while True:
		screen.blit(forest, (0,0))
		MOUSE_POS = pygame.mouse.get_pos()

		TEXT = ui_font.render('Choose Wisely!', True, white)
		RECT = TEXT.get_rect(center=(690, 100))
		screen.blit(TEXT, RECT)
		# button attributes
		COMPASS = Button(image=None, pos=(700, 300), text_input="Use Your Compass and Map", font=button_font, base_color="#d7fcd4", hovering_color="white")
		WALK = Button(image=None, pos=(700, 500), text_input="Keep Walking", font=button_font, base_color="#d7fcd4", hovering_color="white")
		if not water_visited:
			WATER = Button(image=None, pos=(700, 700), text_input="Search for Water", font=button_font, base_color="#d7fcd4", hovering_color="white")
			WATER.changeColor(MOUSE_POS)
			WATER.update(screen)
		# button colour change
		for button in [COMPASS, WALK]:
			button.changeColor(MOUSE_POS)
			button.update(screen)
		# what to do when user presses mouse down on button
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if COMPASS.checkForInput(MOUSE_POS):
					call(["python", "compass.py"])
					compass()
				if WALK.checkForInput(MOUSE_POS):
					death_jaguar()
				if WATER.checkForInput(MOUSE_POS):
					water_collect()
		pygame.display.update()

#****************************************************************
# Program Name: Compass
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Options Page for the "What to do after mapping your way out" question
#*****************************************************************

def compass():
	clock.tick(1)
	call(["python", "night_fall.py"])
	while True:
		screen.blit(compass_bg, (0,0))
		MOUSE_POS = pygame.mouse.get_pos()
		# text blit
		TEXT = ui_font.render('Night is Approaching Fast', True, white)
		RECT = TEXT.get_rect(center=(690, 100))
		screen.blit(TEXT, RECT)
		# button attributes
		RUN = Button(image=None, pos=(700, 400), text_input="Run Through the Forest to the Exit", font=button_font, base_color="#d7fcd4", hovering_color="white")
		SHELTER = Button(image=None, pos=(700, 600), text_input="Build a Shelter to Spend the Night", font=button_font, base_color="#d7fcd4", hovering_color="white")
		# button command
		for button in [RUN, SHELTER]:
			button.changeColor(MOUSE_POS)
			button.update(screen)

		# mouse down check
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

#****************************************************************
# Program Name: water Collect
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Options Page for the collect rations decision
#*****************************************************************

def water_collect():
	global water_visited
	global pond_drank
	water_visited = True
	while True:
		screen.blit(river, (0,0))
		MOUSE_POS = pygame.mouse.get_pos()
		# blit 
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

#****************************************************************
# Program Name: Shelter
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Options Page for the "Build a Shelter" question
#*****************************************************************

def shelter():
	while True:
		screen.blit(clear_area, (0,0))
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

#****************************************************************
# Program Name: Escape
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Ending screen for the animation (with a twist) 
#*****************************************************************

def escape():
	global water_visited
	global pond_drank
	if not pond_drank:
		call(["python", "escape_video.py"])
	while True:
		screen.blit(escaped, (0,0))
		MOUSE_POS = pygame.mouse.get_pos()
		# if and else statement fot the twist ending
		if not pond_drank:
			TEXT = ui_font.render("You Sucessfully Survived", True, black)
			RECT = TEXT.get_rect(center=(690, 100))
			TEXT2 = ui_font.render("and Found your Friends!", True, black)
			RECT2 = TEXT.get_rect(center=(715, 200))
		if water_visited and not pond_drank:
			TEXT3 = ui_font.render("BTW You didn't need the water", True, white)
			RECT3 = TEXT.get_rect(center=(575, 625))
			TEXT4 = ui_font.render("as you only camped a single day!", True, white)
			RECT4 = TEXT.get_rect(center=(550, 700))
			screen.blit(TEXT3, RECT3)
			screen.blit(TEXT4, RECT4)
		else:
			screen.fill("Black")
			TEXT = ui_font.render('You Drank Pond Water', True, white)
			RECT = TEXT.get_rect(center=(690, 100))
			TEXT2 = back_button_font.render('Yesterday and Died from the Bacteria', True, white)
			RECT2 = TEXT.get_rect(center=(690, 200))
			TEXT3 = ui_font.render('How Unfortunate!', True, white)
			RECT3 = TEXT.get_rect(center=(760, 260))
			screen.blit(TEXT3, RECT3)
		# display on screen
		screen.blit(TEXT, RECT)
		screen.blit(TEXT2, RECT2)
		MENU = Button(image=None, pos=(700, 350), text_input="MAIN MENU", font=button_font, base_color="#d7fcd4", hovering_color="white")

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

#****************************************************************
# Program Name: Tarp Death
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Death screen for if you choose to use just a tarp for shelter
#*****************************************************************

def tarp_death():
	while True:
		screen.blit(tarp_death_img, (0,0))
		MOUSE_POS = pygame.mouse.get_pos()

		# button attributes
		TEXT = ui_font.render('Your Tarp Flew Away!', True, white)
		RECT = TEXT.get_rect(center=(700, 50))
		TEXT2 = back_button_font.render('The Temperature at Night Dropped Rapidly and', True, white)
		RECT2 = TEXT.get_rect(center=(550, 150))
		TEXT3 = back_button_font.render('You Died of Hypothermia!', True, red)
		RECT3 = TEXT.get_rect(center=(810, 240))

		# button blit
		screen.blit(TEXT, RECT)
		screen.blit(TEXT2, RECT2)
		screen.blit(TEXT3, RECT3)
		DEATH_MENU = Button(image=None, pos=(1175, 725), text_input="Main Menu", font=button_font, base_color="red", hovering_color="white")

		DEATH_MENU.changeColor(MOUSE_POS)
		DEATH_MENU.update(screen)

		# mouse down check
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if DEATH_MENU.checkForInput(MOUSE_POS):
					main_menu()
		pygame.display.update()

#****************************************************************
# Program Name: Compass
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Options Page for the "First choice on wheter to continue walking or take a moment to think" question
#*****************************************************************

#path 3
def walking1():
	while True:
		screen.blit(path, (0,0))
		MOUSE_POS = pygame.mouse.get_pos()

		TEXT = ui_font.render('Are you Sure?', True, white)
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

#****************************************************************
# Program Name: death_spider
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Death screen for the "continue walking without thinking" option
#*****************************************************************

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

#****************************************************************
# Program Name: death_jaguar
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Death screen for the "continue walking without thinking" where you are killed by a jaguar option
#*****************************************************************

def death_jaguar():
	#call(["python", "test_video.py"])
	while True:
		screen.blit(jaguar_death, (0,0))
		MOUSE_POS = pygame.mouse.get_pos()


		TEXT = ui_font.render('You were Jumped by a Jaguar!', True, white)
		RECT = TEXT.get_rect(center=(690, 50))
		TEXT2 = back_button_font.render('Your confused movements alerted a hungry jaguar.', True, white)
		RECT2 = TEXT.get_rect(center=(680, 150))

		screen.blit(TEXT, RECT)
		screen.blit(TEXT2, RECT2)
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

#****************************************************************
# Program Name: quiz
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Quiz initialization and score tally along with buttons
#*****************************************************************

def quiz():
	global score

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
					score = 0
					question1()
		pygame.display.update()

#****************************************************************
# Program Name: Quiz Questions
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Displays the Questions 1- 5 for the quiz
#*****************************************************************

def question1():
	global score
	global quiz_started
	quiz_started = True
	while True:
		MOUSE_POS = pygame.mouse.get_pos()

		screen.blit(heat, (0,0))

		TEXT = ui_font.render('What is the MOST Reliable', True, white)
		RECT = TEXT.get_rect(center=(690, 150))
		TEXT2 = ui_font.render('Source of Heat?', True, white)
		RECT2 = TEXT.get_rect(center=(900, 240))
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

		screen.blit(water, (0,0))

		# button attributes
		TEXT = ui_font.render('How do you Make Sure that', True, black)
		RECT = TEXT.get_rect(center=(690, 100))
		TEXT2 = ui_font.render('Your Water is Safe?', True, black)
		RECT2 = TEXT.get_rect(center=(850, 190))
		screen.blit(TEXT, RECT)
		screen.blit(TEXT2, RECT2)
		OPT1 = Button(image=None, pos=(500, 400), text_input="Drink Clear", font=back_button_font, base_color="orange", hovering_color="black")
		OPT1B = Button(image=None, pos=(500, 450), text_input="Pond Water", font=back_button_font, base_color="Black", hovering_color="black")
		OPT2 = Button(image=None, pos=(900, 400), text_input="Drink Green", font=back_button_font, base_color="orange", hovering_color="black")
		OPT2B = Button(image=None, pos=(900, 450), text_input="River Water", font=back_button_font, base_color="Black", hovering_color="black")
		OPT3 = Button(image=None, pos=(500, 600), text_input="Boil Water", font=back_button_font, base_color="orange", hovering_color="black")
		OPT3B = Button(image=None, pos=(500, 650), text_input="with Heat Vision", font=back_button_font, base_color="Black", hovering_color="black")
		OPT4 = Button(image=None, pos=(900, 600), text_input="Boil Water", font=back_button_font, base_color="orange", hovering_color="black")
		OPT4B = Button(image=None, pos=(900, 650), text_input="with a Fire", font=back_button_font, base_color="Black", hovering_color="black")

		for button in [OPT1, OPT2, OPT3, OPT4]:
			button.changeColor(MOUSE_POS)
			button.update(screen)
		for button in [OPT1B, OPT2B, OPT3B, OPT4B]:
			button.update(screen)

		# mouse down check
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

		screen.blit(scratch, (0,0))

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

		screen.blit(acronym, (0,0))

		TEXT = ui_font.render("The Best Way to Remember These", True, black)
		RECT = TEXT.get_rect(center=(680, 100))
		TEXT2 = ui_font.render("Tips is Through the Acronym:", True, black)
		RECT2 = TEXT.get_rect(center=(800, 190))
		screen.blit(TEXT, RECT)
		screen.blit(TEXT2, RECT2)
		OPT1 = Button(image=None, pos=(500, 500), text_input="SHOP", font=back_button_font, base_color="red", hovering_color="white")
		OPT2 = Button(image=None, pos=(900, 500), text_input="STOP", font=back_button_font, base_color="red", hovering_color="white")
		OPT3 = Button(image=None, pos=(500, 625), text_input="RICK ASTLEY", font=back_button_font, base_color="red", hovering_color="white")
		OPT4 = Button(image=None, pos=(900, 625), text_input="WATER", font=back_button_font, base_color="red", hovering_color="white")

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

		screen.blit(shelter_bg, (0,0))

		TEXT = ui_font.render('It is Okay to use ______ to Make', True, white)
		RECT = TEXT.get_rect(center=(690, 100))
		TEXT2 = ui_font.render('an Insulation Layer', True, white)
		RECT2 = TEXT.get_rect(center=(850, 190))
		TEXT3 = ui_font.render('When Making Your Tent?', True, white)
		RECT3 = TEXT.get_rect(center=(760, 280))
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
					confirm()
				if OPT2.checkForInput(MOUSE_POS):
					confirm()
				if OPT3.checkForInput(MOUSE_POS):
					confirm()
				if OPT4.checkForInput(MOUSE_POS):
					confirm()    
		pygame.display.update()

#****************************************************************
# Program Name: confirm
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Used to ask the user wheter they way to show the answer os just skip to results
#*****************************************************************

def confirm():
	while True:
		MOUSE_POS = pygame.mouse.get_pos()

		screen.fill("black")
		CTEXT = ui_font.render('Do you Want to See the Answers?', True, white)
		CRECT = CTEXT.get_rect(center=(690, 75))
		screen.blit(CTEXT, CRECT)

		ANSWER = Button(image=None, pos=(500, 700), text_input="Show", font=back_button_font, base_color="red", hovering_color="white")
		RESULTS = Button(image=None, pos=(900, 700), text_input="Skip to Results", font=back_button_font, base_color="red", hovering_color="white")
		for button in [ANSWER, RESULTS]:
			button.changeColor(MOUSE_POS)
			button.update(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if ANSWER.checkForInput(MOUSE_POS):
					answers()
				if RESULTS.checkForInput(MOUSE_POS):
					results()
		pygame.display.update()

#****************************************************************
# Program Name: answer
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Answers page for the quiz
#*****************************************************************

def answers():
	while True:
		MOUSE_POS = pygame.mouse.get_pos()
		screen.fill("black")
		# button attributes
		TEXT = ui_font.render('Answers', True, white)
		RECT = TEXT.get_rect(center=(690, 75))
		ANS1 = back_button_font.render('1. Body Heat', True, "Green")
		ANS1R = TEXT.get_rect(center=(705, 200))
		ANS2 = back_button_font.render('2. Boil Water with a Fire', True, "Green")
		ANS2R = TEXT.get_rect(center=(590, 300))
		ANS3 = back_button_font.render('3. No', True, "Green")
		ANS3R = TEXT.get_rect(center=(790, 400))
		ANS4 = back_button_font.render('4. STOP', True, "Green")
		ANS4R = TEXT.get_rect(center=(760, 500))
		ANS5 = back_button_font.render('5. Leaves', True, "Green")
		ANS5R = TEXT.get_rect(center=(750, 600))
		screen.blit(TEXT, RECT)
		screen.blit(ANS1, ANS1R)
		screen.blit(ANS2, ANS2R)
		screen.blit(ANS3, ANS3R)
		screen.blit(ANS4, ANS4R)
		screen.blit(ANS5, ANS5R)

		RESULTS = Button(image=None, pos=(1200, 670), text_input="Results", font=back_button_font, base_color="red", hovering_color="white")
		RESULTS.changeColor(MOUSE_POS)
		RESULTS.update(screen)


		# mouse down check
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if RESULTS.checkForInput(MOUSE_POS):
					results()    
		pygame.display.update()

#****************************************************************
# Program Name: results
# Program Author(s): Surya T., Srivathsan Prasanna
# Revision Date: 2022-06-16
# Description: Page to show the user did on the quiz along with code for the buttons to take you back to the Main menu 
#*****************************************************************

def results():
	global score
	global quiz_started
	#call(["python", "test_video.py"])
	while True:
		MOUSE_POS = pygame.mouse.get_pos()
		if not quiz_started:
			screen.fill("black")
			TEXT = ui_font.render("You didn't Begin the Quiz Yet!", True, white)
			RECT = TEXT.get_rect(center=(720, 150))
			screen.blit(TEXT, RECT)
		else:
			if score <= 2:
				screen.fill("red")
				TEXT = ui_font.render("You scored a " + str(score) + " out of 5" + " (" + str(20 * score) + "%)", True, white)
				RECT = TEXT.get_rect(center=(690, 150))
				TEXT2 = ui_font.render("YOU DID TERRIBLE!", True, white)
				RECT2 = TEXT.get_rect(center=(890, 300))
			elif score == 3:
				TEXT = ui_font.render("You scored a " + str(score) + " out of 5" + " (" + str(20 * score) + "%)", True, white)
				RECT = TEXT.get_rect(center=(690, 150))
				TEXT2 = ui_font.render("YOU DID DECENT!", True, white)
				RECT2 = TEXT.get_rect(center=(890, 300))
			elif score == 4:
				TEXT = ui_font.render("You scored a " + str(score) + " out of 5" + " (" + str(20 * score) + "%)", True, white)
				RECT = TEXT.get_rect(center=(690, 150))
				TEXT2 = ui_font.render("SO CLOSE!!!", True, white)
				RECT2 = TEXT.get_rect(center=(1025, 300))
			else: 
				TEXT = ui_font.render("You scored a " + str(score) + " out of 5" + " (" + str(20 * score) + "%)", True, white)
				RECT = TEXT.get_rect(center=(720, 150))
				TEXT2 = ui_font.render("YOU ARE THE EMBODIMENT", True, white)
				RECT2 = TEXT.get_rect(center=(600, 300))
				TEXT3 = ui_font.render("OF PERFECTION", True, white)
				RECT3 = TEXT.get_rect(center=(850, 400))
				TEXT4 = hehe_font.render("like Sujay!!", True, white)
				RECT4 = TEXT.get_rect(center=(1800, 775))
				screen.blit(TEXT3, RECT3)
				screen.blit(TEXT4, RECT4)

			screen.blit(TEXT, RECT)
			screen.blit(TEXT2, RECT2)

			BACK = Button(image=None, pos=(690, 700), text_input="MAIN MENU", font=back_button_font, base_color="White", hovering_color="red")
			TRY_AGAIN = Button(image=None, pos=(690, 600), text_input="TO THE QUIZ!", font=back_button_font, base_color="White", hovering_color="Green")

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
						quiz()
			pygame.display.update()
landing()
# Note: Ignore any errors related to any method calls that involve the keyword pygame.

import pygame
import random
# starting python engine
pygame.init()

# text methods
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, x, y, size, color):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (x, y + (size / 2))
    screen.blit(TextSurf, TextRect)
# calling the text method: message_display("Message", x, y, size, color)


# classes and methods should go here- just definitions, no method calls



# Declaring colors - use black and white as shades of gray
GRAY0 = (  0,   0,   0) # black
GRAY255 = (255, 255, 255) # white
GRAY230 = (230, 230, 230) # whitesmoke color from css - could use for information screens, it is a calming color
GRAY200 = (200, 200, 200) # very light gray - could use for metal, sidewalks
GRAY150 = (150, 150, 150) # semilight gray - could use for pavement, buildings
GRAY100 = (100, 100, 100) # semidark gray - could use for fresh asphalt, cracks in sidewalks
GRAY50 = (50, 50, 50) # dark gray - could use for tires
BLUE =  (  0,   0, 255) 
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255, 255,  0)

TEST = (80, 170, 80)


# Define more colors as is necessary.
# This is a color that is transparent to semi-transparent- use to overlay the screen in a nighttime enviroment
# setting the variable that we can change to adjust the transparency
darkness = 0
NIGHT_OVERLAY = (0, 0, 50, darkness) # third parameter gives it a slight blue tint
# remember, to use this variable, call it before calling any draw() methods so that it displays on top of anything that is drawn.


# declaring width and height of screen - change as you see fit
display_width = 800
display_height = 600
size = [display_width, display_height]
# putting this into the pygame engine
screen = pygame.display.set_mode(size)
# setting the title of the pygame window - change this to the title of the game.
pygame.display.set_caption("___________")


# Main game state variable
done = False
# initializing a way to keep track of time
clock = pygame.time.Clock()
# Main game loop
while not done:
    # setting the refresh rate - can be anywhere from 1 to around 300- leave this line out for max speed.
    clock.tick(100)
    # code for if user closes the pygame window
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            # exiting the main game loop
            done=True 

    # screen refresh code - need this line. Must initialize colors to work
    screen.fill(TEST)

    # HERE GOES ALL THE MAIN GAME LOGIC - method calls, control structures, conditional statements and more.





    # update the screen at the next loop iteration.
    pygame.display.flip()
 
# Terminating pygame engine when user has exited main game loop- see lines 65 and 67
pygame.quit()


# template built 6/11/2019 by jamin debu
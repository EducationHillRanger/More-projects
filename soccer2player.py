# Note: Ignore any errors related to any method calls that involve the keyword pygame.

# Game building started: 6/11/2019
# Game building ended: 7/15/2019 


# 0.1 Achieved: yes
# 0.2 Achieved: yes
# 0.3 Achieved: yes
# 0.4 Achieved: yes 
# 0.5 Achieved: yes
# 1.0 Achieved: yes


# THIS GAME IS NON-SCREEN-ADAPTABLE! CHANGING SCREEN SIZE DOES NOT AFFECT LOCATIONS OF VISIBLE ITEMS!
# screen should be set to x:1200, y:600

import pygame
import random
import time

# starting python engine
pygame.init()

##################################################################################
##################################################################################


# text methods
def text_objects(text, font, color):
    # change color
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, x, y, size, color):
    # change size and font as you see fit
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (x, y + (size / 2))
    screen.blit(TextSurf, TextRect)




###########################################################################
# classes and methods should go here- just definitions, no method calls
############################################################################



# call for drawing the arena during countdown before gameplay: DO NOT CALL THIS METHOD IN ACTUAL GAMEPLAY!
def draw_arena():
    screen.fill(GRASSGREEN)

    ball.draw()

    # Field lines
    for i in range (20):
        pygame.draw.rect(screen, DARKGRASSYELLOW, [100 + (i * 200), 0, 100, 600])


    # drawing left goal
    for i in range (90):
        GOALCOL = (230 - (i * 1.444), 230 - (i/3), 230 - (i * 1.722))
        pygame.draw.rect(screen, GOALCOL, [10 + i, 245 - i, 1, 110 + (i * 2)])
    pygame.draw.rect(screen, RED, [0, 150, 100, 10])
    pygame.draw.rect(screen, RED, [0, 440, 100, 10])
    pygame.draw.rect(screen, RED, [0, 150, 10, 300])

    # drawing right goal
    for i in range (90):
        GOALCOL = (230 - (i * 1.444), 230 - (i/3), 230 - (i * 1.722))
        pygame.draw.rect(screen, GOALCOL, [1190 - i, 245 - i, 1, 110 + (i * 2)])
    pygame.draw.rect(screen, BLUE, [1100, 150, 100, 10])
    pygame.draw.rect(screen, BLUE, [1100, 440, 100, 10])
    pygame.draw.rect(screen, BLUE, [1190, 150, 10, 300])

    # Players and ball- DO NOT USE THIS CODE ANYWHERE ELSE!
    pygame.draw.rect(screen, RED, [400, 275, 50, 50])
    pygame.draw.circle(screen, GRAY50, [425, 300], 25)

    pygame.draw.rect(screen, BLUE, [750, 275, 50, 50])
    pygame.draw.circle(screen, GRAY50, [775, 300], 25)

    pygame.draw.circle(screen, GRAY200, [600, 300], 15)



################################################################################
################################################################################


# drawing arena without the players
def draw_arena_static():
    screen.fill(GRASSGREEN)
    # Field lines
    for i in range (20):
        pygame.draw.rect(screen, DARKGRASSYELLOW, [100 + (i * 200), 0, 100, 600])
    # drawing left goal
    for i in range (90):
        GOALCOL = (230 - (i * 1.444), 230 - (i/3), 230 - (i * 1.722))
        pygame.draw.rect(screen, GOALCOL, [10 + i, 245 - i, 1, 110 + (i * 2)])
    pygame.draw.rect(screen, RED, [0, 150, 100, 10])
    pygame.draw.rect(screen, RED, [0, 440, 100, 10])
    pygame.draw.rect(screen, RED, [0, 150, 10, 300])

    # drawing right goal
    for i in range (90):
        GOALCOL = (230 - (i * 1.444), 230 - (i/3), 230 - (i * 1.722))
        pygame.draw.rect(screen, GOALCOL, [1190 - i, 245 - i, 1, 110 + (i * 2)])
    pygame.draw.rect(screen, BLUE, [1100, 150, 100, 10])
    pygame.draw.rect(screen, BLUE, [1100, 440, 100, 10])
    pygame.draw.rect(screen, BLUE, [1190, 150, 10, 300])




###############################################################################
###############################################################################

    

# class for red player
class RedPlayer:
    # constructor method
    def __init__(self, x, y):
        # starting x and y locations - remember- top left corner!
        self.x = x
        self.y = y
        self.width = 50
        

        self.stepx = 0
        self.stepy = 0

        self.accelx = 0
        self.accely = 0

        self.maxspeed = 2

        
#################################################################################

    # RED
    def draw_WASD(self):
        

        # drawing player
        pygame.draw.rect(screen, RED, [int(self.x), int(self.y), self.width, self.width])
        pygame.draw.circle(screen, GRAY50, [int(self.x + 25), int(self.y + 25)], 25)


        # bouncing off sides
        if self.x < 0:
            self.stepx = -(self.stepx / 2)
            self.x = 1

        if self.x > 1150:
            self.stepx = -(self.stepx / 2)
            self.x = 1149

        if self.y < 0: 
            self.stepy = -(self.stepy / 2)
            self.y = 1
       
        if self.y > 550:
            self.stepy = -(self.stepy / 2)
            self.y = 549

        # bouncing off goals: 
        # Left goal, top post
        if self.y > 100 and self.y < 103 and self.x < 100:
            self.stepy = -(self.stepy / 2)
            self.y = 99
        if self.y < 160 and self.y > 157 and self.x < 100:
            self.stepy = -(self.stepy / 2)
            self.y = 161
        if self.y > 100 and self.y < 160 and self.x < 100 and self.x > 97:
            self.stepx = -(self.stepx / 2)
            self.x = 101

        # Left goal, back post
        if self.y > 160 and self.y < 390 and self.x < 10:
            self.stepx = -(self.stepx / 2)
            self.x = 11

        # Left goal, bottom post
        if self.y > 390 and self.y < 393 and self.x < 100:
            self.stepy = -(self.stepy / 2)
            self.y = 389
        if self.y < 450 and self.y > 447 and self.x < 100:
            self.stepy = -(self.stepy / 2)
            self.y = 451
        if self.y > 390 and self.y < 450 and self.x < 100 and self.x > 97:
            self.stepx = -(self.stepx / 2)
            self.x = 101
 
        # Right goal, top post
        if self.y > 100 and self.y < 103 and self.x > 1050:
            self.stepy = -(self.stepy / 2)
            self.y = 99
        if self.y < 160 and self.y > 157 and self.x > 1050:
            self.stepy = -(self.stepy / 2)
            self.y = 161
        if self.y > 100 and self.y < 160 and self.x > 1050 and self.x < 1053:
            self.stepx = -(self.stepx / 2)
            self.x = 1049

        # Right goal, back post
        if self.y > 160 and self.y < 390 and self.x > 1140:
            self.stepx = -(self.stepx / 2)
            self.x = 1139

        # Right goal, bottom post
        if self.y > 390 and self.y < 393 and self.x > 1050:
            self.stepy = -(self.stepy / 2)
            self.y = 389
        if self.y < 450 and self.y > 447 and self.x > 1050:
            self.stepy = -(self.stepy / 2)
            self.y = 451
        if self.y > 390 and self.y < 450 and self.x > 1050 and self.x < 1533:
            self.stepx = -(self.stepx / 2)
            self.x = 1049



        # making red interact with blue in all directions
        # bottom side
        if self.x > blue.x - 50 and self.x < blue.x + 50 and self.y > blue.y - 50 and self.y < blue.y - 45:
            self.stepy = -self.stepy / 2
            self.stepy = self.stepy - 1
            
        # top side
        if self.x > blue.x - 50 and self.x < blue.x + 50 and self.y < blue.y + 50 and self.y > blue.y + 45:
            self.stepy = -self.stepy / 2
            self.stepy = self.stepy + 1
            
        # Right side
        if self.x > blue.x - 50 and self.x < blue.x - 45 and self.y > blue.y - 50 and self.y < blue.y + 50:
            self.stepx = -self.stepx / 2
            self.stepx = self.stepx - 1

        # Left side
        if self.x < blue.x + 50 and self.x > blue.x + 45 and self.y > blue.y - 50 and self.y < blue.y + 50:
            self.stepx = -self.stepx / 2
            self.stepx = self.stepx + 1



        

        # making red interact with ball in all directions
        # bottom side
        if self.x > ball.x - 50 and self.x < ball.x + 30 and self.y > ball.y - 50 and self.y < ball.y - 45:
            self.stepy = self.stepy * 1
           
            
        # top side
        if self.x > ball.x - 50 and self.x < ball.x + 30 and self.y < ball.y + 30 and self.y > ball.y + 25:
            self.stepy = self.stepy * 1
            
        # Right side
        if self.x > ball.x - 50 and self.x < ball.x - 45 and self.y > ball.y - 50 and self.y < ball.y + 30:
            self.stepx = self.stepx * 1

        # Left side
        if self.x < ball.x + 30 and self.x > ball.x + 25 and self.y > ball.y - 50 and self.y < ball.y + 30:
            self.stepx = self.stepx * 1
        


    
    # moving player up
    def up_WASD(self):
        # going up
        self.accely = -0.02

        # cancelling out right and left directions
        if self.stepx >= 0:
            self.accelx = -0.01
            if self.stepx < 0:
                self.stepx = 0
        if self.stepx <= 0: 
            self.accelx = 0.01
            if self.stepx > 0: 
                self.stepx = 0

        # setting the speed limit
        if self.stepy < -self.maxspeed:
            self.stepy = -self.maxspeed

        # incrementing variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely

    # moving player right
    def right_WASD(self):
        # going right
        self.accelx = 0.02

        # cancelling out up and down directions
        if self.stepy >= 0:
            self.accely = -0.01
            if self.stepy < 0:
                self.stepy = 0
        if self.stepy <= 0: 
            self.accely = 0.01
            if self.stepy > 0:
                self.stepy = 0

        # setting the speed limit
        if self.stepx > self.maxspeed:
            self.stepx = self.maxspeed

        # incrementing speed variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely

    # moving player down
    def down_WASD(self):
        # going down
        self.accely = 0.02

        # cancelling out right and left directions
        if self.stepx >= 0:
            self.accelx = -0.01
            if self.stepx < 0:
                self.stepx = 0
        if self.stepx <= 0: 
            self.accelx = 0.01
            if self.stepx > 0: 
                self.stepx = 0

        # setting the speed limit
        if self.stepy > self.maxspeed:
            self.stepy = self.maxspeed

        # incrementing speed variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely

    # moving player left
    def left_WASD(self):
        # going left
        self.accelx = -0.02

        # cancelling out up and down directions
        if self.stepy >= 0:
            self.accely = -0.01
            if self.stepy < 0:
                self.stepy = 0
        if self.stepy <= 0: 
            self.accely = 0.01
            if self.stepy > 0:
                self.stepy = 0

        # setting speed limit
        if self.stepx < -self.maxspeed:
            self.stepx = -self.maxspeed

        # incrementing speed variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely


##################################################################################


    # method called when no key is being pressed
    def default(self):
        # cancelling out ALL directions
        # cancelling right
        if self.stepx > 0:
            self.accelx = -0.01
            if self.stepx <= 0:
                self.stepx = 0
        # cancelling left
        if self.stepx < 0: 
            self.accelx = 0.01
            if self.stepx >= 0: 
                self.stepx = 0
        # cancelling down
        if self.stepy > 0:
            self.accely = -0.01
            if self.stepy <= 0:
                self.stepy = 0
        # cancelling up
        if self.stepy < 0: 
            self.accely = 0.01
            if self.stepy >= 0:
                self.stepy = 0

        # incrementing speed variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely


    # method that resets all properties to starting positions and values
    def reset(self):
        self.x = 400
        self.y = 275
        self.stepx = 0
        self.stepy = 0
        self.accelx = 0
        self.accely = 0


################################################################################
################################################################################

# class for blue player
class BluePlayer:
    # constructor method
    def __init__(self, x, y):
        # starting x and y locations - remember- top left corner!
        self.x = x
        self.y = y
        self.width = 50
        

        self.stepx = 0
        self.stepy = 0

        self.accelx = 0
        self.accely = 0

        self.maxspeed = 2

        
#################################################################################

    # BLUE
    def draw_arrows(self):
        

        # drawing player
        pygame.draw.rect(screen, BLUE, [int(self.x), int(self.y), self.width, self.width])
        pygame.draw.circle(screen, GRAY50, [int(self.x + 25), int(self.y + 25)], 25)


        # bouncing off sides
        if self.x < 0:
            self.stepx = -(self.stepx / 2)
            self.x = 1

        if self.x > 1150:
            self.stepx = -(self.stepx / 2)
            self.x = 1149

        if self.y < 0: 
            self.stepy = -(self.stepy / 2)
            self.y = 1
       
        if self.y > 550:
            self.stepy = -(self.stepy / 2)
            self.y = 549

        # bouncing off goals: 
        # Left goal, top post
        if self.y > 100 and self.y < 103 and self.x < 100:
            self.stepy = -(self.stepy / 2)
            self.y = 99
        if self.y < 160 and self.y > 157 and self.x < 100:
            self.stepy = -(self.stepy / 2)
            self.y = 161
        if self.y > 100 and self.y < 160 and self.x < 100 and self.x > 97:
            self.stepx = -(self.stepx / 2)
            self.x = 101

        # Left goal, back post
        if self.y > 160 and self.y < 390 and self.x < 10:
            self.stepx = -(self.stepx / 2)
            self.x = 11

        # Left goal, bottom post
        if self.y > 390 and self.y < 393 and self.x < 100:
            self.stepy = -(self.stepy / 2)
            self.y = 389
        if self.y < 450 and self.y > 447 and self.x < 100:
            self.stepy = -(self.stepy / 2)
            self.y = 451
        if self.y > 390 and self.y < 450 and self.x < 100 and self.x > 97:
            self.stepx = -(self.stepx / 2)
            self.x = 101
 
        # Right goal, top post
        if self.y > 100 and self.y < 103 and self.x > 1050:
            self.stepy = -(self.stepy / 2)
            self.y = 99
        if self.y < 160 and self.y > 157 and self.x > 1050:
            self.stepy = -(self.stepy / 2)
            self.y = 161
        if self.y > 100 and self.y < 160 and self.x > 1050 and self.x < 1053:
            self.stepx = -(self.stepx / 2)
            self.x = 1049

        # Right goal, back post
        if self.y > 160 and self.y < 390 and self.x > 1140:
            self.stepx = -(self.stepx / 2)
            self.x = 1139

        # Right goal, bottom post
        if self.y > 390 and self.y < 393 and self.x > 1050:
            self.stepy = -(self.stepy / 2)
            self.y = 389
        if self.y < 450 and self.y > 447 and self.x > 1050:
            self.stepy = -(self.stepy / 2)
            self.y = 451
        if self.y > 390 and self.y < 450 and self.x > 1050 and self.x < 1533:
            self.stepx = -(self.stepx / 2)
            self.x = 1049


        # making blue interact with red in all directions
        # bottom side
        if self.x > red.x - 50 and self.x < red.x + 50 and self.y > red.y - 50 and self.y < red.y - 45:
            self.stepy = -self.stepy / 2
            self.stepy = self.stepy - 1
            
        # top side
        if self.x > red.x - 50 and self.x < red.x + 50 and self.y < red.y + 50 and self.y > red.y + 45:
            self.stepy = -self.stepy / 2
            self.stepy = self.stepy + 1
            
        # Right side
        if self.x > red.x - 50 and self.x < red.x - 45 and self.y > red.y - 50 and self.y < red.y + 50:
            self.stepx = -self.stepx / 2
            self.stepx = self.stepx - 1

        # Left side
        if self.x < red.x + 50 and self.x > red.x + 45 and self.y > red.y - 50 and self.y < red.y + 50:
            self.stepx = -self.stepx / 2
            self.stepx = self.stepx + 1


        # making blue interact with ball in all directions
        # bottom side
        if self.x > ball.x - 50 and self.x < ball.x + 30 and self.y > ball.y - 50 and self.y < ball.y - 45:
            self.stepy = self.stepy * 1
           
            
        # top side
        if self.x > ball.x - 50 and self.x < ball.x + 30 and self.y < ball.y + 30 and self.y > ball.y + 25:
            self.stepy = self.stepy * 1
            
        # Right side
        if self.x > ball.x - 50 and self.x < ball.x - 45 and self.y > ball.y - 50 and self.y < ball.y + 30:
            self.stepx = self.stepx * 1

        # Left side
        if self.x < ball.x + 30 and self.x > ball.x + 25 and self.y > ball.y - 50 and self.y < ball.y + 30:
            self.stepx = self.stepx * 1

    
    # moving player up
    def up_arrows(self):
        # going up
        self.accely = -0.02

        # cancelling out right and left directions
        if self.stepx >= 0:
            self.accelx = -0.01
            if self.stepx < 0:
                self.stepx = 0
        if self.stepx <= 0: 
            self.accelx = 0.01
            if self.stepx > 0: 
                self.stepx = 0

        # setting the speed limit
        if self.stepy < -self.maxspeed:
            self.stepy = -self.maxspeed

        # incrementing variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely

    # moving player right
    def right_arrows(self):
        # going right
        self.accelx = 0.02

        # cancelling out up and down directions
        if self.stepy >= 0:
            self.accely = -0.01
            if self.stepy < 0:
                self.stepy = 0
        if self.stepy <= 0: 
            self.accely = 0.01
            if self.stepy > 0:
                self.stepy = 0

        # setting the speed limit
        if self.stepx > self.maxspeed:
            self.stepx = self.maxspeed

        # incrementing speed variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely

    # moving player down
    def down_arrows(self):
        # going down
        self.accely = 0.02

        # cancelling out right and left directions
        if self.stepx >= 0:
            self.accelx = -0.01
            if self.stepx < 0:
                self.stepx = 0
        if self.stepx <= 0: 
            self.accelx = 0.01
            if self.stepx > 0: 
                self.stepx = 0

        # setting the speed limit
        if self.stepy > self.maxspeed:
            self.stepy = self.maxspeed

        # incrementing speed variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely

    # moving player left
    def left_arrows(self):
        # going left
        self.accelx = -0.02

        # cancelling out up and down directions
        if self.stepy >= 0:
            self.accely = -0.01
            if self.stepy < 0:
                self.stepy = 0
        if self.stepy <= 0: 
            self.accely = 0.01
            if self.stepy > 0:
                self.stepy = 0

        # setting speed limit
        if self.stepx < -self.maxspeed:
            self.stepx = -self.maxspeed

        # incrementing speed variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely


####################################################################################

    # method called when no key is being pressed
    def default(self):
        # cancelling out ALL directions
        # cancelling right
        if self.stepx > 0:
            self.accelx = -0.01
            if self.stepx <= 0:
                self.stepx = 0
        # cancelling left
        if self.stepx < 0: 
            self.accelx = 0.01
            if self.stepx >= 0: 
                self.stepx = 0
        # cancelling down
        if self.stepy > 0:
            self.accely = -0.01
            if self.stepy <= 0:
                self.stepy = 0
        # cancelling up
        if self.stepy < 0: 
            self.accely = 0.01
            if self.stepy >= 0:
                self.stepy = 0

        # incrementing speed variables
        self.x += self.stepx
        self.y += self.stepy

        self.stepx += self.accelx
        self.stepy += self.accely


    # method to reset all things and return to default values
    def reset(self):
        self.x = 400
        self.y = 275
        self.stepx = 0
        self.stepy = 0
        self.accelx = 0
        self.accely = 0



################################################################################################
################################################################################################


# Ball class
class Ball:
    def __init__(self):

        self.x = 585
        self.y = 285
        
        self.stepx = 0
        self.stepy = 0
        self.decelx = 0
        self.decely = 0

        self.max_speed = 3


        

    def draw(self):

        pygame.draw.circle(screen, GRAY200, [int(self.x + 15),int(self.y + 15)], 15)



        self.x += self.stepx
        self.y += self.stepy
        self.stepx += self.decelx
        self.stepy += self.decely


        # bouncing off sides
        if self.x < 0:
            self.stepx = -self.stepx
            
            self.x = 1

        if self.x > 1170:
            self.stepx = -self.stepx
            
            self.x = 1169

        if self.y < 0: 
            self.stepy = -self.stepy
            
            self.y = 1
       
        if self.y > 570:
            self.stepy = -self.stepy
            
            self.y = 569


        # bouncing off goals:
        # Left goal, top post
        if self.y > 120 and self.y < 123 and self.x < 100:
            self.stepy = -self.stepy
            self.y = 119
        if self.y < 160 and self.y > 157 and self.x < 100:
            self.stepy = -self.stepy
            self.y = 161
        if self.y > 120 and self.y < 160 and self.x < 100 and self.x > 97:
            self.stepx = -self.stepx
            self.x = 101

        # Left goal, back post
        if self.y > 160 and self.y < 410 and self.x < 10:
            self.stepx = -self.stepx
            self.x = 11

        # Left goal, bottom post
        if self.y > 410 and self.y < 413 and self.x < 100:
            self.stepy = -self.stepy
            self.y = 409
        if self.y < 450 and self.y > 447 and self.x < 100:
            self.stepy = -self.stepy
            self.y = 451
        if self.y > 410 and self.y < 450 and self.x < 100 and self.x > 97:
            self.stepx = -self.stepx
            self.x = 101
 
        # Right goal, top post
        if self.y > 120 and self.y < 123 and self.x > 1070:
            self.stepy = -self.stepy
            self.y = 119
        if self.y < 160 and self.y > 157 and self.x > 1070:
            self.stepy = -self.stepy
            self.y = 161
        if self.y > 120 and self.y < 160 and self.x > 1070 and self.x < 1073:
            self.stepx = -self.stepx
            self.x = 1069

        # Right goal, back post
        if self.y > 160 and self.y < 410 and self.x > 1160:
            self.stepx = -self.stepx
            self.x = 1159

        # Right goal, bottom post
        if self.y > 410 and self.y < 413 and self.x > 1070:
            self.stepy = -self.stepy
            self.y = 409
        if self.y < 450 and self.y > 447 and self.x > 1070:
            self.stepy = -self.stepy
            self.y = 451
        if self.y > 410 and self.y < 450 and self.x > 1070 and self.x < 1073:
            self.stepx = -self.stepx
            self.x = 1069


        # making ball interact with red in all directions
        # bottom side
        if self.x > red.x - 30 and self.x < red.x + 50 and self.y > red.y - 30 and self.y < red.y - 25:
            self.stepy = -self.max_speed
            self.y -= 5
            
        # top side
        if self.x > red.x - 30 and self.x < red.x + 50 and self.y < red.y + 50 and self.y > red.y + 45:
            self.stepy = self.max_speed
            self.y += 5
            
        # Right side
        if self.x > red.x - 30 and self.x < red.x - 25 and self.y > red.y - 30 and self.y < red.y + 50:
            self.stepx = -self.max_speed
            self.x -= 5

        # Left side
        if self.x < red.x + 50 and self.x > red.x + 45 and self.y > red.y - 30 and self.y < red.y + 50:
            self.stepx = self.max_speed
            self.x += 5


        # making ball interact with blue in all directions
        # bottom side
        if self.x > blue.x - 30 and self.x < blue.x + 50 and self.y > blue.y - 30 and self.y < blue.y - 25:
            self.stepy = -self.max_speed
            self.y -= 5
            
        # top side
        if self.x > blue.x - 30 and self.x < blue.x + 50 and self.y < blue.y + 50 and self.y > blue.y + 45:
            self.stepy = self.max_speed
            self.y += 5
            
        # Right side
        if self.x > blue.x - 30 and self.x < blue.x - 25 and self.y > blue.y - 30 and self.y < blue.y + 50:
            self.stepx = -self.max_speed
            self.x -= 5

        # Left side
        if self.x < blue.x + 50 and self.x > blue.x + 45 and self.y > blue.y - 30 and self.y < blue.y + 50:
            self.stepx = self.max_speed
            self.x += 5




        # cancelling out ALL directions - slowing down
        # cancelling right
        if self.stepx > 0:
            self.decelx = -0.02
            if self.stepx <= 0:
                self.stepx = 0
        # cancelling left
        if self.stepx < 0: 
            self.decelx = 0.02
            if self.stepx >= 0: 
                self.stepx = 0
        # cancelling down
        if self.stepy > 0:
            self.decely = -0.02
            if self.stepy <= 0:
                self.stepy = 0
        # cancelling up
        if self.stepy < 0: 
            self.decely = 0.02
            if self.stepy >= 0:
                self.stepy = 0


    # methods that return true if contact is detected with players.
    
    # horizontal directions
    def check_hit_red_h(self):
        # Red
            
        # Right side
        if self.x > red.x - 30 and self.x < red.x - 25 and self.y > red.y - 30 and self.y < red.y + 50:
            return True

        # Left side
        if self.x < red.x + 50 and self.x > red.x + 45 and self.y > red.y - 30 and self.y < red.y + 50:
            return True

        return False


    def check_hit_blue_h(self):

        # Blue
        # Right side
        if self.x > blue.x - 30 and self.x < blue.x - 25 and self.y > blue.y - 30 and self.y < blue.y + 50:
            return True

        # Left side
        if self.x < blue.x + 50 and self.x > blue.x + 45 and self.y > blue.y - 30 and self.y < blue.y + 50:
            return True

        return False


    # vertical directions
    def check_hit_red_v(self):
        # Red
        # bottom side
        if self.x > red.x - 30 and self.x < red.x + 50 and self.y > red.y - 30 and self.y < red.y - 25:
            return True
            
        # top side
        if self.x > red.x - 30 and self.x < red.x + 50 and self.y < red.y + 50 and self.y > red.y + 45:
            return True

        return False

    def check_hit_blue_v(self):

        # Blue
        # bottom side
        if self.x > blue.x - 30 and self.x < blue.x + 50 and self.y > blue.y - 30 and self.y < blue.y - 25:
            return True
            
        # top side
        if self.x > blue.x - 30 and self.x < blue.x + 50 and self.y < blue.y + 50 and self.y > blue.y + 45:
            return True
        
        return False
            

    # checking for all contacts of wall and goals in vertical directions
    def check_hit_wall_v(self):

        # hitting wall, goals

        # WALLS:
        # bouncing off sides
        

        if self.y < 0: 
            return True
       
        if self.y > 570:
            return True


        # GOALS:
        # bouncing off goals:
        # Left goal, top post
        if self.y > 120 and self.y < 123 and self.x < 100:
            return True
        if self.y < 160 and self.y > 157 and self.x < 100:
            return True
        

        # Left goal, bottom post
        if self.y > 410 and self.y < 413 and self.x < 100:
            return True
        if self.y < 450 and self.y > 447 and self.x < 100:
            return True
        
 
        # Right goal, top post
        if self.y > 120 and self.y < 123 and self.x > 1070:
            return True
        if self.y < 160 and self.y > 157 and self.x > 1070:
            return True
        

        # Right goal, bottom post
        if self.y > 410 and self.y < 413 and self.x > 1070:
            return True
        if self.y < 450 and self.y > 447 and self.x > 1070:
            return True
        

        return False


    # checking for all contacts of wall and goals in horizontal directions
    def check_hit_wall_h(self):
        # walls
        if self.x < 0:
            return True

        if self.x > 1170:
            return True


        # goal parts
        if self.y > 120 and self.y < 160 and self.x < 100 and self.x > 97:
            return True

        # Left goal, back post
        if self.y > 160 and self.y < 410 and self.x < 10:
            return True
        
        if self.y > 410 and self.y < 450 and self.x < 100 and self.x > 97:
            return True


        if self.y > 120 and self.y < 160 and self.x > 1070 and self.x < 1073:
            return True
        
        # Right goal, back post
        if self.y > 160 and self.y < 410 and self.x > 1160:
            return True

        if self.y > 410 and self.y < 450 and self.x > 1070 and self.x < 1073:
            return True
        

        return False


    # methods for scoring into goals
    def left_goal(self):
        if self.x < 70 and self.y > 155 and self.y < 410:
            return True
        return False
    
    def right_goal(self):
        if self.x > 1070 and self.y > 155 and self.y < 410:
            return True
        return False

########################################################################################
########################################################################################

# Scorekeeping class
class Score:
    def __init__(self):
        self.disp_red_x = 100
        self.disp_blue_x = 1085
        self.disp_y = 10
        self.info_x = 600
        self.text_size = 60

    def draw (self, redscore, bluescore, info):
        self.redscore = redscore
        self.bluescore = bluescore
        self.info = info
        # red and blue scores
        message_display("Red: " + str(self.redscore), self.disp_red_x, self.disp_y, self.text_size, GRAY0)
        message_display("Blue: " + str(self.bluescore), self.disp_blue_x, self.disp_y, self.text_size, GRAY0)
        # info message
        message_display(str(self.info), self.info_x, self.disp_y, self.text_size, GRAY0)

########################################################################################
########################################################################################

# confetti class for when a player wins 
class Confetti:
    def __init__(self):
        self.x = random.randint(0, 1200)
        self.y = random.randint(0, 600)

    def draw(self):
        pygame.draw.line(screen, BLUE, [self.x - 5, self.y], [self.x, self.y], 2)
        pygame.draw.line(screen, RED, [self.x, self.y - 5], [self.x, self.y], 2)
        pygame.draw.line(screen, GREEN, [self.x + 5, self.y], [self.x, self.y], 2)
        pygame.draw.line(screen, YELLOW, [self.x, self.y + 5], [self.x, self.y], 2)
        
        self.y += 1
        if self.y > 605:
            self.y = -5

########################################################################################
########################################################################################

# method for returning all values to starting positions
def default():
    red.x = 400
    red.y = 275
    red.stepx = 0
    red.stepy = 0

    blue.x = 750
    blue.y = 275
    blue.stepx = 0
    blue.stepy = 0

    ball.x = 585
    ball.y = 285
    ball.stepx = 0
    ball.stepy = 0
    

#########################################################################################
#########################################################################################

# END OF MAKING CLASSES AND METHODS


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
GRASSYELLOW = (200, 255, 100)
DARKGRASSYELLOW = (95, 190, 72)
# Define more colors as is necessary.
GRASSGREEN = (100, 200, 75)

# This is a color that is transparent to semi-transparent- use to overlay the screen in a nighttime enviroment
# setting the variable that we can change to adjust the transparency
darkness = 0
NIGHT_OVERLAY = (0, 0, 50, darkness) # third parameter gives it a slight blue tint
# remember, to use this variable, call it after calling any draw() methods so that it displays on top of anything that is drawn.



##########################################################################################
##########################################################################################



# declaring width and height of screen - change as you see fit
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
# putting this into the pygame engine
screen = pygame.display.set_mode(size)
# setting the title of the pygame window - change this to the title of the game.
pygame.display.set_caption("1v1 soccer")



#########################################################################################
#########################################################################################



# Main game state variable
done = False
startscreen = True
countdown = False
countdownpos = 700
countdownstate = 3
# screens for red and blue winning
redwins = False
bluewins = False

bounce_frequency = 20
# timers for ball-popping out if being bounced vertically
timers_v = list([bounce_frequency, 0])


# timers for ball-popping out if being bounced horizontally
timers_h = list([bounce_frequency, 0])

# Booleans for keeping track of what was last hit
red_was_hit_v = False
red_was_hit_h = False
blue_was_hit_v = False
blue_was_hit_h = False
wall_was_hit_v = False
wall_was_hit_h = False

# red and blue scores
redscore = 0
bluescore = 0
maxscore = 5
info = "GO!"
info_ = "__________"


maingame = False
gotimer = 200
# initializing a way to keep track of time
clock = pygame.time.Clock()



#######################################################################################
#######################################################################################
# class variables
red = RedPlayer(400, 275)
blue = BluePlayer(750, 275)
ball = Ball()
score = Score()

confettis = []
for i in range(100):
    confetti = Confetti()
    confettis.append(confetti)


#####################################################################################
#####################################################################################

# Main game loop
while not done:
    # setting the refresh rate - can be anywhere from 1 to around 300- leave this line out for max speed.
    # clock.tick(100)
    # code for if user closes the pygame window
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            # exiting the main game loop
            done=True 


    ######################################################################################
    ######################################################################################


    # code for start/info screen
    if startscreen:
        # displaying info on the start screen
        screen.fill(GRAY230)
        message_display("Red player controls: WASD", 200, 100, 20, GRAY0)
        message_display("Blue player controls: Arrow keys", 950, 100, 20, GRAY0)
        message_display("Red: You are defending the left side goal! Don't let the ball go in! Blue: You are defending the right side goal! Don't let the ball go in!", 600, 400, 18, GRAY0)
        message_display("Press enter when you are ready to begin!", 600, 500, 20, GRAY50)

        # exiting the start screen with an enter key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            startscreen = False
            countdown = True
            # startscreen has been exited


    ############################################################################################
    ############################################################################################     

    # countdown screen
    if countdown:
        # drawing arena background
        draw_arena()

        # code for countdown numbers
        if countdownstate == 3:
            message_display("3", 600 - countdownpos, 200, 200, YELLOW)
            message_display("3", 600 + countdownpos, 200, 200, YELLOW)
            countdownpos -= 6

            if countdownpos <= -700:
                countdownstate = 2
                countdownpos = 700

        if countdownstate == 2:
            message_display("2", 600 - countdownpos, 200, 200, RED)
            message_display("2", 600 + countdownpos, 200, 200, RED)
            countdownpos -= 6

            if countdownpos <= -700:
                countdownstate = 1
                countdownpos = 700

        if countdownstate == 1:
            message_display("1", 600 - countdownpos, 200, 200, BLUE)
            message_display("1", 600 + countdownpos, 200, 200, BLUE)
            countdownpos -= 6

            if countdownpos <= -700:
                countdownstate = 0
                countdown = False
                maingame = True

    
    

        
    ###################################################################################
    ###################################################################################

       


    # ALL of the main game code
    if maingame:
        draw_arena_static()
        # call arena draw method above


        

        # variables that keep track of direction
        arrows = pygame.key.get_pressed()
        WASD = pygame.key.get_pressed()

        # draw players here
        
        # movement for red player- WASD
        if WASD[pygame.K_w]:
            red.up_WASD()
        elif WASD[pygame.K_d]:
            red.right_WASD()
        elif WASD[pygame.K_s]:
            red.down_WASD()
        elif WASD[pygame.K_a]:
            red.left_WASD()
        else:
            red.default()

        red.draw_WASD()


        # movement for blue player- arrows
        if arrows[pygame.K_UP]:
            blue.up_arrows()
        elif arrows[pygame.K_RIGHT]:
            blue.right_arrows()
        elif arrows[pygame.K_DOWN]:
            blue.down_arrows()
        elif arrows[pygame.K_LEFT]:
            blue.left_arrows()
        else:
            blue.default()

        blue.draw_arrows()


        #####################################################################################

        # variable that sets how much time is needed in between each bounce for the ball to be popped out
        

        # vertical ball-bouncing-out code- If ball is being bounced up and down fast, code for popping it out
        # red in vertical direcion- if red was hit, red cannot be hit again until something else is hit
        if ball.check_hit_red_v() == True and red_was_hit_v == False:
            # turning on red_was_hit_v
            red_was_hit_v = True
            blue_was_hit_v = False
            wall_was_hit_v = False
            # pushing a new timer onto the end of the existing Timer array
            newTimer = 0
            timers_v.append(newTimer)

        # blue in vertical direcion- if blue was hit, blue cannot be hit again until something else is hit
        if ball.check_hit_blue_v() == True and blue_was_hit_v == False:
            # turning on red_was_hit_v
            blue_was_hit_v = True
            red_was_hit_v = False
            wall_was_hit_v = False
            # pushing a new timer onto the end of the existing Timer array
            newTimer = 0
            timers_v.append(newTimer)
        
        # wall in vertical direcion- if wall was hit, wall cannot be hit again until something else is hit
        if ball.check_hit_wall_v() == True and wall_was_hit_v == False:
            # turning on red_was_hit_v
            wall_was_hit_v = True
            red_was_hit_v = False
            blue_was_hit_v = False
            # pushing a new timer onto the end of the existing Timer array
            newTimer = 0
            timers_v.append(newTimer)

        # getting current length of the timer array
        timerLength_v = timers_v.__len__() - 1
        # actual code for popping ball out- If statement checks distance between timer values
        if (timers_v[timerLength_v - 1] - timers_v[timerLength_v]) < bounce_frequency:
            # randomizing the direction in which the ball pops out
            random_direction = random.randint(1, 2)
            if random_direction == 1:
                ball.x -= 50
                ball.stepx = -ball.max_speed
            
            else:
                ball.x += 50
                ball.stepx = ball.max_speed

            # putting last element out of range of if statement a few lines ago :)
            timers_v[timerLength_v] -= bounce_frequency

            # red_was_hit_v = False
            # blue_was_hit_v = False
            # wall_was_hit_v = False

            

        
        for index_timers, _ in enumerate(timers_v):
            timers_v[index_timers] += 1



        # horizontal ball-bouncing-out code- If ball is being bounced up and down fast, code for popping it out
        # red in horizontal direcion- if red was hit, red cannot be hit again until something else is hit
        if ball.check_hit_red_h() == True and red_was_hit_h == False:
            # pushing a new timer onto the end of the existing Timer array
            newTimer = 0
            timers_h.append(newTimer)
            red_was_hit_h = True
            blue_was_hit_h = False
            wall_was_hit_h = False

        # blue in horizontal direcion- if blue was hit, blue cannot be hit again until something else is hit
        if ball.check_hit_blue_h() == True and blue_was_hit_h == False:
            # pushing a new timer onto the end of the existing Timer array
            newTimer = 0
            timers_h.append(newTimer)
            blue_was_hit_h = True
            red_was_hit_h = False
            wall_was_hit_h = False

        # wall in horizontal direcion- if wall was hit, wall cannot be hit again until something else is hit
        if ball.check_hit_wall_h() == True and wall_was_hit_h == False:
            # pushing a new timer onto the end of the existing Timer array
            newTimer = 0
            timers_h.append(newTimer)
            wall_was_hit_h = True
            red_was_hit_h = False
            blue_was_hit_h = False

        # getting current length of the timer array
        timerLength_h = timers_h.__len__() - 1
        # actual code for popping ball out- If statement checks distance between timer values
        if (timers_h[timerLength_h - 1] - timers_h[timerLength_h]) < bounce_frequency:
            # randomizing the direction in which the ball pops out
            random_direction = random.randint(1, 2)
            if random_direction == 1:
                ball.y -= 50
                ball.stepy = -ball.max_speed
            
            else:
                ball.y += 50
                ball.stepy = ball.max_speed

            # putting last element out of range of if statement on line 1188
            timers_h[timerLength_h] -= bounce_frequency

            # red_was_hit_h = False
            # blue_was_hit_h = False
            # wall_was_hit_h = False

        
        for index_timers, _ in enumerate(timers_h):
            timers_h[index_timers] += 1


        
        # checking if ball went into goals
        if ball.left_goal():
            info = "Blue scores!"
            bluescore += 1
            default()
            
        if ball.right_goal():
            info = "Red scores!"
            redscore += 1
            default()

        # checking for a winner
        if bluescore == maxscore:
            maingame = False
            bluewins = True
            bluescore = 0
            redscore = 0
            default()

        if redscore == maxscore: 
            maingame = False
            redwins = True
            bluescore = 0
            redscore = 0
            default()
        

        ball.draw()
        score.draw(redscore, bluescore, info)
        

    if bluewins: 
        screen.fill(GRAY100)
        for i in range(100):
            confettis[i].draw()

        message_display("Blue wins! Press enter to play again!", 600, 300, 40, BLUE)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            bluewins = False
            maingame = True

    if redwins:
        screen.fill(GRAY100)
        for i in range(100):
            confettis[i].draw()

        message_display("Red wins! Press enter to play again!", 600, 300, 40, RED)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            redwins = False
            maingame = True


    ####################################################################################
    ####################################################################################


    # update the screen at the next loop iteration.
    pygame.display.flip()
 
# Terminating pygame engine when user has exited main game loop- see lines 51 and 53
pygame.quit()


# template built 6/11/2019 by jamin debu
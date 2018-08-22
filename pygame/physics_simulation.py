# Python Physics Simulation

import pygame, sys
from pygame.locals import *

FPS = 60            # frames per second setting
WINDOWWIDTH = 1920   # size of the window's width in pixels
WINDOWHEIGHT = 1080  # size of the window's height in pixels

fpsClock = pygame.time.Clock()

# Initialise pygame and setup the window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0 , 32)
pygame.display.set_caption('Physics Simulation')

## Selection of various colour variables
#               R    G    B
GRAY        = (100, 100, 100)
NAVYBLUE    = ( 60,  60, 100)
WHITE       = (255, 255, 255)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
BLUE        = (  0,   0, 255)
YELLOW      = (255, 255,   0)
ORANGE      = (255, 128,   0)
PURPLE      = (255,   0, 255)
CYAN        = (  0, 255, 255)

BGCOLOUR = WHITE

startSimulation = False


# Class for the ball
class Ball(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        # Load the sprite image
        self.image = pygame.image.load('physics_ball.png')
        self.original = self.image
        self.rect = self.image.get_rect(center=pos)

        # Set X & Y velocity of the ball
        self.change_x = 0
        self.change_y = 0

    # Calculate the movement of the ball
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if the ball bounces on the floor
        if self.rect.y >= WINDOWHEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = (-self.change_y * 0.8)
            self.rect.y = WINDOWHEIGHT - self.rect.height

        # See if the ball hits the walls
        if self.rect.x >= WINDOWWIDTH - self.rect.width and self.change_x >= 0:
            self.change_x = (-self.change_x * 0.8)
            self.rect.x = WINDOWWIDTH - self.rect.width
        elif self.rect.x <= 0 and self.change_x <= 0:
            self.change_x = (-self.change_x * 0.8)
            self.rect.x = 0


    # Update Method
    def update(self):
        # Gravity
        self.calc_grav()
            
        # Move left/right
        self.rect.x += self.change_x

        # Move up/down
        self.rect.y += self.change_y


# Subroutine for closing the game cleanly
def closeGame():
    print('The game will now close')
    pygame.quit()
    sys.exit()

active_sprite_list = pygame.sprite.Group()
ball = Ball((200, WINDOWHEIGHT/2 - 100))
ball.change_x = 14
ball.change_y = 5
active_sprite_list.add(ball)



# Main Game Loop
while True:

    # Event handling in the game loop
    for event in pygame.event.get():
        ## For when the player presses the close window button
        if event.type == QUIT:
            closeGame()
        ## For when the player presses a key on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                startSimulation = True
            if event.key == pygame.K_ESCAPE:
                closeGame()

    DISPLAYSURF.fill([255, 255, 255])
    #DISPLAYSURF.blit(BackGround.image, BackGround.rect)

    if(startSimulation == True):
        active_sprite_list.update()
    
    active_sprite_list.draw(DISPLAYSURF)
            
    pygame.display.update()
    fpsClock.tick(FPS)

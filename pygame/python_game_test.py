# Python Testing Game
# By Ashley Cromack (ashleydavidcromack@gmail.com)

import pygame, sys
from pygame.locals import *

FPS = 60 # frames per second setting
WINDOWWIDTH = 640 # size of the window's width in pixels
WINDOWHEIGHT = 480 # size of the window's height in pixels

fpsClock = pygame.time.Clock()

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0 , 32)
pygame.display.set_caption('Animation')

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
CURRCOLNUM = 0
COLOURARRAY = [GRAY, NAVYBLUE, WHITE, RED, GREEN, YELLOW, ORANGE, PURPLE, CYAN]

catImg = pygame.image.load('cat.png')
catX = 10
catY = 10
direction = 'right'

# Load in a wav file to play as background music
pygame.mixer.music.load('ChillingMusic.wav')
# Play the music in the background in a looping manner
pygame.mixer.music.play(-1)

# Subroutine for closing the game cleanly
def closeGame():
    print('The game will now close')
    pygame.quit()
    sys.exit()

# Main Game Loop
while True:
    DISPLAYSURF.fill(BGCOLOUR)

    if direction == 'right':
        catX += 5
        if catX == 280:
            direction = 'down'
    elif direction == 'down':
        catY += 5
        if catY == 220:
            direction = 'left'
    elif direction == 'left':
        catX -= 5
        if catX == 10:
            direction = 'up'
    elif direction == 'up':
        catY -= 5
        if catY == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catX, catY))

    # Event handling in the game loop
    for event in pygame.event.get():
        ## For when the player presses the close window button
        if event.type == QUIT:
            closeGame()
        ## For when the player presses a key on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if CURRCOLNUM > 0:
                    CURRCOLNUM -= 1
                    BGCOLOUR = COLOURARRAY[CURRCOLNUM]
            if event.key == pygame.K_RIGHT:
                if CURRCOLNUM < 8:
                    CURRCOLNUM += 1
                    BGCOLOUR = COLOURARRAY[CURRCOLNUM]
            if event.key == pygame.K_ESCAPE:
                closeGame()
            
    pygame.display.update()
    fpsClock.tick(FPS)

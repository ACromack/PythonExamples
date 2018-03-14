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

catImg = pygame.image.load('katamari.png')
direction = 'right'

def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect


# Class for the player
class Player(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        # Load the sprite image
        self.image = pygame.image.load('prince.png')
        self.original = self.image
        # Fetch the rect object that has the image's dimensions
        #self.rect = self.image.get_rect()
        #self.image = pygame.transform.scale(image, (168, 113))
        self.rect = self.image.get_rect(center=pos)


        self.angle = 0
        self.angle_change = 0


    # Update Method
    def update(self):
        if self.angle_change != 0:
            self.angle+= self.angle_change
            self.image = pygame.transform.rotozoom(self.original, self.angle, 1)
            self.rect = self.image.get_rect(center=self.rect.center)
            
        self.rect.x = self.rect.x
        

# Class for the level background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



# Load in a wav file to play as background music
#pygame.mixer.music.load('ChillingMusic.wav')
pygame.mixer.music.load('LonelyRollingStar.mp3')
pygame.mixer.music.set_volume(0.1)
# Play the music in the background in a looping manner
pygame.mixer.music.play(-1)

# Subroutine for closing the game cleanly
def closeGame():
    print('The game will now close')
    pygame.quit()
    sys.exit()

active_sprite_list = pygame.sprite.Group()
player = Player((WINDOWWIDTH/2, WINDOWHEIGHT/2))
active_sprite_list.add(player)

BackGround = Background('background2.png', [0,-280])

effect = pygame.mixer.Sound('PickupCoin.wav')
effect.set_volume(0.1)


# Main Game Loop
while True:
    DISPLAYSURF.fill([255, 255, 255])
    #DISPLAYSURF.blit(BackGround.image, BackGround.rect)

    if BackGround.rect.x > -1400:
        BackGround.rect.x -= 1
        DISPLAYSURF.blit(BackGround.image, BackGround.rect)
    elif BackGround.rect.x <= -1400:
        BackGround.rect.x += 1400
        DISPLAYSURF.blit(BackGround.image, BackGround.rect)
        


    active_sprite_list.update()
    active_sprite_list.draw(DISPLAYSURF)

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
                    #BGCOLOUR = COLOURARRAY[CURRCOLNUM]
                    player.angle_change = 3
            if event.key == pygame.K_RIGHT:
                if CURRCOLNUM < 8:
                    CURRCOLNUM += 1
                    #BGCOLOUR = COLOURARRAY[CURRCOLNUM]
                    player.angle_change = -3
            if event.key == pygame.K_SPACE:
                effect.play()
            if event.key == pygame.K_ESCAPE:
                closeGame()
            
    pygame.display.update()
    fpsClock.tick(FPS)

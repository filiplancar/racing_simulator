#Import modules
import pygame
import os

#Initialize pygame
pygame.init()

#Sizes
class Sizes:
    def __init__(self, font_size, width, height):
        self.font_size = font_size
        self.width = width
        self.height = height

s = Sizes(20, 840, 650)


#Images and font
BG = pygame.image.load(os.path.join('assets', 'background-1.png'))
CAR_0 = pygame.image.load(os.path.join('assets', 'car0.png'))
CAR_1 = pygame.image.load(os.path.join('assets', 'car1.png'))
FONT = pygame.font.Font('Arial', s.font_size)

#Set display
pygame.display.set_mode((s.width, s.height))
pygame.display.set_caption('Racing Simulator')

#Game loop
# running = True

# while running:
#     for event

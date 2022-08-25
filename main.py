#Import modules
import pygame
import os

#Initialize pygame
pygame.init()

#Sizes
FONT_SIZE = 20
WIDTH = 840
HEIGHT = 650

#Images and font
BG = pygame.image.load(os.path.join('assets', 'background-1.png'))
CAR_0 = pygame.image.load(os.path.join('assets', 'car0.png'))
CAR_1 = pygame.image.load(os.path.join('assets', 'car1.png'))
FONT = pygame.font.Font('Arial', FONT_SIZE)

pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racing Simulator')

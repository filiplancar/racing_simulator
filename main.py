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

#Get background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

bg = Background(os.path.join('assets', 'background-1.png', [0,0]))

#Images and font
# BG = pygame.image.load(os.path.join('assets', 'background-1.png'))
CAR_0 = pygame.image.load(os.path.join('assets', 'car0.png'))
CAR_1 = pygame.image.load(os.path.join('assets', 'car1.png'))
FONT = pygame.font.SysFont('Arial', s.font_size)

#Set display
WIN = pygame.display.set_mode((s.width, s.height))
pygame.display.set_caption('Racing Simulator')

#Game loop
def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()

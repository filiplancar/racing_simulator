#Import modules
import pygame
import os

#Initialize pygame
pygame.init()

#Colors
WHITE = (255,255,255)

#Sizes
class Sizes:
    def __init__(self, font_size, width, height):
        self.font_size = font_size
        self.width = width
        self.height = height

s = Sizes(20, 840, 650)

#Images and font
CAR_1 = pygame.image.load(os.path.join('assets', 'car1.png'))
FONT = pygame.font.SysFont('Arial', s.font_size)

#Get background
class Background(pygame.sprite.Sprite):
    def __init__(self, path, img, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(path, img))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

bg = Background('assets', 'background-1.png', (0,0))

#Set display
screen = pygame.display.set_mode((s.width, s.height))
pygame.display.set_caption('Racing Simulator')

#Get car for player 
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, path, img, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(path, img))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#Game loop
def main():
    
    pos_x = 360
    pos_y = 410
    second_pos_y = pos_y - 50

    vel = 5
    fps = 60

    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pos_x -= vel
        
        if keys[pygame.K_RIGHT]:
            pos_x += vel
        
        if pos_y != second_pos_y:
            pos_y -= vel
        
        player_car = PlayerCar('assets', 'car0.png', (pos_x, pos_y))
        player_car.image = pygame.transform.scale(player_car.image, (120, 240))

        screen.fill(WHITE)    
        screen.blit(bg.image, bg.rect)
        screen.blit(player_car.image, player_car.rect)

        pygame.display.update()

if __name__ == "__main__":
    main()

#Snažím sa dať auto do pohybu
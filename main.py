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

# player_car = PlayerCar('assets', 'car0.png', (360,410))

#Game loop
def main():
    
    x = 360
    y = 410
    # player_car = PlayerCar('assets', 'car0.png', (x, y))
    
    vel = 5

    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel
        
        if keys[pygame.K_RIGHT]:
            x += vel

        player_car = PlayerCar('assets', 'car0.png', (x, y))
        player_car.image = pygame.transform.scale(player_car.image, (120, 240))

        screen.fill(WHITE)    
        screen.blit(bg.image, bg.rect)
        screen.blit(player_car.image, player_car.rect)

        pygame.display.update()

if __name__ == "__main__":
    main()

#Snažím sa dať auto do pohybu
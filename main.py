#Import modules and initialize pygame
# from tkinter import font
import pygame
import os
import random
pygame.init()

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#Sizes
class Sizes:
    def __init__(self, font_size, width, height):
        self.font_size = font_size
        self.width = width
        self.height = height

s = Sizes(20, 840, 650)

#Images and font
myfont = pygame.font.SysFont('Arial', s.font_size)

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
class Car(pygame.sprite.Sprite):
    def __init__(self, path, img, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(path, img))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#Game loop
def main():
    #Positions for player car
    player_x = 360
    player_y = 410
    second_pos_y = player_y - 50

    #Borders of road
    left_border = 140
    right_border = 585

    #Positions for obstacle cars
    obstacle_x = random.randint(left_border, right_border)
    obstacle_y = -250
    
    #Velocity and fps
    vel = 5
    fps = 60

    #score
    score = 0

    #Clock and running 
    clock = pygame.time.Clock()
    running = True


    while running:
        #Connect clock with fps
        clock.tick(fps)

        #Ending the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        #Positions for obstacle cars
        if obstacle_y >= s.height:
            obstacle_x = random.randint(left_border, right_border)
            obstacle_y = -250
            
            #Change velocity
            vel+=0.5

            #Change score
            score+=1

        keys = pygame.key.get_pressed()

        #Moving with player car
        if keys[pygame.K_LEFT] and player_x > left_border:
            player_x -= vel
        
        if keys[pygame.K_RIGHT] and player_x < right_border:
            player_x += vel
        
        if player_y != second_pos_y:
            player_y -= vel    
        
        #Moving with obstacle car
        obstacle_y += vel
        
        #Cars objects
        player_car = Car('assets', 'car0.png', (player_x, player_y))
        player_car.image = pygame.transform.scale(player_car.image, (120, 240))

        obstacle_car = Car('assets', 'car1.png', (obstacle_x, obstacle_y))
        obstacle_car.image = pygame.transform.scale(obstacle_car.image, (120, 240))

        #Fill and blit screen
        screen.fill(WHITE)    
        screen.blit(bg.image, bg.rect)
        screen.blit(player_car.image, player_car.rect)

        screen.blit(obstacle_car.image, obstacle_car.rect)

        scoretext = myfont.render("Score = "+str(score), 1, (BLACK))
        screen.blit(scoretext, (5,10))

        velocitytext = myfont.render("Velocity = "+str(vel), 1, (BLACK))
        screen.blit(velocitytext, (5,35))

        pygame.display.update()

if __name__ == "__main__":
    main()

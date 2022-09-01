#Import modules and initialize pygame
import pygame
import os
import random
pygame.init()

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE = (255, 191, 0)

#Sizes
class Sizes:
    def __init__(self, b_font_size, s_font_size, width, height):
        self.b_font_size = b_font_size
        self.s_font_size = s_font_size
        self.width = width
        self.height = height

s = Sizes(100, 20, 840, 650)

#Images and font
smallfont = pygame.font.SysFont('Arial', s.s_font_size)
bigfont = pygame.font.SysFont('Arial',s.b_font_size)


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
        super().__init__()
        self.image = pygame.image.load(os.path.join(path, img))
        self.image = pygame.transform.scale(self.image, (120, 240))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        # self.hitbox = (self.rect.left + 20, self.rect.top, 28, 60)

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

    #Texts
    crashtext = bigfont.render("CRASH", 1, (ORANGE))
    anothergametext = smallfont.render("Another game? (Press any key)", 1, (ORANGE))

    while running:
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
        obstacle_car = Car('assets', 'car1.png', (obstacle_x, obstacle_y))
        

        #Fill and blit screen
        screen.fill(WHITE)    
        screen.blit(bg.image, bg.rect)
        screen.blit(player_car.image, player_car.rect)

        screen.blit(obstacle_car.image, obstacle_car.rect)

        scoretext = smallfont.render("Score = "+str(score), 1, (BLACK))
        screen.blit(scoretext, (5,10))

        velocitytext = smallfont.render("Velocity = "+str(vel), 1, (BLACK))
        screen.blit(velocitytext, (5,35))

        #Colission
        if player_car.rect.colliderect(obstacle_car):
            screen.blit(crashtext, (260, 360))
            screen.blit(anothergametext, (300, 460))
            pygame.display.update()
            
            pause = True
            while pause:
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        pause = False
                        running = False

                    if event.type == pygame.KEYDOWN:
                        score = 0
                        vel = 5

                        player_x = 360
                        player_y = 410
                        second_pos_y = player_y - 50

                        obstacle_x = random.randint(left_border, right_border)
                        obstacle_y = -250
                            
                        pause = False

        #Connect clock with fps
        clock.tick(fps)
        pygame.display.update()

if __name__ == "__main__":
    main()

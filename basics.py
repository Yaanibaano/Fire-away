import pygame
import random
import math
import enemies
from pygame import mixer

#initializing the game
pygame.init()


#constants
width = 800
height = 600 
count = 0
background = (135,206,236)
char_sizes = 76
font = pygame.font.Font("freesansbold.ttf",34)
game_over_font = pygame.font.Font("freesansbold.ttf",100)

def render_score():
    score = font.render("Score: "+ str(count),True,(0,0,0))
    screen.blit(score,(10,10))

def game_over():
    game_over - font.render("Game Over",True,(300,200))

#Game Window settings
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Basics")
icon = pygame.image.load("assets/moose.png")
pygame.display.set_icon(icon)

#Player
player_image = pygame.image.load("assets/military.png")
player_image = pygame.transform.scale(player_image,(char_sizes,char_sizes))
player_x,player_y = int(width/2-char_sizes/2),int(height-(char_sizes+30))
player_xchange = 0

def render_player(x,y):
    screen.blit(player_image,(x,y))
    
#Enemies
enemies_list = []

for i in range(6):
    enemy = enemies.Enemy()
    enemies_list.append(enemy)

def render_enemy(i,x,y):
    screen.blit(i.image,(x,y))

    
#Missiles
missile = pygame.image.load("assets/missile.png")
missile = pygame.transform.scale(missile,(40,40))
missile = pygame.transform.rotate(missile,(180))
missile_x = player_x
missile_y = player_y
missile_speed = 1
missile_status = "ready"

def fire_missile(x,y):
    global missile_status
    missile_status = "fire"
    screen.blit(missile,(x,y))


running = True

def ischecked(x,y,ex,ey):
    distance = math.sqrt(((x - ex)**2)+((y-ey)**2))
    if distance <= char_sizes:
        return True
    return False
        

while running:

    speed = 0.2
    screen.fill(background) 
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_xchange = -speed
            if event.key == pygame.K_d:
                player_xchange = speed
            if event.key == pygame.K_SPACE:
                if missile_status == "ready":
                    sound = mixer.Sound("assets/launch16.wav")
                    sound.play()
                    missile_x = player_x      
                    fire_missile(missile_x,missile_y)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_xchange = 0
    
    #Player Boundry conditions
    if player_x <= 0:
        player_x = 0
    elif player_x >= width-char_sizes:
        player_x = width-char_sizes
        
    #Enemy Boundry conditions    
    for i in enemies_list:
        render_enemy(i,i.x,i.y)
        i.set_boundry(width)
        collided = i.is_collided(missile_x,missile_y)
        i.change()
        if collided:
            sound = mixer.Sound("assets/explosion.wav")
            sound.play()
            i.reset()
            count += 1
            print(count)
            missile_x = player_x
            missile_y = player_y
            missile_status = "ready"
    
    #Missiles Boundry Condition
    if missile_y <= 0:
        missile_y = player_y
        missile_x = player_x
        missile_status = "ready"
        
    if missile_status == "fire":
        missile_y -= missile_speed
        fire_missile(missile_x,missile_y)
        
    
    player_x += player_xchange
    render_score()
    render_player(player_x,player_y)
    pygame.display.update()





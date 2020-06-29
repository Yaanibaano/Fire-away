import random
import pygame
import math

char_sizes = 76
width = 800

def getImage():
    enemy_image = pygame.image.load("assets/airplane.png")
    enemy_image = pygame.transform.scale(enemy_image,(char_sizes,char_sizes))
    enemy_image = pygame.transform.rotate(enemy_image,180)
    return enemy_image
    
class Enemy:
    
    def  __init__(self):
        self.image =  getImage()
        self.x = random.randint(0,int(800-char_sizes))
        self.y = enemy_y = random.randint(0,150)
        self.xchange = 0.2
        self.ychange = 30
    
    def set_boundry(self,width):
            if self.x <= 0:
                    self.xchange = 0.2
                    self.y += self.ychange 
            elif self.x >= width-char_sizes:
                    self.xchange = -0.2
                    self.y += self.ychange
    
    def reset(self):
         self.x = random.randint(0,int(width-char_sizes))
         self.y = enemy_y = random.randint(0,150)
    
    def is_collided(self,ex,ey):
        distance = math.sqrt(((self.x - ex)**2)+((self.y-ey)**2))
        if distance < char_sizes:
            return True
        
    def change(self):
        self.x += self.xchange
    
        
        
        
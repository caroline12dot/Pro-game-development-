import pygame
import random
import time
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((900,900))

def changebg(image):
    bg=pygame.image.load("venv//pro game development//images//"+image)
    bg=pygame.transform.scale(bg,(900,900))
    screen.blit(bg,(0,0))
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("venv//pro game development//images//bin.png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()
class Nonrecycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("venv//pro game development//images//plastic.png")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
class Recycle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load("venv//pro game development//images//"+img)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()
images=["bag.png","pencil.png","woodenbox.png"]
itemlist=pygame.sprite.Group()
allsprites=pygame.sprite.Group()
plasticlist=pygame.sprite.Group()
for i in range(40):
    item=Recycle(random.choice(images))
    item.rect.x=random.randrange(900)
    item.rect.y=random.randrange(900)
    itemlist.add(item)
    allsprites.add(item)
    
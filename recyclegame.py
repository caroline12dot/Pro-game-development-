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
for i in range(20):
    item=Nonrecycle()
    item.rect.x=random.randrange(900)
    item.rect.y=random.randrange(900)
    plasticlist.add(item)
    allsprites.add(item)
bin=Bin()
allsprites.add(bin)
score=0
clock=pygame.time.Clock()
starttime=time.time()
font=pygame.font.SysFont("Calibri",25)
text=font.render("score: "+str(score),True,"White")
while True:
    clock.tick(30)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    timeelapsed=time.time()-starttime
    if timeelapsed>=60:
        if score>25:
            text=font.render("Well Done",True,"Red")
            changebg("win.jpg")
        else:
            text=font.render("Well Tried",True,"Red")
            changebg("lose.jpg")
        screen.blit(text,(300,40))

    else:
        changebg("bground.png")
        countdown=font.render("timeleft: "+str(60-int(timeelapsed)),True,"White")
        screen.blit(countdown,(20,10))
        keys=pygame.key.get_pressed()
        if keys [pygame.K_w]:
            if bin.rect.y>0:
                bin.rect.y-=5
        if keys [pygame.K_s]:
            if bin.rect.y<830:
                bin.rect.y+=5
        if keys [pygame.K_a]:
            if bin.rect.x>0:
                bin.rect.x-=5
        if keys [pygame.K_d]:
            if bin.rect.x<830:
                bin.rect.x+=5
        itemhit=pygame.sprite.spritecollide(bin,itemlist,True)
        plastichit=pygame.sprite.spritecollide(bin,plasticlist,True)
        for i in itemhit:
            score+=5
            text=font.render("score="+str(score),True,"Red")
        for i in plastichit:
            score-=5
            text=font.render("score="+str(score),True,"Red")
        screen.blit(text,(20,50))
        allsprites.draw(screen)
    pygame.display.update()
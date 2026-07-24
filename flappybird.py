import pygame 
from pygame.locals import *
import random
pygame.init()
w=864
h=936
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("flappybird")
font=pygame.font.SysFont("Calibri",20)
clock=pygame.time.Clock()
fps=60
groundscroll=0
scrollspeed=4

bg=pygame.image.load("venv//pro game development//images//bg.png")
ground=pygame.image.load("venv//pro game development//images//ground.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(1,4):
            img=pygame.image.load(f"venv//pro game development//images//bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
    def update(self):
        self.counter+=1
        flap_pulldown=5
        if self.counter>flap_pulldown:
            self.counter=0
            self.index+=1
            if self.index>=len(self.images):
                self.index=0
        self.image=self.images[self.index]

birdgroup=pygame.sprite.Group()
flappy=Bird(100,int(h/2))
birdgroup.add(flappy)

run=True
while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    screen.blit(ground,(groundscroll,768))
    groundscroll-=scrollspeed
    if abs(groundscroll)>35:
        groundscroll=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()



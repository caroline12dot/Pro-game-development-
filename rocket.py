import pygame
from pygame.locals import *
from time import *
pygame.init()
screen=pygame.display.set_mode((600,600))
keys=[False,False,False,False]
rocket=pygame.image.load("venv//pro game development//rocket.png")
space=pygame.image.load("venv//pro game development//space.png")
rocketx=200
rockety=200
while rockety<600:
    screen.blit(space,(0,0))
    screen.blit(rocket,(rocketx,rockety))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            if i.key==K_w:
                keys[0]=True
            if i.key==K_s:
                keys[1]=True
            if i.key==K_a:
                keys[2]=True
            if i.key==K_d:
                keys[3]=True
        if i.type==pygame.KEYUP:
            if i.key==K_w:
                keys[0]=False
            if i.key==K_s:
                keys[1]=False
            if i.key==K_a:
                keys[2]=False
            if i.key==K_d:
                keys[3]=False
    if keys[0]:
        if rockety>0:
            rockety-=7
    elif keys[1]:
        if rockety<536:
            rockety+=7
    elif keys[2]:
        if rocketx>0:
            rocketx-=7
    elif keys[3]:
        if rocketx<536:
            rocketx+=7
    rockety+=5
    sleep(0.05)
print("GAMEOVER")
    
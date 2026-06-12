import pygame
from pygame.locals import *
from time import *
pygame.init()
screen=pygame.display.set_mode((600,600))
keys=[False,False,False,False]
balloon=pygame.image.load("venv//pro game development//hotairballoon.png")
sky=pygame.image.load("venv//pro game development//sky.png")
balloonx=200
balloony=200
while balloony<600:
    screen.blit(sky,(0,0))
    screen.blit(balloon,(balloonx,balloony))
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
        if balloony>0:
            balloony-=7
    elif keys[1]:
        if balloony<536:
            balloony+=7
    elif keys[2]:
        if balloonx>0:
            balloonx-=7
    elif keys[3]:
        if balloonx<536:
            balloonx+=7
    balloony+=5
    sleep(0.05)
print("GAMEOVER")
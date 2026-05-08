import pygame
pygame.init()
screen=pygame.display.set_mode((800,800))
run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    screen.fill("black")
    pygame.display.update()
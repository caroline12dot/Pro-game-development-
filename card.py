import pygame
import time
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Birthday card")
birth1=pygame.image.load("venv/pro game development/birthday1.png")
birth1img=pygame.transform.scale(birth1,(800,800))
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    screen.fill("blue")
    screen.blit(birth1img,(0,0))
    font=pygame.font.SysFont("arial",50)
    text=font.render("Happy birthday!!",True,"red")
    screen.blit(text,(350,20))
    pygame.display.update()
    time.sleep(2)
    birth2=pygame.image.load("venv/pro game development/birthday2.png")
    birth2img=pygame.transform.scale(birth2,(800,800))
    screen.fill("blue")
    screen.blit(birth2img,(0,0))
    text1=font.render("YAY ITS YOUR BIRTHDAY!!",True,"Black")
    screen.blit(text1,(150,20))
    pygame.display.update()
    time.sleep(2)
    birth3=pygame.image.load("venv/pro game development/birthday3.png")
    birth3img=pygame.transform.scale(birth3,(800,800))
    screen.fill("blue")
    screen.blit(birth3img,(0,0))
    pygame.display.update()
    time.sleep(2)
    
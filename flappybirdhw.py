import pygame

pygame.init()
screen=pygame.display.set_mode((1200,900))
screen.fill("pink")
font=pygame.font.SysFont("calibri",25)
tiktok=pygame.image.load("venv//pro game development//images//tiktok.png")
screen.blit(tiktok,(60,10))
text1=font.render("Tiktok",True,"blue")
screen.blit(text1,(300,390))
safari=pygame.image.load("venv//pro game development//images//safari.png")
screen.blit(safari,(60,190))
text2=font.render("Safari",True,"blue")
screen.blit(text2,(300,590))
mcdonalds=pygame.image.load("venv//pro game development//images//mcdonalds.png")
screen.blit(mcdonalds,(60,390))
text3=font.render("Mcdonalds",True,"blue")
screen.blit(text3,(300,10))
google=pygame.image.load("venv/pro game development/images/google.png")
screen.blit(google,(60,590))
text4=font.render("Google",True,"blue")
screen.blit(text4,(300,190))
pygame.display.update()
while True:
    event=pygame.event.poll()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
          pygame.quit()
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(screen,"pink",(pos),15)
        pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
        pos1=pygame.mouse.get_pos()
        pygame.draw.line(screen,"red",(pos),(pos1),5)
        pygame.draw.circle(screen,"purple",(pos1),15)
        pygame.display.update()
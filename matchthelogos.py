import pygame

pygame.init()
screen=pygame.display.set_mode((1200,900))
screen.fill("pink")
font=pygame.font.SysFont("calibri",25)
candy=pygame.image.load("venv//pro game development//images//candycrush.jpg")
screen.blit(candy,(60,10))
text1=font.render("Candy crush",True,"blue")
screen.blit(text1,(300,390))
templerun=pygame.image.load("venv/pro game development/images/templerun.png")
screen.blit(templerun,(60,190))
text2=font.render("TempleRun",True,"blue")
screen.blit(text2,(300,590))
subway=pygame.image.load("venv/pro game development/images/subwaysurfer.png")
screen.blit(subway,(60,390))
text3=font.render("SubwaySurfer",True,"blue")
screen.blit(text3,(300,10))
ludo=pygame.image.load("venv/pro game development/images/ludo.png")
screen.blit(ludo,(60,590))
text4=font.render("Ludo",True,"blue")
screen.blit(text4,(300,190))
pygame.display.update()
while True:
    event=pygame.event.poll()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(screen,"red",(pos),15)
        pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
        pos1=pygame.mouse.get_pos()
        pygame.draw.line(screen,"red",(pos),(pos1),5)
        pygame.draw.circle(screen,"red",(pos1),15)
        pygame.display.update()

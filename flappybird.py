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
flying=False
gameover=False
pipegap=150
pipefrequency=2500
lastpipe=pygame.time.get_ticks()-pipefrequency
score=0
passpipe=False
def draw_text(text, f, color, x, y):
    image=font.render(text, True, color)
    screen.blit(image,(x,y))



bg=pygame.image.load("venv//pro game development//images//bg.png")
ground=pygame.image.load("venv//pro game development//images//ground.png")
restart=pygame.image.load("venv//pro game development//images//restart.png")
def reset_game():
    pipegroup.empty()
    flappy.rect.x=100
    flappy.rect.y=int(h/2)
    score=0
    return score
class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def draw(self):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action=True
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

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
        self.velocity=0
        self.click=False

    def update(self):
        if flying==True:
            self.velocity+=0.5
            if self.velocity>8:
                self.velocity=8
            if self.rect.bottom<768:
                self.rect.y+=int(self.velocity)
        if gameover==False:
            if pygame.mouse.get_pressed()[0]==1 and self.click==False:
                self.click=True
                self.velocity=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.click=False
            
            self.counter+=1
            flap_pulldown=5
            if self.counter>flap_pulldown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
            self.image=self.images[self.index]
            self.image=pygame.transform.rotate(self.images[self.index],self.velocity*-2)
        else:
            self.image=pygame.transform.rotate(self.images[self.index],-90)
class Pipe(pygame.sprite.Sprite):
    def __init__ (self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("venv//pro game development//images//pipe.png")
        self.rect=self.image.get_rect()
        if position ==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipegap/2)]
        if position== -1:
            self.rect.topleft=[x,y+int(pipegap/2)]
    def update(self):
        self.rect.x-=scrollspeed
        if self.rect.right<0:
            self.kill()
pipegroup=pygame.sprite.Group()

birdgroup=pygame.sprite.Group()
flappy=Bird(100,int(h/2))
birdgroup.add(flappy)
button=Button(w//2-50,h//2-100,restart)

run=True
while run:
    clock.tick(fps)
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    birdgroup.update()
    pipegroup.draw(screen)
    screen.blit(ground,(groundscroll,768))
    if len(pipegroup)>0:
        if birdgroup.sprites()[0].rect.left>pipegroup.sprites()[0].rect.left and birdgroup.sprites()[0].rect.right<pipegroup.sprites()[0].rect.right and passpipe==False:
            passpipe=True
        if passpipe==True:
            if birdgroup.sprites()[0].rect.left>pipegroup.sprites()[0].rect.right:
                score+=1
                passpipe=False
    draw_text(str(score),font,"White",int(w/2),30)
    if pygame.sprite.groupcollide(birdgroup,pipegroup,False,False)or flappy.rect.top<0:
        gameover=True
    if flappy.rect.bottom>768:
        gameover=True
        flying=False
    if gameover==False and flying==True:
        timenow=pygame.time.get_ticks()
        if timenow-lastpipe>pipefrequency:
            pipeheight=random.randint(-100,100)
            bottompipe=Pipe(w,int(h/2)+pipeheight,-1)
            toppipe=Pipe(w,int(h/2)+pipeheight,1)
            pipegroup.add(bottompipe)
            pipegroup.add(toppipe)
            lastpipe=timenow
        pipegroup.update()
        groundscroll-=scrollspeed
        if abs(groundscroll)>35:
            groundscroll=0
    if gameover==True:
        if button.draw()==True:
            gameover=False
            score=reset_game()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and gameover==False:
            flying=True
    pygame.display.update()
    




import pygame

pygame.init()
w,h=900,500
screen=pygame.display.set_mode((w,h))
white="white"
black="black"
R="red"
B="black"
border=pygame.Rect(w//2-5,0,10,h)
font=pygame.font.SysFont("Calibri",20)
fps=60
velocity=5
bulletvelocity=7
maxbullets=3
ssw,ssh=55,40
blackufo=pygame.image.load("venv//pro game development//images//blackufo.png")
blkufo=pygame.transform.rotate(pygame.transform.scale(blackufo,(ssw,ssh)),90)
redufo=pygame.image.load("venv//pro game development//images//redufo.png")
rdufo=pygame.transform.rotate(pygame.transform.scale(redufo,(ssw,ssh)),270)
space=pygame.transform.scale(pygame.image.load("venv//pro game development//images//space3.png"),(w,h))
hitsound=pygame.mixer.Sound("venv//pro game development//Grenade+1.mp3")
firesound=pygame.mixer.Sound("venv/pro game development/Gun+Silencer.mp3")
blackhit=pygame.USEREVENT+1
redhit=pygame.USEREVENT+2
def draw(red,black,redbullets,blkbullets,redhealth,blkhealth):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,B,border)
    redhealthtxt=font.render("Health= "+str(redhealth),1,white)
    blkhealthtxt=font.render("Health= "+str(blkhealth),1,white)
    screen.blit(redhealthtxt,(w-redhealthtxt.get_width()-20,10))
    screen.blit(blkhealthtxt,(20,10))
    screen.blit(blkufo,(black.x,black.y))
    screen.blit(rdufo,(red.x,red.y))
    for i in redbullets:
        pygame.draw.rect(screen,R,i)
    for i in blkbullets:
        pygame.draw.rect(screen,B,i)
    pygame.display.update()

def blkmovement(keys_pressed,black):
    if keys_pressed[pygame.K_a]and black.x-velocity>0:
        black.x-=velocity
    if keys_pressed[pygame.K_d]and black.x+velocity+black.width<border.x:
        black.x+=velocity
    if keys_pressed[pygame.K_s]and black.y+velocity+black.height<h-15:
        black.y+=velocity
    if keys_pressed[pygame.K_w]and black.y-velocity>0:
        black.y-=velocity

def redmovement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]and red.x-velocity>border.x+border.width:
        red.x-=velocity
    if keys_pressed[pygame.K_RIGHT]and red.x+velocity+red.width<w:
        red.x+=velocity
    if keys_pressed[pygame.K_UP]and red.y-velocity>0:
        red.y-=velocity
    if keys_pressed[pygame.K_DOWN]and red.y+velocity+red.height<h-15:
        red.y+=velocity

def bullets(blkbullets,redbullets,black,red):
    for i in blkbullets:
        i.x+=bulletvelocity
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(redhit))
            blkbullets.remove(i)
        elif i.x>w:
            blkbullets.remove(i)
    for i in redbullets:
        i.x-=bulletvelocity
        if black.colliderect(i):
            pygame.event.post(pygame.event.Event(blackhit))
            redbullets.remove(i)
        elif i.x<0:
            redbullets.remove(i)
    

red=pygame.Rect(700,300,ssw,ssh)
black=pygame.Rect(100,300,ssw,ssh)
redbullets=[]
blkbullets=[]
redhealth=10
blkhealth=10
clock=pygame.time.Clock()
run=True
while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE and len(blkbullets)<maxbullets:
                bullet=pygame.Rect(black.x+black.width,black.y+black.height//2-2,10,5)
                blkbullets.append(bullet)
            if i.key==pygame.K_LSHIFT and len(redbullets)<maxbullets:
                bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                redbullets.append(bullet)
    draw(red,black,redbullets,blkbullets,redhealth,blkhealth)
    keys_pressed=pygame.key.get_pressed()
    blkmovement(keys_pressed,black)
    redmovement(keys_pressed,red)
    bullets(blkbullets,redbullets,black,red)

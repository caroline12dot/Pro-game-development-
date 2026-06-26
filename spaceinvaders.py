import pygame

pygame.init()
w,h=900,500
screen=pygame.display.set_mode((w,h))
white="white"
black="black"
R="red"
Y="yellow"
border=pygame.Rect(w//2-5,0,10,h)
font=pygame.font.SysFont("Calibri",20)
fps=60
velocity=5
bulletvelocity=7
maxbullets=3
ssw,ssh=55,40
yellowspaceship=pygame.image.load("venv//pro game development//images//spaceship_yellow.png")
yellowss=pygame.transform.rotate(pygame.transform.scale(yellowspaceship,(ssw,ssh)),90)
redspaceship=pygame.image.load("venv//pro game development//images//spaceship_red.png")
redss=pygame.transform.rotate(pygame.transform.scale(redspaceship,(ssw,ssh)),270)
space=pygame.transform.scale(pygame.image.load("venv//pro game development//images//space1.png"),(w,h))
hitsound=pygame.mixer.Sound("venv//pro game development//Grenade+1.mp3")
firesound=pygame.mixer.Sound("venv/pro game development/Gun+Silencer.mp3")
yellowhit=pygame.USEREVENT+1
redhit=pygame.USEREVENT+2
def draw(red,yellow,redbullets,yellowbullets,redhealth,yellowhealth):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,black,border)
    redhealthtxt=font.render("Health= "+str(redhealth),1,white)
    yellowhealthtxt=font.render("Health= "+str(yellowhealth),1,white)
    screen.blit(redhealthtxt,(w-redhealthtxt.get_width()-20,10))
    screen.blit(yellowhealthtxt,(20,10))
    screen.blit(yellowss,(yellow.x,yellow.y))
    screen.blit(redss,(red.x,red.y))
    for i in redbullets:
        pygame.draw.rect(screen,R,i)
    for i in yellowbullets:
        pygame.draw.rect(screen,Y,i)
    pygame.display.update()

def yellowmovement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]and yellow.x-velocity>0:
        yellow.x-=velocity
    if keys_pressed[pygame.K_d]and yellow.x+velocity+yellow.width<border.x:
        yellow.x+=velocity
    if keys_pressed[pygame.K_s]and yellow.y+velocity+yellow.height<h-15:
        yellow.y+=velocity
    if keys_pressed[pygame.K_w]and yellow.y-velocity>0:
        yellow.y-=velocity

def redmovement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]and red.x-velocity>border.x+border.width:
        red.x-=velocity
    if keys_pressed[pygame.K_RIGHT]and red.x+velocity+red.width<w:
        red.x+=velocity
    if keys_pressed[pygame.K_UP]and red.y-velocity>0:
        red.y-=velocity
    if keys_pressed[pygame.K_DOWN]and red.y+velocity+red.height<h-15:
        red.y+=velocity

def winner(text):
    t=font.render(text,1,white)
    screen.blit(t,(w/2-t.get_width()/2,h/2-t.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
     

def bullets(yellowbullets,redbullets,yellow,red):
    for i in yellowbullets:
        i.x+=bulletvelocity
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(redhit))
            yellowbullets.remove(i)
        elif i.x>w:
            yellowbullets.remove(i)
    for i in redbullets:
        i.x-=bulletvelocity
        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event(yellowhit))
            redbullets.remove(i)
        elif i.x<0:
            redbullets.remove(i)
    

red=pygame.Rect(700,300,ssw,ssh)
yellow=pygame.Rect(100,300,ssw,ssh)
redbullets=[]
yellowbullets=[]
redhealth=10
yellowhealth=10
clock=pygame.time.Clock()
run=True
while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE and len(yellowbullets)<maxbullets:
                bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                yellowbullets.append(bullet)
                firesound.play()
    
            if i.key==pygame.K_LSHIFT and len(redbullets)<maxbullets:
                bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                redbullets.append(bullet)
                firesound.play()
        if i.type==redhit:
            redhealth-=1
            hitsound.play()
        if i.type==yellowhit:
            yellowhealth-=1
            hitsound.play()
    winnertext=""
    
    if redhealth<=0:
        winnertext="Yellow wins"
    if yellowhealth<=0:
        winnertext="Red wins"
    if winnertext !="":
        winner(winnertext)
        break

    draw(red,yellow,redbullets,yellowbullets,redhealth,yellowhealth)
    keys_pressed=pygame.key.get_pressed()
    yellowmovement(keys_pressed,yellow)
    redmovement(keys_pressed,red)
    bullets(yellowbullets,redbullets,yellow,red)


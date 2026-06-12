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
    screen.blit(yellowss,(yellow.x,yellow.y))
    screen.blit(redss,(red.x,red.y))
    pygame.display.update()
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
    draw(red,yellow,redbullets,yellowbullets,redhealth,yellowhealth)

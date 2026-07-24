import pygame 
pygame.init()
screen=pygame.display.set_mode((600,600))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("venv//pro game development//images//redufo.png")
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()
    def update(self,keyspressed):
        if keyspressed[pygame.K_UP]:
            self.rect.y-=5
        if keyspressed[pygame.K_DOWN]:
            self.rect.y+=5
        if keyspressed[pygame.K_RIGHT]:
            self.rect.x+=5
        if keyspressed[pygame.K_LEFT]:
            self.rect.x-=5
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>600:
            self.rect.right=600
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>600:
            self.rect.bottom=600
group1=pygame.sprite.Group()
ufo=Player()
group1.add(ufo)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    keyspressed=pygame.key.get_pressed()
    ufo.update(keyspressed)
    screen.blit(pygame.image.load("venv//pro game development//images//space1.png"),(0,0))
    group1.draw(screen)
    pygame.display.update()
import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("White")
class Rectangle:
    def  __init__(self,color,x,y,width,height):
        self.screen=screen
        self.x=x
        self.y=y
        self.w=width
        self.h=height
        self.c=color
    def draw(self):
        pygame.draw.rect(self.screen,self.c,(self.x,self.y,self.w,self.h))
    def growrectangle(self,x):
        self.h+=x
        self.w+=x
        pygame.draw.rect(self.screen,self.c,(self.x,self.y,self.w,self.h))
object1=Rectangle("red",300,300,90,5)
object2=Rectangle("blue",459,298,110,5)
object3=Rectangle("green",250,398,140,5)
object4=Rectangle("orange",189,470,170,5)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            object1.draw()
            object2.draw()
            object3.draw()
            object4.draw()
        elif i.type==pygame.MOUSEBUTTONUP:
            object1.growrectangle(5)
            object2.growrectangle(5)
            object3.growrectangle(5)
            object4.growrectangle(5)
        pygame.display.update()
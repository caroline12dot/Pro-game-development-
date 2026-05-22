import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("White")
class Circle:
    def  __init__(self,color,position,radius,width):
        self.screen=screen
        self.c=color
        self.pos=position
        self.r=radius
        self.w=width
    def draw(self):
        pygame.draw.circle(self.screen,self.c,self.pos,self.r,self.w)
    def growcircle(self,x):
        self.r+=x
        pygame.draw.circle(self.screen,self.c,self.pos,self.r,self.w)
object1=Circle("red",(300,300),90,5)
object2=Circle("blue",(300,300),110,5)
object3=Circle("orange",(300,300),140,5)
object4=Circle("green",(300,300),170,5)
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
            object1.growcircle(5)
            object2.growcircle(5)
            object3.growcircle(5)
            object4.growcircle(5)
        elif i.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            smallcircle=Circle("black",pos,10,0)
            smallcircle.draw()
        pygame.display.update()
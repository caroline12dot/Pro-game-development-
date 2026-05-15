import pgzrun

WIDTH=1200
HEIGHT=800
GRAVITY=2000.0
class Ball():
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.vx=200
        self.vy=0
        self.radius=r
    def circle(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,"red")
    
object=Ball(600,400,190)
object1=Ball(890,200,95)

def draw():
    screen.clear()
    object.circle()
    object1.circle()
def update(dt):
    uy=object.vy
    object.vy+=GRAVITY*dt
    object.y+=(uy+object.vy)*0.5*dt
    if object.y>HEIGHT-190:
        object.y=HEIGHT-190
        object.vy=-object.vy*0.9
    object.x+=object.vx*dt
    if object.x>WIDTH-190 or object.x<190:
        object.vx=-object.vx
    uy=object1.vy
    object1.vy+=GRAVITY*dt
    object1.y+=(uy+object1.vy)*0.5*dt
    if object1.y>HEIGHT-95:
        object1.y=HEIGHT-95
        object1.vy=-object1.vy*0.9
    object1.x+=object1.vx*dt
    if object1.x>WIDTH-95 or object1.x<95:
        object1.vx=-object1.vx
def on_key_down(key):
    if key==keys.SPACE:
        object.vy=-500
    if key==keys.S:
        object1.vy=-500
pgzrun.go()
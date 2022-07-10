import param
from modules.mygeometry import *
from modules.par import *
from modules.page2 import *

class Button:
    def __init__(self,name,x,y,surface,w,h,pr):

        self.name = name
        self.x = x
        self.y = y
        self.surface = surface
        self.width = w
        self.height= h
        self.pr = pr
        self.selected = False
        self.clicked  = False
        self.hover = False

    def border(self,colore):
        pygame.draw.rect(self.surface,colore,(self.x,self.y,self.width,self.height),self.pr.r1(6))

    def area(self,colore):
        self.myriquadro = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
        self.myriquadro.fill(colore)
        self.surface.blit(self.myriquadro,(self.x,self.y))

    def text(self,colore):

        font = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_NORM"])
        part = font.render(self.name,True,colore)
        delta = font.size(self.name)
        self.surface.blit(part,(self.x + 0.5*self.width - 0.5*delta[0],self.y + 0.5*self.height - 0.5*delta[1]))

    def shift_click(self,myclick):
        return myclick^self.clicked

    def shift_hover(self,myhover):
        return myhover^self.hover

    def shift_select(self,myselect):
        return myselect^self.selected

    def inside(self,x,y):
        return (x > self.x) and (x < (self.x + self.width)) and (y > self.y) and (y < (self.y + self.height))

    def run(self):
        if self.selected:
            self.area(red2)
        else:
            self.area(grey)

        if self.hover:
            self.text(white)
        else:
            self.text(black)
            
        if self.clicked:
            self.border(dgreen)
        else:
            self.border(grey)
            
            




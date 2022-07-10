from modules.mygeometry import *
from modules.par import *
from modules.media import *


class Description:
    def __init__(self,surface,pr):
        self.surface = surface
        self.pr = pr

    def description_blit(self,stringa,i,color):

        x = self.pr.r1(80)
        width = self.pr.r1(750)
        show_d = Plain_hf(x , self.pr.r1(250 + i*200),width,self.surface,color,True,grey,False)
        show_d.write(stringa,self.pr.p["FONT_NORM"],black)

    def display_title(self):
        title = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_BIG"]).render(d.str_page_1[4],True,white)
        self.surface.blit(title,(self.pr.r1(640),self.pr.r1(10)))

    def display_footnote(self):
        commands = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_NORM"]).render(d.str_page_1[3],True,white)
        self.surface.blit(commands,(self.pr.r1(440),self.pr.r1(975)))

    def section(self):
        self.title = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_BIG"]).render(d.str_page_1[5],True,blue)
        self.surface.blit(self.title,(self.pr.r1(80) , self.pr.r1(110)))

    def body(self):

        image1 = pygame.transform.scale(pygame.image.load(d.images[4]), (self.pr.r1(675), self.pr.r1(813)))
        self.surface.blit(image1, [self.pr.r1(940), self.pr.r1(100)])

        self.description_blit(d.str_page_1[0],0,orange)
        self.description_blit(d.str_page_1[1],1,red)
        self.description_blit(d.str_page_1[2],2,purple)

    def write(self):

        self.section()
        self.body()
        self.display_title()
        self.display_footnote()




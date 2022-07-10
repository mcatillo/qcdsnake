import param
from modules.mygeometry import *
from modules.par import *
from modules.media import *


class Howto:
    def __init__(self,surface,pr):
        self.surface = surface
        self.pr = pr
        self.xl = self.pr.r1(80)
        self.xr = self.pr.r1(900)
        self.width = self.pr.r1(720)

    def howto_blit(self,stringa,i,color):

        x = self.pr.r1(80)
        width = self.pr.r1(750)
        show_h = Plain_hf(x , self.pr.r1(160 + i*200),width,self.surface,color,True,grey,False)
        show_h.write(stringa,self.pr.p["FONT_NORM"],black)

    def display_title(self):
        font = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_BIG"])
        title = font.render(d.str_page_2[2],True,white)
        self.surface.blit(title,(self.pr.r1(640),self.pr.r1(10)))

    def display_footnote(self):

        commands = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_NORM"]).render(d.str_page_2[0],True,white)
        self.surface.blit(commands,(self.pr.r1(240),self.pr.r1(975)))

    def section(self):
        font = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_BIG"])
        self.title = font.render(d.str_page_2[3],True,blue)
        self.surface.blit(self.title,(self.pr.r1(80) , self.pr.r1(110)))

    def note1(self):

        show_h = Plain_hf(self.xl , self.pr.r1(440),self.width,self.surface,orange,True,grey,False)
        show_h.write(d.str_page_2[1],self.pr.p["FONT_NORM"],black)

    def note2(self):

        show_h = Plain_hf(self.xl , self.pr.r1(80),self.width,self.surface,red,False,grey,False)
        show_h.write(d.str_page_2[5],self.pr.p["FONT_LARGE"],blue)

    def note3(self):
        show_h = Plain_hf(self.xr -self.pr.r1(60), self.pr.r1(400),self.pr.r1(380),self.surface,purple,False,grey,False)
        show_h.write(d.str_page_2[6],self.pr.p["FONT_LARGE"],black)

        show_h = Plain_hf(self.xr  -self.pr.r1(60), self.pr.r1(720),self.pr.r1(340),self.surface,purple,False,grey,False)
        show_h.write(d.str_page_2[8],self.pr.p["FONT_LARGE"],black)

        show_h = Plain_hf(self.xr  -self.pr.r1(60), self.pr.r1(80),self.width,self.surface,purple,False,grey,False)
        show_h.write(d.str_page_2[9],self.pr.p["FONT_LARGE"],blue)

    def img1(self):
        image1 = pygame.image.load(d.images[2])
        image1 = pygame.transform.scale(image1, (self.pr.r1(728), self.pr.r1(315)))

        self.surface.blit(image1, [self.xl, self.pr.r1(580)])
        str_title = Plain_hf(self.xl+self.pr.r1(460),self.pr.r1(580),self.pr.r1(250),self.surface,red,False,white,False)
        str_title.write(d.str_page_2[10],self.pr.p["FONT_NORM"],black)

    def img2(self):
        image2 = pygame.image.load(d.images[5])
        image2 = pygame.transform.scale(image2, (self.pr.r1(654), self.pr.r1(226)))
        self.surface.blit(image2, [self.xl, self.pr.r1(180)])

    def img3(self):
        image3 = pygame.image.load(d.images[6])
        image3 = pygame.transform.scale(image3, (self.pr.r1(272), self.pr.r1(429)))
        self.surface.blit(image3, [self.xr + self.pr.r1(360), self.pr.r1(180)])

    def img4(self):
        image4 = pygame.image.load(d.images[7])
        image4 = pygame.transform.scale(image4, (self.pr.r1(428), self.pr.r1(217)))
        self.surface.blit(image4, [self.xr + self.pr.r1(280), self.pr.r1(700)])

    def write(self):
        self.img2()
        self.img3()
        self.img4()
        self.img1()
        self.note1()
        self.note2()
        self.note3()
        self.display_title()
        self.display_footnote()
        
class SetupParam:
    def __init__(self,surface,pr):
        self.pr = pr
        self.ybase = self.pr.r1(50)
        self.surface = surface
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.str_title = ""
        self.myfont = self.pr.p["FONT_NORM"]
    
    def group_title(self):
        pyfont = pygame.font.SysFont(FONT_STYLE,self.myfont)

        self.x = self.pr.r1(1640)
        self.y = self.ybase 
        self.w = self.pr.r1(280)
        self.h = self.pr.r1(pyfont.size(self.str_title)[1]) + 2*self.pr.r1(self.pr.p["FONT_NORM"])

        self.ybase = self.y + self.h
    
    def groupsection(self):
        self.myfont = self.pr.p["FONT_LARGE"]
        self.str_title = d.str_button_3[0]
        self.group_title()
        return (Plain_hf(self.x,self.y,self.w,self.surface,red,False,green,False),self.str_title,self.myfont,white)
        
    def groupbutton0(self):
        self.myfont = self.pr.p["FONT_NORM"]
        self.str_title = d.str_button_3[1]
        self.group_title()
        return (Plain_hf(self.x,self.y,self.w,self.surface,red,False,green,False),self.str_title,self.myfont,white)
    
    def groupbutton1(self):
        self.myfont = self.pr.p["FONT_NORM"]
        self.str_title = d.str_button_3[2]
        self.group_title()
        return (Plain_hf(self.x,self.y,self.w,self.surface,red,False,green,False),self.str_title,self.myfont,white)
        
    def groupbutton2(self):
        self.myfont = self.pr.p["FONT_NORM"]
        self.str_title = d.str_button_3[3]
        self.group_title()
        return (Plain_hf(self.x,self.y,self.w,self.surface,red,False,green,False),self.str_title,self.myfont,white)
        
    def groupbutton3(self):
        self.myfont = self.pr.p["FONT_NORM"]
        self.str_title = d.str_button_3[4]
        self.group_title()
        return (Plain_hf(self.x,self.y,self.w,self.surface,red,False,green,False),self.str_title,self.myfont,white)

        




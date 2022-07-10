#   Welcome to the QCD-Snake! by Marco Catillo (Zurich, 2022)

from modules.buttons import *
from modules.par import *
from modules.mygeometry import *
from modules.setparam import *
from modules.media import *

class GroupButtons:
    def __init__(self,bot,setup,surface,titles_buttons,pr):
        self.bot = bot
        self.setup = setup
        self.surface = surface
        self.titles_buttons = titles_buttons
        self.pr = pr

    def groupbutton0(self):
        self.titles_buttons.append(self.setup.groupsection())
        self.titles_buttons.append(self.setup.groupbutton0())

        text_buttons = ["Up","Down","Charm","Strange","Top","Bottom"]
        num_buttons = len(text_buttons)
        for j in range(MAX_j[0]):
            for i in range(MAX_i[0]):
                k = i + j*MAX_i[0]
                x = self.pr.r1(1660+125*i)
                y = self.pr.r1(3) + self.setup.ybase
                w = self.pr.r1(114)
                h = self.pr.r1(40)
                self.bot.append(Button(text_buttons[k],x,y,self.surface,w,h,self.pr))
            self.setup.ybase = y + h

    def groupbutton1(self):
        self.titles_buttons.append(self.setup.groupbutton1())

        text_buttons = ["5","10","15","20"]
        for j in range(MAX_j[1]):
            for i in range(MAX_i[1]):
                k = i + j*MAX_i[1]
                x = self.pr.r1(1660 + 125*i)
                y = self.pr.r1(3) + self.setup.ybase
                w = self.pr.r1(114)
                h = self.pr.r1(40)
                self.bot.append(Button(text_buttons[k],x,y,self.surface,w,h,self.pr))
            self.setup.ybase = y + h

    def groupbutton2(self):
        self.titles_buttons.append(self.setup.groupbutton2())

        text_buttons = [d.str_button_3[5],d.str_button_3[6],d.str_button_3[7]]
        i = 0
        for j in range(MAX_j[2]):
            k = j
            x = self.pr.r1(1660)
            y = self.pr.r1(3) + self.setup.ybase
            w = self.pr.r1(228)
            h = self.pr.r1(40)
            self.bot.append(Button(text_buttons[k],x,y,self.surface,w,h,self.pr))
            self.setup.ybase = y + h

    def groupbutton3(self):
        self.titles_buttons.append(self.setup.groupbutton3())

        text_buttons = ["0.07","0.08","0.09","0.10"]
        for j in range(MAX_j[3]):#column
            for i in range(MAX_i[3]): #row
                k = i + j*MAX_i[3]
                x = self.pr.r1(1660 + 125*i)
                y = self.pr.r1(3) + self.setup.ybase
                w = self.pr.r1(114)
                h = self.pr.r1(40)
                self.bot.append(Button(text_buttons[k],x,y,self.surface,w,h,self.pr))
            self.setup.ybase = y + h

    def buttonenter(self):
        x = self.pr.r1(1665)
        y =  self.setup.ybase + self.pr.r1(40)
        w = self.pr.r1(228)
        h = self.pr.r1(40)
        self.bot.append(Button(d.str_button_3[8],x,y,self.surface,w,h,self.pr))
        self.setup.ybase = y + h

    def buttonexit(self):
        x = self.pr.r1(1665)
        y = self.setup.ybase + self.pr.r1(10)
        w = self.pr.r1(228)
        h = self.pr.r1(40)
        self.bot.append(Button(d.str_button_3[9],x,y,self.surface,w,h,self.pr))


    def writeallbuttons(self):
        self.groupbutton0()
        self.groupbutton1()
        self.groupbutton2()
        self.groupbutton3()
        self.buttonenter()
        self.buttonexit()

class MovethroughButtons:
    def __init__(self,si,sj,sz,titles_buttons):
        self.si = si
        self.sj = sj
        self.sz = sz
        self.titles_buttons = titles_buttons
        self.sk = self.si + self.sj*MAX_j[self.sz] + 17

    def define_buttons(self,bot,setup,surface,pr):
        self.bot = bot
        self.setup = setup
        self.surface = surface
        self.pr = pr
        g = GroupButtons(self.bot,self.setup,self.surface,self.titles_buttons,self.pr)
        g.writeallbuttons()
        setBUTTONS(self.bot)
        self.bot[self.sk].selected = True

    def cond(self,x,y,e):
        return (x and e)^(y and (not e))

    def buttons_logic(self,e):
        for i in range(6):
            if self.cond(self.bot[i].hover,self.bot[i].selected,e):
                self.bot[i].clicked = self.bot[i].clicked^True
                count = 0
                for j in range(6):
                    if self.bot[j].clicked:
                        count += 1
                if count == 0:
                    self.bot[i].clicked = True
                else:
                    setNUM_FLAVOR(self.bot[i])
        for i in range(6,10):
            if self.cond(self.bot[i].hover,self.bot[i].selected,e):
                for j in range(6,10):
                    self.bot[j].clicked = False
                self.bot[i].clicked = True
                setNUM_APPLES(self.bot[i])
        for i in range(10,13):
            if self.cond(self.bot[i].hover,self.bot[i].selected,e):
                for j in range(10,13):
                    self.bot[j].clicked = False
                self.bot[i].clicked = True
                setPARITY(self.bot[i])

        for i in range(13,17):
            if self.cond(self.bot[i].hover,self.bot[i].selected,e):
                for j in range(13,17):
                    self.bot[j].clicked = False
                self.bot[i].clicked =  True
                setSPEED(self.bot[i])
        if self.cond(self.bot[17].hover,self.bot[17].selected,e):
            #self.restart()
            return (1,0)
        if self.cond(self.bot[18].hover,self.bot[18].selected,e):
            #self.running = False
            return (0,1)
        return (0,0)

    def select_button(self,event,pos):
        for i in range(len(self.bot)):
            if  self.bot[i].inside(pos[0],pos[1]):
                self.bot[i].hover = True
            else:
                self.bot[i].hover = False

        if pygame.mouse.get_pressed()[0]:
            if event.type == MOUSEBUTTONDOWN:
                return self.buttons_logic(True)

        if event.type == KEYDOWN:
            K_directions = K_UP or K_DOWN or K_RIGHT or K_LEFT

            if K_directions:
                if event.key == K_UP:
                    self.sj -= 1
                    if(self.sj<0):
                        self.sz = (self.sz-1)%MAX_z
                        self.si = 0
                        self.sj = MAX_j[self.sz] - 1

                elif event.key == K_DOWN:
                    self.sj += 1
                    if(self.sj>=MAX_j[self.sz]):
                        self.sz = (self.sz+1)%MAX_z
                        self.si = 0
                        self.sj = 0

                elif event.key == K_RIGHT:
                    self.si += 1
                    if(self.si>=MAX_i[self.sz]):
                        self.si = 0

                elif event.key == K_LEFT:
                    self.si -= 1
                    if(self.si<0):
                        self.si = MAX_i[self.sz] -1
                Z = 0
                for z in range(self.sz):
                    Z += MAX_i[z]*MAX_j[z]

                k = self.si + self.sj*MAX_i[self.sz] + Z
                for s in range(NUM_BUTTONS):
                    self.bot[s].selected = False
                self.bot[k].selected = True

                if event.key == K_RETURN:
                    return self.buttons_logic(False)
        return (0,0)

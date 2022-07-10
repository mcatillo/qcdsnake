#import pygame
import random
from pygame.locals import *
import json
import itertools
from modules.media import *
from modules.mygeometry import *
from modules.par import *
from modules.setparam import *


class MapToQuark:
    def __init__(self):
        pass
    def maptoflavor(self,flavor_content):

        i_max = len(flavor_content)
        lett = ""
        for i in range(i_max):
            if(flavor_content[i] == 1):
                lett += 'u'
            if(flavor_content[i] == 2):
                lett += 'd'
            if(flavor_content[i] == 3):
                lett += 's'
            if(flavor_content[i] == 4):
                lett += 'c'
            if(flavor_content[i] == 5):
                lett += 'b'
            if(flavor_content[i] == 6):
                lett += 't'
        return lett

    def maptocolor(self,color):
        i_max = len(color)
        my_col  = white
        for i in range(i_max):
            if(color[i] == 1):
                my_col = red
            if(color[i] == 2):
                my_col = green
            if(color[i] == 3):
                my_col = blue
        return my_col

class Blocco:
    def __init__(self,x,y,ind,color,flavor,parity,type_particle,evidence):
        self.ind = ind
        self.color = color
        self.flavor = flavor
        self.parity = parity
        self.x = x
        self.y = y
        self.type_particle = type_particle
        self.evidence = evidence

    def head(self,screen,direction):

        surf = pygame.Surface((pr.p["SIZE"],pr.p["SIZE"]),pygame.SRCALPHA)
        pygame.draw.circle(surf, (0,0,0),[0.5*pr.p["SIZE"], 0.5*pr.p["SIZE"]], 0.5*pr.p["SIZE"],pr.r1(5))
        pygame.draw.circle(surf, (0,0,0),[0.5*pr.p["SIZE"], 0.5*pr.p["SIZE"]], 0.125*pr.p["SIZE"],0)
        screen.blit(surf,(self.x,self.y))

    def circles(self,surf):
        if(self.type_particle == 'quark'):
            font = pygame.font.SysFont(FONT_STYLE,pr.p["FONT_LARGE"])
            mapquark = MapToQuark()
            lett = mapquark.maptoflavor((self.flavor,))
            colore_back = mapquark.maptocolor((self.color,))
            if(self.parity == 0):
                colore_lett = white
            if(self.parity == 1):
                colore_lett = black
            pygame.draw.circle(surf, colore_back,[0.5*pr.p["SIZE"], 0.5*pr.p["SIZE"]], 0.5*pr.p["SIZE"],0)
            pygame.draw.circle(surf, black,[0.5*pr.p["SIZE"], 0.5*pr.p["SIZE"]], 0.5*pr.p["SIZE"],2)
            self.line1 = font.render(lett,True,colore_lett)
            surf.blit(self.line1,(pr.p["CENTER_BALL_X"],pr.p["CENTER_BALL_Y"]))

        else:
            font = pygame.font.SysFont(FONT_STYLE,pr.p["FONT_LARGE"])
            if(self.parity == 0):
                colore_lett = white
                colore_back = black
                pygame.draw.circle(surf, colore_back,[0.5*pr.p["SIZE"], 0.5*pr.p["SIZE"]], 0.5*pr.p["SIZE"],0)
            if(self.parity == 1):
                colore_lett = black
                colore_back = black
                pygame.draw.circle(surf, colore_back,[0.5*pr.p["SIZE"], 0.5*pr.p["SIZE"]], 0.5*pr.p["SIZE"],3)

            if(self.type_particle == 'baryons'):
                lett = "B"
                self.line1 = font.render(lett,True,colore_lett)
                surf.blit(self.line1,(pr.p["CENTER_B_X"],pr.p["CENTER_B_Y"]))
            elif(self.type_particle == 'mesons'):
                lett = "M"
                self.line1 = font.render(lett,True,colore_lett)
                surf.blit(self.line1,(pr.p["CENTER_M_X"],pr.p["CENTER_M_Y"]))

    def draw(self,parent_screen):

        surf = pygame.Surface((pr.p["SIZE"],pr.p["SIZE"]),pygame.SRCALPHA)
        self.circles(surf)
        parent_screen.blit(surf,(self.x,self.y))

class Apple:
    def __init__(self,parent_screen):

        self.parent_screen = parent_screen
        self.rando = random.randint(0,len(param.NUM_FLAVOR)-1)
        self.rand_flavor = param.NUM_FLAVOR[self.rando]
        self.rand_color = random.randint(1,NUM_COLORS)
        self.rand_pa = random.randint(param.PARITY[0],param.PARITY[1])
        self.x = pr.p["SHIFT_X"] + (random.randint(0,(((pr.p["GAME_SIZE_X"])/pr.p["SIZE"]) - 1))*pr.p["SIZE"])
        self.y = pr.p["SHIFT_Y"] + (random.randint(0,(((pr.p["GAME_SIZE_Y"])/pr.p["SIZE"]) - 1))*pr.p["SIZE"])

    def draw(self):
        self.random_apple = Blocco(self.x,self.y,-1,self.rand_color,self.rand_flavor,self.rand_pa,'quark',4)
        self.random_apple.draw(self.parent_screen)

    def move(self):
        self.rando = random.randint(0,len(param.NUM_FLAVOR)-1)
        self.rand_flavor = param.NUM_FLAVOR[self.rando]
        self.rand_color = random.randint(1,NUM_COLORS)
        self.rand_pa = random.randint(param.PARITY[0],param.PARITY[1])
        self.x = pr.p["SHIFT_X"] + (random.randint(0,(((pr.p["GAME_SIZE_X"])/pr.p["SIZE"]) - 1)))*pr.p["SIZE"]
        self.y = pr.p["SHIFT_Y"] + (random.randint(0,(((pr.p["GAME_SIZE_Y"])/pr.p["SIZE"]) - 1)))*pr.p["SIZE"]

class InfoSnake:
    def __init__(self,name,mass,symbol,parity,quarks,flavor,hadron,evidence):
        self.name = name
        self.mass = mass
        self.symbol = symbol
        self.parity = parity
        self.quarks = quarks
        self.flavor = flavor
        self.hadron = hadron
        self.evidence = evidence

class FindHadrons:
    def __init__(self,myblock,length,parent_screen):

        self.ihadron = InfoSnake([0],[0],[0],0,0,0,0,4)
        self.parent_screen = parent_screen
        self.mynewblock = myblock
        self.length = len(self.mynewblock)
        self.lengthbaryon = length[1]
        self.lengthmeson  = length[2]
        self.length_effective = self.length - self.lengthbaryon - self.lengthmeson

    def evaluate(self,myblock,hadron_type):

        #f = open(PATH_JSON+HADRON,'r')
        #datahadron = json.load(f)

        if(hadron_type == "mesons"):
            flavor_content = (myblock[1].flavor,myblock[2].flavor)
            if(myblock[1].flavor<myblock[2].flavor):
                parity_content = int(str(myblock[1].parity)+str(myblock[2].parity)) >> 3
            else:
                #flavor_content = (myblock[2].flavor,myblock[1].flavor)
                parity_content = int(str(myblock[2].parity)+str(myblock[1].parity)) >> 3
        if(hadron_type == "baryons"):
            flavor_content = (myblock[1].flavor,myblock[2].flavor,myblock[3].flavor)
            parity_content = myblock[1].parity

        found = 0
        count = 1
        all_hadrons = len(d.datahadron['hadrons'][hadron_type])
        while((found!=1) and (count<=all_hadrons)):
            j = str(count)
            perm = list(itertools.permutations(d.datahadron['hadrons'][hadron_type][j]['combination']))
            i_max = len(perm)
            i=0
            while((found == 0) and (i<i_max)):
                if(flavor_content == perm[i]):
                    found = 1
                i += 1
            count+=1

        string_content = MapToQuark()
        n = d.datahadron['hadrons'][hadron_type][j]['particle'][parity_content]['name']
        m = d.datahadron['hadrons'][hadron_type][j]['masses']
        s = d.datahadron['hadrons'][hadron_type][j]['particle'][parity_content]['latex']
        p = parity_content
        q = string_content.maptoflavor(flavor_content)
        f = flavor_content
        h = hadron_type
        e = d.datahadron['hadrons'][hadron_type][j]['particle'][parity_content]['evidence']
        if(found == 1):
            self.ihadron = InfoSnake(n,m,s,p,q,f,h,e)
            print(""+str(self.ihadron.symbol[0])
                    +" ("+str(self.ihadron.name[0])+") "
                    +str(self.ihadron.quarks)+" parity: "
                    +str(self.ihadron.parity)+" hadron_type: "
                    +str(self.ihadron.hadron)+" m: "
                    +str(self.ihadron.mass[0])+" MeV, evidence: "
                    +str(self.ihadron.evidence)
                    )
        else:
            e = 3
            self.ihadron = InfoSnake([0],[0],[0],p,q,f,h,3)
            print("Evidence 3. Hadron not theoretically expected.")
        return e


    def play_sound(self,name):
        sound = pygame.mixer.Sound(name)
        pygame.mixer.Sound.play(sound)

    def checkmeson(self):
        mylength = len(self.mynewblock)
        #if(mylength>2):
        #    if(self.mynewblock[1].color>0 and self.mynewblock[2].color>0):
        #        if(self.mynewblock[1].color == self.mynewblock[2].color):
        #            if (self.mynewblock[1].parity != self.mynewblock[2].parity):
        #                e = self.evaluate(self.mynewblock,'mesons')
        #                if(e<3):
        #                    for i in range(3,self.length):
        #                        self.mynewblock[i-2] = self.mynewblock[i]
        #                    for i in range(1,3):
        #                        del self.mynewblock[self.length-i]
        #                    smallsound.play_sound(d.sounds[3])
        #                self.length = len(self.mynewblock)


        if(mylength>6):
            if(self.mynewblock[1].color>0 and self.mynewblock[2].color>0 and self.mynewblock[3].color>0 and self.mynewblock[4].color>0 and self.mynewblock[5].color>0 and self.mynewblock[6].color>0):
                control1 = 0
                control2 = 0
                for i in range(3,7,1):
                    if((self.mynewblock[1].flavor == self.mynewblock[i].flavor) and (self.mynewblock[1].parity == self.mynewblock[i].parity)):
                        control1 += 1
                    if((self.mynewblock[2].flavor == self.mynewblock[i].flavor) and (self.mynewblock[2].parity == self.mynewblock[i].parity)):
                        control2 += 1

                if((self.mynewblock[1].color == self.mynewblock[2].color)
                   and (self.mynewblock[3].color == self.mynewblock[4].color)
                   and (self.mynewblock[5].color == self.mynewblock[6].color)
                   and (self.mynewblock[1].color != self.mynewblock[3].color)
                   and (self.mynewblock[5].color != self.mynewblock[1].color)
                   and (self.mynewblock[5].color != self.mynewblock[3].color)
                   and (self.mynewblock[1].parity != self.mynewblock[2].parity)
                   and (control1 == 2) and (control2 == 2)):
                    e = self.evaluate(self.mynewblock,'mesons')
                    if(e<3):
                        for i in range(7,self.length):
                            self.mynewblock[i-6] = self.mynewblock[i]
                        for i in range(1,7):
                            del self.mynewblock[self.length-i]
                        self.play_sound(d.sounds[3])
                    self.length = len(self.mynewblock)

    def checkbaryon(self):
        mylength = len(self.mynewblock)
        if(mylength>3):
            if(self.mynewblock[1].color>0 and self.mynewblock[2].color>0 and self.mynewblock[3].color>0):
                if((self.mynewblock[1].color!=self.mynewblock[2].color)
                and (self.mynewblock[1].color!=self.mynewblock[3].color)
                and (self.mynewblock[2].color!=self.mynewblock[3].color)
                and (self.mynewblock[1].parity==self.mynewblock[2].parity)
                and (self.mynewblock[1].parity==self.mynewblock[3].parity)
                and (self.mynewblock[2].parity==self.mynewblock[3].parity)):
                    e = self.evaluate(self.mynewblock,'baryons')
                    if(e<3):
                        for i in range(4,self.length):
                            self.mynewblock[i-3] = self.mynewblock[i]

                        del self.mynewblock[self.length-1]
                        del self.mynewblock[self.length-2]
                        del self.mynewblock[self.length-3]
                        self.play_sound(d.sounds[3])
                    self.length = len(self.mynewblock)

class Snake:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.x = [pr.p["SIZE"] + pr.p["SHIFT_X"]]
        self.y = [pr.p["SIZE"] + pr.p["SHIFT_Y"]]

        self.direction = 'right'
        self.myblock = [1]
        self.myblock[0] = Blocco(self.x[0],self.y[0],0,0,0,0,'quark',4)
        self.length = [len(self.myblock),0,0]
        self.score = [0,0,0]
        self.scoretot = 0

        self.infos = InfoSnake([0],[0],[0],0,0,0,0,4)
        self.infos_baryons = []
        self.infos_mesons = []

    def update(self,blocco_aggiunto):

        self.infos = InfoSnake([0],[0],[0],0,0,0,0,4)
        if((self.infos.hadron == 0) or (self.infos.evidence > 2)):
            self.myblock.insert(1,blocco_aggiunto)
            self.x.append(self.x[0])
            self.y.append(self.x[0])
            self.myblock[1] = Blocco(self.x[1],self.y[1],self.length[0],blocco_aggiunto.color,blocco_aggiunto.flavor,blocco_aggiunto.parity,'quark',4)

            self.myhadron = FindHadrons(self.myblock,self.length,self.parent_screen)
            self.myhadron.checkbaryon()
            self.myhadron.checkmeson()
            self.infos = self.myhadron.ihadron
            self.score[0] += 1
            self.scoretot += SCORE_QUARK

        if((self.infos.hadron != 0) and (self.infos.evidence < 3 )):
            self.x.append(self.x[0])
            self.y.append(self.x[0])
            myparity = self.infos.parity
            myflavor = self.infos.quarks
            blocco_adronico = Blocco(self.x[self.length[0]-1],self.y[self.length[0]-1],self.length,0,myflavor,myparity,self.infos.hadron,self.infos.evidence)
            self.myblock.append(blocco_adronico)

            if(self.infos.hadron == 'baryons'):
                self.infos_baryons.insert(0,self.infos)
                self.score[1] += 1
                self.scoretot += SCORE_BARYON
            if(self.infos.hadron == 'mesons'):
                self.infos_mesons.insert(0,self.infos)
                self.score[2] += 1
                self.scoretot += SCORE_MESON

        self.length = [len(self.myblock),len(self.infos_baryons),len(self.infos_mesons)]

    def draw(self):
        self.myblock[0].x = self.x[0]
        self.myblock[0].y = self.y[0]
        self.myblock[0].head(self.parent_screen,self.direction)
        mialength = len(self.myblock)
        for i in range(1,mialength):
            self.myblock[i].x = self.x[i]
            self.myblock[i].y = self.y[i]
            self.myblock[i].draw(self.parent_screen)

    def move_left(self):
        self.direction = 'left'

    def move_up(self):
        self.direction = 'up'

    def move_right(self):
        self.direction = 'right'

    def move_down(self):
        self.direction = 'down'

    def walk(self,go):
        if go:
            for i in range(len(self.myblock)-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            if self.direction == 'up':
                self.y[0] -= pr.p["SIZE"]
            if self.direction == 'down':
                self.y[0] += pr.p["SIZE"]
            if self.direction == 'right':
                self.x[0] += pr.p["SIZE"]
            if self.direction == 'left':
                self.x[0] -= pr.p["SIZE"]

        self.draw()

import param
from modules.mygeometry import *
from modules.par import *
from modules.media import *


class FinalScore:
    def __init__(self,surface,pr,score,scoretot):
        self.surface = surface
        self.pr = pr
        self.score = score
        self.scoretot = scoretot

    def show_hadron_specs(self,hadron,shift_x):
        initial_length = len(hadron)
        local_hadron = []
        for i in range(initial_length):
            local_hadron.append(hadron[i])
        count = []
        i = 0
        while(i<initial_length):
            count.append(1)
            j = i+1
            while(j<initial_length):
                if(local_hadron[i].name == local_hadron[j].name):
                    count[i]+=1
                    local_hadron.pop(j)
                    j-=1
                j+=1
                initial_length = len(local_hadron)
            i+=1

        str_hs = ""

        max_length = 22
        i = 0
        while((i<initial_length) and (i<max_length)) :
            str_hs += f"{count[i]}x {local_hadron[i].symbol[0]} ({local_hadron[i].quarks}) {local_hadron[i].name[0]}"
            if(local_hadron[i].mass[0]!="Unknown"):
                str_hs += " "+d.str_page_3[0] +f" = {local_hadron[i].mass[0]} MeV \n "
            else:
                str_hs += " ("+d.str_page_3[1]+") \n "
            if(i == max_length - 1):
                str_hs += " "+d.str_page_3[2]+" ... "
            i += 1

        if (initial_length!=0):
            x = self.pr.r1(80 + shift_x)
            y = self.pr.r1(360)
            show_hs = Plain_hf(x,y,self.pr.r1(740),self.surface,green,True,dgreen,False)
            show_hs.write(str_hs,self.pr.p["FONT_NORM"],black)

    def display_title(self):
        title = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_BIG"]).render(d.str_page_1[4],True,white)
        self.surface.blit(title,(self.pr.r1(650),self.pr.r1(10)))

        commands = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_NORM"]).render(d.str_page_3[3],True,white)
        self.surface.blit(commands,(self.pr.r1(240),self.pr.r1(975)))


    def render_background(self):

        self.surface.fill(BACKGROUND_COLOR)
        surf = pygame.Surface((self.pr.p["GAME_SIZE_X"],self.pr.p["GAME_SIZE_Y"]))
        pygame.draw.rect(surf, white,pygame.Rect(0, 0, self.pr.p["GAME_SIZE_X"], self.pr.p["GAME_SIZE_Y"]),0)
        self.surface.blit(surf,(self.pr.p["SHIFT_X"], self.pr.p["SHIFT_Y"]))

    def show_game_over(self,baryons,mesons):
        local_baryons = baryons
        local_mesons = mesons
        self.render_background()

        str_gameended = Plain_hf(self.pr.r1(640),self.pr.r1(110),self.pr.r1(400),self.surface,green,False,grey,False)
        str_gameended.write(d.str_page_3[4],self.pr.p["FONT_BIG"],red)

        str_result = Plain_hf(self.pr.r1(705),self.pr.r1(190),self.pr.r1(800),self.surface,green,False,grey,False)
        str_result.write(f""+d.str_page_3[5]+f" {self.scoretot}",self.pr.p["FONT_LARGE"],black)

        str_det = Plain_hf(self.pr.r1(505),self.pr.r1(250),self.pr.r1(800),self.surface,green,False,grey,False)
        str_det.write(f" ("+d.str_page_3[6]+f" {SCORE_QUARK}, "+d.str_page_3[7]+f" {SCORE_BARYON}, "+d.str_page_3[8]+f" {SCORE_MESON}"+d.str_page_3[9]+")",self.pr.p["FONT_NORM"],black)

        str_baryons = Plain_hf(self.pr.r1(340),self.pr.r1(290),self.pr.r1(200),self.surface,green,False,grey,False)
        str_baryons.write(f""+d.str_page_3[10]+f": {self.score[1]}",self.pr.p["FONT_LARGE"],red)

        str_mesons = Plain_hf(self.pr.r1(1150),self.pr.r1(290),self.pr.r1(200),self.surface,green,False,grey,False)
        str_mesons.write(f""+d.str_page_3[11]+f": {self.score[2]}",self.pr.p["FONT_LARGE"],red)

        self.show_hadron_specs(local_baryons,0)
        self.show_hadron_specs(local_mesons,780)
        self.display_title()




class DisplayScore:
    def __init__(self,snake,surface,pr):

        self.snake = snake
        self.surface = surface
        self.pr = pr

    def display_param(self):
        str_param = f""+d.str_button_3[4]+f" = {param.SPEED} \n "\
            +f""+d.str_page_3[12]+f" = {param.NUM_APPLES} \n "+d.str_page_3[13]+" \n "
        if((param.PARITY[0] == 0) and (param.PARITY[1] == 1)):
            str_param += "= "+d.str_button_3[7]+" \n "
        if((param.PARITY[0] == param.PARITY[1]) and (param.PARITY[1] == 1)):
            str_param += "= "+d.str_button_3[6]+" \n "
        if((param.PARITY[0] == param.PARITY[1]) and (param.PARITY[1] == 0)):
            str_param += "= "+d.str_button_3[5]+" \n "

        str_param += d.str_page_3[14]
        for i in range(0,len(param.NUM_FLAVOR)):

            if(param.NUM_FLAVOR[i] == 1):
                str_param += "up "
            if(param.NUM_FLAVOR[i] == 2):
                str_param += "down "
            if(param.NUM_FLAVOR[i] == 3):
                str_param += "strange "
            if(param.NUM_FLAVOR[i] == 4):
                str_param += "charm "
            if(param.NUM_FLAVOR[i] == 5):
                str_param += "bottom "
            if(param.NUM_FLAVOR[i] == 6):
                str_param += "top "

        x = self.pr.r1(1660)
        y = self.pr.r1(740)
        width = self.pr.r1(240)
        show_par = Plain_hf(x,y,width,self.surface,black,False,black,False)
        show_par.write(str_param,self.pr.p["FONT_NORM"],white)


    def display_evidence(self,evidence):
        if (evidence == 1):
            str_evidence = d.str_page_3[15]
        elif (evidence == 2):
            str_evidence = d.str_page_3[16]
        elif(evidence == 3):
            str_evidence = d.str_page_3[17]
        if (evidence > 0):
            show_evidence = Plain_hf(self.pr.r1(1660),self.pr.r1(520),self.pr.r1(240),self.surface,green,True,green,False)
            show_evidence.write(str_evidence,self.pr.p["FONT_NORM"],white)

    def display_meson(self,evidence):
        if (evidence<3):
            num_mesons = len(self.snake.infos_mesons[0].symbol)
            str_meson = d.str_page_3[18]
            if(num_mesons>1):
                str_meson += ""+d.str_page_3[19]+" \n "
                for k in range(num_mesons):
                    str_meson += str(self.snake.infos_mesons[0].symbol[k])+" ("+d.str_page_3[0]+"="+str(self.snake.infos_mesons[0].mass[k])+" MeV) \n "
                str_meson += ""+d.str_page_3[20]+"! \n "

            else:
                str_meson += str(self.snake.infos_mesons[0].symbol[0])+" ("+d.str_button_3[0]+"="+str(self.snake.infos_mesons[0].mass[0])+" MeV) "+d.str_page_3[21]+" \n "

            myflavor = [char for char in str(self.snake.infos_mesons[0].quarks)]
            if(self.snake.infos_mesons[0].parity == 0):
                str_meson += ""+d.str_page_3[22]+": "+myflavor[0]+" anti-"+myflavor[1]
            else:
                str_meson += ""+d.str_page_3[22]+": "+myflavor[1]+" anti-"+myflavor[0]

            show_meson = Plain_hf(self.pr.r1(1660),self.pr.r1(290),self.pr.r1(220),self.surface,red,True,green,False)
            show_meson.write(str_meson,self.pr.p["FONT_NORM"],white)
        self.display_evidence(evidence)

    def display_baryon(self,evidence):

        if (evidence<3):
            str_baryon = d.str_page_3[23]+str(self.snake.infos_baryons[0].symbol[0])+" "+d.str_page_3[33]+"!!! \n "
            if(self.snake.infos_baryons[0].parity == 0):
                str_baryon += " \n "+d.str_page_3[22]+": "+str(self.snake.infos_baryons[0].quarks)
            if(self.snake.infos_baryons[0].parity == 1):
                str_baryon += " \n "+d.str_page_3[22]+" (anti-) "+str(self.snake.infos_baryons[0].quarks)
            str_baryon += " \n "+d.str_page_3[24]+": "+str(self.snake.infos_baryons[0].name[0])
            str_baryon += " \n "+d.str_page_3[25]+"="+str(self.snake.infos_baryons[0].mass[0])+" MeV"

            show_baryon = Plain_hf(self.pr.r1(1660),self.pr.r1(290),self.pr.r1(240),self.surface,red,True,green,False)
            show_baryon.write(str_baryon,self.pr.p["FONT_NORM"],white)

        self.display_evidence(evidence)

    def display_hadron(self):
        last = len(self.snake.myblock)-1
        last_hadron = self.snake.myblock[last].type_particle
        evidence_hadron = self.snake.myblock[last].evidence

        if(last_hadron == "baryons"):
            self.display_baryon(evidence_hadron)
        elif(last_hadron == "mesons"):
            self.display_meson(evidence_hadron)

    def display_author(self):
        author = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_NORM"],italic=True).render("by Marco Catillo",True,white)
        self.surface.blit(author,(self.pr.r1(1700),self.pr.r1(940)))

    def display_title(self):
        title = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_BIG"]).render(d.str_page_3[27],True,white)
        self.surface.blit(title,(self.pr.r1(650),self.pr.r1(10)))

        commands = pygame.font.SysFont(FONT_STYLE,self.pr.p["FONT_NORM"]).render(d.str_page_3[26],True,white)
        self.surface.blit(commands,(self.pr.r1(440),self.pr.r1(975)))

    def display_score(self):
        str_score = d.str_page_3[29]+": "+str(self.snake.scoretot)+" \n \n "+d.str_page_3[28]+": "+str(self.snake.score[0])+" \n "+d.str_page_3[30]+": "+str(self.snake.score[1] + self.snake.score[2]) + " \n "+d.str_page_3[31]+": "+str(self.snake.score[1])+" \n "+d.str_page_3[32]+": "+str(self.snake.score[2])

        show_score = Plain_hf(self.pr.r1(1660),self.pr.r1(90),self.pr.r1(240),self.surface,red,True,black,True)
        show_score.write(str_score,self.pr.p["FONT_NORM"],white)

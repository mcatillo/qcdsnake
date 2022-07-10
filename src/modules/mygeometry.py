# set important feature of the program geometry

import os
import pygame
import pyautogui as pg
from screeninfo import get_monitors
from modules.par import *

class Factor:
    def __init__(self):
        self.m = get_monitors()
        self.pg = pg.position()
        self.num_monitors = len(self.m)
        self.monitor_pos = 0
        self.factor = 1

        # Find the primary monitor and set self.monitor_pos the monitor number corresponding to the primary monitor

        for i in range(self.num_monitors):
            if self.m[i].is_primary:
                self.monitor_pos = i
                
    # Find in which monitor is the mouse cursor
    def position_mouse(self):
        i = 0
        notfound = True
        while notfound:
            cond_x = (self.pg.x > self.m[i].x) and (self.pg.x < (self.m[i].x + self.m[i].width))
            cond_y = (self.pg.y > self.m[i].y) and (self.pg.y < (self.m[i].y + self.m[i].height))
            if (cond_x and cond_y):
                notfound = False
            i += 1
        self.monitor_pos = i-1

    # Open the window in the monitor self.monitor_pos, which should be where the mouse is located
    def position_window(self):

        x = self.m[self.monitor_pos].x
        y = self.m[self.monitor_pos].y
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (x,y)
        print("Monitor in ",x,y)

    # Find the Ratio between a 1920x1080 monitor and the current monitor where the game is running and return this value back
    def initial_factor(self):
        # Optimal for 16:9 monitors, not good for monitors with ratio larger than 1.77 like: 180:101 and 57:32
        self.position_mouse()
        self.position_window()
        return int(self.m[self.monitor_pos].width/WINDOW_WIDTH)
    def new_factor(self):
        return int(self.m[self.monitor_pos].width/WINDOW_WIDTH)

class Parameters:

    def __init__(self):

        # Parameters for the geometry of the game according to a 1920x1080 monitor
        self.p = {"SIZE": 40,
                  "WINDOW_SIZE_X": 1920,
                  "WINDOW_SIZE_Y": 1020,
                  "GAME_SIZE_X": 1600,
                  "GAME_SIZE_Y": 880,
                  "SHIFT_X": 40,
                  "SHIFT_Y": 70,
                  "CENTER_BALL_X": 12,
                  "CENTER_BALL_Y": 5,
                  "CENTER_B_X": 10,
                  "CENTER_B_Y": 7,
                  "CENTER_M_X": 7,
                  "CENTER_M_Y": 7,
                  "FONT_SMALL": 10,
                  "FONT_NORM": 20,
                  "FONT_LARGE": 30,
                  "FONT_BIG": 40
                  }
        self.factor = 1

    def r1(self,var):
        return int(var*self.factor)
    
    def rc(self):
        for m in self.p:
            self.p[m] = self.r1(self.p[m])
        

class Plain:

    def __init__(self,x,y,width,height,surface,colorborder,border,colorbackground,background):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface

        self.border = border
        self.background = background
        self.colorborder = colorborder
        self.colorbackground = colorbackground
        self.give_color()

    def give_color(self):

        if self.background:
            my_image2 = pygame.Surface((self.width,self.height), pygame.SRCALPHA)
            pygame.draw.rect(my_image2, self.colorbackground, my_image2.get_rect())
            self.surface.blit(my_image2,(self.x,self.y))

        if self.border:
            my_image = pygame.Surface((self.width,self.height), pygame.SRCALPHA)
            pygame.draw.rect(my_image, self.colorborder, my_image.get_rect(), 5)
            self.surface.blit(my_image,(self.x,self.y))

        pygame.display.flip()

    def write(self,string,font,color):
        
        self.font = font
        self.color = color
        self.string = string
        pyfont = pygame.font.SysFont(FONT_STYLE,self.font)
        
        sarray = self.string.split(' ')
        num_words = len(sarray)

        offset = pyfont.size(" ")
        x_in = 2*offset[0] + self.x
        y_in = offset[1] + self.y
        y_max = self.y + self.height - offset[1]
        i = 0
        while ((i<num_words) and (y_in < y_max)):

            word = pyfont.render(sarray[i]+" ",True,self.color)
            len_word = pyfont.size(sarray[i]+" ")

            x_max = self.x + self.width
            x_i   = x_in + len_word[0]

            if((x_i < x_max) and (sarray[i] != '\n')):
                self.surface.blit(word,(x_in,y_in))
                x_in += len_word[0]
            else:
                x_in = 2*offset[0] + self.x
                y_in += offset[1]
                if (sarray[i] != '\n') and (y_in < y_max):
                    self.surface.blit(word,(x_in,y_in))
                    x_in += len_word[0]

            i+=1
        pygame.display.flip()

class Plain_hf:

    def __init__(self,x,y,width,surface,colorborder,border,colorbackground,background):

        self.x = x
        self.y = y
        self.width = width
        self.surface = surface

        self.border = border
        self.background = background
        self.colorborder = colorborder
        self.colorbackground = colorbackground


    def give_color(self,height):
        self.height = height

        if self.background:
            my_image2 = pygame.Surface((self.width,self.height), pygame.SRCALPHA)
            pygame.draw.rect(my_image2, self.colorbackground, my_image2.get_rect())
            self.surface.blit(my_image2,(self.x,self.y))

        if self.border:
            my_image = pygame.Surface((self.width,self.height), pygame.SRCALPHA)
            pygame.draw.rect(my_image, self.colorborder, my_image.get_rect(), 5)
            self.surface.blit(my_image,(self.x,self.y))

    def write_logic(self,string,font,color,switch):

        self.font = font
        self.color = color
        self.string = string
        pyfont = pygame.font.SysFont(FONT_STYLE,self.font)

        sarray = self.string.split(' ')
        num_words = len(sarray)

        offset = pyfont.size(" ")
        x_in = 2*offset[0] + self.x
        y_in = offset[1] + self.y
        i = 0
        while i<num_words:

            word = pyfont.render(sarray[i]+" ",True,self.color)
            len_word = pyfont.size(sarray[i]+" ")

            x_max = self.x + self.width
            x_i   = x_in + len_word[0]

            if((x_i < x_max) and (sarray[i] != '\n')):
                if switch:
                    self.surface.blit(word,(x_in,y_in))
                x_in += len_word[0]
            else:
                x_in = 2*offset[0] + self.x
                y_in += 1.2*offset[1]
                if sarray[i] != '\n' :
                    if switch:
                        self.surface.blit(word,(x_in,y_in))
                    x_in += len_word[0]
            i+=1
        return (y_in,offset[1])

    def write(self,string,font,color):
        (y_in,offset_y) = self.write_logic(string,font,color,False)
        self.give_color(y_in - self.y + 2*offset_y)
        (y_in,offset_y) = self.write_logic(string,font,color,True)


pos_window = Factor()
pr = Parameters()
        
        
        
        





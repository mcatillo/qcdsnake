#   Welcome to the QCD-Snake! by Marco Catillo (Zurich, 2022)
#
#   Here there is the main Program of the Game, which is composed by two main classes:
#
#   * SetupGame
#   * Game
#
#   You can look line by line through this code for further comments on how the game works

import sys
import os
import pygame
import time
import random
from pygame.locals import *
import param
from modules.media import *
from modules.mygeometry import *
from modules.par import *
from modules.page1 import *
from modules.page2 import *
from modules.page4 import *
from modules.buttons import *
from modules.setparam import *
from modules.groupbuttons import *
from modules.game_logic import *

# In this class I define the main variables of the Game and there is the loop of events in the function run()

class SetupGame:
    def __init__(self):

        pygame.init()
        self.id_pages = {"id_description": True, "id_howto": False, "id_play": False, "id_end": False}

    def inizialize(self):
        self.go = True
        self.running = True
        self.bot = []
        self.game = Game()
        self.setup = SetupParam(self.game.surface,pr)
        self.movethroughbuttons = MovethroughButtons(0,0,4,[])
        self.movethroughbuttons.define_buttons(self.bot,self.setup,self.game.surface,pr)

    # Set the window that should appear to screen. All windows are set to False except the one which you are currently viewing which is set to False
    def id_set(self,whichTrue):
        for m in self.id_pages:
            self.id_pages[m] = False
        self.id_pages[whichTrue] = True

    # Switch on or off the music while you are playing the game
    def music_on_off(self,go):
        if go:
            self.game.play_background_music()
        else:
            pygame.mixer.music.fadeout(10)

    # Change the monitor on which the game is running and adapt with the screen size
    def change_monitor(self):
        pygame.display.quit()
        pos_window.monitor_pos = (pos_window.monitor_pos + 1)%pos_window.num_monitors
        pos_window.position_window()
        pr.factor = pos_window.new_factor()
        pr.rc()
        game = SetupGame()
        game.run()

    # Restart the game in case of end game, or you just want to restart over the game
    def restart(self):
        self.id_set("id_play")
        self.go = True
        self.music_on_off(self.go)
        self.game.reset()

    # Main event loop where I define what keyboard  keys and mouse click should do in the program
    def run(self):

        direction = (1,0)
        self.mx = 0
        self.my = 0
        count_num = 256
        sleep = 0.02
        clock = pygame.time.Clock()
        self.inizialize()
        while self.running:
            for event in pygame.event.get():
                self.mx,self.my = pygame.mouse.get_pos()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                    elif event.key == K_m:
                        self.running = False
                        self.change_monitor()

                    elif (event.key == K_SPACE and self.id_pages["id_end"]) or (event.key == K_SPACE and self.id_pages["id_howto"]) or (event.key == K_RETURN) and (self.id_pages["id_play"]):
                        self.restart()

                    elif (event.key == K_SPACE and self.id_pages["id_play"]) or (event.key == K_SPACE and self.id_pages["id_description"]):
                        self.id_set("id_howto")

                    elif event.key == K_d:
                        self.id_set("id_description")

                    elif event.key == K_p :
                        self.go = self.go^True
                        self.music_on_off(self.go)

                    elif event.key == K_l:
                        num = len(LANGUAGES)
                        for i in range(num):
                            if d.language == LANGUAGES[i]:
                                j = i
                        d.language = LANGUAGES[(j+1)%num]
                        d.fill()
                        self.inizialize()

                    elif self.id_pages["id_play"] and self.go:
                        if ((event.key == K_UP) and (direction[1] == 0)):
                            self.game.snake.move_up()
                            direction = (0,1)
                        elif ((event.key == K_DOWN) and (direction[1] == 0)):
                            self.game.snake.move_down()
                            direction = (0,1)
                        elif ((event.key == K_LEFT) and (direction[0] == 0)):
                            self.game.snake.move_left()
                            direction = (1,0)
                        elif ((event.key == K_RIGHT) and (direction[0] == 0)):
                            self.game.snake.move_right()
                            direction = (1,0)

                if self.id_pages["id_howto"] or self.id_pages["id_end"]:
                    move = self.movethroughbuttons.select_button(event,(self.mx,self.my))
                    if  ((move == (1,0)) or (move == (1,1))):
                        self.restart()
                    if move == (0,1):
                        self.running = False

                if event.type == QUIT: # la finestra si chiude quando clicco su quit
                    self.running = False

            try:
                if self.id_pages["id_play"]:
                    self.game.play(self.go)
                    time.sleep(param.SPEED-sleep)

            except Exception as e:
                self.id_set("id_end")
                direction = (1,0)

            if self.id_pages["id_description"]:
                if (count_num == 0):
                    self.game.description_game()
                    count_num = 256
                count_num = count_num >> 1

            elif self.id_pages["id_howto"]:
                self.game.howto_game(self.bot,self.setup,self.movethroughbuttons.titles_buttons)

            elif self.id_pages["id_end"]:
                self.game.end_game(self.bot,self.setup,self.movethroughbuttons.titles_buttons)
            time.sleep(sleep)
            clock.tick(20)

#   In the following class the main game windows are defined. There are in total 4 main windows. The first which appears is about the description of the game and the function description_game() inside this class call this window. Then there is a window which describes how to play and set the game parameters, this is called by function howto_game(). Then there is the window where the player can move the snake in order to eat as much quarks as possible, and this is called by the function play(). Finally there is the window with the results/score of the game and you can also set again the parameters. This is called by the function end_game().

class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((pr.p["WINDOW_SIZE_X"],pr.p["WINDOW_SIZE_Y"]))
        pygame.display.set_caption('The Quark Snake Game!')
        Icon = pygame.image.load(d.images[8])
        pygame.display.set_icon(Icon)

        pygame.mixer.init()
        self.surface.fill(white)

        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = [0]*param.NUM_APPLES
        

        for i in range(param.NUM_APPLES):
            control = 1
            while(control > 0):
                control = 0
                self.apple[i] = Apple(self.surface)
                for a in range(1,i+1):
                    if((self.apple[i].x == self.apple[i-a].x)
                       and (self.apple[i-a].y == self.apple[i-a].y)):
                        control = 1

    # Check if there is a collision of the snake with itself
    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + pr.p["SIZE"]:
            if y1 >= y2 and y1 < y2 + pr.p["SIZE"]:
                return True
        return False

    # Play the background music while you are playing
    def play_background_music(self):
        pygame.mixer.music.load(d.sounds[0])
        pygame.mixer.music.play(loops=-1)

    # Set the main structure of the window game
    def render_background(self,background_color):
        self.surface.fill(BACKGROUND_COLOR)
        surf = pygame.Surface((pr.p["GAME_SIZE_X"],pr.p["GAME_SIZE_Y"]))
        pygame.draw.rect(surf, background_color,pygame.Rect(0, 0, pr.p["GAME_SIZE_X"], pr.p["GAME_SIZE_Y"]),0)
        self.surface.blit(surf,(pr.p["SHIFT_X"], pr.p["SHIFT_Y"]))

    # When called it shows on your screen, the window with the game description
    def description_game(self):
        pygame.mixer.music.fadeout(1000)
        self.render_background(white)
        self.description = Description(self.surface,pr)
        self.description.write()
        pygame.display.flip()

    # When called it shows the section on where you can modify the parameters
    def set_game(self,bot,setup,titles):
        setup.ybase = pr.p["SHIFT_Y"]

        titles[0][0].write(titles[0][1],titles[0][2],titles[0][3])
        titles[1][0].write(titles[1][1],titles[1][2],titles[1][3])
        titles[2][0].write(titles[2][1],titles[2][2],titles[2][3])
        titles[3][0].write(titles[3][1],titles[3][2],titles[3][3])
        titles[4][0].write(titles[4][1],titles[4][2],titles[4][3])

        for i in range(NUM_BUTTONS):
            bot[i].run()

    # When called it shows on your screen, the window with tthe information on how to play and set the parameters
    def howto_game(self,bot,setup,titles):
        pygame.mixer.music.fadeout(1000)
        self.render_background(white)
        self.howto = Howto(self.surface,pr)
        self.set_game(bot,setup,titles)
        self.howto.write()
        pygame.display.flip()

    # Put in pause the game
    def pause(self,go):
        x = pr.p["SHIFT_X"]
        y = pr.p["SHIFT_Y"]-pr.r1(60)
        width = pr.r1(500)
        if not go:
            self.show_go = Plain_hf(x,y,width,self.surface,red,False,grey,False)
            self.show_go.write(d.str_pause[0],pr.p["FONT_NORM"],white)

            image = pygame.image.load(d.images[1])
            image = pygame.transform.scale(image, (pr.r1(40), pr.r1(40)))
            self.surface.blit(image, [pr.p["SHIFT_X"] + pr.r1(10), y + pr.r1(10)])
        else:
            self.show_go = Plain_hf(x,y,width,self.surface,green,False,grey,False)
            self.show_go.write(d.str_pause[1],pr.p["FONT_NORM"],white)

            image = pygame.image.load(d.images[0])
            image = pygame.transform.scale(image, (pr.r1(40), pr.r1(40)))
            self.surface.blit(image, [pr.p["SHIFT_X"] + pr.r1(10), y + pr.r1(10)])

    # Play the small sound allerts of when a snake eats a quark
    def play_sound(self,name):
        sound = pygame.mixer.Sound(name)
        pygame.mixer.Sound.play(sound)

    # Start the game to play
    def play(self,go):
        self.render_background(BACKGROUND_GAME)
        self.snake.walk(go)
        for i in range(param.NUM_APPLES):
            self.apple[i].draw()
        self.display_score = DisplayScore(self.snake,self.surface,pr)
        self.display_score.display_title()
        self.display_score.display_score()
        self.display_score.display_hadron()
        self.display_score.display_author()
        self.display_score.display_param()
        self.pause(go)
        pygame.display.flip()

        for i in range(param.NUM_APPLES):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple[i].x,self.apple[i].y):
                self.play_sound(d.sounds[2])
                self.blocco_mangiato = Blocco(self.apple[i].x,self.apple[i].y,-1,self.apple[i].rand_color,self.apple[i].rand_flavor,self.apple[i].rand_pa,'quark',4)
                self.snake.update(self.blocco_mangiato)
                # choose another apple
                self.apple[i].move()

        for i in range (5,self.snake.length[0]):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                self.play_sound(d.sounds[1])
                raise "Game over"
        if ((self.snake.x[0] < pr.p["SHIFT_X"]) or (self.snake.x[0] >= pr.p["GAME_SIZE_X"]+pr.p["SHIFT_X"])):
            self.play_sound(d.sounds[1])
            raise "Game over"
        if ((self.snake.y[0] < pr.p["SHIFT_Y"]) or (self.snake.y[0] >= pr.p["GAME_SIZE_Y"]+pr.p["SHIFT_Y"])):
            self.play_sound(d.sounds[1])
            raise "Game over"

    # It shows the last window with the score obtained from the game
    def end_game(self,bot,setup,titles):
        pygame.mixer.music.fadeout(1000)
        baryons = self.snake.infos_baryons
        mesons = self.snake.infos_mesons
        self.end = FinalScore(self.surface,pr,self.snake.score,self.snake.scoretot)
        self.end.show_game_over(baryons,mesons)
        self.set_game(bot,setup,titles)
        pygame.display.flip()

    # Reset the game
    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = [0]*param.NUM_APPLES
        for i in range(param.NUM_APPLES):
            self.apple[i] = Apple(self.surface)

if __name__ == "__main__":
    pr.factor = pos_window.initial_factor()
    pr.rc()

    game = SetupGame()
    game.run()



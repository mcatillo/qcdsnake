import sys
import os
import pygame
from pygame.locals import *
import param
from modules.media import *


def setNUM_FLAVOR(bot):
    if bot.name == "Up" and bot.clicked:
        param.NUM_FLAVOR.append(1)
    elif bot.name == "Up" and not bot.clicked:
        param.NUM_FLAVOR.remove(1)

    if bot.name == "Down" and bot.clicked:
        param.NUM_FLAVOR.append(2)
    elif bot.name == "Down" and not bot.clicked:
        param.NUM_FLAVOR.remove(2)

    if bot.name == "Charm" and bot.clicked:
        param.NUM_FLAVOR.append(4)
    elif bot.name == "Charm" and not bot.clicked:
        param.NUM_FLAVOR.remove(4)

    if bot.name == "Strange" and bot.clicked:
        param.NUM_FLAVOR.append(3)
    elif bot.name == "Strange" and not bot.clicked:
        param.NUM_FLAVOR.remove(3)

    if bot.name == "Top" and bot.clicked:
        param.NUM_FLAVOR.append(6)
    elif bot.name == "Top" and not bot.clicked:
        param.NUM_FLAVOR.remove(6)

    if bot.name == "Bottom" and bot.clicked:
        param.NUM_FLAVOR.append(5)
    elif bot.name == "Bottom" and not bot.clicked:
        param.NUM_FLAVOR.remove(5)
    param.NUM_FLAVOR.sort()

def setNUM_APPLES(bot):
    if bot.name == "5" and bot.clicked:
        param.NUM_APPLES = 5
    elif bot.name == "10" and bot.clicked:
        param.NUM_APPLES = 10
    elif bot.name == "15" and bot.clicked:
        param.NUM_APPLES = 15
    elif bot.name == "20" and bot.clicked:
        param.NUM_APPLES = 20

def setPARITY(bot):
    if bot.name == d.str_button_3[5] and bot.clicked:
        param.PARITY = [0,0]
    if bot.name == d.str_button_3[6] and bot.clicked:
        param.PARITY = [1,1]
    if bot.name == d.str_button_3[7] and bot.clicked:
        param.PARITY = [0,1]

def setSPEED(bot):
    if bot.name == "0.07" and bot.clicked:
        param.SPEED = 0.07
    elif bot.name == "0.08" and bot.clicked:
        param.SPEED = 0.08
    elif bot.name == "0.09" and bot.clicked:
        param.SPEED = 0.09
    elif bot.name == "0.10" and bot.clicked:
        param.SPEED = 0.10

def setBUTTONS(bot):

    for i in range(len(param.NUM_FLAVOR)):
        for k in range(6):
            if param.NUM_FLAVOR[i] == k+1:
                bot[k].clicked = True

    for k in range(6,10):
        if param.NUM_APPLES == int(bot[k].name):
            bot[k].clicked = True

    if (param.PARITY[0] == param.PARITY[1]) and (param.PARITY[0] == 0):
        bot[10].clicked = True
    elif(param.PARITY[0] == param.PARITY[1]) and (param.PARITY[0] == 1):
        bot[11].clicked = True
    elif(param.PARITY[0] != param.PARITY[1]):
        bot[12].clicked = True


    for k in range(13,17):
        if param.SPEED == float(bot[k].name):
            bot[k].clicked = True




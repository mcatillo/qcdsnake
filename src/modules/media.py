import sys
import os
import os.path
import json
import param
from modules.par import *

PATH_MEDIA = "resources/"
PATH_JSON = "database/"
MEDIA = "media.json"
STRINGS = "strings.json"
HADRON = "hadrons.json"


def remove_src():
    base_path = os.path.abspath("./")
    base_array=base_path.split("/")
    len_base = len(base_array)
    base_new = ""
    for i in range(len_base-1):
        base_new += base_array[i]+"/"

    return base_new

def openfile(MYPATH,FILE):

    if not os.path.exists(remove_src()+MYPATH+FILE):
        return open(MYPATH+FILE,'r')
    else:
        return open(remove_src()+MYPATH+FILE,'r')

def check_path(MYPATH,FILE):

    if not os.path.exists(remove_src()+MYPATH+FILE):
        return MYPATH+FILE
    else:
        return remove_src()+MYPATH+FILE


class Database:
    def __init__(self):
        self.language = LANGUAGE

    def fill(self):
        f = openfile(PATH_JSON,MEDIA)
        data = json.load(f)

        self.images = []
        for key in data['images']:
            self.images.append(check_path(PATH_MEDIA,data['images'][key]))

        self.sounds = []
        for key in data['sounds']:
            self.sounds.append(check_path(PATH_MEDIA,data['sounds'][key]))

        f = openfile(PATH_JSON,STRINGS)
        data = json.load(f)

        self.str_page_1 = []
        for key in data['Page-1']:
            self.str_page_1.append(data['Page-1'][key][self.language])

        self.str_page_2 = []
        for key in data['Page-2']:
            self.str_page_2.append(data['Page-2'][key][self.language])

        self.str_button_3 = []
        for key in data['Buttons']:
            self.str_button_3.append(data['Buttons'][key][self.language])

        self.str_page_3 = []
        for key in data['Page-3']:
            self.str_page_3.append(data['Page-3'][key][self.language])

        self.str_pause = []
        for key in data['Pause']:
            self.str_pause.append(data['Pause'][key][self.language])

        f = openfile(PATH_JSON,HADRON)
        self.datahadron = json.load(f)

d = Database()
d.fill()


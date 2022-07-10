# Parameters

NUM_COLORS = 3

# Game score

SCORE_BARYON = 1
SCORE_QUARK = 0.5
SCORE_MESON = 3

# Colors

BACKGROUND_COLOR = (17,0,102)
red = (255, 0, 0,150)
red2 = (255, 0, 0)
orange = (255,165,0)
purple = (160,32,240)
green = (0, 255, 0,150)
dgreen = (0, 200, 0)
blue  = (0, 0, 255,150)
dblue  = (0, 0, 155)
white = (255,255,255)
black = (0,0,0)
grey = (192,192,192)
celeste = (178, 255, 255)
BACKGROUND_GAME = (255, 230, 230)


# Geometry

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Font

FONT_STYLE = 'arial'


MAX_i = [2,2,1,2,1,1] #max x
MAX_j = [3,2,3,2,1,1] #max y
MAX_z = len(MAX_j) # total number of groups of buttons
NUM_BUTTONS =  0
for i in range(MAX_z):
    NUM_BUTTONS += MAX_i[i]*MAX_j[i]

# Language

LANGUAGES = ["en","it"]
LANGUAGE = "en"


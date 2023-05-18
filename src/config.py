import PIL.Image
import os, sys

APP_NAME = "OutlookAuto"

try:      
    basepath = sys._MEIPASS
except: 
    basepath = os.path.abspath(".")

ON_ICON = PIL.Image.open(os.path.abspath(os.path.join(basepath,"./assets/img/on_icon.png")))
OFF_ICON = PIL.Image.open(os.path.abspath(os.path.join(basepath,"./assets/img/off_icon.png")))
AWAY_ICON = PIL.Image.open(os.path.abspath(os.path.join(basepath,"./assets/img/brk_icon.png")))

STATUS_CACHE = os.path.abspath(os.path.join(basepath,"./cache/status"))

with open(os.path.abspath(os.path.join(basepath, "..\configuration\configuration.txt")), "r") as f: 
        d = f.readlines()
        SEND_TO = d[0]
        NAME = d[1]


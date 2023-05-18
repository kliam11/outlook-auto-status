import PIL.Image
import os, sys

APP_NAME = "OutlookAuto"

basepath = sys._MEIPASS

ON_ICON = PIL.Image.open(os.path.abspath(os.path.join(basepath,"./assets/img/on_icon.png")))
OFF_ICON = PIL.Image.open(os.path.abspath(os.path.join(basepath,"./assets/img/off_icon.png")))
AWAY_ICON = PIL.Image.open(os.path.abspath(os.path.join(basepath,"./assets/img/brk_icon.png")))

SEND_TO = ''
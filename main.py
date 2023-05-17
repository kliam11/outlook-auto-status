import config
from const import *
import pystray
import threading 
import mail


CURR_STATUS = OFF_STATUS 

def set_on(): 
    global CURR_STATUS
    if(CURR_STATUS!=ON_STATUS):
        do_on()
        CURR_STATUS = ON_STATUS

def set_off(): 
    global CURR_STATUS
    if(CURR_STATUS!=OFF_STATUS):
        do_off()
        CURR_STATUS = OFF_STATUS
def set_away(): 
    global CURR_STATUS
    if(CURR_STATUS!=AWAY_STATUS):
        do_away()
        CURR_STATUS = AWAY_STATUS
def set_back(): 
    global CURR_STATUS
    if(CURR_STATUS!=ON_STATUS):
        do_back()
        CURR_STATUS = ON_STATUS

def update_on(): 
    try: 
        mail.send_on()
        main.icon = config.ON_ICON
        main.notify('You are now ONLINE')
    except: 
        main.notify('AN error occured. Contact the developer for details.')
def update_off(): 
    try:
        mail.send_off()
        main.icon = config.OFF_ICON
        main.notify('You are now OFFLINE')
    except: 
        main.notify('AN error occured. Contact the developer for details.')
def update_away(): 
    try:
        mail.send_away()
        main.icon = config.AWAY_ICON
        main.notify('You are now AWAY')
    except: 
        main.notify('AN error occured. Contact the developer for details.')
def update_back(): 
    try: 
        mail.send_back()
        main.icon = config.ON_ICON
        main.notify('You are now BACK ONLINE')
    except: 
        main.notify('AN error occured. Contact the developer for details.')

def do_on(): 
    thread = threading.Thread(target=update_on) 
    thread.start()
def do_off(): 
    thread = threading.Thread(target=update_off) 
    thread.start()
def do_away(): 
    thread = threading.Thread(target=update_away) 
    thread.start()
def do_back(): 
    thread = threading.Thread(target=update_back) 
    thread.start()

menu = pystray.Menu(
    pystray.MenuItem("On", set_on), 
    pystray.MenuItem("Off", set_off),
    pystray.MenuItem("Away", set_away),
    pystray.MenuItem("Back", set_back)
)
main = pystray.Icon(config.APP_NAME, config.OFF_ICON, menu=menu)
main.title = config.APP_NAME
    

if __name__=="__main__": 
    main.run()


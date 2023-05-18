import pystray
import threading 
import logging

import config
from const import *
import mail


CURR_STATUS = OFF_STATUS

logging.basicConfig(filename='./tmp/err.log', level=logging.ERROR, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s') 
logger=logging.getLogger(__name__)

def set_on(): 
    global CURR_STATUS
    if(CURR_STATUS!=ON_STATUS):
        do_on()
        CURR_STATUS = ON_STATUS
        save_status()
def set_off(): 
    global CURR_STATUS
    if(CURR_STATUS!=OFF_STATUS):
        do_off()
        CURR_STATUS = OFF_STATUS
        save_status()
def set_away(): 
    global CURR_STATUS
    if(CURR_STATUS!=AWAY_STATUS):
        do_away()
        CURR_STATUS = AWAY_STATUS
        save_status()
def set_back(): 
    global CURR_STATUS
    if(CURR_STATUS!=ON_STATUS):
        do_back()
        CURR_STATUS = ON_STATUS
        save_status()

def update_on(): 
    try: 
        mail.send_on()
        main.icon = config.ON_ICON
        main.notify('You are now ONLINE')
    except Exception as e: 
        logger.error(e)
        main.notify(e.__str__)
def update_off(): 
    try:
        mail.send_off()
        main.icon = config.OFF_ICON
        main.notify('You are now OFFLINE')
    except Exception as e: 
        logger.error(e)
        main.notify(e.__str__)
def update_away(): 
    try:
        mail.send_away()
        main.icon = config.AWAY_ICON
        main.notify('You are now AWAY')
    except Exception as e: 
        logger.error(e)
        main.notify(e.__str__)
def update_back(): 
    try: 
        mail.send_back()
        main.icon = config.ON_ICON
        main.notify('You are now BACK ONLINE')
    except Exception as e: 
        logger.error(e)
        main.notify(e.__str__)

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

def open_status(): 
    with open(config.STATUS_CACHE, "r") as f: 
        global CURR_STATUS
        CURR_STATUS = int(f.readline())

def save_status(): 
    with open(config.STATUS_CACHE, "w") as f: 
        global CURR_STATUS
        f.write(str(CURR_STATUS))


menu = pystray.Menu(
    pystray.MenuItem("On", set_on), 
    pystray.MenuItem("Off", set_off),
    pystray.MenuItem("Away", set_away),
    pystray.MenuItem("Back", set_back)
)
main = pystray.Icon(config.APP_NAME, config.OFF_ICON, menu=menu)
main.title = config.APP_NAME
    

if __name__=="__main__": 
    try: 
        open_status()
        if(CURR_STATUS==ON_STATUS): main.icon = config.ON_ICON
        if(CURR_STATUS==OFF_STATUS): main.icon = config.OFF_ICON
        if(CURR_STATUS==AWAY_STATUS): main.icon = config.AWAY_ICON

    except Exception as e: 
        logger.error(e)
        
    main.run()


import win32com.client as win32 
import pythoncom
import config
import datetime

def send_on():
    pythoncom.CoInitialize()
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = config.SEND_TO
    mail.Subject = '[Telework] Online'
    mail.HTMLBody = "<h2> "+config.NAME+""" is now ONLINE</h2><p>Reach out via MS Teams or by Email.</p>""" + 'TIMESTAMP: ' + str(datetime.datetime.now()) 
    mail.Send()

def send_off():
    pythoncom.CoInitialize()
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = config.SEND_TO
    mail.Subject = '[Telework] Offline'
    mail.HTMLBody = "<h2> "+config.NAME+""" is now OFFLINE</h2>TIMESTAMP: """ + str(datetime.datetime.now()) 
    mail.Send()

def send_away():
    pythoncom.CoInitialize()
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = config.SEND_TO
    mail.Subject = '[Telework] Away for Lunch/Break/Else'
    mail.HTMLBody = "<h2> "+config.NAME+""" is now AWAY FOR LUNCH/BREAK</h2>""" + 'TIMESTAMP: ' + str(datetime.datetime.now()) 
    mail.Send()

def send_back():
    pythoncom.CoInitialize()
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = config.SEND_TO
    mail.Subject = '[Telework] Back from Lunch/Break/Else'
    mail.HTMLBody = "<h2> "+config.NAME+""" is now BACK ONLINE</h2><p>Reach out via Microsoft Teams or by Email.</p>""" + 'TIMESTAMP: ' + str(datetime.datetime.now()) 
    mail.Send()


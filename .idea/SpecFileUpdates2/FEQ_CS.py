import time
import pyautogui as pg

#print(pg.size())
#print(pyautogui.position())
def cursorPos():
    print(pg.size())
#print cursorPos()

def cursorPos():
    print(pg.position())
#cursorPos()
#login to remote
def login():
    pg.click(3429, 776)
    pg.typewrite("seeds001seeds001")
    pg.press('enter')
#login()

#open spec file
#click coax setup
def openSpec():
    pg.click(3065, 288)
    pg.click(3065, 319)

#openSpec()

#add Genesis Drop
def feqcs():
    pg.press('alt+tab')
    time.sleep(1)
    pg.press('tab')  #eq
    time.sleep(.1)
    pg.press('enter')  #open
    time.sleep(.5)
    pg.press('end')  #end
    time.sleep(.5)
    pg.press('up')  #JXP-EQ
    time.sleep(.5)
    pg.press('tab')  #tab
    pg.press('tab')  # eq
    time.sleep(.1)
    pg.press('enter')  # open
    time.sleep(.5)
    pg.press('end')  # end
    time.sleep(.5)
    pg.press('up')  #up
    time.sleep(.5)
    pg.press('up')  #up JXP-CS
    time.sleep(.5)
    pg.press('tab')  # tab
    time.sleep(.1)
    pg.press('enter')  # open
    time.sleep(.5)
    pg.press('end')  # end
    time.sleep(.5)
    pg.press('tab')  # tab
    pg.press('tab')  # tab
    time.sleep(.1)
    pg.press('enter')  # open
    time.sleep(.5)
    pg.press('down')  # alert user
    time.sleep(.1)
    pg.press('tab')  # tab
    time.sleep(.1)
    pg.press('enter')  # open
    time.sleep(.5)
    pg.press('end')  # end


feqcs()















#print(pyautogui.position())

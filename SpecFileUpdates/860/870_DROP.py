import time
import pyautogui as pg
import keyboard

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

def addDrop870():
    input("Is caps on? Press enter to continue")
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    pg.typewrite('genesis')  # enter new model name
    time.sleep(1)
    pg.press('tab')  # move to tap window
    time.sleep(.1)
    pg.typewrite('99')  # update tap window
    time.sleep(.1)
    pg.press('tab')  # move to RvsWindow
    time.sleep(.1)
    pg.typewrite('8')
    time.sleep(.1)
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')  # move to levels
    time.sleep(.1)
    pg.typewrite('43')
    time.sleep(.1)
    pg.press('tab')
    pg.press('tab')
    time.sleep(.1)
    pg.typewrite('43')
    time.sleep(.1)
    pg.press('tab')
    time.sleep(.1)
    pg.typewrite('12')
    time.sleep(.1)
    pg.press('tab')
    pg.press('tab')
    pg.press('tab')
    pg.typewrite('19')
    pg.press('enter')
    pg.press('enter')
    pg.press('enter')
    pg.press('enter')
    pg.press('enter')
    pg.press('enter')
    pg.press('enter')
    pg.press('enter')

addDrop870()







#print(pyautogui.position())

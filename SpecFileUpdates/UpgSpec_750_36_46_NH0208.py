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
def selectCopy():
    pg.click(1400,370)  #select "Copy"
#Upgrade spec 750-750_7
def upgEQ():
    pg.press('alt+tab')
    time.sleep(1)
    pg.press('numlock')
    #Select "Copy"
    selectCopy()  #start

    #Go to bottom list
    pg.press('down', presses=3)  #Go to EQs
    pg.press('right')
    pg.press('end')
    #copy cable sim
    pg.press('up', presses=2)  #Copy JPX_CS
    pg.press('enter')
    pg.press('enter')

    #Return start next
    selectCopy()

    #Go to bottom list
    pg.press('down', presses=3)  #Go to EQs
    pg.press('right')
    pg.press('end')
    #copy EQ
    pg.press('up', presses=1)  #Copy JPX_EQ
    pg.press('enter')
    pg.press('enter')

    # Return start next
    selectCopy()
    # Go to bottom list
    pg.press('down', presses=3)  # Go to EQs
    pg.press('right')
    pg.press('end')  # Copy SRE-5-85
    # copy EQ
    pg.press('enter')
    pg.press('enter')
upgEQ()
    # Return start next
selectCopy()

def upgPads():
    # Go to bottom list
    pg.press('down', presses=5)  # Go to EQs
    pg.press('right')
    pg.press('end')  # Copy NPB-##0
    pg.press('enter')
    pg.press('enter')
upgPads()
 # Return start next
selectCopy()

def upgAmps():
    # Go to bottom list
    pg.press('right')
    pg.press('end')
    pg.press('up', presses=2)  # genesis actives
    pg.press('enter')
    pg.press('enter')
    selectCopy()
    # Go to bottom list
    pg.press('right')
    pg.press('end')
    pg.press('up', presses=1)  # Arris Nodes_3
    pg.press('enter')
    pg.press('enter')
    selectCopy()
    # Go to bottom list
    pg.press('right')
    pg.press('end')
    # Harmonic Nodes
    pg.press('enter')
    pg.press('enter')
upgAmps()
 # Return start next
selectCopy()

def upgCable():
    # Go to bottom list
    pg.press('down')
    pg.press('right')
    pg.press('end')
    pg.press('up', presses=2)  # new cable
    pg.press('enter')
    pg.press('enter')
    selectCopy()
    # Go to bottom list
    pg.press('down')
    pg.press('right')
    pg.press('end')
    pg.press('up', presses=1)  # New AC Only
    pg.press('enter')
    pg.press('enter')
    selectCopy()
    # Go to bottom list
    pg.press('down')
    pg.press('right')
    pg.press('end')  # Exist AC Only
    pg.press('enter')
    pg.press('enter')
upgCable()
 # Return start next
selectCopy()

def upg2way():
    # Go to bottom list
    pg.press('down', presses=7)
    pg.press('right')
    pg.press('end')
    pg.press('up', presses=2)  # New Couplers
    pg.press('enter')
    pg.press('enter')
    selectCopy()
    # Go to bottom list
    pg.press('down', presses=7)
    pg.press('right')
    pg.press('end')
    pg.press('up', presses=1)  # Power Equipment
    pg.press('enter')
    pg.press('enter')
    selectCopy()
    # Go to bottom list
    pg.press('down', presses=7)
    pg.press('right')
    pg.press('end')  # Internals_G
    pg.press('enter')
    pg.press('enter')
upg2way()
 # Return start next
selectCopy()

def upg3way():
    # Go to bottom list
    pg.press('down', presses=8)
    pg.press('right')
    pg.press('end')  # New Couplers
    pg.press('enter')
    pg.press('enter')
upg3way()
 # Return start next
selectCopy()

def upgPI():
    # Go to bottom list
    pg.press('down', presses=11)
    pg.press('right')
    pg.press('end')  # Power Inserters
    pg.press('enter')
    pg.press('enter')
upgPI()

 # Return start next
selectCopy()
def upgPS():
    # Go to bottom list
    pg.press('down', presses=12)
    pg.press('right')
    pg.press('end')  # Upg PS
    pg.press('up')
    pg.press('enter')
    pg.press('enter')
    selectCopy()
    pg.press('down', presses=12)
    pg.press('right')
    pg.press('end')  # New PS
    pg.press('enter')
    pg.press('enter')
upgPS()
pg.press('numlock')

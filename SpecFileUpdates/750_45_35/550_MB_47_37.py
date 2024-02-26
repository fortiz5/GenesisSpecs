#ask from pick list of MB, LE, MBVT.
    #ask for Frequency
        #HighOutput_Tilt
        #set values


#get things started
import keyboard
import pyautogui as pg
import time


#550_750 Upgrade 47_37


#Start with curor in name field

def MB120_47_T10():
    MB120_47_T10_rename()
    MB120_47_T10_heside()
    MB120_47_T10_ds1()
    MB120_47_T10_ds1()
    MB_pwr()
    MB_fgain10()
    fpads_i5()
    # Interstage
    #print("Interstage = 0")
    #input("Press enter to continue")
    #keyboard.press_and_release('alt+tab')
    time.sleep(2)
    rgainlng()
    rpads()



#rename
def MB120_47_T10_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('MB120_47_T10')
#HE Side
def MB120_47_T10_heside():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('42')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('42')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('10.4')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('10.8')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('10.9')
#Update DS side 1
def MB120_47_T10_ds1():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('18')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('18')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('37')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('44.3')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('47.2')


#update DS2
def ds2():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('18')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('18')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('35')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('42.3')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('45.2')
#powering
def MB_pwr():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.97')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.81')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.76')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.66')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.67')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.67')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('45')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('55')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('60')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('70')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('80')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('90')

def BLE_pwr():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.74')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.67')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.66')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.63')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.60')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('.54')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('45')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('55')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('60')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('70')
    keyboard.press_and_release('tab')
    keyboard.write('80')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('90')
#UPDATE GAIN
def MB_fgain10():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('41.2')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('10.2')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')

def MB_fgain14():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('41.2')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('13.8')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')

def rgainlng():
    keyboard.press_and_release('tab')
    keyboard.write('24')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    keyboard.write('0')
def fpads_i5():
    pg.press('numlock')
    pg.press('tab')  #eq
    time.sleep(.01)
    pg.press('enter')  #open
    time.sleep(.01)
    pg.press('end')  #end
    time.sleep(.01)
    pg.press('up')  #JXP-EQ
    time.sleep(.01)
    pg.press('tab')  # eq
    time.sleep(.01)
    pg.press('enter')  # open
    time.sleep(.01)
    pg.press('end')  # end
    time.sleep(.01)
    pg.press('up')  #up
    time.sleep(.01)
    pg.press('up')  #up JXP-CS
    time.sleep(.01)
    pg.press('tab')  # tab
    time.sleep(.01)
    pg.press('enter')  # open
    time.sleep(.01)
    pg.press('end')  # end fpad
    time.sleep(.01)
    pg.press('tab')  # tab
    time.sleep(.01)
    pg.press('enter')  # open
    time.sleep(.01)
    pg.press('home')  # none inter eq
    time.sleep(.01)
    pg.press('tab')  # tab
    pg.press('enter')  # open
    time.sleep(.01)
    pg.press('home')
    time.sleep(.01)
    pg.press('down')  #alert user
    time.sleep(.01)
    pg.press('tab')  # tab
    time.sleep(.01)
    pg.press('enter')  # open npb
    time.sleep(.01)
    pg.press('end')  # end
    time.sleep(.01)
    pg.press('tab')  # tab
    time.sleep(.01)
    pg.press('enter')  # open interstage
    time.sleep(.01)
    pg.press('home') #to the top
    time.sleep(.01)
    pg.press('down') #00
    time.sleep(.01)
    pg.press('down') #01
    time.sleep(.01)
    pg.press('down')  #02
    time.sleep(.01)
    pg.press('down')  #03
    time.sleep(.01)
    pg.press('down')  #04
    time.sleep(.01)
    pg.press('down')  #05
    time.sleep(.01)
    #pg.press('down')  #06
    #time.sleep(.01)
    pg.press('enter')
    pg.press('numlock')
def rpads():
    time.sleep(.01)
    pg.press('tab')  #req
    time.sleep(.01)
    pg.press('enter')  #open
    time.sleep(.01)
    pg.press('numlock')
    time.sleep(.01)
    pg.press('end')  #end
    time.sleep(.01)
    pg.press('tab')  #tab
    time.sleep(.01)
    pg.press('enter')  # open
    time.sleep(.01)
    pg.press('end')  # end
    time.sleep(.01)
    pg.press('tab')  # tab
    pg.press('tab')  # eq
    pg.press('tab')  # tab
    pg.press('tab')  # eq
    pg.press('numlock')

#Reverse Gain options



MB120_47_T10()
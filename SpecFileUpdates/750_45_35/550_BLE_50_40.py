#ask from pick list of MB, LE, MBVT.
    #ask for Frequency
        #HighOutput_Tilt
        #set values


#get things started
import keyboard
import pyautogui as pg
import time


#550-750UG 50_40
#BLE120_54_T14

#Start with curor in name field

def BLE120_54_T14():
    BLE120_54_T14_rename()
    BLE120_54_T14_heside()
    BLE120_54_T14_ds1()
    BLE_pwr()
    BLE_fgain14()
    # Interstage
    #print("Interstage = 0")
    #input("Press enter to continue")
    #keyboard.press_and_release('alt+tab')
    time.sleep(2)
    fpads_i0()
    rgainlng()
    rpads()




#rename
def BLE120_54_T14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('BLE120_54_T14')
#HE Side
def BLE120_54_T14_heside():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('42')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    #keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    keyboard.write('42')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('7.7')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    #keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    keyboard.write('13.1')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('15.2')
#Update DS side 1
def BLE120_54_T14_ds1():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('18')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    #keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    keyboard.write('18')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('40')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    #keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    keyboard.write('49.8')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('53.8')


#update DS2
def ds2():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('18')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('18')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('35')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('42.3')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('45.2')
#powering
def MB_pwr():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.97')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.81')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.76')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.66')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.67')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.67')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('45')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('55')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('60')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('70')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('80')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('90')

def BLE_pwr():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.74')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.67')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.66')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.63')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.60')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('.54')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('45')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('55')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('60')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('70')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('80')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('90')
#UPDATE GAIN
def mb_fgain10():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('41.2')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('10.2')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')

def BLE_fgain10():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('34.5')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('10.2')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')

def BLE_fgain12():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('34.5')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('12.6')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')

def BLE_fgain14():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('34.5')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('13.8')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
#Reverse Gain options
def fpads_i0():
    pg.press('numlock')
    pg.press('tab')  #eq
    time.sleep(.2)
    pg.press('enter')  #open
    time.sleep(.2)
    pg.press('end')  #end
    time.sleep(.2)
    pg.press('up')  #JXP-EQ
    time.sleep(.2)
    pg.press('tab')  # eq
    time.sleep(.2)
    pg.press('enter')  # open
    time.sleep(.2)
    pg.press('end')  # end
    time.sleep(.2)
    pg.press('up')  #up
    time.sleep(.2)
    pg.press('up')  #up JXP-CS
    time.sleep(.2)
    pg.press('tab')  # tab
    time.sleep(.2)
    pg.press('enter')  # open
    time.sleep(.2)
    pg.press('end')  # end fpad
    time.sleep(.2)
    pg.press('tab')  # tab
    time.sleep(.1)
    pg.press('enter')  # open
    time.sleep(.2)
    pg.press('home')  # none inter eq
    time.sleep(.2)
    pg.press('tab')  # tab
    pg.press('enter')  # open
    time.sleep(.2)
    pg.press('home')
    time.sleep(.2)
    pg.press('down')  #alert user
    time.sleep(.1)
    pg.press('tab')  # tab
    time.sleep(.2)
    pg.press('enter')  # open npb
    time.sleep(.2)
    pg.press('end')  # end
    time.sleep(.1)
    pg.press('tab')  # tab
    time.sleep(.2)
    pg.press('enter')  # open interstage
    time.sleep(.2)
    pg.press('home') #to the top
    time.sleep(.2)
    pg.press('down') #00
    time.sleep(.2)
    #pg.press('down') #01
    #time.sleep(.2)
    #pg.press('down')  #02
    #time.sleep(.2)
    #pg.press('down')  #03
    #time.sleep(.2)
    #pg.press('down')  #04
    #time.sleep(.2)
    #pg.press('down')  #05
    #time.sleep(.2)
    #pg.press('down')  #06
    #time.sleep(.2)
    pg.press('enter')
    pg.press('numlock')
def rgainlng():
    keyboard.press_and_release('tab')
    keyboard.write('24')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    keyboard.write('0')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    keyboard.write('0')
def rpads():
    time.sleep(.1)
    pg.press('tab')  #req
    time.sleep(.1)
    pg.press('enter')  #open
    time.sleep(.2)
    pg.press('numlock')
    time.sleep(.2)
    pg.press('end')  #end
    time.sleep(.2)
    pg.press('tab')  #tab
    time.sleep(.1)
    pg.press('enter')  # open
    time.sleep(.2)
    pg.press('end')  # end
    time.sleep(.2)
    pg.press('tab')  # tab
    pg.press('tab')  # eq
    pg.press('tab')  # tab
    pg.press('tab')  # eq
    pg.press('numlock')
BLE120_54_T14()
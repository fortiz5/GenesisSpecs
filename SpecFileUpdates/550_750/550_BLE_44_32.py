#ask from pick list of MB, LE, MBVT.
    #ask for Frequency
        #HighOutput_Tilt
        #set values


#get things started
import keyboard
import time
import pyautogui as pg

#5FREQ_550 44_30 (44_32)
#BLE120_44_T12

#Start with curor in name field

def BLE120_44_T12():
    BLE120_44_T12_rename()
    heside_550()
    ds_550()
    BLE_pwr()
    BLE_fgain12()
    fpads_i6()
    # Interstage
    #print("Interstage = 8")
    #input("Press enter to continue")
    #keyboard.press_and_release('alt+tab')
    time.sleep(2)
    rgainlng()
    rpads()




#rename
def BLE120_44_T12_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('BLE120_44_T12')
#HE Side
def heside_550():
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
    keyboard.write('42')  #HES 5
    keyboard.press_and_release('tab')
    time.sleep(.01)
    #keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    keyboard.write('42')  #HES 40
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('9.7')  #HES 54
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('14.2')   #HES 550
    keyboard.press_and_release('tab')
    time.sleep(.01)
    #keyboard.write('14.9')  #HES 625
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    keyboard.write('16.1')  # HES 750
#Update DS side 1
def ds_550():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('18')  #DS 5
    keyboard.press_and_release('tab')
    time.sleep(.01)
    #keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    keyboard.write('18')  #DS 40
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('32')  #DS 54
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('41.0')  #DS 550
    keyboard.press_and_release('tab')
    time.sleep(.01)
    #keyboard.write('44.6')  #DS 625
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    keyboard.write('44.6')  #DS 750


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
    time.sleep(.01)
    keyboard.write('80')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('90')
#UPDATE GAIN
def mb_fgain10():
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

def BLE_fgain10():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('34.5')
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

def BLE_fgain12():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('34.5')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('12.0')
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

def BLE_fgain14():
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('34.5')
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


def fpads_i6():
    pg.press('numlock')
    pg.press('tab')  #eq
    time.sleep(.2)
    pg.press('enter')  #open
    time.sleep(.01)
    pg.press('end')  #end
    time.sleep(.01)
    pg.press('up')  #JXP-EQ
    time.sleep(.01)
    pg.press('tab')  # eq
    time.sleep(.2)
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
    time.sleep(.2)
    pg.press('down')  #alert user
    time.sleep(.01)
    pg.press('tab')  # tab
    time.sleep(.2)
    pg.press('enter')  # open npb
    time.sleep(.01)
    pg.press('end')  # end
    time.sleep(.01)
    pg.press('tab')  # tab
    time.sleep(.2)
    pg.press('enter')  # open interstage
    time.sleep(.2)
    pg.press('home') #to the top
    time.sleep(.2)
    pg.press('down') #00
    time.sleep(.2)
    pg.press('down') #01
    time.sleep(.2)
    pg.press('down')  #02
    time.sleep(.2)
    pg.press('down')  #03
    time.sleep(.2)
    pg.press('down')  #04
    time.sleep(.2)
    pg.press('down')  #05
    time.sleep(.2)
    pg.press('down')  #06
    time.sleep(.2)
    #pg.press('down')  # 07
    #time.sleep(.2)
    #pg.press('down')  # 08
    #time.sleep(.2)
    pg.press('enter')
    pg.press('numlock')



#Reverse Gain options

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

def rpads():
    pg.press('numlock')
    pg.press('tab')  #req
    time.sleep(.01)
    pg.press('enter')  #open
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

BLE120_44_T12()
#ask from pick list of MB, LE, MBVT.
    #ask for Frequency
        #HighOutput_Tilt
        #set values


#get things started
import keyboard
import pyautogui as pg
import time


#5 FREQ 5,40,54,550,750 convert 52/38
#MB120_54_T14

#Start with curor in name field

def MB120_54_T14():

    MB120_54_T14_rename()
    heside_550()
    ds_550()
    ds_550()
    MB_pwr()
    MB_fgain14()
    fpads_i0()
    # Interstage
    #print("Interstage = 2")
    #input("Press enter to continue")
    #keyboard.press_and_release('alt+tab')
    time.sleep(2)
    rgainlng()
    rpads()



#rename
def MB120_54_T14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('MB120_54_T14')
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
    keyboard.write('8.4')  #HES 54
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('11.3')   #HES 550
    keyboard.press_and_release('tab')
    time.sleep(.01)
    #keyboard.write('8.8')  #HES 625
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    keyboard.write('12.5')  # HES 750
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
    keyboard.write('40')  #DS 54
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('49.8')  #DS 550
    keyboard.press_and_release('tab')
    time.sleep(.01)
    #keyboard.write('48.3')  #DS 625
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    keyboard.write('53.8')  #DS 750



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
def fgain10():
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
def MB_fgain12():
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
def fpads_i0():
    pg.press('numlock')
    pg.press('tab')  #eq
    time.sleep(.1)
    pg.press('enter')  #open
    time.sleep(.1)
    pg.press('end')  #end
    time.sleep(.1)
    pg.press('up')  #JXP-EQ
    time.sleep(.1)
    pg.press('tab')  # eq
    time.sleep(.1)
    pg.press('enter')  # open
    time.sleep(.1)
    pg.press('end')  # end
    time.sleep(.1)
    pg.press('up')  #up
    time.sleep(.1)
    pg.press('up')  #up JXP-CS
    time.sleep(.1)
    pg.press('tab')  # tab
    time.sleep(.1)
    pg.press('enter')  # open
    time.sleep(.1)
    pg.press('end')  # end fpad
    time.sleep(.1)
    pg.press('tab')  # tab
    time.sleep(.01)
    pg.press('enter')  # open
    time.sleep(.1)
    pg.press('home')  # none inter eq
    time.sleep(.1)
    pg.press('tab')  # tab
    pg.press('enter')  # open
    time.sleep(.1)
    pg.press('home')
    time.sleep(.1)
    pg.press('down')  #alert user
    time.sleep(.01)
    pg.press('tab')  # tab
    time.sleep(.1)
    pg.press('enter')  # open npb
    time.sleep(.1)
    pg.press('end')  # end
    time.sleep(.01)
    pg.press('tab')  # tab
    time.sleep(.1)
    pg.press('enter')  # open interstage
    time.sleep(.1)
    pg.press('home') #to the top
    time.sleep(.1)
    pg.press('down') #00
    time.sleep(.1)
    #pg.press('down') #01
    #time.sleep(.1)
    #pg.press('down')  #02
    #pg.press('down')  #03
    #time.sleep(.1)
    #time.sleep(.1)
    #pg.press('down')  #04
    #time.sleep(.1)
    #pg.press('down')  #05
    #time.sleep(.1)
    #pg.press('down')  #06
    #time.sleep(.1)
    #pg.press('down')  # 07
    #time.sleep(.1)
    #pg.press('down')  # 08
    #time.sleep(.1)
    #pg.press('down')  # 09
    #time.sleep(.1)
    #pg.press('down')  # 10
    time.sleep(.1)
    pg.press('enter')
    pg.press('numlock')
def rpads():
    time.sleep(.01)
    pg.press('tab')  #req
    time.sleep(.01)
    pg.press('enter')  #open
    time.sleep(.1)
    pg.press('numlock')
    time.sleep(.1)
    pg.press('end')  #end
    time.sleep(.1)
    pg.press('tab')  #tab
    time.sleep(.01)
    pg.press('enter')  # open
    time.sleep(.1)
    pg.press('end')  # end
    time.sleep(.1)
    pg.press('tab')  # tab
    pg.press('tab')  # eq
    pg.press('tab')  # tab
    pg.press('tab')  # eq
    pg.press('numlock')
#Reverse Gain options


#####Nodes
def OM6K_1X2_50_T14():
    OM6K_1X2_50T_14_rename()
    node_heside()
    MB120_54_T14_ds1()
    MB120_54_T14_ds1()

def OM6K_1X2_50T_14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('OM6K 1X2_50_T14')
def node_heside():
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
    keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')


def OM6K_2X4_50_T14():
    OM6K_2X4_50_T14_rename()
    node_heside()
    MB120_54_T14_ds1()


def OM6K_2X4_50_T14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('OM6K 2X4_50_T14')

###Harmonic Nodes

def COS_RPL_1X2_50_T14():
    COS_RPL_1X2_50T_14_rename()
    node_heside()
    MB120_54_T14_ds1()
    MB120_54_T14_ds1()
def COS_RPL_1X2_50T_14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('COS-RPL 1X2_50_T14')

def node_heside():
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
    keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.01)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('0')

def COS_RPL_2x4_50_T14():
    COS_RPL_2x4_50_T14_rename()
    node_heside()
    MB120_54_T14_ds1()
def COS_RPL_2x4_50_T14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.press_and_release('tab')
    time.sleep(.01)
    keyboard.write('COS-RPL 2X4_50_T14')




MB120_54_T14()
#OM6K_1X2_50_T14()
#OM6K_2X4_50_T14()
#COS_RPL_1X2_50_T14()
#COS_RPL_2x4_50_T14()

def node_1x2():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    ds_625()
    ds_625()

#node_1x2()
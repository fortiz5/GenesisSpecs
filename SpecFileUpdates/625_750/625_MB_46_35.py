#ask from pick list of MB, LE, MBVT.
    #ask for Frequency
        #HighOutput_Tilt
        #set values


#get things started
import keyboard
import pyautogui as pg
import time

##################not updated
#6 FREQ 625 45_35
#MB120_45_T10

#Start with curor in name field

def MB120_45_T10():
    MB120_45_T10_rename()
    heside_625()
    ds_625()
    ds_625()
    MB_pwr()
    MB_fgain10()
    fpads_i7()
    # Interstage
    #print("Interstage = 7")
    #input("Press enter to continue")
    #keyboard.press_and_release('alt+tab')
    time.sleep(2)
    rgainlng()
    rpads()



#rename
def MB120_45_T10_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('MB120_45_T10')
#HE Side

def heside_625():
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
    keyboard.write('42')  #HES 5
    keyboard.press_and_release('tab')
    time.sleep(.1)
    #keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    keyboard.write('42')  #HES 40
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('10.4')  #HES 54
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('10.8')   #HES 550
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('10.8')  #HES 625
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('10.9')  # HES 750
#Update DS side 1
def ds_625():
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('18')  #DS 5
    keyboard.press_and_release('tab')
    time.sleep(.1)
    #keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    keyboard.write('18')  #DS 40
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('35')  #DS 54
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('43.1')  #DS 550
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('44.3')  #DS 625
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('46.4')  #DS 750



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
    keyboard.write('80')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('90')
#UPDATE GAIN
def fgain10():
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

def MB_fgain10():
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
def fpads_i7():
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
    pg.press('down')  # 07
    #time.sleep(.2)
    #pg.press('down')  # 08
    #time.sleep(.2)
    #pg.press('down')  # 09
    #time.sleep(.2)
    #pg.press('down')  # 10
    time.sleep(.2)
    pg.press('enter')
    pg.press('numlock')
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
#Reverse Gain options


#####Nodes
def OM6K_1X2_50_T14():
    OM6K_1X2_50T_14_rename()
    node_heside()
    MB120_45_T10_ds1()
    MB120_45_T10_ds1()

def OM6K_1X2_50T_14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('OM6K 1X2_50_T14')
def node_heside():
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
    keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')


def OM6K_2X4_50_T14():
    OM6K_2X4_50_T14_rename()
    node_heside()
    MB120_45_T10_ds1()


def OM6K_2X4_50_T14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('OM6K 2X4_50_T14')

###Harmonic Nodes

def COS_RPL_1X2_50_T14():
    COS_RPL_1X2_50T_14_rename()
    node_heside()
    MB120_45_T10_ds1()
    MB120_45_T10_ds1()
def COS_RPL_1X2_50T_14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('COS-RPL 1X2_50_T14')

def node_heside():
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
    keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    #keyboard.press_and_release('tab')
    #time.sleep(.1)
    #keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('0')

def COS_RPL_2x4_50_T14():
    COS_RPL_2x4_50_T14_rename()
    node_heside()
    MB120_45_T10_ds1()
def COS_RPL_2x4_50_T14_rename():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.press_and_release('tab')
    time.sleep(.1)
    keyboard.write('COS-RPL 2X4_50_T14')




#not updatedMB120_45_T10()
#OM6K_1X2_50_T14()
#OM6K_2X4_50_T14()
#COS_RPL_1X2_50_T14()
#COS_RPL_2x4_50_T14()
def node_1x2():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)
    ds_625()
    ds_625()

node_1x2()
import time
import keyboard
import pyautogui as pg

def ampBlock():
    #keyboard.press_and_release('alt+tab')
    #time.sleep(2)
    pg.press('alt+tab')
    time.sleep(1)
    pg.click(3095, 423)  #des 1
    time.sleep(.1)
    pg.click(3398, 421)  #ampname
    time.sleep(.1)
    pg.click(3325, 734)  #set fill-in 1
    time.sleep(.1)
    pg.click(3089, 445)  #des 2
    time.sleep(.1)
    pg.click(3678, 663)  #scroll
    time.sleep(.1)
    pg.click(3416, 578)  #model name
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
    time.sleep(.1)
    pg.click(3043, 464)  #des 3
    time.sleep(.1)
    pg.click(3678, 663)  # scroll
    time.sleep(.1)
    pg.click(3386, 654)  #user5
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
    time.sleep(.1)
    pg.click(3080, 483)  # des 4
    time.sleep(.1)
    pg.click(3380, 673)  # user6
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
    time.sleep(.1)
    pg.click(3080, 501)  # des 5
    time.sleep(.1)
    pg.click(3380, 689)  # user7
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
    time.sleep(.1)
    pg.click(3080, 519)  # des 6
    time.sleep(.1)
    pg.click(3386, 578)  # user1
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
    time.sleep(.1)
    pg.click(3080, 538)  # des 7
    time.sleep(.1)
    pg.click(3380, 595)  # user2
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
    time.sleep(.1)
    pg.click(3080, 558)  # des 8
    time.sleep(.1)
    pg.click(3380, 613)  # user3
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
    time.sleep(.1)
    pg.click(3080, 578)  # des 9
    time.sleep(.1)
    pg.click(3380, 634)  # user4
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
    time.sleep(.1)
    pg.click(3080, 598)  # des 10
    time.sleep(.1)
    pg.click(3380, 500)  # ps name
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
    time.sleep(.1)
    pg.click(3080, 618)  # des 11
    time.sleep(.1)
    pg.click(3380, 539)  # voltage
    time.sleep(.1)
    pg.click(3325, 734)  # set fill-in
#ampBlock()


def ampBlock2():
    pg.press('alt+tab')
    time.sleep(1)


def holdsetfillin1():
    rtn_next()
    set_fillin2()
    rtn_next()
    set_fillin3()
    rtn_next()
    set_fillin4()
    rtn_next()
    set_fillin5()
    rtn_next()
    set_fillin6()
    rtn_next()
    set_fillin7()
    rtn_next()
    set_fillin8()
    rtn_next()
    set_fillin9()
    rtn_next()
    set_fillin10()
    rtn_next()
    set_fillin11()

def setfillin1():
    pg.press('tab', presses=2)
    time.sleep(.1)
    pg.press('home')  # amp name
    time.sleep(.1)
def rtn_next():
    pg.press('tab')
    time.sleep(.1)
    pg.press('enter')  # set fill in
    time.sleep(.1)
    pg.press('shift+tab')
    time.sleep(.1)
    pg.press('shift+tab')
    time.sleep(.1)
    pg.press('down') # move to next dest
    time.sleep(.1)
    pg.press('tab')
    time.sleep(.1)
def set_fillin2():
    pg.press('home')  # model name
    time.sleep(.1)
    pg.press('pagedown',presses=2)
    time.sleep(.1)
    pg.press('up', presses=5)
    time.sleep(.1)
def set_fillin3(): # user 5
    pg.press('home')  # move to fill-in top of list
    time.sleep(.1)
    pg.press('pagedown',presses=3)
    time.sleep(.1)
def set_fillin4(): # user 6
    pg.press('home')  # move to fill-in top of list
    time.sleep(.1)
    pg.press('pagedown',presses=3)
    time.sleep(.1)
    pg.press('down', presses=1)
def set_fillin5(): # user 7
    pg.press('home')  # move to fill-in top of list
    time.sleep(.1)
    pg.press('pagedown',presses=3)
    time.sleep(.1)
    pg.press('down', presses=2)
def set_fillin6(): # user 1
    pg.press('home')  # move to fill-in top of list
    time.sleep(.1)
    pg.press('pagedown',presses=3)
    time.sleep(.1)
    pg.press('up', presses=4)
def set_fillin7(): # user 2
    pg.press('home')  # move to fill-in top of list
    time.sleep(.1)
    pg.press('pagedown',presses=3)
    time.sleep(.1)
    pg.press('up', presses=3)
def set_fillin8(): # user 3
    pg.press('home')  # move to fill-in top of list
    time.sleep(.1)
    pg.press('pagedown',presses=3)
    time.sleep(.1)
    pg.press('up', presses=2)
def set_fillin9(): # user 4
    pg.press('home')  # move to fill-in top of list
    time.sleep(.1)
    pg.press('pagedown',presses=3)
    time.sleep(.1)
    pg.press('up', presses=1)
def set_fillin10(): # PS name
    pg.press('home')  # move to fill-in top of list
    time.sleep(.1)
    pg.press('pagedown',presses=3)
    time.sleep(.1)
    pg.press('up', presses=8)
def set_fillin11(): # voltage
    pg.press('home')  # move to fill-in top of list
    time.sleep(.1)
    pg.press('pagedown',presses=3)
    time.sleep(.1)
    pg.press('up', presses=6)


ampBlock2()




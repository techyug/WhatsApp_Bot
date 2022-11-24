import pyautogui as pt
import pyperclip
import time
from cv2 import imread
from gui_automation import GuiAuto
gcurser = GuiAuto()

time.sleep(1)
# this function reads the message after clicking on unread chat


def copymsg():
    msg = ""
    if(pt.locateOnScreen('1ur.png', 0.8)):
        print("1 unread messege detected")
        pt.moveTo(pt.locateOnScreen('1ur.png', 0.8))
        if (pt.locateOnScreen('smiley.png', 0.8)):
            sml = pt.locateOnScreen('smiley.png', 0.8)
            pt.moveTo(sml)
            pt.moveTo((sml[0]+30), (sml[1]-90))
            pt.tripleClick((sml[0]+30), (sml[1]-90))
            pt.hotkey('ctrl', 'c')
            msg = pyperclip.paste()

            pt.moveTo(sml)

            pt.moveTo((sml[0]+200), (sml[1]))

            pt.click()
        else:
            msg = ""
            print("whatsapp is not visible completely")
    else:
        print("No masseges Detected!")

    if (str(msg).lower() == 'good morning'):
        pt.typewrite('good morning ', 0.01)
        pt.press('enter')

    elif (str(msg).lower() == 'good evening'):
        pt.typewrite('good evening ', 0.01)
        pt.press('enter')
    else:
        print("Unknown Massege detected!")

    if((pt.locateOnScreen('1ur.png', 0.8))):
        checkfornewmsg()

    else:
        time.sleep(10)
        if((pt.locateOnScreen('1ur.png', 0.8))):
            checkfornewmsg()
        else:
            print("Rescaning in 10 seconds")
            time.sleep(10)
        copymsg()

# it will find unread messages on screen


def checkfornewmsg():
    if (pt.locateOnScreen('1ur.png', 0.8)):
        ur2 = (pt.locateOnScreen('1ur.png', 0.8))
        pt.moveTo(ur2)
        pt.moveRel(-50, 1)
        pt.click()

        copymsg()

# this function will check messages on confirming


def afcking():
    ur = pt.confirm('Want to check for unread masegges', buttons=['yes', 'no'])
    if ur == 'yes':
        checkfornewmsg()
    else:
        pt.alert('No problem')

# this function will run when user enters name and password


def openwhatsapp():
    # pt.click(pt.locateOnScreen('win11.png',0.8))
    pt.press('win')
    time.sleep(0.1)
    pt.typewrite('whatsapp', 0.01)
    pt.press('enter')
    time.sleep(5)
    afcking()


def start():
    pt.confirm('Enter option.', buttons=['Enter name', 'Enter password'])
    usrnm = pt.prompt('What is your name?')
    if usrnm == 'yogendra':
        usrpw = pt.password('Enter password?')
        if usrpw == 'naman':
            pt.alert('logged in successfuly')
            openwhatsapp()
        else:
            pt.alert('wrong password')
            cf = pt.confirm('want to try again?.', buttons=['yes', 'no'])
            if cf == 'yes':
                start()
            else:
                pt.alert('Thankyou')
    else:

        pt.alert('Wrong User Name')

        print("Wrong user name ")


start()
print("program started")

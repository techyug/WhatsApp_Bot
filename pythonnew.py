import time
import pyautogui as pt
import pyperclip


def copymsg():
    print(pt.locateOnScreen('smiley.png', 0.8))
    sml = pt.locateOnScreen('smiley.png', 0.8)
    pt.moveTo(sml)
    pt.moveTo(sml[0], (sml[1]-70))
    pt.tripleClick(sml[0], (sml[1]-70))
    pt.hotkey('ctrl', 'c')
    msg = pyperclip.paste()
    if str(msg).lower() == 'g evening' or str(msg).lower() == 'good evening' or str(msg).lower() == 'very good evening':
        reply = 'good evening sir/mam  : autobot'
        pyperclip.copy(reply)
        pt.hotkey('ctrl', 'v')
        pt.press('enter')
    elif str(msg).lower() == 'g morning' or str(msg).lower() == 'good morning' or str(msg).lower() == 'good moring bhai' or str(msg).lower() == 'very good evening':
        reply = 'Very Good Morning sir/mam  : autobot'
        pyperclip.copy(reply)
        pt.hotkey('ctrl', 'v')
        pt.press('enter')
    else:
        reply = 'please wait yogendra will reply soon : autobot'
        pyperclip.copy(reply)
        pt.hotkey('ctrl', 'v')
        pt.press('enter')


copymsg()

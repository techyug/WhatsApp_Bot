import pyautogui as pt
if(pt.locateOnScreen('1ur.png', 0.8)):
    print("1 unread messege detected")
else:
    print("Not detected")
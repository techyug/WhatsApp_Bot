from cv2 import imread
from gui_automation import GuiAuto
gcurser = GuiAuto()
def ckmsg():
    if gcurser.detect(imread('.\1ur.png'),0.8):
        print(1)
    else:
        print(0)
ckmsg()

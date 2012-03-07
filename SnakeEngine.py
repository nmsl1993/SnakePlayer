import Tkinter  
import Image
import ScreenShotTaker as sst
import KeyPresser as kp
import os
from time import sleep

# open a SPIDER image and convert to byte format
#im = Image.open('pbj.jpeg')

os.system('opera https://apps.facebook.com/mj-snake/?tr=0U01&ref=ts')
sleep
im= sst.getLinuxScreenshot()

#im.show()

sleep(5)

count = 0
while True:
    sleep(1.2)
    if count % 4 == 0:
        kp.keypress('d')
    elif count % 4 == 1:
        kp.keypress('s')
    elif count % 4 == 2:
        kp.keypress('a')
    elif count % 4 == 3:
        kp.keypress('w')
    count += 1




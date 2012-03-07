import Tkinter  
import Image
import ScreenShotTaker as sst
import KeyPresser as kp
import os
import cv
from time import sleep
import ImageRecognitionEngine as ire
# open a SPIDER image and convert to byte format
#im = Image.open('pbj.jpeg')


os.system('opera https://apps.facebook.com/mj-snake/?tr=0U01&ref=ts')
sleep
im= sst.getLinuxScreenshot()

cv_im = ire.toCVImg(im)
cv_im = ire.findRectangle(cv_im, 385, 120, 720, 450 )
cv.SaveImage("foo.png", cv_im)


#sleep(5)
'''
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
'''



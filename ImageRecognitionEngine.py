import cv
import Image
def toCVImg(pil_img):
    cv_img = cv.CreateImageHeader(pil_img.size, cv.IPL_DEPTH_8U, 3)  # RGB image
    cv.SetData(cv_img, pil_img.tostring(), pil_img.size[0]*3)
    return cv_img
def toPILImg(cv_im):
    pi = Image.fromstring("L", cv.GetSize(cv_im), cv_im.tostring())
    return pi

def findRectangle(cv_im, x, y, width, height):
    sub = cv.GetSubRect(cv_im, (x, y, width, height))  # sub is 32x32 patch within img
    #cv.SetZero(sub)
    return sub 
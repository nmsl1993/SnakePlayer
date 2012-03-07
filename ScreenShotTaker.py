import gtk.gdk
import pyscreenshot as ig

import Image

def pixbuf2Image(pb):
    width,height = pb.get_width(),pb.get_height()
    return Image.fromstring("RGB",(width,height),pb.get_pixels() ) 

def getLinuxScreenshot():
    return ig.grab()

'''
    w  = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    #print "The size of the window is %d x %d" % sz
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        return pixbuf2Image(pb)
        #return pb
    else:
        print "Unable to get the screenshot."
'''

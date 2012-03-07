import os

def keypresses(*kps):
    for kp in kps:
        keypress(kp)   
def keypress(k):
    st = 'xte' + " \"key " + k + "\""
    os.system(st)

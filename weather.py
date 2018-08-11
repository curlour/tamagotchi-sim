import pygame, sys
import os
from pygame.locals import *
import time

def chktime(avars):
    if 2 < int(time.strftime("%m")) < 6:
        s = 0
        c = 5
        r = 7
    elif 5 < int(time.strftime("%m")) < 9:
        s = 1
        c = 7
        r = 8
    elif 8 < int(time.strftime("%m")) < 12:
        s = 2
        c = 2
        r = 5
    else:
        s = 3
        c = 3
        r = 6
    if 6 < int(avars[3][6][:2]) < 17:
        tm = 0
    elif int(avars[3][6][:2]) < 19:
        tm = 1
    else:
        tm = 2
    y = time.strftime("%y")
    m = time.strftime("%m")
    d = time.strftime("%d")
    w1 = str(int(y[len(y) - 1]) + (int(m[len(m) - 1]) * int(d[len(d) - 1])))
    w2 = str(int(w1[len(w1) - 1]) + tm)
    if int(w2[len(w2) - 1]) < c:
        w = 0
    elif int(w2[len(w2) - 1]) < r:
        w = 1
    else:
        w = 2
    return s, tm, w

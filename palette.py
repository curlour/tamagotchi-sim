import pygame, sys
import os
from pygame.locals import *
import time
from random import *

def palch(img, g, opal):
    
    def sec(pal, cc):
        l = [0, 1, 2]
        l.pop(l.index(cc))
        for i in range(2, 32):
            c = [pal[i][0], pal[i][1], pal[i][2]]
            c[l[0]], c[l[1]] = c[l[1]], c[l[0]]
            c.append(255)
            pal[i] = tuple(c)
        return(pal)
    
    def opp(pal, opal):
        e = opal.index((0, 255, 255, 255))
        opal = opal[:e]
        for i in range(2, 32):
            if pal[i] in opal:
                p = opal.index(pal[i]) + 1
                try:
                    pal[i] = opal[p]
                except:
                    pass
        return(pal)

    if g < 0:
        g = 4294967296 + g

    pal = img.get_palette()
    pal = list(pal)

    for i in range(2, 32):
        if pal[i] in opal:
            n = opal.index(pal[i])
            if n % 2:
                pal.pop(i)
    
    i = 0
    for c in pal:
        if c in [(0, 153, 238, 255), (255, 102, 0, 255), (0, 0, 100, 255)]:
            break
        i += 1

    pal[i], pal[1] = pal[1], pal[i]

    gc = '%08x' % g
    gl = [(gc[0] == 'f'), (gc[1] == 'f'), (gc[2] == 'f')]

    tot = [0, 0, 0]
    for c in range(opal.index((0, 255, 255, 255))):
        if (c % 2) == (sum(gl) > 1):
            tot[0] += opal[c][0]
            tot[1] += opal[c][1]
            tot[2] += opal[c][2]

    if sum(gl) > 1:
        pal = opp(pal, opal)
    if 0 < sum(gl) < 3:
        if sum(gl) == 1:
            lc = gl.index(1)
            cl = tot.index(max(tot))
        else:
            lc = gl.index(0)
            cl = tot.index(min(tot))
        if cl == lc:
            cc = cl
        else:
            l = [0, 1, 2]
            l.pop(l.index(cl))
            l.pop(l.index(lc))
            cc = l[0]
        pal = sec(pal, cc)

    if gc[3] in ['f', '0', 'a']:
        pal[1] = [(0, 153, 238, 255), (255, 102, 0, 255), (0, 0, 100, 255)][['f', '0', 'a'].index(gc[3])]

    pal[i], pal[1] = pal[1], pal[i]

    img.set_palette(pal)

    return(img)

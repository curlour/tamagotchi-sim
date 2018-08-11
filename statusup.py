import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import shelve

def chngsts(avars):

    def stsupd(a, avars):
        if avars[a][21]:
            if avars[a][1] == 1:
                hngt = 300
                hppt = 360
                if avars[a][2] == 900:
                    if avars[a][20]:
                        avars[a][19] += 1
                    else:
                        avars[a][20] = True
                if 1800 < avars[a][2] < 2100:
                    avars[a][21] = False
                    if avars[a][4] > 0 and avars[a][30] == 0:
                        avars[a][30] = 1
            elif avars[a][1] == 2:
                hngt = 3000
                hppt = 2700
                if int(avars[3][6][:2]) > 19 or int(avars[3][6][:2]) < 9:
                    avars[a][21] = False
                    if avars[a][4] > 0 and avars[a][30] == 0:
                        avars[a][30] = 1
            elif avars[a][1] == 3:
                hngt = 2700
                hppt = 3600
                if int(avars[3][6][:2]) > 20 or int(avars[3][6][:2]) < 9:
                    avars[a][21] = False
                    if avars[a][4] > 0 and avars[a][30] == 0:
                        avars[a][30] = 1
            elif avars[a][1] < 6:
                hngt = 4800
                hppt = 6000
                if int(avars[3][6][:2]) > 21 or int(avars[3][6][:2]) < 9:
                    avars[a][21] = False
                    if avars[a][4] > 0 and avars[a][30] == 0:
                        avars[a][30] = 1
            else:
                if ((avars[a][2] - 1382400) // 230400) > avars[a][19]:
                    avars[a][19] = ((avars[a][2] - 1382400) // 230400)
                hngt = 4800 // (avars[a][19] + 1)
                hppt = 6000 // (avars[a][19] + 1)
                if int(avars[3][6][:2]) > 19 or int(avars[3][6][:2]) < 9:
                    avars[a][21] = False
                    if avars[a][4] > 0 and avars[a][30] == 0:
                        avars[a][30] = 1
            if ((avars[a][2] / hngt) - (avars[a][2] // hngt)) == 0:
                if avars[a][16] == 0:
                    avars[a][19] += 1
                    if avars[a][4] == 0:
                        s = randint(0, 2)
                    elif avars[a][4] < 8:
                        s = randint(0, 1)
                    else:
                        s = 0
                    if s == 0:
                        if avars[a][20]:
                            avars[a][19] += 1
                        else:
                            avars[a][20] = True
                else:
                    avars[a][16] -= 1
            if ((avars[a][2] / hppt) - (avars[a][2] // hppt)) == 0:
                if avars[a][17] == 0:
                    avars[a][19] += 1
                    if avars[a][4] == 0:
                        s = randint(0, 2)
                    elif avars[a][4] < 8:
                        s = randint(0, 1)
                    else:
                        s = 0
                    if s == 0:
                        if avars[a][20]:
                            avars[a][19] += 1
                        else:
                            avars[a][20] = True
                else:
                    avars[a][17] -= 1
            if (((avars[a][2] - 30) / (2 * hngt)) - ((avars[a][2] - 30) // (2 * hngt))) == 0 and avars[a][2] > 60:
                if avars[a][18] > 3:
                    avars[a][18] -= 2
                else:
                    avars[a][18] = 1
                if avars[a][4] < 8 and avars[a][33] < 4:
                    avars[a][4] += 1
                elif avars[a][4] == 8:
                    if avars[a][20]:
                        avars[a][19] += 1
                    else:
                        avars[a][20] = True
        else:
            if avars[a][1] == 1:
                if avars[a][2] > 2100:
                    avars[a][21] = True
                    if avars[a][30] < 2:
                        avars[a][30] += 1
                    else:
                        avars[a][19] += 1
            elif avars[a][1] > 1:
                if avars[a][1] in [2, 6]:
                    b = 20
                elif avars[a][1] == 3:
                    b = 21
                elif avars[a][1] < 6:
                    b = 22
                if 8 < int(avars[3][6][:2]) < b:
                    avars[a][21] = True
                    if avars[a][30] < 2:
                        avars[a][30] += 1
                    else:
                        avars[a][19] += 1
        return(avars)
    
    if len(avars[0]) > 0:
        avars = stsupd(0, avars)
    if len(avars[1]) > 0:
        avars = stsupd(1, avars)
    if len(avars[2]) > 0:
        avars = stsupd(2, avars)
    return(avars)

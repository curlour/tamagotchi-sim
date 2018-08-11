import pygame, sys
import os
from pygame.locals import *
from random import *

def getborders(bordl, tbb, inic, cret):
    try:
        bordim = pygame.image.load(bordl).convert()
    except:
        bordim = pygame.Surface([240, 72]).convert()
        bordim.fill((51, 51, 204))
    tpborder = pygame.Surface([240, 24]).convert()
    btborder = pygame.Surface([240, 24]).convert()
    tpborder.blit(bordim, [0, 0])
    if tbb == 0:
        btborder.blit(bordim, [0, -24])
        return(tpborder, btborder)
    else:
        btborder.blit(bordim, [0, -48])
        borderico = pygame.Surface([20, 20]).convert()
        borderico.blit(bordim, [-(11 + (22 * inic)), -26])
        if not cret:
            c = pygame.Surface([12, 20]).convert()
            c.blit(bordim, [-200, -50])
            btborder.blit(c, [212, 2])
        return(tpborder, btborder, borderico)

def drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, name, anifr, hn, hp, sk, sl):
    def icoanim():
        if avars[avars[3][5]][1] == 0:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                ico = 0
            else:
                ico = 1
        else:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                ico = 1
            else:
                ico = 2
        ix = (176+ (22 * avars[3][5])) + ((16 - asprs[avars[3][5]][ico].get_width()) // 2)
        iy = 4 + ((16 - asprs[avars[3][5]][ico].get_height()) // 2)
        return(ico, ix, iy)
    screen.blit(tpborder, [0, 0])
    screen.blit(btborder, [0, 136])
    if borderico != 0:
        screen.blit(borderico, [26, 138])
        screen.blit((fnt.render(avars[avars[3][5]][22], 1, (0, 0, 100))), [67, 6])
    screen.blit((fnt.render(avars[3][6], 1, (0, 0, 100))), [11, 6])
    if len(avars[0]) > 0:
        if not (name and (avars[3][5] == 0)) and avars[0][1] > 0:
            if avars[0][16] == 0:
                screen.blit(hn, [174, 2])
            if avars[0][17] == 0:
                screen.blit(hp, [188, 2])
            if avars[0][20]:
                screen.blit(sk, [174, 16])
            if not avars[0][21]:
                screen.blit(sl, [188, 16])
        if avars[3][5] != 0:
            screen.blit(asprs[0][0], [(176 + ((16 - asprs[0][0].get_width()) // 2)), (4 + ((16 - asprs[0][0].get_height()) // 2))])
    if len(avars[1]) > 0:
        if not (name and (avars[3][5] == 1)) and avars[1][1] > 0:
            if avars[1][16] == 0:
                screen.blit(hn, [196, 2])
            if avars[1][17] == 0:
                screen.blit(hp, [210, 2])
            if avars[1][20]:
                screen.blit(sk, [196, 16])
            if not avars[1][21]:
                screen.blit(sl, [210, 16])
        if avars[3][5] != 1:
            screen.blit(asprs[1][0], [(198 + ((16 - asprs[1][0].get_width()) // 2)), (4 + ((16 - asprs[1][0].get_height()) // 2))])
    if len(avars[2]) > 0:
        if not (name and (avars[3][5] == 2)) and avars[2][1] > 0:
            if avars[2][16] == 0:
                screen.blit(hn, [218, 2])
            if avars[2][17] == 0:
                screen.blit(hp, [232, 2])
            if avars[2][20]:
                screen.blit(sk, [218, 16])
            if not avars[2][21]:
                screen.blit(sl, [232, 16])
        if avars[3][5] != 2:
            screen.blit(asprs[2][0], [(220 + ((16 - asprs[2][0].get_width()) // 2)), (4 + ((16 - asprs[2][0].get_height()) // 2))])
    ico, ix, iy = icoanim()
    screen.blit(asprs[avars[3][5]][ico], [ix, iy])
    return(screen)

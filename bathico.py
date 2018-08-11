import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import shelve
import sounds
import borders
import varsup
import statusup
import dirty
import mainscreen

def bathroom(avars, md, asprs, screen):
    
    kr = True

    chngsts = False

    tm = 0

    go = False

    def charaanim():
        flip = False
        if md == 0:
            if tm < 14:
                spr = 16
            else:
                spr = 17
            if avars[avars[3][5]][1] < 3:
                sprx = 106 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                spry = 84 + (32 - asprs[avars[3][5]][spr].get_height())
            else:
                flip = True
                sprx = 12 + (32 - asprs[avars[3][5]][spr].get_width())
                spry = 76 + (32 - asprs[avars[3][5]][spr].get_height())
        elif md == 1:
            if tm < 14 and ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 3
            else:
                spr = 5
            sprx = 106 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            if avars[avars[3][5]][1] < 2:
                spry = 90 + (32 - asprs[avars[3][5]][spr].get_height())
            else:
                spry = 95 + (32 - asprs[avars[3][5]][spr].get_height())
            if tm > 13:
                spry -= 8
        return(spr, sprx, spry, flip)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 2, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()
    
    try:
        bck = pygame.image.load(avars[3][21]).convert()
        if bck.get_size() != (240, 160):
            raise Exception("Wrong size!")
    except pygame.error:
        bck = pygame.Surface([240, 160]).convert()
        bck.fill((51, 51, 204))
    try:
        tbck = pygame.image.load(avars[3][18]).convert()
        if tbck.get_size() != (240, 160):
            raise Exception("Wrong size!")
    except pygame.error:
        tbck = pygame.Surface([240, 160]).convert()
        tbck.fill((51, 51, 204))
    try:
        bath = pygame.image.load(avars[3][22]).convert()
        if bath.get_size() != (64, 32):
            raise Exception("Wrong size!")
    except pygame.error:
        bath = pygame.Surface([64, 32]).convert()
        bath.fill((51, 51, 204))
    try:
        toilet = pygame.image.load(avars[3][19]).convert()
        if toilet.get_size() != (48, 48):
            raise Exception("Wrong size!")
    except pygame.error:
        toilet = pygame.Surface([48, 48]).convert()
        toilet.fill((51, 51, 204))
    try:
        btoilet = pygame.image.load(avars[3][20]).convert()
        if btoilet.get_size() != (32, 32):
            raise Exception("Wrong size!")
    except pygame.error:
        btoilet = pygame.Surface([32, 32]).convert()
        btoilet.fill((51, 51, 204))

    vap = pygame.image.load("Sprites/Misc/emo/vapor.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    sound = sounds.imprtsnd(avars)

    clock = pygame.time.Clock()

    if md == 0 and avars[avars[3][5]][33] < 4 and avars[avars[3][5]][17] < 6:
        avars[avars[3][5]][17] += 1

    if md == 0:
        if avars[avars[3][5]][18] > 3:
            avars[avars[3][5]][18] -= 2
        else:
            avars[avars[3][5]][18] = 1

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if md == 0:
            screen.blit(tbck, [0, 0])
        else:
            screen.blit(bck, [0, 0])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
        spr, sprx, spry, flip = charaanim()
        screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [sprx, spry])
        if md == 0:
            if avars[avars[3][5]][1] < 3:
                screen.blit(btoilet, [104, 98])
            else:
                screen.blit(toilet, [4, 82])
        else:
            screen.blit(bath, [88, 98])
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                screen.blit(vap, [138, 72])
                screen.blit(pygame.transform.flip(vap, 1, 0), [90, 84])
            else:
                screen.blit(pygame.transform.flip(vap, 1, 0), [138, 84])
                screen.blit(vap, [90, 72])
        for event in pygame.event.get():
            if event.type == QUIT:
                varsup.updtvrs(avars)
                kr = False
                pygame.quit()
                sys.exit()
            if event.type == USEREVENT + 1:
                if avars[3][3] == 0:
                    avars[3][6] = time.strftime("%H:%M")
                else:
                    avars[3][7] += 1
                    if avars[3][7] == 60:
                        if int(avars[3][6][3:]) != 59:
                            nhour = avars[3][6][:3] + ("%02d" % (int(avars[3][6][3:]) + 1))
                            avars[3][6] = nhour
                        else:
                            nhour = ("%02d" % (int(avars[3][6][:2]) + 1)) + ":00"
                            if nhour == "24:00":
                                nhour = "00:00"
                            avars[3][6] = nhour
                        avars[3][7] = 0
                if len(avars[0]) > 0:
                    avars[0][2] += 1
                if len(avars[1]) > 0:
                    avars[1][2] += 1
                if len(avars[2]) > 0:
                    avars[2][2] += 1
        if tm == 14 and anifr % 6 == 0:
            if md == 0:
                pygame.mixer.stop()
                sound[5].play()
            else:
                pygame.mixer.stop()
                sound[6].play()
        if tm == 16:
            go = True
            chngsts = True
        if anifr < 23:
            anifr += 1
        else:
            anifr = 0
        if chngsts:
            avars = statusup.chngsts(avars)
            chngsts = False
        if go:
            avars[avars[3][5]][2] += 25
            return(avars)
        if anifr % 6 == 0:
            tm += 1
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

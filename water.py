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
import weather
import dirty
import mainscreen

def game(avars, asprs, screen, tsprs):
    
    kr = True

    chngsts = False

    scr = 0

    ret = 1

    plntl = [0, 0, 0, 0, 0, 0, 0, 0]

    wtplnt = 0

    tuts = True
    strt = False
    play = False
    end = 0

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    classbg = pygame.image.load("Sprites/Misc/bg/kndclass.png").convert()

    pgbk = ["pgbk", "pgbks", "pgbka", "pgbkw"]

    s, tm , w = weather.chktime(avars)

    tutimg = pygame.image.load("Sprites/Misc/bg/watert.png").convert()
    
    gamebg = pygame.image.load("Sprites/Misc/bg/" + pgbk[s] + ".png").convert()
    gardbg = pygame.image.load("Sprites/Misc/bg/waterbg.png").convert()

    gamebg.blit(gardbg, [0, 0])

    plnt1 = pygame.image.load("Sprites/Misc/bg/water1.png").convert()
    plnt2 = pygame.image.load("Sprites/Misc/bg/water2.png").convert()
    plnt3 = pygame.image.load("Sprites/Misc/bg/water3.png").convert()

    plnts = [plnt2, plnt3]

    plntg = pygame.image.load("Sprites/Misc/bg/water4.png").convert()

    wtcan = pygame.image.load("Sprites/Misc/obj/watercan.png").convert()

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    toobad = pygame.image.load("Sprites/Misc/bg/toobad.png").convert()
    good = pygame.image.load("Sprites/Misc/bg/good.png").convert()
    great = pygame.image.load("Sprites/Misc/bg/great.png").convert()
    excellent = pygame.image.load("Sprites/Misc/bg/excellent.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if tuts:
            screen.blit(tutimg, [0, 0])
        elif strt:
            screen.blit(classbg, [0, 0])
            if anifr == 16:
                pygame.mixer.stop()
                sound[11].play()
            if anifr < 16:
                screen.blit(ready, [80, 40])
                tcs = 0
                spr = 3
            else:
                screen.blit(go, [95, 40])
                tcs = 2
                spr = 5
            screen.blit(tsprs[tcs], [136, 98])
            screen.blit(asprs[avars[3][5]][spr], [(72 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
        elif play:
            screen.blit(gamebg, [0, 0])
            if end < 2:
                tcs = 0 + (anifr % 12 < 6)
                spr = 3 + (anifr % 12 < 6)
            elif end == 2:
                tcs = 1
                spr = 12
            else:
                tcs = 2 + (scr < 1152)
                spr = 5 + (scr < 1152)
            if end < 3:
                a = 0
                while a < 8:
                    if end == 0:
                        screen.blit(plnt1, [(10 + (28 * a)), 88])
                    else:
                        screen.blit(plnts[plntl[a] // 4], [(10 + (28 * a)), 88])
                    a += 1
            if end == 3:
                if scr < 1152:
                    a = 0
                    while a < 8:
                        screen.blit(plnts[plntl[a] // 5], [(10 + (28 * a)), 88])
                        a += 1
                else:
                    screen.blit(plntg, [10, 80])
            if end == 0:
                screen.blit(wtcan, [(26 + (28 * (anifr // 3))), 72])
            elif end == 2:
                screen.blit(wtcan, [(26 + (28 * wtplnt)), 72])
            screen.blit(tsprs[tcs], [205, 101])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], 1, 0), [(3 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (101 + (32 - asprs[avars[3][5]][spr].get_height()))])
        else:
            screen.blit(classbg, [0, 0])
            if end == 4:
                if scr < 4:
                    screen.blit(toobad, [71, 40])
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 6
                        tcs = 1
                    else:
                        spr = 7
                        tcs = 3
                else:
                    if scr < 8:
                        screen.blit(good, [94, 40])
                    elif scr < 12:
                        screen.blit(great, [85, 40])
                    else:
                        screen.blit(excellent, [51, 40])
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 4
                        tcs = 1
                    else:
                        spr = 5
                        tcs = 2
            screen.blit(tsprs[tcs], [136, 98])
            screen.blit(asprs[avars[3][5]][spr], [(72 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
        for event in pygame.event.get():
            if event.type == QUIT:
                varsup.updtvrs(avars)
                kr = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mp = event.pos
                d = (screen.get_size()[0] // 240)
                mp = ((mp[0] // d), (mp[1] // d))
                pb = event.button
                if pb == 1:
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            pygame.mixer.stop()
                            sound[4].play()
                            return(avars, ret)
                        elif 212 < mp[0] < 224:
                            pygame.mixer.stop()
                            sound[4].play()
                            ret = 0
                            return(avars, ret)
                    if (24 < mp[1] < 136) and tuts:
                        pygame.mixer.stop()
                        sound[10].play()
                        tuts = False
                        strt = True
                        anifr = -1
                    elif 88 < mp[1] < 112 and 8 < mp[0] < 232 and play and end == 1:
                        end = 2
                        wtplnt = (mp[0] - 8) // 28
                        plntl[wtplnt] = 0
                        anifr = 19
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
                chngsts = True
        if chngsts:
            avars = statusup.chngsts(avars)
            chngsts = False
        if anifr < 23:
            anifr += 1
        else:
            anifr = 0
            if strt:
                play = True
                strt = False
            elif play:
                if end == 0:
                    end = 1
                    pygame.mixer.stop()
                    sound[9].play()
                elif end == 2:
                    end = 1
                elif end == 3:
                    play = False
                    end = 4
                    scr //= 96
                    if scr < 4:
                        pygame.mixer.stop()
                        sound[14].play()
                    else:
                        pygame.mixer.stop()
                        sound[1].play()
                    avars[avars[3][5]][7] += scr
            elif end == 4:
                ret = 0
                return(avars, ret)
        if play and end < 3:
            scr += 1
            if scr >= 1152:
                end = 3
                anifr = 12
                pygame.mixer.stop()
                sound[9].play()
        if play and end == 1 and anifr % 4 == 0:
            a = 0
            b = 0
            while a < 8:
                plntl[a] += choice([0, 0, 0, 1])
                b += plntl[a] > 7
                a += 1
            if b > 0:
                end = 3
                anifr = 12
                plnts.pop(0)
                plnts.append(plnt1)
                pygame.mixer.stop()
                sound[12].play()
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

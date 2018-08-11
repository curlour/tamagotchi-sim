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

def game(avars, asprs, screen, pchr1, psps1, pchr2, psps2, pchr3, psps3, mfsps):
    
    kr = True

    chngsts = False

    scr = 0

    chlst = [0, 1, 2]
    shuffle(chlst)

    xlst = [164, 116, 68]

    pcx1 = 208
    pcx2 = 208
    pcx3 = 208
    sprx = 208

    move = 0
    lose = False

    last = 3

    ret = 1

    tuts = True
    strt = False
    play = False
    end = 0

    swthr = ["skyd", "skyaf", "skyn"]
    cwthr = ["skydc", "skydc", "skync"]
    wthrbk = [swthr, cwthr, cwthr]

    pgbk = ["pgbk", "pgbks", "pgbka", "pgbkw"]

    def outbg():
        bg = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
        a = pygame.image.load("Sprites/Misc/bg/" + pgbk[s] + ".png").convert()
        b = pygame.Surface([240, 160]).convert()
        c = (0, 0, 0)
        if w != 0:
            if w == 2:
                if s == 3:
                    a.blit(snowg, [0, 0])
                else:
                    a.blit(raing, [0, 0])
        a.blit(presout, [0, 0])
        if w != 0:
            b.fill((204, 204, 204))
            c = (81, 81, 81)
            b.set_alpha(102)
            a.blit(b, [0, 0])
        a.set_colorkey(c)
        bg.blit(a, [0, 0])
        return(bg)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    tutimg = pygame.image.load("Sprites/Misc/bg/statuest.png").convert()

    presin = pygame.image.load("Sprites/Misc/bg/presin.png").convert()
    presout = pygame.image.load("Sprites/Misc/bg/presout.png").convert()

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    toobad = pygame.image.load("Sprites/Misc/bg/toobad.png").convert()
    good = pygame.image.load("Sprites/Misc/bg/good.png").convert()
    great = pygame.image.load("Sprites/Misc/bg/great.png").convert()
    excellent = pygame.image.load("Sprites/Misc/bg/excellent.png").convert()

    rain = pygame.image.load("Sprites/Misc/bg/rain.png").convert()
    snow = pygame.image.load("Sprites/Misc/bg/snow.png").convert()

    raing = pygame.image.load("Sprites/Misc/bg/rpgb.png").convert()
    snowg = pygame.image.load("Sprites/Misc/bg/spgb.png").convert()

    s, tm , w = weather.chktime(avars)

    obgi = outbg()

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
            screen.blit(presin, [0, 0])
            if anifr == 16:
                pygame.mixer.stop()
                sound[11].play()
            if anifr < 16:
                screen.blit(ready, [80, 40])
                mfs = 0
                spr = 3
                pcs1 = 3
                pcs2 = 3
                pcs3 = 3
            else:
                screen.blit(go, [95, 40])
                mfs = 2
                spr = 5
                pcs1 = 5
                pcs2 = 5
                pcs3 = 5
            screen.blit(mfsps[mfs], [104, 54])
            screen.blit(psps1[pcs1], [66, 106])
            screen.blit(psps2[pcs2], [94, 106])
            screen.blit(asprs[avars[3][5]][spr], [122, 106])
            screen.blit(psps3[pcs3], [150, 106])
        elif play:
            screen.blit(obgi, [0, 0])
            if w == 2:
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    y = 0
                else:
                    if s < 3:
                        y = 16
                    else:
                        y = 8
                if s < 3:
                    screen.blit(rain, [0, y])
                else:
                    screen.blit(snow, [0, y])
            if ((anifr / 6) - (anifr // 6)) == 0:
                if move == 1 or move == 2:
                    sprx -= 4
                    if move == 1:
                        move = 2
                    else:
                        move = 0
                    if anifr > 41:
                        lose = True
            if move == 2:
                if anifr < 42:
                    spr = 13
                else:
                    spr = 9
            elif move == 0 and lose:
                spr = 9
            else:
                spr = 11
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                mfs = 0
                if scr == 0:
                    if anifr == 12 or anifr == 24 or anifr == 36:
                        pcx1 -= 4
                        pcx2 -= 4
                        pcx3 -= 4
                    pcs1 = 11
                    pcs2 = 11
                    pcs3 = 11
                elif scr == 1:
                    if anifr == 12 or anifr == 24:
                        pcx1 -= 4
                        pcx2 -= 4
                        pcx3 -= 4
                    elif anifr == 36:
                        if chlst[0] != 0:
                            pcx1 -= 4
                        if chlst[0] != 1:
                            pcx2 -= 4
                        if chlst[0] != 2:
                            pcx3 -= 4
                    pcs1 = 11
                    pcs2 = 11
                    pcs3 = 11
                elif scr == 2:
                    if anifr == 12 or anifr == 24 or anifr == 36:
                        if chlst[0] != 0:
                            pcx1 -= 4
                        if chlst[0] != 1:
                            pcx2 -= 4
                        if chlst[0] != 2:
                            pcx3 -= 4
                    if chlst[0] == 0:
                        pcs1 = 6
                        pcs2 = 11
                        pcs3 = 11
                    elif chlst[0] == 1:
                        pcs1 = 11
                        pcs2 = 6
                        pcs3 = 11
                    else:
                        pcs1 = 11
                        pcs2 = 11
                        pcs3 = 6
                elif scr == 3:
                    if anifr == 12 or anifr == 24:
                        if chlst[0] != 0:
                            pcx1 -= 4
                        if chlst[0] != 1:
                            pcx2 -= 4
                        if chlst[0] != 2:
                            pcx3 -= 4
                    elif anifr == 36:
                        if chlst[2] == 0:
                            pcx1 -= 4
                        if chlst[2] == 1:
                            pcx2 -= 4
                        if chlst[2] == 2:
                            pcx3 -= 4
                    if chlst[0] == 0:
                        pcs1 = 6
                        pcs2 = 11
                        pcs3 = 11
                    elif chlst[0] == 1:
                        pcs1 = 11
                        pcs2 = 6
                        pcs3 = 11
                    else:
                        pcs1 = 11
                        pcs2 = 11
                        pcs3 = 6
                elif scr == 4:
                    if anifr == 12 or anifr == 24 or anifr == 36:
                        if chlst[2] == 0:
                            pcx1 -= 4
                        if chlst[2] == 1:
                            pcx2 -= 4
                        if chlst[2] == 2:
                            pcx3 -= 4
                    if chlst[2] == 0:
                        pcs1 = 11
                        pcs2 = 6
                        pcs3 = 6
                    elif chlst[2] == 1:
                        pcs1 = 6
                        pcs2 = 11
                        pcs3 = 6
                    else:
                        pcs1 = 6
                        pcs2 = 6
                        pcs3 = 11
                elif scr == 5:
                    if anifr == 12 or anifr == 24:
                        if chlst[2] == 0:
                            pcx1 -= 4
                        if chlst[2] == 1:
                            pcx2 -= 4
                        if chlst[2] == 2:
                            pcx3 -= 4
                    if chlst[2] == 0:
                        pcs1 = 11
                        pcs2 = 6
                        pcs3 = 6
                    elif chlst[2] == 1:
                        pcs1 = 6
                        pcs2 = 11
                        pcs3 = 6
                    else:
                        pcs1 = 6
                        pcs2 = 6
                        pcs3 = 11
            else:
                if anifr < 42:
                    mfs = 1
                else:
                    mfs = 2
                if scr == 0:
                    if anifr == 6 or anifr == 18 or anifr == 30:
                        pcx1 -= 4
                        pcx2 -= 4
                        pcx3 -= 4
                    if anifr < 42:
                        pcs1 = 13
                        pcs2 = 13
                        pcs3 = 13
                    else:
                        pcs1 = 11
                        pcs2 = 11
                        pcs3 = 11
                elif scr == 1:
                    if anifr == 6 or anifr == 18:
                        pcx1 -= 4
                        pcx2 -= 4
                        pcx3 -= 4
                    elif anifr == 30:
                        if chlst[0] != 0:
                            pcx1 -= 4
                        if chlst[0] != 1:
                            pcx2 -= 4
                        if chlst[0] != 2:
                            pcx3 -= 4
                    elif anifr == 42:
                        if chlst[0] == 0:
                            pcx1 -= 4
                        if chlst[0] == 1:
                            pcx2 -= 4
                        if chlst[0] == 2:
                            pcx3 -= 4
                    if anifr < 30:
                        pcs1 = 13
                        pcs2 = 13
                        pcs3 = 13
                    elif anifr < 42:
                        if chlst[0] == 0:
                            pcs1 = 11
                            pcs2 = 13
                            pcs3 = 13
                        elif chlst[0] == 1:
                            pcs1 = 13
                            pcs2 = 11
                            pcs3 = 13
                        else:
                            pcs1 = 13
                            pcs2 = 13
                            pcs3 = 11
                    else:
                        if chlst[0] == 0:
                            pcs1 = 9
                            pcs2 = 11
                            pcs3 = 11
                        elif chlst[0] == 1:
                            pcs1 = 11
                            pcs2 = 9
                            pcs3 = 11
                        else:
                            pcs1 = 11
                            pcs2 = 11
                            pcs3 = 9
                elif scr == 2:
                    if anifr == 6 or anifr == 18 or anifr == 30:
                        if chlst[0] != 0:
                            pcx1 -= 4
                        if chlst[0] != 1:
                            pcx2 -= 4
                        if chlst[0] != 2:
                            pcx3 -= 4
                    if anifr < 42:
                        if chlst[0] == 0:
                            pcs1 = 7
                            pcs2 = 13
                            pcs3 = 13
                        elif chlst[0] == 1:
                            pcs1 = 13
                            pcs2 = 7
                            pcs3 = 13
                        else:
                            pcs1 = 13
                            pcs2 = 13
                            pcs3 = 7
                    else:
                        if chlst[0] == 0:
                            pcs1 = 7
                            pcs2 = 11
                            pcs3 = 11
                        elif chlst[0] == 1:
                            pcs1 = 11
                            pcs2 = 7
                            pcs3 = 11
                        else:
                            pcs1 = 11
                            pcs2 = 11
                            pcs3 = 7
                elif scr == 3:
                    if anifr == 6 or anifr == 18:
                        if chlst[0] != 0:
                            pcx1 -= 4
                        if chlst[0] != 1:
                            pcx2 -= 4
                        if chlst[0] != 2:
                            pcx3 -= 4
                    elif anifr == 30:
                        if chlst[2] == 0:
                            pcx1 -= 4
                        if chlst[2] == 1:
                            pcx2 -= 4
                        if chlst[2] == 2:
                            pcx3 -= 4
                    elif anifr == 42:
                        if chlst[1] == 0:
                            pcx1 -= 4
                        if chlst[1] == 1:
                            pcx2 -= 4
                        if chlst[1] == 2:
                            pcx3 -= 4
                    if anifr < 30:
                        if chlst[0] == 0:
                            pcs1 = 7
                            pcs2 = 13
                            pcs3 = 13
                        elif chlst[0] == 1:
                            pcs1 = 13
                            pcs2 = 7
                            pcs3 = 13
                        else:
                            pcs1 = 13
                            pcs2 = 13
                            pcs3 = 7
                    elif anifr < 42:
                        if chlst[0] == 0:
                            pcs1 = 7
                        elif chlst[0] == 1:
                            pcs2 = 7
                        else:
                            pcs3 = 7
                        if chlst[1] == 0:
                            pcs1 = 11
                        elif chlst[1] == 1:
                            pcs2 = 11
                        else:
                            pcs3 = 11
                        if chlst[2] == 0:
                            pcs1 = 13
                        elif chlst[2] == 1:
                            pcs2 = 13
                        else:
                            pcs3 = 13
                    else:
                        if chlst[0] == 0:
                            pcs1 = 7
                        elif chlst[0] == 1:
                            pcs2 = 7
                        else:
                            pcs3 = 7
                        if chlst[1] == 0:
                            pcs1 = 9
                        elif chlst[1] == 1:
                            pcs2 = 9
                        else:
                            pcs3 = 9
                        if chlst[2] == 0:
                            pcs1 = 11
                        elif chlst[2] == 1:
                            pcs2 = 11
                        else:
                            pcs3 = 11
                elif scr == 4:
                    if anifr == 6 or anifr == 18 or anifr == 30:
                        if chlst[2] == 0:
                            pcx1 -= 4
                        if chlst[2] == 1:
                            pcx2 -= 4
                        if chlst[2] == 2:
                            pcx3 -= 4
                    if anifr < 42:
                        if chlst[2] == 0:
                            pcs1 = 13
                            pcs2 = 7
                            pcs3 = 7
                        elif chlst[2] == 1:
                            pcs1 = 7
                            pcs2 = 13
                            pcs3 = 7
                        else:
                            pcs1 = 7
                            pcs2 = 7
                            pcs3 = 13
                    else:
                        if chlst[2] == 0:
                            pcs1 = 11
                            pcs2 = 7
                            pcs3 = 7
                        elif chlst[2] == 1:
                            pcs1 = 7
                            pcs2 = 11
                            pcs3 = 7
                        else:
                            pcs1 = 7
                            pcs2 = 7
                            pcs3 = 11
                elif scr == 5:
                    if anifr == 6 or anifr == 18 or anifr == 42:
                        if chlst[2] == 0:
                            pcx1 -= 4
                        if chlst[2] == 1:
                            pcx2 -= 4
                        if chlst[2] == 2:
                            pcx3 -= 4
                    if anifr < 30:
                        if chlst[2] == 0:
                            pcs1 = 13
                            pcs2 = 7
                            pcs3 = 7
                        elif chlst[2] == 1:
                            pcs1 = 7
                            pcs2 = 13
                            pcs3 = 7
                        else:
                            pcs1 = 7
                            pcs2 = 7
                            pcs3 = 13
                    elif anifr < 42:
                        if chlst[2] == 0:
                            pcs1 = 11
                            pcs2 = 7
                            pcs3 = 7
                        elif chlst[2] == 1:
                            pcs1 = 7
                            pcs2 = 11
                            pcs3 = 7
                        else:
                            pcs1 = 7
                            pcs2 = 7
                            pcs3 = 11
                    else:
                        if chlst[2] == 0:
                            pcs1 = 9
                            pcs2 = 7
                            pcs3 = 7
                        elif chlst[2] == 1:
                            pcs1 = 7
                            pcs2 = 9
                            pcs3 = 7
                        else:
                            pcs1 = 7
                            pcs2 = 7
                            pcs3 = 9
            screen.blit(mfsps[mfs], [32, 98])
            screen.blit(psps1[pcs1], [pcx1, 98])
            screen.blit(psps2[pcs2], [pcx2, 102])
            screen.blit(asprs[avars[3][5]][spr], [sprx, 106])
            screen.blit(psps3[pcs3], [pcx3, 110])
            if anifr == 42:
                if lose:
                    pygame.mixer.stop()
                    sound[12].play()
                else:
                    pygame.mixer.stop()
                    sound[9].play()
        else:
            screen.blit(presin, [0, 0])
            if end == 4:
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    mfs = 1
                else:
                    mfs = 2
                if scr < 1:
                    screen.blit(toobad, [71, 40])
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 6
                        pcs1 = 4
                        pcs2 = 4
                        pcs3 = 4
                    else:
                        spr = 7
                        pcs1 = 5
                        pcs2 = 5
                        pcs3 = 5
                else:
                    if scr < 2:
                        screen.blit(good, [94, 40])
                    elif scr < 3:
                        screen.blit(great, [85, 40])
                    else:
                        screen.blit(excellent, [51, 40])
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 4
                        if last == 0:
                            pcs1 = 6
                            pcs2 = 4
                            pcs3 = 4
                        elif last == 1:
                            pcs1 = 4
                            pcs2 = 6
                            pcs3 = 4
                        else:
                            pcs1 = 4
                            pcs2 = 4
                            pcs3 = 6
                    else:
                        spr = 5
                        if last == 0:
                            pcs1 = 7
                            pcs2 = 5
                            pcs3 = 5
                        elif last == 1:
                            pcs1 = 5
                            pcs2 = 7
                            pcs3 = 5
                        else:
                            pcs1 = 5
                            pcs2 = 5
                            pcs3 = 7
                screen.blit(mfsps[mfs], [104, 54])
                screen.blit(psps1[pcs1], [66, 106])
                screen.blit(psps2[pcs2], [94, 106])
                screen.blit(asprs[avars[3][5]][spr], [122, 106])
                screen.blit(psps3[pcs3], [150, 106])
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
                    elif 24 < mp[1] < 136 and play and move == 0:
                        move = 1
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
        if (anifr < 23 and (strt or end == 4)) or (anifr < 47 and play):
            anifr += 1
        else:
            anifr = 0
            if strt:
                play = True
                strt = False
            elif play:
                scr += 1
                if scr == 6 or lose:
                    pcx1 = xlst[chlst.index(0)]
                    pcx2 = xlst[chlst.index(1)]
                    pcx3 = xlst[chlst.index(2)]
                    wnlst = [pcx1, pcx2, pcx3, sprx]
                    wnlst.sort()
                    wnlst.reverse()
                    scr = wnlst.index(sprx)
                    if wnlst[0] == pcx1:
                        last = 0
                    elif wnlst[0] == pcx2:
                        last = 1
                    elif wnlst[0] == pcx3:
                        last = 2
                    play = False
                    if scr < 1:
                        pygame.mixer.stop()
                        sound[14].play()
                    else:
                        pygame.mixer.stop()
                        sound[1].play()
                    end = 4
                    if (avars[avars[3][5]][17] + scr) < 6:
                        avars[avars[3][5]][17] += scr
                    else:
                        avars[avars[3][5]][17] = 6
                    if (avars[avars[3][5]][18] - scr) > 1:
                        avars[avars[3][5]][18] -= scr
                    else:
                        avars[avars[3][5]][18] = 1
                    b = randint(0, 5)
                    avars[avars[3][5]][(5 + b)] += scr
            elif end == 4:
                ret = 0
                return(avars, ret)
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

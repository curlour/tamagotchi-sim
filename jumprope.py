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

    rpos = 2
    rdir = False

    lose = 3
    pchr = [0, 1, 2]
    last = 3

    jump = 0

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

    tutimg = pygame.image.load("Sprites/Misc/bg/jumpropet.png").convert()

    presin = pygame.image.load("Sprites/Misc/bg/presin.png").convert()
    presout = pygame.image.load("Sprites/Misc/bg/presout.png").convert()

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    toobad = pygame.image.load("Sprites/Misc/bg/toobad.png").convert()
    good = pygame.image.load("Sprites/Misc/bg/good.png").convert()
    great = pygame.image.load("Sprites/Misc/bg/great.png").convert()
    excellent = pygame.image.load("Sprites/Misc/bg/excellent.png").convert()

    rope1 = pygame.image.load("Sprites/Misc/obj/rope1.png").convert()
    rope2 = pygame.image.load("Sprites/Misc/obj/rope2.png").convert()
    rope3 = pygame.image.load("Sprites/Misc/obj/rope3.png").convert()

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
                if jump == 1:
                    jump = 2
                elif jump == 2:
                    jump = 0
                if rdir:
                    rpos += 1
                    if rpos == 2:
                        rdir = False
                        if jump == 2:
                            scr += 1
                        if scr == 12 or jump < 2:
                            anifr = 18
                        if ((scr / 4) - (scr // 4)) == 0 and scr > 0 and ((scr // 4) + len(pchr)) == 4:
                            a = randint(0, (len(pchr) - 1))
                            lose = pchr[a]
                else:
                    rpos -= 1
                    if lose < 3:
                        if len(pchr) == 3:
                            last = lose
                        pchr.pop(a)
                        lose = 3
                    if rpos == 0:
                        rdir = True
                if rpos == 2 and jump < 2:
                    pygame.mixer.stop()
                    sound[12].play()
                elif rpos == 2 or jump == 2:
                    pygame.mixer.stop()
                    sound[9].play()
            if rpos == 0:
                screen.blit(rope3, [8, 98])
                mfs = 2
                if jump == 2:
                    spr = 5
                    spry = 98
                else:
                    spr = 3
                    spry = 106
                pcs1 = 3
                pcs2 = 3
                pcs3 = 3
                pcy1 = 106
                pcy2 = 106
                pcy3 = 106
            elif rpos == 1:
                if not rdir:
                    screen.blit(rope1, [8, 98])
                mfs = 0
                if jump == 2:
                    spr = 5
                    spry = 98
                else:
                    spr = 3
                    spry = 106
                pcs1 = 3
                pcs2 = 3
                pcs3 = 3
                pcy1 = 106
                pcy2 = 106
                pcy3 = 106
            else:
                mfs = 1
                if jump == 2:
                    spr = 5
                    spry = 98
                else:
                    spr = 7
                    spry = 106
                if lose == 0:
                    pcs1 = 7
                    pcy1 = 104
                else:
                    pcs1 = 5
                    pcy1 = 98
                if lose == 1:
                    pcs2 = 7
                    pcy2 = 104
                else:
                    pcs2 = 5
                    pcy2 = 98
                if lose == 2:
                    pcs3 = 7
                    pcy3 = 104
                else:
                    pcs3 = 5
                    pcy3 = 98
            screen.blit(mfsps[mfs], [172, 98])
            if 0 in pchr:
                screen.blit(psps1[pcs1], [40, pcy1])
            if 1 in pchr:
                screen.blit(psps2[pcs2], [76, pcy2])
            screen.blit(asprs[avars[3][5]][spr], [112, spry])
            if 2 in pchr:
                screen.blit(psps3[pcs3], [148, pcy3])
            if rdir and rpos == 1:
                screen.blit(rope1, [8, 98])
            elif rpos == 2:
                screen.blit(rope2, [8, 98])
        else:
            screen.blit(presin, [0, 0])
            if end == 4:
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    mfs = 1
                else:
                    mfs = 2
                if scr < 4:
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
                    if scr < 8:
                        screen.blit(good, [94, 40])
                    elif scr < 12:
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
                    elif play:
                        if (112 < mp[0] < 136) and (106 < mp[1] < 130) and jump == 0:
                            jump = 1
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
            elif play and (scr == 12 or (rpos == 2 and jump < 2)):
                if scr < 4:
                    pygame.mixer.stop()
                    sound[14].play()
                else:
                    pygame.mixer.stop()
                    sound[1].play()
                end = 4
                if (avars[avars[3][5]][17] + (scr // 3)) < 6:
                    avars[avars[3][5]][17] += (scr // 3)
                else:
                    avars[avars[3][5]][17] = 6
                if (avars[avars[3][5]][18] - (scr // 3)) > 1:
                    avars[avars[3][5]][18] -= (scr // 3)
                else:
                    avars[avars[3][5]][18] = 1
                b = randint(0, 5)
                avars[avars[3][5]][(5 + b)] += (scr // 6)
                play = False
            elif end == 4:
                ret = 0
                return(avars, ret)
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

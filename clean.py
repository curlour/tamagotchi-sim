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

    pool = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    ret = 1

    act = 0

    tuts = True
    strt = False
    play = False
    end = 0

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    tutimg = pygame.image.load("Sprites/Misc/bg/cleant.png").convert()

    classbg = pygame.image.load("Sprites/Misc/bg/humclass.png").convert()
    toiletbg = pygame.image.load("Sprites/Misc/bg/cleanbg.png").convert()

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    toobad = pygame.image.load("Sprites/Misc/bg/toobad.png").convert()
    good = pygame.image.load("Sprites/Misc/bg/good.png").convert()
    great = pygame.image.load("Sprites/Misc/bg/great.png").convert()
    excellent = pygame.image.load("Sprites/Misc/bg/excellent.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    poos = [pygame.image.load("Sprites/Misc/poo/bpoo1.png").convert(), pygame.image.load("Sprites/Misc/obj/unchikun.png").convert()]
    clnob = pygame.image.load("Sprites/Misc/obj/cleanob.png").convert()
    unclg = pygame.image.load("Sprites/Misc/obj/unclog.png").convert()

    pooy = [110, 72, 52, 42, 32, 47, 62, 90]

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
            screen.blit(toiletbg, [0, 0])
            if end == 0:
                flip = False
                tcs = 0 + (anifr % 12 > 5)
                spr = 3 + (anifr % 12 > 5)
                screen.blit(unclg, [14, (76 + (8 * (anifr % 12 > 5)))])
            elif end == 1:
                flip = act == 2
                tcs = 0 + (anifr % 12 > 5)
                spr = 3 + (8 * (act > 0))
            elif end == 2:
                flip = False
                tcs = 2 + (scr < 60)
                spr = 5 + (2 * (scr < 60))
            if end > 0:
                if act > 0:
                    screen.blit(pygame.transform.flip(clnob, (act - 1), 0), [(140 + (56 * (act - 1))), 106])
                a = 0
                while a < 8:
                    if pool[a][0] > 0:
                        screen.blit(poos[(pool[a][0] - 1)], [(18 + (18 * (7 - a)) + (pool[a][1] * (8 * (7 - a)))), pooy[a]])
                    a += 1
            screen.blit(tsprs[tcs], [40, 98])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [(164 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
        else:
            screen.blit(classbg, [0, 0])
            if end == 4:
                if scr < 20:
                    screen.blit(toobad, [71, 40])
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 6
                        tcs = 1
                    else:
                        spr = 7
                        tcs = 3
                else:
                    if scr < 40:
                        screen.blit(good, [94, 40])
                    elif scr < 60:
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
                if 24 < mp[1] < 136 and end == 1 and play and pb in [1, 3]:
                    act = [1, 3].index(pb) + 1
            if event.type == MOUSEBUTTONUP:
                ub = event.button
                if end == 1 and play and pb in [1, 3]:
                    act = 0
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
                    pygame.mixer.stop()
                    sound[5].play()
                    end = 1
                elif end == 2:
                    play = False
                    end = 4
                    if scr < 20:
                        pygame.mixer.stop()
                        sound[14].play()
                    else:
                        pygame.mixer.stop()
                        sound[1].play()
                    avars[avars[3][5]][8] += (scr // 5)
            elif end == 4:
                ret = 0
                return(avars, ret)
        if anifr % 6 == 0 and play and end == 1:
            pool.pop(0)
            a = 0
            b = 0
            while a < 7:
                b += pool[a][0] > 0
                a += 1
            if (scr + b < 60) and (pool[6][0] == 0):
                pool.append([choice([0, 1, 1, 1, 1, 1, 1, 2]), randint(0, 1)])
            else:
                pool.append([0, 0])
            if pool[0][0] > 0:
                if (pool[0][0] == 1 and (act - 1) != pool[0][1]) or (pool[0][0] == 2 and (act - 1) == pool[0][1]):
                    pygame.mixer.stop()
                    sound[12].play()
                    anifr = 12
                    end = 2
                elif pool[0][0] == 1 and (act - 1) == pool[0][1]:
                    pygame.mixer.stop()
                    sound[6].play()
                    scr += 1
                    if scr == 60:
                        pygame.mixer.stop()
                        sound[9].play()
                        anifr = 12
                        end = 2
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

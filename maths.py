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

    tuts = True
    strt = False
    play = False
    end = 0

    def newvals():
        optp = randint(0, 3)
        if optp < 2:
            a = randint(0, 255)
            t2 = randint(0, 255)
            c = a + t2
            t1 = (a * (optp == 0)) + (c * (optp == 1))
            res = (c * (optp == 0)) + (a * (optp == 1))
        else:
            a = randint(10, 99)
            t2 = randint(1, 9)
            c = a * t2
            t1 = (a * (optp == 2)) + (c * (optp == 3))
            res = (c * (optp == 2)) + (a * (optp == 3))
        t1tx = fnt.render(str(t1), 1, (0, 128, 255))
        t2tx = fnt.render(str(t2), 1, (0, 128, 255))
        restx = fnt.render(str(res), 1, (0, 128, 255))
        yans = ""
        yanstx = fnt.render(yans, 1, (0, 0, 100))
        return(t1, t1tx, t2, t2tx, res, restx, yans, yanstx, optp)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    tutimg = pygame.image.load("Sprites/Misc/bg/mathst.png").convert()

    classbg = pygame.image.load("Sprites/Misc/bg/intclass.png").convert()
    blackbg = pygame.image.load("Sprites/Misc/bg/mathsbg.png").convert()

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    toobad = pygame.image.load("Sprites/Misc/bg/toobad.png").convert()
    good = pygame.image.load("Sprites/Misc/bg/good.png").convert()
    great = pygame.image.load("Sprites/Misc/bg/great.png").convert()
    excellent = pygame.image.load("Sprites/Misc/bg/excellent.png").convert()

    mtsim = [pygame.image.load("Sprites/Misc/bg/mathsadd.png").convert(),
           pygame.image.load("Sprites/Misc/bg/mathssub.png").convert(),
           pygame.image.load("Sprites/Misc/bg/mathsmul.png").convert(),
           pygame.image.load("Sprites/Misc/bg/mathsdiv.png").convert()]

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
            screen.blit(blackbg, [0, 0])
            screen.blit(t1tx, [(138 - t1tx.get_width()), 50])
            screen.blit(t2tx, [(138 - t2tx.get_width()), 66])
            screen.blit(yanstx, [(48 - yanstx.get_width()), 74])
            if end == 0:
                tcs = 0 + (anifr % 12 < 6)
                spr = 3 + (anifr % 12 < 6)
            else:
                screen.blit(restx, [(138 - restx.get_width()), 90])
                tcs = 2 + (int(yans) != res)
                spr = 5 + (2 * (int(yans) != res))
            screen.blit(mtsim[optp], [88, 64])
            screen.blit(tsprs[tcs], [205, 101])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], 1, 0), [(3 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (101 + (32 - asprs[avars[3][5]][spr].get_height()))])
        else:
            screen.blit(classbg, [0, 0])
            if end == 4:
                if scr < 2:
                    screen.blit(toobad, [71, 40])
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 6
                        tcs = 1
                    else:
                        spr = 7
                        tcs = 3
                else:
                    if scr < 4:
                        screen.blit(good, [94, 40])
                    elif scr < 6:
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
            if event.type == pygame.KEYDOWN and end == 0 and play:
                if pygame.K_0 <= event.key <= pygame.K_9 and len(yans) < 3:
                    num = chr(event.key)
                    yans += str(num)
                if event.key == pygame.K_BACKSPACE and len(yans) != 0:
                    yans = yans[:len(yans) - 1]
                if event.key == pygame.K_RETURN and len(yans) != 0:
                    end = 1
                    anifr = 11
                    pygame.mixer.stop()
                    sound[12 - (3 * (int(yans) == res))].play()
                yanstx = fnt.render(str(yans), 1, (0, 0, 100))
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
                t1, t1tx, t2, t2tx, res, restx, yans, yanstx, optp = newvals()
            elif play:
                if end == 1:
                    if int(yans) == res:
                        scr += 1
                        if scr < 6:
                            end = 0
                            t1, t1tx, t2, t2tx, res, restx, yans, yanstx, optp = newvals()
                        else:
                            play = False
                            end = 4
                    else:
                        play = False
                        end = 4
                if not play:
                    if scr < 2:
                        pygame.mixer.stop()
                        sound[14].play()
                    else:
                        pygame.mixer.stop()
                        sound[1].play()
                    avars[avars[3][5]][5] += (scr * 2)
            elif end == 4:
                ret = 0
                return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

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

    gdpl = [32, 32, 32, 32, 32, 32]
    wipng = False

    tuts = True
    strt = False
    play = False
    end = 0

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    tutimg = pygame.image.load("Sprites/Misc/bg/wipet.png").convert()

    classbg = pygame.image.load("Sprites/Misc/bg/pasclass.png").convert()
    gymbg = pygame.image.load("Sprites/Misc/bg/wipebg.png").convert()

    wipeob = pygame.image.load("Sprites/Misc/obj/wipeob.png").convert()

    gdp1 = pygame.image.load("Sprites/Misc/bg/wipebg1.png").convert()
    gdp2 = pygame.image.load("Sprites/Misc/bg/wipebg2.png").convert()
    gdp3 = pygame.image.load("Sprites/Misc/bg/wipebg3.png").convert()
    gdp4 = pygame.image.load("Sprites/Misc/bg/wipebg4.png").convert()
    gdp5 = pygame.image.load("Sprites/Misc/bg/wipebg5.png").convert()
    gdp6 = pygame.image.load("Sprites/Misc/bg/wipebg6.png").convert()

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
            screen.blit(gymbg, [0, 0])
            if end == 0:
                tcs = 0 + (anifr % 12 < 6)
                spr = 3 + (anifr % 12 < 6) + (8 * wipng)
            else:
                tcs = 2
                spr = 5
            if gdpl[0] > 0:
                screen.blit(gdp1, [64, 120])
            if gdpl[1] > 0:
                screen.blit(gdp2, [10, 110])
            if gdpl[2] > 0:
                screen.blit(gdp3, [148, 92])
            if gdpl[3] > 0:
                screen.blit(gdp4, [170, 49])
            if gdpl[4] > 0:
                screen.blit(gdp5, [119, 95])
            if gdpl[5] > 0:
                screen.blit(gdp6, [19, 43])
            if wipng:
                screen.blit(pygame.transform.flip(wipeob, flip, 0), [(wipex + (4 * (anifr % 12 < 6))), wipey])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [(charax + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (charay + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit(tsprs[tcs], [184, 98])
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
                    elif play and end == 0:
                        if 64 < mp[0] < 112 and 120 < mp[1] < 136 and gdpl[0] > 0:
                            gdpl[0] -= 1
                            charax = 40
                            charay = 102
                            flip = True
                            if gdpl[0] > 0:
                                wipng = True
                                wipex = 64
                                wipey = 120
                            else:
                                wipng = False
                                pygame.mixer.stop()
                                sound[9].play()
                        if 10 < mp[0] < 52 and 110 < mp[1] < 124 and gdpl[1] > 0:
                            gdpl[1] -= 1
                            charax = 54
                            charay = 92
                            flip = False
                            if gdpl[1] > 0:
                                wipng = True
                                wipex = 20
                                wipey = 106
                            else:
                                wipng = False
                                pygame.mixer.stop()
                                sound[9].play()
                        if 148 < mp[0] < 186 and 92 < mp[1] < 130 and gdpl[2] > 0:
                            gdpl[2] -= 1
                            charax = 116
                            charay = 98
                            flip = True
                            if gdpl[2] > 0:
                                wipng = True
                                wipex = 150
                                wipey = 84
                            else:
                                wipng = False
                                pygame.mixer.stop()
                                sound[9].play()
                        if 170 < mp[0] < 213 and 49 < mp[1] < 75 and gdpl[3] > 0:
                            gdpl[3] -= 1
                            charax = 196
                            charay = 72
                            flip = False
                            if gdpl[3] > 0:
                                wipng = True
                                wipex = 182
                                wipey = 62
                            else:
                                wipng = False
                                pygame.mixer.stop()
                                sound[9].play()
                        if 119 < mp[0] < 149 and 95 < mp[1] < 115 and gdpl[4] > 0:
                            gdpl[4] -= 1
                            charax = 84
                            charay = 84
                            flip = True
                            if gdpl[4] > 0:
                                wipng = True
                                wipex = 120
                                wipey = 87
                            else:
                                wipng = False
                                pygame.mixer.stop()
                                sound[9].play()
                        if 19 < mp[0] < 61 and 43 < mp[1] < 91 and gdpl[5] > 0:
                            gdpl[5] -= 1
                            charax = 56
                            charay = 72
                            flip = False
                            if gdpl[5] > 0:
                                wipng = True
                                wipex = 32
                                wipey = 59
                            else:
                                wipng = False
                                pygame.mixer.stop()
                                sound[9].play()
                        if sum(gdpl) == 0:
                            pygame.mixer.stop()
                            sound[9].play()
                            end = 1
                            anifr = 971
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
        if anifr < (23 + (960 * play)):
            anifr += 1
        else:
            anifr = 0
            if strt:
                play = True
                strt = False
                charax = 72
                charay = 98
                flip = False
            elif play:
                play = False
                end = 4
                scr = (192 - sum(gdpl)) // 16
                if scr < 4:
                    pygame.mixer.stop()
                    sound[14].play()
                else:
                    pygame.mixer.stop()
                    sound[1].play()
                avars[avars[3][5]][10] += scr
            elif end == 4:
                ret = 0
                return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

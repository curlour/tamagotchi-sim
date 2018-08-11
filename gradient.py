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

    def setcolour(col1, col2, resc):
        gradim = pygame.image.load("Sprites/Misc/bg/gradientbg1.png")
        gradim.set_palette_at(4, col1)
        gradim.set_palette_at(5, resc)
        gradim.set_palette_at(6, col2)
        gradim.convert()
        return(gradim)

    def gencolour():
        r1 = randint(0, 3)
        r2 = randint(0, 3)
        g1 = randint(0, 3)
        g2 = randint(0, 3)
        b1 = randint(0, 3)
        b2 = randint(0, 3)
        col1 = ((r1 * 84), (g1 * 84), (b1 * 84), 255)
        col2 = ((r2 * 84), (g2 * 84), (b2 * 84), 255)
        col3 = (((r1 + r2) * 42), ((g1 + g2) * 42), ((b1 + b2) * 42), 255)
        resc = (0, 0, 0, 255)
        gradim = setcolour(col1, col2, resc)
        return(col1, col2, col3, resc, gradim)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    tutimg = pygame.image.load("Sprites/Misc/bg/gradientt.png").convert()

    classbg = pygame.image.load("Sprites/Misc/bg/styclass.png").convert()
    whitebg = pygame.image.load("Sprites/Misc/bg/gradientbg.png").convert()

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
            screen.blit(whitebg, [0, 0])
            screen.blit(gradim, [17, 32])
            if end == 0:
                tcs = 0 + (anifr % 12 < 6)
                spr = 3 + (anifr % 12 < 6)
            elif end == 1:
                tcs = 1
                spr = 12
            else:
                tcs = 2 + (resc != col3)
                spr = 5 + (2 * (resc != col3))
            screen.blit(tsprs[tcs], [205, 101])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], 1, 0), [(3 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (101 + (32 - asprs[avars[3][5]][spr].get_height()))])
        else:
            screen.blit(classbg, [0, 0])
            if end == 4:
                if scr < 1:
                    screen.blit(toobad, [71, 40])
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 6
                        tcs = 1
                    else:
                        spr = 7
                        tcs = 3
                else:
                    if scr < 2:
                        screen.blit(good, [94, 40])
                    elif scr < 3:
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
                    elif 82 < mp[1] < 118 and play and end == 0:
                        if 80 < mp[0] < 94:
                            if ((mp[1] - 82) // 18) == 0 and resc[0] < 252:
                                resc = ((resc[0] + 42), resc[1], resc[2], 255)
                            elif ((mp[1] - 82) // 18) == 1 and resc[0] > 0:
                                resc = ((resc[0] - 42), resc[1], resc[2], 255)
                        elif 128 < mp[0] < 142:
                            if ((mp[1] - 82) // 18) == 0 and resc[1] < 252:
                                resc = (resc[0], (resc[1] + 42), resc[2], 255)
                            elif ((mp[1] - 82) // 18) == 1 and resc[1] > 0:
                                resc = (resc[0], (resc[1] - 42), resc[2], 255)
                        elif 176 < mp[0] < 190:
                            if ((mp[1] - 82) // 18) == 0 and resc[2] < 252:
                                resc = (resc[0], resc[1], (resc[2] + 42), 255)
                            elif ((mp[1] - 82) // 18) == 1 and resc[2] > 0:
                                resc = (resc[0], resc[1], (resc[2] - 42), 255)
                        if (resc == col1) or (resc == col2):
                            pygame.mixer.stop()
                            sound[9].play()
                        gradim = setcolour(col1, col2, resc)
                        anifr = 20
                        end = 1
                    if 32 < mp[1] < 80 and play and end == 0:
                        end = 2
                        anifr = 11
                        pygame.mixer.stop()
                        sound[12 - (3 * (resc == col3))].play()
                        gradim = setcolour(col1, col2, col3)
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
                col1, col2, col3, resc, gradim = gencolour()
            elif play:
                if end == 1:
                    end = 0
                elif end == 2:
                    if resc == col3:
                        scr += 1
                        if scr < 3:
                            end = 0
                            col1, col2, col3, resc, gradim = gencolour()
                        else:
                            play = False
                            end = 4
                    else:
                        play = False
                        end = 4
                if not play:
                    if scr < 1:
                        pygame.mixer.stop()
                        sound[14].play()
                    else:
                        pygame.mixer.stop()
                        sound[1].play()
                    avars[avars[3][5]][6] += (scr * 4)
            elif end == 4:
                ret = 0
                return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

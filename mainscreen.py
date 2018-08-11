import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import shelve
import sounds
import varsup
import borders
import growth
import eggsel
import dirty
import palette
import stsico
import foodico
import bathico
import doorico
import heartico
import mailico
import itmico
import notebk
import optico
import preschool
import tamaschool

def mnscr():
    screen = pygame.display.set_mode((240, 160))
    pygame.display.set_caption('Tamagotchi PC')
    pygame.display.set_icon(pygame.image.load("Sprites/Misc/icon/icon.png").convert())
    
    kr = True

    global flip
    flip = False

    def chsprs(chara, dirt, g):
        sprs = []
        if chara > 0:
            try:
                bs = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "b.png")
                ss = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "s.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, g, opal)
                if dirt:
                    bs = dirty.dirt(bs)
                ss = palette.palch(ss, g, opal)
            except:
                bs = pygame.image.load("Sprites/NPC/Nazotchi.png")
                ss = pygame.image.load("Sprites/NPC/Nazo.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, g, opal)
                ss = palette.palch(ss, g, opal)
            for i in range(3):
                a = pygame.Surface([16, 16])
                a.fill((0, 255, 255))
                a.blit(ss, [-(16 * (i % 2)), -(16 * (i // 2))])
                a.set_colorkey((0, 255, 255))
                a.convert()
                sprs.append(a)
            s = (bs.get_width() // 4)
            for i in range(16):
                spr = pygame.Surface([s, s]).convert()
                spr.fill((0, 255, 255))
                spr.blit(bs, [-(s * (i % 4)), -(s * (i // 4))])
                spr.set_colorkey((0, 255, 255))
                sprs.append(spr)
        else:
            bs = pygame.image.load("Sprites/Eggs/egg_" + str(-chara) + "b.png")
            ss = pygame.image.load("Sprites/Eggs/egg_" + str(-chara) + "s.png")
            for i in range(2):
                a = pygame.Surface([16, 16])
                a.fill((0, 255, 255))
                a.blit(ss, [-(16 * (i % 2)), 0])
                a.set_colorkey((0, 255, 255))
                a.convert()
                sprs.append(a)
            for i in range(4):
                spr = pygame.Surface([24, 24]).convert()
                spr.fill((0, 255, 255))
                spr.blit(bs, [-(24 * (i % 2)), -(24 * (i // 2))])
                spr.set_colorkey((0, 255, 255))
                sprs.append(spr)
        return(sprs)

    def charaanim():
        global spr
        global sprx
        global spry
        global flip
        flip = False
        if avars[avars[3][5]][1] == 0:
            sprx = 108
            spry = 106
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 2
            else:
                spr = 3
        if avars[avars[3][5]][1] > 0:
            if name:
                genbk= pygame.Surface([240, 24]).convert()
                if avars[avars[3][5]][14] % 2 == 0:
                    genbk.fill((0, 0, 100))
                    genbk.blit(boytxt, [102, 4])
                else:
                    genbk.fill((100, 0, 0))
                    genbk.blit(girltxt, [96, 4])
                screen.blit(genbk, [0, 24])
                sprx = 112
                spry = 114
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    spr = 6
                else:
                    spr = 7
            elif dying:
                spr = 7
                sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                if anifr < 60:
                    spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                else:
                    spry = 160 + (32 - asprs[avars[3][5]][spr].get_height())
            elif btoilet:
                spr = 14
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    sprx = 103 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                else:
                    sprx = 105 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            elif poo:
                spr = 12
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                if avars[avars[3][5]][4] < 4:
                    sprx = 170 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                else:
                    sprx = 170 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            elif clean:
                screen.blit(clnbr, [170, (28 + (3 * anifr))])
            elif happyani:
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    spr = 4
                    spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                else:
                    spr = 5
                    spry = 90 + (32 - asprs[avars[3][5]][spr].get_height())
                sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            elif not avars[avars[3][5]][21]:
                spr = 18
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            elif evoa:
                if anifr < 36:
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 11
                    else:
                        spr = 3
                elif anifr < 126:
                    spr = 9
                elif anifr < 138:
                    spr = 10
                else:
                    spr = 5
                if 35 < anifr < 126:
                    spry = 98 + ((32 - asprs[avars[3][5]][spr].get_height()) // 2)
                else:
                    spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            else:
                if avars[avars[3][5]][16] == 0 or avars[avars[3][5]][17] == 0 or avars[avars[3][5]][20]:
                    if cure:
                        if anifr < 5:
                            spr = 6
                        elif anifr < 10:
                            spr = 7
                        elif anifr < 15:
                            spr = 10
                    else:
                        if ((anifr / 12) - (anifr // 12)) < 0.5:
                            spr = 6
                        else:
                            spr = 7
                    sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                elif avars[avars[3][5]][16] < 4 or avars[avars[3][5]][17] < 4:
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 3
                    else:
                        spr = 4
                    spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                    if 0 <= anifr < 6:
                        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 6 <= anifr < 12:
                        sprx = 90 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 12 <= anifr < 18:
                        sprx = 80 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 18 <= anifr < 24:
                        sprx = 72 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 24 <= anifr < 30:
                        flip = True
                        sprx = 76 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 30 <= anifr < 36:
                        flip = True
                        sprx = 90 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 36 <= anifr < 42:
                        flip = True
                        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 42 <= anifr < 48:
                        flip = True
                        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 48 <= anifr < 54:
                        flip = True
                        sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 54 <= anifr < 60:
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 60 <= anifr < 66:
                        flip = True
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 66 <= anifr < 72:
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 72 <= anifr < 78:
                        flip = True
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 78 <= anifr < 84:
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 84 <= anifr < 90:
                        flip = True
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 90 <= anifr < 96:
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 96 <= anifr < 102:
                        flip = True
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 102 <= anifr < 108:
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 108 <= anifr < 114:
                        sprx = 132 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 114 <= anifr < 120:
                        sprx = 124 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 120 <= anifr < 126:
                        sprx = 116 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 126 <= anifr < 132:
                        sprx = 112 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 132 <= anifr < 138:
                        sprx = 108 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 138 <= anifr:
                        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                elif avars[avars[3][5]][16] > 3 and avars[avars[3][5]][17] > 3:
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        if 12 <= anifr < 18 or 36 <= anifr < 42 or 48 <= anifr < 54 or 96 <= anifr < 102 or 132 <= anifr < 138:
                            spr = 5
                        elif 0 <= anifr < 6 or 24 <= anifr < 30 or 84 <= anifr < 90 or 108 <= anifr < 114:
                            spr = 10
                        else:
                            spr = 3
                    else:
                        spr = 4
                    spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                    if 0 <= anifr < 6:
                        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 6 <= anifr < 12:
                        sprx = 90 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 12 <= anifr < 18:
                        spry -= 8
                        sprx = 80 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 18 <= anifr < 24:
                        sprx = 72 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 24 <= anifr < 30:
                        flip = True
                        sprx = 76 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 30 <= anifr < 36:
                        flip = True
                        sprx = 90 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 36 <= anifr < 42:
                        spry -= 8
                        flip = True
                        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 42 <= anifr < 48:
                        flip = True
                        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 48 <= anifr < 54:
                        spry -= 8
                        flip = True
                        sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 54 <= anifr < 60:
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 60 <= anifr < 66:
                        flip = True
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 66 <= anifr < 72:
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 72 <= anifr < 78:
                        flip = True
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 78 <= anifr < 84:
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 84 <= anifr < 90:
                        flip = True
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 90 <= anifr < 96:
                        sprx = 140 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 96 <= anifr < 102:
                        spry -= 8
                        sprx = 138 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 102 <= anifr < 108:
                        sprx = 134 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 108 <= anifr < 114:
                        sprx = 132 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 114 <= anifr < 120:
                        sprx = 124 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 120 <= anifr < 126:
                        sprx = 116 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 126 <= anifr < 132:
                        sprx = 112 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 132 <= anifr < 138:
                        spry -= 8
                        sprx = 108 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    if 138 <= anifr:
                        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)

    def egghatch(screen):
        global avars
        global asprs
        htch = True
        anifr = -1
        while htch:
            screen.blit(bgi, [0, 0])
            screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, 0, fnt, name, anifr, hn, hp, sk, sl)
            spr = 4
            spry = 106
            if ((anifr / 4) - (anifr // 4)) < 0.5:
                sprx = 107
            else:
                sprx = 109
            if anifr < 23:
                anifr += 1
                screen.blit(asprs[avars[3][5]][spr], [sprx, spry])
            else:
                pygame.mixer.stop()
                sound[8].play()
                avars[avars[3][5]][1] += 1
                avars = growth.grw(avars)
                eggspr = asprs[avars[3][5]][5]
                asprs = aspr()
                chspr = 5
                screen.blit(asprs[avars[3][5]][chspr], [112, 107])
                screen.blit(eggspr, [108, 109])
                r = pygame.Surface([240, 160]).convert()
                r.blit(screen, [0, 0])
                s = pygame.Surface([240, 160]).convert()
                s.blit(screen, [0, 0])
                s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
                screen.blit(s, [0, 0])
                pygame.display.update()
                pygame.time.delay(1500)
                screen.blit(r, [0, 0])
                htch = False
            s = pygame.Surface([240, 160]).convert()
            s.blit(screen, [0, 0])
            s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
            screen.blit(s, [0, 0])
            clock.tick(16)
            pygame.display.update()
            if not htch:
                screen.blit(r, [0, 0])

    def stsupd(a, avars, asprs):
        global btoilet
        global poo
        global clean
        global evoa
        global dying
        global cure
        global anifr
        if not (name * (avars[3][5] == a)) and avars[a][1] > 0:
            if avars[a][21]:
                if avars[a][2] > 30:
                    if avars[a][1] == 1:
                        hngt = 300
                        hppt = 360
                        evot = 3600
                        if avars[a][2] == 900:
                            if avars[a][20]:
                                avars[a][19] += 1
                            else:
                                avars[a][20] = True
                            pygame.mixer.stop()
                            sound[0].play()
                        if 1800 < avars[a][2] < 2100:
                            avars[a][21] = False
                            if avars[a][4] > 0 and avars[a][30] == 0:
                                avars[a][30] = 1
                    elif avars[a][1] == 2:
                        hngt = 3000
                        hppt = 2700
                        evot = 176400
                        if int(avars[3][6][:2]) > 19 or int(avars[3][6][:2]) < 9:
                            avars[a][21] = False
                            if avars[a][4] > 0 and avars[a][30] == 0:
                                avars[a][30] = 1
                    elif avars[a][1] == 3:
                        hngt = 2700
                        hppt = 3600
                        evot = 435600
                        if int(avars[3][6][:2]) > 20 or int(avars[3][6][:2]) < 9:
                            avars[a][21] = False
                            if avars[a][4] > 0 and avars[a][30] == 0:
                                avars[a][30] = 1
                    elif avars[a][1] < 6:
                        hngt = 4800
                        hppt = 6000
                        evot = 1382400
                        if int(avars[3][6][:2]) > 21 or int(avars[3][6][:2]) < 9:
                            avars[a][21] = False
                            if avars[a][4] > 0 and avars[a][30] == 0:
                                avars[a][30] = 1
                    else:
                        if ((avars[a][2] - 1382400) // 230400) > avars[a][19]:
                            avars[a][19] = ((avars[a][2] - 1382400) // 230400)
                        hngt = 4800 // (avars[a][19] + 1)
                        hppt = 6000 // (avars[a][19] + 1)
                        evot = 4294967295
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
                        if avars[a][16] == 0:
                            pygame.mixer.stop()
                            sound[0].play()
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
                        if avars[a][17] == 0:
                            pygame.mixer.stop()
                            sound[0].play()
                    if avars[3][5] == a and not evoa:
                        if ((((avars[a][2] // 60) / (hngt // 30)) - ((avars[a][2] // 60) // (hngt // 30))) == 0) and ((avars[a][2] - (60 * (avars[a][2] // 60))) < 30):
                            if avars[a][33] < 4:
                                if avars[a][4] < 8:
                                    btoilet = True
                                    pygame.mixer.stop()
                                    sound[10].play()
                            else:
                                avars = bathico.bathroom(avars, 0, asprs, screen)
                        if (((avars[a][2] - 29) / (2 * hngt)) - ((avars[a][2] - 29) // (2 * hngt))) == 0:
                            if avars[a][4] == 8:
                                if avars[a][20]:
                                    avars[a][19] += 1
                                else:
                                    avars[a][20] = True
                    elif avars[a][2] < evot:
                        if (((avars[a][2] - 30) / (2 * hngt)) - ((avars[a][2] - 30) // (2 * hngt))) == 0:
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
                    if avars[a][2] >= evot and not evoa:
                        if avars[3][5] == a:
                            btoilet = False
                            anifr = 0
                            evoa = True
                        else:
                            avars[a][1] += 1 + (avars[a][1] == 4)
                            b = avars[3][5]
                            avars[3][5] = a
                            avars = growth.grw(avars)
                            avars[3][5] = b
                            avars[a][19] = 0
                            if avars[a][1] == 2:
                                avars[a][31] = 1
                            elif avars[a][1] == 6:
                                avars[a][31] = 40
                            asprs = aspr()
                    if avars[a][19] > 5:
                        if avars[3][5] == a:
                            anifr = 0
                            dying = True
                            btoilet = False
                            poo = False
                            clean = False
                            evoa = False
                            pygame.mixer.stop()
                            sound[17].play()
                        else:
                            b = avars[3][10]
                            b.append([avars[a][1],
                                      avars[a][2],
                                      avars[a][3],
                                      avars[a][14],
                                      avars[a][15],
                                      avars[a][22],
                                      avars[a][24]])
                            avars[3][10] = b
                            varsup.updtvrs(avars)
                            d = shelve.open('save_db')
                            del d['egg' + str(a + 1)]
                            d.close()
                            avars = impvrs()
                            asprs = aspr()
            else:
                if avars[a][1] == 1:
                    if avars[a][2] > 2100:
                        avars[a][21] = True
                        if avars[a][30] < 2:
                            avars[a][30] += 1
                        else:
                            avars[a][19] += 1
                        asprs = aspr()
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
                        asprs = aspr()
                        avars[3][11] = -1
        return(avars, asprs)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    sickbg = pygame.image.load("Sprites/Misc/bg/sick.png").convert()
    sickbg.set_alpha(204)

    skull = pygame.image.load("Sprites/Misc/sick/skull.png").convert()
    cure1 = pygame.image.load("Sprites/Misc/sick/med1.png").convert()
    cure2 = pygame.image.load("Sprites/Misc/sick/med2.png").convert()

    deathg = pygame.image.load("Sprites/Misc/sick/deathgod.png").convert()
    ghost = pygame.image.load("Sprites/Misc/sick/ghost.png").convert()

    slpbg = pygame.Surface([240, 160]).convert()
    slpbg.fill((0, 0, 100))
    slpbg.set_alpha(204)

    embk = pygame.Surface([240, 160]).convert()
    embk.fill((0, 0, 100))

    evoa1 = pygame.image.load("Sprites/Misc/bg/evo1.png").convert()
    evoa2 = pygame.image.load("Sprites/Misc/bg/evo2.png").convert()
    evoa3 = pygame.Surface([240, 160]).convert()
    evoa3.fill((255, 255, 240))
    evoa3.set_alpha(204)
    evoa3.blit(pygame.image.load("Sprites/Misc/bg/evo3.png").convert(), [0, 0])

    slp1 = pygame.image.load("Sprites/Misc/emo/sleep1.png").convert()
    slp2 = pygame.image.load("Sprites/Misc/emo/sleep2.png").convert()

    bpoo = [pygame.image.load("Sprites/Misc/poo/bpoo1.png").convert(), pygame.image.load("Sprites/Misc/poo/bpoo2.png").convert()]
    spoo = [pygame.image.load("Sprites/Misc/poo/spoo1.png").convert(), pygame.image.load("Sprites/Misc/poo/spoo2.png").convert()]
    poop = 0

    happys = pygame.image.load("Sprites/Misc/emo/happy.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    boytxt = fnt.render("BOY", 1, (204, 204, 255))

    girltxt = fnt.render("GIRL", 1, (255, 204, 204))

    wrttxt = fnt.render("WRITE", 1, (102, 102, 255))

    clnbr = pygame.image.load("Sprites/Misc/poo/clean.png").convert()

    clock = pygame.time.Clock()

    def impvrs():
        d = shelve.open('save_db')
        if ('egg1' in d):
            var1 = [d['egg1'], d['charag1'], d['time1'], d['gene1'], d['poo1'], d['int1'], d['sty1'], d['knd1'], d['hum1'], d['gor1'], d['pas1'], d['grp1'], d['grpf1'],
                    d['grpm1'], d['gender1'], d['chara1'], d['hungry1'], d['happy1'], d['weight1'], d['caremiss1'], d['sick1'], d['awake1'], d['chname1'], d['room1'],
                    d['stages1'], d['parent1'], d['pspouse1'], d['gparent1'], d['gpspouse1'] ,d['agen1'], d['dirty1'], d['edu1'], d['frnd1'], d['pttrain1']]
        else:
            var1 = []

        if ('egg2' in d):
            var2 = [d['egg2'], d['charag2'], d['time2'], d['gene2'], d['poo2'], d['int2'], d['sty2'], d['knd2'], d['hum2'], d['gor2'], d['pas2'], d['grp2'], d['grpf2'],
                    d['grpm2'], d['gender2'], d['chara2'], d['hungry2'], d['happy2'], d['weight2'], d['caremiss2'], d['sick2'], d['awake2'], d['chname2'], d['room2'],
                    d['stages2'], d['parent2'], d['pspouse2'], d['gparent2'], d['gpspouse2'], d['agen2'], d['dirty2'], d['edu2'], d['frnd2'], d['pttrain2']]
        else:
            var2 = []

        if ('egg3' in d):
            var3 = [d['egg3'], d['charag3'], d['time3'], d['gene3'], d['poo3'], d['int3'], d['sty3'], d['knd3'], d['hum3'], d['gor3'], d['pas3'], d['grp3'], d['grpf3'],
                    d['grpm3'], d['gender3'], d['chara3'], d['hungry3'], d['happy3'], d['weight3'], d['caremiss3'], d['sick3'], d['awake3'], d['chname3'], d['room3'],
                    d['stages3'], d['parent3'], d['pspouse3'], d['gparent3'], d['gpspouse3'], d['agen3'], d['dirty3'], d['edu3'], d['frnd3'], d['pttrain3']]
        else:
            var3 = []

        gvar = [d['uname'], d['bday'], d['money'], d['speed'], d['food'], d['selchara'], d['hour'], d['secs'], d['vol'], d['item'], d['grave'], d['mail'],
                d['lstdt'], d['border'], d['chegg'], d['kitchen'], d['table'], d['chair'], d['wc'], d['toilet'], d['btoilet'], d['bathr'], d['bath'], d['dex']]

        avars = [var1, var2, var3, gvar]
        d.close()
        return(avars)

    try:
        global avars
        avars =  impvrs()
    except KeyError:
        if os.path.isfile("save_db.dat"):
            os.remove('save_db.dat')
        if os.path.isfile("save_db.bak"):
            os.remove('save_db.bak')
        if os.path.isfile("save_db.dir"):
            os.remove('save_db.dir')
        for file in os.listdir("Sprites/Misc/mail/tm1"):
            if file.endswith(".png"):
                os.remove("Sprites/Misc/mail/tm1/" + file)
        for file in os.listdir("Sprites/Misc/mail/tm2"):
            if file.endswith(".png"):
                os.remove("Sprites/Misc/mail/tm2/" + file)
        for file in os.listdir("Sprites/Misc/mail/tm3"):
            if file.endswith(".png"):
                os.remove("Sprites/Misc/mail/tm3/" + file)
        if os.path.isfile("Sprites/Misc/mail/news.png"):
            os.remove("Sprites/Misc/mail/news.png")
        kr = False
        pygame.quit()
        sys.exit()

    tpborder, btborder = borders.getborders(avars[3][13], 0, 0, 0)

    def aspr():
        if len(avars[0]) > 0:
            if avars[0][1] > 0:
                sprs0 = chsprs(avars[0][15], (avars[0][30] == 2), avars[0][14])
            else:
                sprs0 = chsprs(0 - avars[0][0], 0, 0)
        else:
            sprs0 = []
        if len(avars[1]) > 0:
            if avars[1][1] > 0:
                sprs1 = chsprs(avars[1][15], (avars[1][30] == 2), avars[1][14])
            else:
                sprs1 = chsprs(0 - avars[1][0], 0, 0)
        else:
            sprs1 = []
        if len(avars[2]) > 0:
            if avars[2][1] > 0:
                sprs2 = chsprs(avars[2][15], (avars[2][30] == 2), avars[2][14])
            else:
                sprs2 = chsprs(0 - avars[2][0], 0, 0)
        else:
            sprs2 = []
        asprs = [sprs0, sprs1, sprs2]
        return(asprs)

    global asprs
    asprs = aspr()

    def drawbg():
        try:
            if pygame.image.load(avars[avars[3][5]][23]).get_rect().size == (240, 160):
                bgi = pygame.image.load(avars[avars[3][5]][23]).convert()
            else:
                bgi = pygame.Surface([240, 160]).convert()
                bgi.fill((51, 51, 204))
                bgi.blit(fnt.render("IMAGE SIZE IS", 1, (255, 255, 255)), [8, 34])
                bgi.blit(fnt.render("INCORRECT!!!", 1, (255, 255, 255)), [8, 50])
                bgi.blit(fnt.render("DO NOT MESS", 1, (255, 255, 255)), [8, 66])
                bgi.blit(fnt.render("WITH THE", 1, (255, 255, 255)), [8, 82])
                bgi.blit(fnt.render("GAME FILES!", 1, (255, 255, 255)), [8, 98])
        except pygame.error:
            bgi = pygame.Surface([240, 160]).convert()
            bgi.fill((51, 51, 204))
            bgi.blit(fnt.render("ERROR 404:", 1, (255, 255, 255)), [8, 34])
            bgi.blit(fnt.render("BACKGROUND IMAGE", 1, (255, 255, 255)), [8, 50])
            bgi.blit(fnt.render("NOT FOUND", 1, (255, 255, 255)), [8, 66])
        if int(time.strftime("%m")) == 12 and int(time.strftime("%d")) > 19:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/xmasbg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 1 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/newyearbg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 3 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/girlsbg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 4 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/hanamibg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 5 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/boysbg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 7 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/tanabatabg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 8 and 10 < int(time.strftime("%d")) < 21:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/firewkbg.png").convert(), [0, 0])
        elif (int(time.strftime("%m")) == 10 and int(time.strftime("%d")) > 25) or (int(time.strftime("%m")) == 11 and int(time.strftime("%d")) < 5):
            bgi.blit(pygame.image.load("Sprites/Misc/bg/haweenbg.png").convert(), [0, 0])
        if (time.strftime("%m") + time.strftime("%d")) == avars[3][1]:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/bdaybg.png").convert(), [0, 0])
        return(bgi)

    bgi = drawbg()

    sound = sounds.imprtsnd(avars)

    global anifr
    anifr = 0

    happyani = False

    name = False

    anim = True

    global btoilet
    btoilet = False

    global poo
    poo = False

    global clean
    clean = False

    global evoa
    evoa = False

    global dying
    dying = False

    global cure
    cure = False

    chngsts = False

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")
        if avars[3][12] != time.strftime("%Y/%m/%d"):
            avars[3][11] = -1
            if len(avars[0]) > 0:
                avars[0][2] += 43200
                if avars[0][21]:
                    avars[0][21] = False
            if len(avars[1]) > 0:
                avars[1][2] += 43200
                if avars[1][21]:
                    avars[1][21] = False
            if len(avars[2]) > 0:
                avars[2][2] += 43200
                if avars[2][21]:
                    avars[2][21] = False

    while kr:
        screen.blit(bgi, [0, 0])
        if avars[avars[3][5]][1] > 0 and not name:
            if not avars[avars[3][5]][21]:
                screen.blit(slpbg, [0, 0])
            elif dying:
                if anifr < 36:
                    screen.blit(slpbg, [0, 0])
                    screen.blit(sickbg, [0, 0])
                else:
                    screen.blit(embk, [0, 0])
            elif evoa:
                if 35 < anifr < 120:
                    if 71 < anifr < 84:
                        screen.blit(evoa3, [0, 0])
                    else:
                        if ((anifr / 12) - (anifr // 12)) < 0.5:
                            screen.blit(evoa1, [0, 0])
                        else:
                            screen.blit(evoa2, [0, 0])
            elif avars[avars[3][5]][20]:
                screen.blit(sickbg, [0, 0])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, 0, fnt, name, anifr, hn, hp, sk, sl)
        if avars[avars[3][5]][4] > 0:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                poop = 0
            else:
                poop = 1
            if avars[avars[3][5]][4] > 1:
                screen.blit(bpoo[poop], [218, 116])
                if avars[avars[3][5]][4] > 2:
                    if avars[avars[3][5]][4] > 3:
                        screen.blit(bpoo[poop], [209, 98])
                        if avars[avars[3][5]][4] > 4:
                            if avars[avars[3][5]][4] > 5:
                                screen.blit(bpoo[poop], [202, 116])
                                if avars[avars[3][5]][4] > 6:
                                    if avars[avars[3][5]][4] > 7:
                                        screen.blit(bpoo[poop], [193, 98])
                                    else:
                                        screen.blit(spoo[poop], [193, 98])
                            else:
                                screen.blit(spoo[poop], [202, 116])
                    else:
                        screen.blit(spoo[poop], [209, 98])
            else:
                screen.blit(spoo[poop], [218, 116])
        if avars[avars[3][5]][1] > 0:
            if not avars[avars[3][5]][21]:
                btoilet = False
                happyani = False
                clean = False
                cure = False
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    screen.blit(slp1, [136, 82])
                else:
                    screen.blit(slp2, [136, 82])
            elif dying:
                if anifr < 84:
                    if ((anifr / 12) - (anifr // 12)) == 0.5 or ((anifr / 12) - (anifr // 12)) == 0:
                        deathg = pygame.transform.flip(deathg, 1, 0)
                    if anifr < 12:
                        dgx = 144
                        dgy = 56
                    elif anifr < 24:
                        dgx = 144
                        dgy = 70
                    elif anifr < 60:
                        dgx = 144
                        dgy = 84
                    else:
                        dgx = 114
                        dgy = 114
                    screen.blit(deathg, [dgx, dgy])
                elif anifr > 95 and anifr < 132:
                    if ((anifr / 12) - (anifr // 12)) == 0.5 or ((anifr / 12) - (anifr // 12)) == 0:
                        ghost = pygame.transform.flip(ghost, 1, 0)
                    if anifr < 108:
                        dgy = 106
                    elif anifr < 114:
                        dgy = 82
                    elif anifr < 120:
                        dgy = 64
                    elif anifr < 126:
                        dgy = 46
                    else:
                        dgy = 28
                    screen.blit(ghost, [108, dgy])
            elif avars[avars[3][5]][20]:
                if cure:
                    if anifr < 5 or anifr > 10:
                        screen.blit(cure1, [144, 90])
                    else:
                        screen.blit(cure2, [144, 98])
                else:
                    screen.blit(skull, [144, 56])
        if happyani and ((anifr / 12) - (anifr // 12)) >= 0.5:
            screen.blit(happys, [136, 82])
        if anim:
            charaanim()
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [sprx, spry])
        else:
            anim = True
        for event in pygame.event.get():
            if event.type == QUIT:
                if avars[avars[3][5]][1] > 0:
                    if not name:
                        varsup.updtvrs(avars)
                        kr = False
                        pygame.quit()
                        sys.exit()
            if event.type == USEREVENT + 1:
                if len(avars[0]) > 0:
                    avars[0][2] += 1
                if len(avars[1]) > 0:
                    avars[1][2] += 1
                if len(avars[2]) > 0:
                    avars[2][2] += 1
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
                if avars[avars[3][5]][1] == 0:
                    if avars[avars[3][5]][2] == 60:
                        pygame.mixer.stop()
                        sound[7].play()
                        egghatch(screen)
                        name = True
                        ne = False
                        global nw
                        nw = ""
                        nmwr = fnt.render(nw, 1, (0, 0, 100))
                        anim = True
                else:
                    if not name:
                        chngsts = True
                        if btoilet:
                            if (avars[avars[3][5]][2] - (60 * (avars[avars[3][5]][2] // 60))) == 30:
                                anifr = 0
                                if avars[avars[3][5]][18] > 3:
                                    avars[avars[3][5]][18] -= 2
                                else:
                                    avars[avars[3][5]][18] = 1
                                avars[avars[3][5]][4] += 1
                                pygame.mixer.stop()
                                sound[5].play()
                                poo = True
                                btoilet = False
            if event.type == pygame.KEYDOWN:
                if name:
                    if pygame.K_a <= event.key <= pygame.K_z:
                        ltr = chr(event.key)
                        if len(nw) < 8:
                            nw = (nw + str(ltr)).upper()
                        nmwr = fnt.render(nw, 1, (0, 0, 100))
                        ne = True
                    if event.key == pygame.K_BACKSPACE:
                        if len(nw) != 0:
                            if len(nw) == 1:
                                ne = False
                            nw = nw[:len(nw) - 1]
                            nmwr = fnt.render(nw, 1, (0, 0, 100))
                    if event.key == pygame.K_RETURN:
                        if ne:
                            avars[avars[3][5]][2] = 0
                            avars[avars[3][5]][22] = nw
                            name = False
                            sound[0].play()
                if event.key == pygame.K_F11:
                    if screen.get_size()[0] < 960:
                        screen = pygame.display.set_mode(((screen.get_size()[0] * 2), (screen.get_size()[1] * 2)))
                    else:
                        screen = pygame.display.set_mode((240, 160))
            if event.type == MOUSEBUTTONDOWN and avars[avars[3][5]][1] > 0 and not name:
                mp = event.pos
                d = (screen.get_size()[0] // 240)
                mp = ((mp[0] // d), (mp[1] // d))
                pb = event.button
                if pb == 1 and not cure and not clean and not evoa and not dying:
                    try:
                        if 138 < mp[1] < 158:
                            if 11 < mp[0] < 31:
                                anifr = 0
                                pygame.mixer.stop()
                                sound[3].play()
                                happyani = False
                                btoilet = False
                                avars = stsico.status(avars, asprs, screen)
                            if avars[avars[3][5]][21]:
                                if 55 < mp[0] < 75:
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    if btoilet:
                                        if avars[avars[3][5]][1] > 1:
                                            avars[avars[3][5]][33] += 1
                                        avars = bathico.bathroom(avars, 0, asprs, screen)
                                        btoilet = False
                                        happyani = True
                                        anifr = 122
                                        sound[1].play()
                                    elif avars[avars[3][5]][4] > 0:
                                        if not poo:
                                            clean = True
                                            anifr = 0
                                    else:
                                        strttime = avars[avars[3][5]][2]
                                        avars[avars[3][5]][30] = 0
                                        asprs = aspr()
                                        avars = bathico.bathroom(avars, 1, asprs, screen)
                                        happyani = True
                                        anifr = 122
                                        sound[1].play()
                                if 143 < mp[0] < 163:
                                    if avars[avars[3][5]][20] and not cure:
                                        pygame.mixer.stop()
                                        sound[3].play()
                                        cure = True
                                        anifr = 0
                                    else:
                                        pygame.mixer.stop()
                                        sound[12].play()
                                if not avars[avars[3][5]][20]:
                                    if 33 < mp[0] < 53:
                                        if len(avars[3][4]) > 0:
                                            anifr = 0
                                            pygame.mixer.stop()
                                            sound[3].play()
                                            happyani = False
                                            btoilet = False
                                            avars = foodico.kitchen(avars, asprs, screen)
                                            asprs = aspr()
                                        else:
                                            pygame.mixer.stop()
                                            sound[12].play()
                                    if 77 < mp[0] < 97:
                                        anifr = 0
                                        pygame.mixer.stop()
                                        sound[3].play()
                                        happyani = False
                                        btoilet = False
                                        avars = doorico.door(avars, asprs, screen)
                                        asprs = aspr()
                                        bgi = drawbg()
                                    if 99 < mp[0] < 119:
                                        anifr = 0
                                        pygame.mixer.stop()
                                        sound[3].play()
                                        happyani = False
                                        btoilet = False
                                        varsup.updtvrs(avars)
                                        avars = heartico.com(avars, asprs, screen)
                                        asprs = aspr()
                                        varsup.updtvrs(avars)
                                    if 121 < mp[0] < 141:
                                        anifr = 122
                                        pygame.mixer.stop()
                                        sound[3].play()
                                        happyani = False
                                        btoilet = False
                                        avars = mailico.mailbox(avars, asprs, screen, 1)
                                    if 165 < mp[0] < 185:
                                        if len(avars[3][9]) > 0:
                                            anifr = 122
                                            pygame.mixer.stop()
                                            sound[3].play()
                                            happyani = False
                                            btoilet = False
                                            avars, happyani = itmico.items(avars, asprs, screen)
                                            asprs = aspr()
                                            if happyani:
                                                pygame.mixer.stop()
                                                sound[1].play()
                                        else:
                                            pygame.mixer.stop()
                                            sound[12].play()
                            if 209 < mp[0] < 229:
                                anifr = 0
                                pygame.mixer.stop()
                                sound[3].play()
                                happyani = False
                                btoilet = False
                                avars, asprs = optico.options(avars, asprs, screen)
                                varsup.updtvrs(avars)
                                sound = sounds.imprtsnd(avars)
                                asprs = aspr()
                                bgi = drawbg()
                                tpborder, btborder = borders.getborders(avars[3][13], 0, 0, 0)
                            if 187 < mp[0] < 207:
                                anifr = 0
                                pygame.mixer.stop()
                                sound[3].play()
                                happyani = False
                                btoilet = False
                                avars = notebk.book(avars, asprs, screen)
                        if 2 < mp[1] < 22:
                            if 174 < mp[0] < 194:
                                if len(avars[0]) > 0:
                                    anifr = 0
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    happyani = False
                                    btoilet = False
                                    avars[3][5] = 0
                                    bgi = drawbg()
                            if 196 < mp[0] < 216:
                                if len(avars[1]) > 0:
                                    anifr = 0
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    happyani = False
                                    btoilet = False
                                    avars[3][5] = 1
                                    bgi = drawbg()
                            if 218 < mp[0] < 238:
                                if len(avars[2]) > 0:
                                    anifr = 0
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    happyani = False
                                    btoilet = False
                                    avars[3][5] = 2
                                    bgi = drawbg()
                            if 10 < mp[0] < 54 and avars[3][3]:
                                awkt = 0
                                if len(avars[0]) > 0:
                                    awkt += (avars[0][21] + (avars[0][1] == 1))
                                if len(avars[1]) > 0:
                                    awkt += (avars[1][21] + (avars[1][1] == 1))
                                if len(avars[2]) > 0:
                                    awkt += (avars[2][21] + (avars[2][1] == 1))
                                if awkt == 0:
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    if len(avars[0]) > 0:
                                        if int(avars[3][6][:2]) < 10:
                                            avars[0][2] += 3600 * (9 - int(avars[3][6][:2]))
                                        else:
                                            avars[0][2] += 3600 * (33 - int(avars[3][6][:2]))
                                    if len(avars[1]) > 0:
                                        if int(avars[3][6][:2]) < 10:
                                            avars[1][2] += 3600 * (9 - int(avars[3][6][:2]))
                                        else:
                                            avars[1][2] += 3600 * (33 - int(avars[3][6][:2]))
                                    if len(avars[2]) > 0:
                                        if int(avars[3][6][:2]) < 10:
                                            avars[2][2] += 3600 * (9 - int(avars[3][6][:2]))
                                        else:
                                            avars[2][2] += 3600 * (33 - int(avars[3][6][:2]))
                                    avars[3][6] = "09:00"
                    except:
                        #print('error')
                        pass
        if anifr < 143:
            anifr += 1
            if anifr == 15:
                if happyani:
                    anifr = 0
                    happyani = False
                if clean:
                    avars[avars[3][5]][4] = 0
                    happyani = True
                    clean = False
                    anifr = 122
                    sound[1].play()
                if cure:
                    avars[avars[3][5]][20] = False
                    cure = False
                    happyani = True
                    anifr = 122
                    sound[1].play()
                poo = False
            if evoa and anifr == 72:
                avars[avars[3][5]][1] += 1 + (avars[avars[3][5]][1] == 4)
                avars = growth.grw(avars)
                avars[avars[3][5]][19] = 0
                if avars[avars[3][5]][1] == 2:
                    avars[avars[3][5]][31] = 1
                elif avars[avars[3][5]][1] == 6:
                    avars[avars[3][5]][31] = 40
                asprs = aspr()
            elif evoa and anifr == 36:
                sound[16].play()
        else:
            anifr = 0
            if dying:
                a = avars[3][10]
                a.append([avars[avars[3][5]][1],
                          avars[avars[3][5]][2],
                          avars[avars[3][5]][3],
                          avars[avars[3][5]][14],
                          avars[avars[3][5]][15],
                          avars[avars[3][5]][22],
                          avars[avars[3][5]][24]])
                avars[3][10] = a
                varsup.updtvrs(avars)
                d = shelve.open('save_db')
                if d['selchara'] == 0:
                    del d['egg1']
                elif d['selchara'] == 1:
                    del d['egg2']
                elif d['selchara'] == 2:
                    del d['egg3']
                if ('egg1' in d):
                    d['selchara'] = 0
                elif ('egg2' in d) > 0:
                    d['selchara'] = 1
                elif ('egg3' in d) > 0:
                    d['selchara'] = 2
                else:
                    d['egg1'] = None
                    d.close()
                    eggsel.crdani(screen)
                d.close()
                avars = impvrs()
                dying = False
                asprs = aspr()
                bgi = drawbg()
            if ((avars[3][11] < 5 and int(avars[3][6][:2]) > 15) or avars[3][11] < 0) and avars[avars[3][5]][1] > 1 and avars[avars[3][5]][21]:
                avars = mailico.mailbox(avars, asprs, screen, 0)
            if avars[avars[3][5]][1] > 2 and avars[avars[3][5]][31] < 2:
                avars, a = preschool.pres(avars, asprs, screen)
            if avars[avars[3][5]][2] > 691199 and avars[avars[3][5]][31] < 3 and avars[avars[3][5]][1] > 3:
                avars, a = tamaschool.school(avars, asprs, screen)
                del a
            evoa = False
        if chngsts and not dying:
            if len(avars[0]) > 0:
                avars, asprs = stsupd(0, avars, asprs)
            if len(avars[1]) > 0:
                avars, asprs = stsupd(1, avars, asprs)
            if len(avars[2]) > 0:
                avars, asprs = stsupd(2, avars, asprs)
            chngsts = False
        if avars[avars[3][5]][1] != 0:
            if name:
                screen.blit(nmwr, [67, 6])
                if not ne:
                    screen.blit(wrttxt, [67, 6])
            else:
                try:
                    screen.blit((fnt.render(avars[avars[3][5]][22], 1, (0, 0, 100))), [67, 6])
                except:
                    kr = False
                    pygame.quit()
                    sys.exit()
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        try:
            pygame.display.update()
        except:
            varsup.updtvrs(avars)
            kr = False
            pygame.quit()
            sys.exit()

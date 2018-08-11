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

def game(avars, asprs, screen, fsprs):
    
    kr = True

    chngsts = False

    strt = True
    play = False

    ywn = -1

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    lfnt = pygame.font.Font("Sprites/Misc/font/Tama1.ttf", 16)
    
    bck = pygame.image.load("Sprites/Misc/bg/mamect.png").convert()
    gbck = pygame.image.load("Sprites/Misc/bg/mameg.png").convert()

    cubes = []
    for i in [0, 1, 2, 3]:
        a = pygame.Surface((16, 16))
        a.fill((0, 255, 255))
        a.blit(gbck, [-(16 * i), 0])
        a.set_colorkey((0, 255, 255))
        a.convert()
        cubes.append(a)
        
    cbox = pygame.Surface((16, 16))
    cbox.fill((0, 255, 255))
    cbox.blit(gbck, [-(64), 0])
    cbox.set_colorkey((0, 255, 255))
    cbox.convert()

    cubel = []
    while (len(cubel) < 12):
        cubel.append(randint(0, 3))
    while (cubel.count(0) == cubel.count(1)) or (cubel.count(0) == cubel.count(2)) or (cubel.count(0) == cubel.count(3)) \
          or (cubel.count(1) == cubel.count(2)) or (cubel.count(1) == cubel.count(3)) or (cubel.count(2) == cubel.count(3)):
        cubel = []
        while (len(cubel) < 12):
            cubel.append(randint(0, 3))

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    wint = pygame.image.load("Sprites/Misc/bg/win.png").convert()
    loset = pygame.image.load("Sprites/Misc/bg/lose.png").convert()

    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")
        
    pygame.mixer.stop()
    sound[10].play()

    while kr:
        if strt:
            screen.blit(bck, [0, 0])
            if anifr == 16:
                pygame.mixer.stop()
                sound[11].play()
            if anifr < 16:
                screen.blit(ready, [80, 48])
                spr = 3
            else:
                screen.blit(go, [95, 48])
                spr = 5
            screen.blit(asprs[avars[3][5]][spr], [(136 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit(fsprs[spr], [(72 + ((32 - fsprs[spr].get_width()) // 2)), (98 + (32 - fsprs[spr].get_height()))])
        elif play:
            screen.blit(gbck, [0, 0])
            for i in range(12):
                screen.blit(cubes[cubel[i]], [(24 + (16 * i)), 64])
            if ywn > -1:
                for i in [0, 1]:
                    screen.blit(cbox, [(56 + (112 * i)), 80])
                    screen.blit(cubes[wcl[i != ywn]], [(56 + (112 * i)), 80])
                if anifr == 12:
                    pygame.mixer.stop()
                    sound[12 - (3 * ywn)].play()
            if ywn < 0:
                spr = 6
                frs = 6
            elif anifr < 12:
                spr = 9
                frs = 9
            else:
                spr = 7 - (2 * ywn)
                frs = 5 + (2 * ywn)
            screen.blit(asprs[avars[3][5]][spr], [(160 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit(fsprs[frs], [(48 + ((32 - fsprs[spr].get_width()) // 2)), (98 + (32 - fsprs[spr].get_height()))])
        else:
            screen.blit(bck, [0, 0])
            if ywn:
                screen.blit(wint, [78, 48])
            else:
                screen.blit(loset, [65, 48])
            if anifr % 12 < 6:
                spr = 6 - (2 *  ywn)
                frs = 4 + (2 *  ywn)
            else:
                spr = 7 - (2 *  ywn)
                frs = 5 + (2 *  ywn)
            screen.blit(asprs[avars[3][5]][spr], [(136 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit(fsprs[frs], [(72 + ((32 - fsprs[frs].get_width()) // 2)), (98 + (32 - fsprs[frs].get_height()))])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
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
            elif play and ywn < 0:
                l = [0, 0, 0, 0]
                for i in cubel:
                    l[i] += 1
                wcl = [l.index(max(l))]
                l[wcl[0]] = 0
                wcl.append(l.index(max(l)))
                ywn = randint(0, 1)
                pygame.mixer.stop()
                sound[3].play()
            elif play:
                play = False
                if ywn:
                    if avars[avars[3][5]][17] < 6:
                        avars[avars[3][5]][17] += 1
                    avars[avars[3][5]][5] += 10
                    avars[avars[3][5]][8] += 10
                elif not ywn and avars[avars[3][5]][17] > 0:
                    avars[avars[3][5]][17] -= 1
                pygame.mixer.stop()
                sound[14 - (13 * ywn)].play()
            elif not play:
                return(avars)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

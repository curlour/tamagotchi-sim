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

    term = 0

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    lfnt = pygame.font.Font("Sprites/Misc/font/Tama1.ttf", 16)
    
    bck = pygame.image.load("Sprites/Misc/bg/patchif.png").convert()
    gbck = pygame.image.load("Sprites/Misc/bg/patchig.png").convert()
        
    wave = pygame.Surface((16, 16))
    wave.fill((0, 255, 255))
    wave.blit(gbck, [0, 0])
    wave.set_colorkey((0, 255, 255))
    wave.convert()
        
    redm = pygame.Surface((8, 8))
    redm.fill((0, 255, 255))
    redm.blit(gbck, [-(16), 0])
    redm.set_colorkey((0, 255, 255))
    redm.convert()

    vapor = pygame.image.load("Sprites/Misc/emo/vapor.png").convert()

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
            if term < 2:
                spr = 3
                sy = (104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2))
                frs = 3
                fy = (104 + ((32 - fsprs[spr].get_width()) // 2))
            elif term < 4:
                spr = 10
                sy = (104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2))
                frs = 10
                fy = (104 + ((32 - fsprs[spr].get_width()) // 2))
            else:
                spr = 7 - (2 * ywn)
                sy = (88 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)) + (16 * ywn)
                frs = 5 + (2 * ywn)
                fy = (104 + ((32 - fsprs[spr].get_width()) // 2)) - (16 * ywn)
            if term > 1:
                for i in range(4):
                    screen.blit(vapor, [[8, 88, 136, 216][i], (72 + (16 * ((i % 2) == (anifr % 12 > 5))))])
            for i in range(term):
                screen.blit(redm, [116, (88 - (8 * i))])
            screen.blit(asprs[avars[3][5]][spr], [(168 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), sy])
            screen.blit(fsprs[frs], [(40 + ((32 - fsprs[spr].get_width()) // 2)), fy])
            for i in range(16):
                screen.blit(wave, [((16 * i) - (8 * (anifr % 12 > 5))), 120])
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
            elif play and term < 4:
                term += 1
                if term == 4:
                    ywn = randint(0, 1)
                    pygame.mixer.stop()
                    sound[12 - (3 * ywn)].play()
            elif play:
                play = False
                if ywn:
                    if avars[avars[3][5]][17] < 6:
                        avars[avars[3][5]][17] += 1
                    avars[avars[3][5]][7] += 10
                    avars[avars[3][5]][10] += 10
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

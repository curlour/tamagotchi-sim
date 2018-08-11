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

def game(avars, asprs, screen, fsprs, ywn):
    
    kr = True

    chngsts = False

    gmst = 0

    strt = True
    play = False

    def blnani():
        if gmst < 4:
            if (anifr % 12 < 6) == ywn:
                spr = 4
                frs = 5
            else:
                spr = 5
                frs = 4
        else:
            if ywn:
                spr = 5
                frs = 7
            else:
                spr = 7
                frs = 5
        return(spr, frs)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 4, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    lfnt = pygame.font.Font("Sprites/Misc/font/Tama1.ttf", 16)
    
    bck = pygame.image.load("Sprites/Misc/bg/congamesbg.png").convert()
    bck.blit(asprs[avars[3][5]][1], [(193 + ((16 - asprs[avars[3][5]][1].get_width()) // 2)), (69 + ((16 - asprs[avars[3][5]][1].get_height()) // 2))])
    bck.blit(fsprs[1], [(31 + ((16 - fsprs[1].get_width()) // 2)), (47 + ((16 - fsprs[1].get_height()) // 2))])

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    balloon = [pygame.image.load("Sprites/Misc/obj/blninf1.png").convert(),
               pygame.image.load("Sprites/Misc/obj/blninf2.png").convert(),
               pygame.image.load("Sprites/Misc/obj/blninf3.png").convert(),
               pygame.image.load("Sprites/Misc/obj/blninf4.png").convert(),
               pygame.image.load("Sprites/Misc/obj/blninf5.png").convert()]

    airp = [pygame.image.load("Sprites/Misc/obj/popbln1.png").convert(),
            pygame.image.load("Sprites/Misc/obj/popbln2.png").convert()]

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
        screen.blit(bck, [0, 0])
        if strt:
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
            screen.blit(balloon[gmst], [88, 66])
            spr, frs = blnani()
            if (((anifr % 12 < 6) == ywn) and gmst < 4) or (gmst == 4 and ywn):
                a = 20
            else:
                a = 0
            screen.blit(airp[1], [(72 + (64 * ((((anifr % 12 < 6) == ywn) and gmst < 4) or (gmst == 4 and ywn)))), 98])
            screen.blit(airp[0], [(136 - (64 * ((((anifr % 12 < 6) == ywn) and gmst < 4) or (gmst == 4 and ywn)))), 98])
            screen.blit(asprs[avars[3][5]][spr], [(136 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (58 + a + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit(pygame.transform.flip(fsprs[frs], 1, 0), [(72 + ((32 - fsprs[frs].get_width()) // 2)), (78 - a + (32 - fsprs[frs].get_height()))])
        else:
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
            elif play:
                if gmst < 4:
                    gmst += 1
                    if gmst == 4:
                        anifr = 12
                        pygame.mixer.stop()
                        sound[9].play()
                else:
                    play = False
                    if ywn and avars[avars[3][5]][17] < 6:
                        avars[avars[3][5]][17] += 1
                    elif not ywn and avars[avars[3][5]][17] > 0:
                        avars[avars[3][5]][17] -= 1
                    pygame.mixer.stop()
                    sound[14 - (13 * ywn)].play()
            else:
                return(avars)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

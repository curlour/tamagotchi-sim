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

    strt = True
    play = False

    gmst = 0

    def cbani():
        if gmst < 3:
            if anifr < 12:
                if anifr < 6:
                    spr = 4
                    frs = 3
                else:
                    spr = 3
                    frs = 4
                sprx = 156 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                frx = 52 + ((32 - fsprs[frs].get_width()) // 2)
                screen.blit(ball, [56, 106])
                screen.blit(ball, [160, 106])
            else:
                if anifr < 18:
                    screen.blit(pygame.transform.flip(sweat, 1, 0), [35, 74])
                else:
                    screen.blit(sweat, [189, 74])
                spr = 9
                frs = 9
                sprx = 155 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2) + (2 * (anifr < 18))
                frx = 51 + ((32 - fsprs[frs].get_width()) // 2) + (2 * (anifr > 17))
                screen.blit(ball, [(55 + (2 * (anifr < 18))), 106])
                screen.blit(ball, [(159 + (2 * (anifr > 17))), 106])
            spry = 82 + (32 - asprs[avars[3][5]][spr].get_height())
            fry = 82 + (32 - fsprs[frs].get_height())
        else:
            if ywn:
                screen.blit(cnf, [(164 - (104 * ywn)), 66])
            spr = 7 - (2 * ywn)
            frs = 5 + (2 * ywn)
            sprx = 156 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            frx = 52 + ((32 - fsprs[frs].get_width()) // 2)
            spry = 90 + (32 - asprs[avars[3][5]][spr].get_height()) - (16 * ywn)
            fry = 74 + (32 - fsprs[frs].get_height()) + (16 * ywn)
            screen.blit(ball, [(56 - (8 * ywn)), 106])
            screen.blit(ball, [(152 + (8 * ywn)), 106])
        return(spr, sprx, spry, frs, frx, fry)

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
    
    cnf = pygame.image.load("Sprites/Misc/emo/conf.png").convert()
    sweat = pygame.image.load("Sprites/Misc/emo/sweat.png").convert()
    
    ball = pygame.image.load("Sprites/Misc/item/ball.png").convert()

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
            if gmst < 3 and anifr == 12:
                pygame.mixer.stop()
                sound[4].play()
            spr, sprx, spry, frs, frx, fry = cbani()
            screen.blit(asprs[avars[3][5]][spr], [sprx, spry])
            screen.blit(pygame.transform.flip(fsprs[frs], 1, 0), [frx, fry])
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
                gmst += 1
                if gmst == 3:
                    anifr = 12
                    pygame.mixer.stop()
                    sound[12].play()
                elif gmst == 4:
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

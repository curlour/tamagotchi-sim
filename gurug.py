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

    wait = True

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    shine = pygame.image.load("Sprites/Misc/emo/shine.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    lfnt = pygame.font.Font("Sprites/Misc/font/Tama1.ttf", 16)
    
    bck = pygame.image.load("Sprites/Misc/bg/gurugurut.png").convert()
    gbck = pygame.image.load("Sprites/Misc/bg/gurugurug.png").convert()
        
    brush = pygame.Surface((16, 16))
    brush.fill((0, 255, 255))
    brush.blit(gbck, [0, 0])
    brush.set_colorkey((0, 255, 255))
    brush.convert()

    c1 = ((randint(0, 5) * 51), (randint(0, 5) * 51), (randint(0, 5) * 51))
    c4 = ((randint(0, 5) * 51), (randint(0, 5) * 51), (randint(0, 5) * 51))
    c2 = ((c1[0] - ((c1[0] - c4[0]) // 3)), (c1[1] - ((c1[1] - c4[1]) // 3)), (c1[2] - ((c1[2] - c4[2]) // 3)))
    c3 = ((c4[0] + ((c1[0] - c4[0]) // 3)), (c4[1] + ((c1[1] - c4[1]) // 3)), (c4[2] + ((c1[2] - c4[2]) // 3)))

    rainb = pygame.Surface((240, 32))
    rainb.fill((0, 255, 255))
    pygame.draw.rect(rainb, c2, (0, 8, 240, 8))
    pygame.draw.rect(rainb, c3, (0, 16, 240, 8))
    rainb.set_colorkey((0, 255, 255))
    rainb.convert()

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
            if ywn < 0:
                screen.blit(rainb, [0, 80])
                spr = 11 + (anifr % 12 > 5)
                frs = 11 + (anifr % 12 < 6)
                screen.blit(shine, [(32 + (160 * (anifr % 12 < 6))), 96])
                screen.blit(pygame.transform.flip(brush, 1, 0), [(80 + (8 * (anifr % 12 < 6))), 80])
                screen.blit(brush, [(144 - (8 * (anifr % 12 > 5))), 104])
            else:
                if anifr < 12:
                    screen.blit(rainb, [0, (64 - (16 * (anifr > 5)))])
                    spr = 3 + (anifr > 5)
                    frs = 3 + (anifr < 6)
                else:
                    screen.blit(rainb, [0, 32])
                    if anifr == 12:
                        pygame.mixer.stop()
                        sound[12 - (3 * ywn)].play()
                    spr = 7 - (2 * ywn)
                    frs = 5 + (2 * ywn)
            screen.blit(asprs[avars[3][5]][spr], [(160 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit(pygame.transform.flip(fsprs[frs], 1, 0), [(48 + ((32 - fsprs[spr].get_width()) // 2)), (98 + (32 - fsprs[spr].get_height()))])
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
            elif play and wait:
                wait = False
                rainb = pygame.Surface((240, 32))
                rainb.fill((0, 255, 255))
                pygame.draw.rect(rainb, c1, (0, 0, 60, 8))
                pygame.draw.rect(rainb, c2, (0, 8, 240, 8))
                pygame.draw.rect(rainb, c3, (0, 16, 240, 8))
                pygame.draw.rect(rainb, c4, (180, 24, 60, 8))
                rainb.set_colorkey((0, 255, 255))
                rainb.convert()
            elif play and ywn < 0:
                ywn = randint(0, 1)
                pygame.draw.rect(rainb, c1, (0, 0, (120 * (2 - ywn)), 8))
                pygame.draw.rect(rainb, c2, (0, 8, 240, 8))
                pygame.draw.rect(rainb, c3, (0, 16, 240, 8))
                pygame.draw.rect(rainb, c4, ((120 * (not ywn)), 24, (120 * (1 + ywn)), 8))
                rainb.set_colorkey((0, 255, 255))
                pygame.mixer.stop()
                sound[3].play()
            elif play:
                play = False
                if ywn:
                    if avars[avars[3][5]][17] < 6:
                        avars[avars[3][5]][17] += 1
                    avars[avars[3][5]][6] += 10
                    avars[avars[3][5]][9] += 10
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

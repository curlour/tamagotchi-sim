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
import palette
import growth
import mainscreen

def prk(avars, asprs, screen):
    
    kr = True

    chngsts = False

    ar = True
    talk = False

    ret = 1

    def chsprs(chara, g):
        try:
            sprs = []
            if chara > 0:
                bs = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "b.png")
                ss = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "s.png")
            else:
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
        except:
            sprs = chsprs(0, g)
        return(sprs)

    def arrive():
        flip = True
        pflip = False
        if anifr < 48:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 11
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                pcs = 3
            else:
                spr = 13
                spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
                pcs = 4
            sprx = (0 + (10 * (anifr // 6))) + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            pcy = 98 + (32 -  pchrs[pcs].get_height())
        else:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 3
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                pcs = 3
                pcy = 98 + (32 -  pchrs[pcs].get_height())
            else:
                spr = 5
                spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
                pcs = 5
                pcy = 96 + (32 -  pchrs[pcs].get_height())
            sprx = 80 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        pcx = 122 + ((32 -  pchrs[pcs].get_width()) // 2)
        return spr, sprx, spry, flip, pcs, pcx, pcy, pflip

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    obgi = pygame.image.load("Sprites/Misc/bg/uratown.png").convert()

    boab = pygame.image.load("Sprites/Misc/bg/uraboat.png").convert()

    boat = pygame.Surface((80, 24))
    boat.fill((0, 255, 255))
    boat.blit(boab, [0, 0])
    boat.set_colorkey((0, 255, 255))
    boat.convert()

    waves = pygame.Surface((32, 16))
    waves.fill((0, 255, 255))
    waves.blit(boab, [-80, 0])
    waves.set_colorkey((0, 255, 255))
    waves.convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    sound = sounds.imprtsnd(avars)

    clock = pygame.time.Clock()

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")
    
    p = randint(1, 4)
    t = [0, 3600, 176400, 435600][p - 1]
    g = randint(0, 4294967295)
    while (format(g, '032b')[16:28]) == (format(avars[avars[3][5]][14], '032b')[16:28]):
        g = randint(0, 4294967295)
    g = g | 983042
    a = choice([3, 5, 6])
    c = ["ku", "ma", "me"][(a // 2) - 1]
    d = ["ku", "ma", "me"][(a // 2) - 1]
    k = randint(0, 2)
    ov = [[a, 1, 0, 2, 0, 200, 200, 200, (250 * (1 + (k == 0))), (250 * (1 + (k == 1))), (250 * (1 + (k == 2))), c, c, d, g, 0, 0, 0, 20, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 4], [], [], [0, 0, 0, 0, 0, 0]]
    if (a == 3) and (g % 2):
        ov[0][5], ov[0][9] = ov[0][9], ov[0][5]
    ov = growth.grw(ov)
    while ov[0][1] < p:
        ov[0][1] += 1
        ov = growth.grw(ov)
    pchr = ov[0][15]
    pcharinfo = ["PARK", "", pchr, g, ov[0][13], ov[0][12], ov[0][11], [t, avars[avars[3][5]][2]], 0]
    pchrs = chsprs(pchr, pcharinfo[3])

    while kr:
        if not talk:
            screen.blit(obgi, [0, 0])
        else:
            screen.blit(boab, [0, 0])
        if ar:
            if anifr < 48 and ((anifr / 12) - (anifr // 12)) == 0.5:
                pygame.mixer.stop()
                sound[6].play()
            elif ((anifr / 12) - (anifr // 12)) == 0.5:
                pygame.mixer.stop()
                sound[9].play()
            spr, sprx, spry, flip, pcs, pcx, pcy, pflip = arrive()
            screen.blit(pygame.transform.flip(pchrs[pcs], pflip, 0), [pcx, pcy])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [sprx, spry])
        elif not talk:
            sprx = 80 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)
            pcx = 122 + ((32 -  pchrs[3].get_width()) // 2)
            spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
            pcy = 98 + (32 -  pchrs[3].get_height())
            spr = 4 + (anifr % 16 > 7)
            pcs = 4 + (anifr % 16 < 8)
            screen.blit(pchrs[pcs], [pcx, pcy])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], 1, 0), [sprx, spry])
        else:
            spry = 96 + ((32 - asprs[avars[3][5]][3].get_width()) // 2) + (4 * (anifr % 16 > 7))
            pcy = 96 + ((32 - pchrs[3].get_width()) // 2) + (4 * (anifr % 16 > 7))
            screen.blit(pchrs[16 + (anifr % 16 > 7)], [120, pcy])
            screen.blit(asprs[avars[3][5]][16 + (anifr % 16 < 8)], [84, spry])
            screen.blit(boat, [80, (104 + (4 * (anifr % 16 > 7)))])
            for i in range(8):
                screen.blit(waves, [((32 * i) - (16 * (anifr % 16 > 7))), 120])
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
                            sound[4].play()
                            return(avars, ret)
                        elif 212 < mp[0] < 224:
                            ret = 0
                            sound[4].play()
                            return(avars, ret)
                    if (24 < mp[1] < 136) and not ar and not talk:
                        f = avars[avars[3][5]][32]
                        f.append(pcharinfo)
                        avars[avars[3][5]][32] = f
                        a = ["ma", "me", "ku"].index(pcharinfo[6])
                        avars[avars[3][5]][5 + a] += 10
                        avars[avars[3][5]][8 + a] += 10
                        sound[9].play()
                        talk = True
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
            if avars[avars[3][5]][20] or not avars[avars[3][5]][21]:
                return(avars, ret)
            chngsts = False
        if anifr < 63:
            anifr += 1
        else:
            anifr = 0
            if ar:
                ar = False
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

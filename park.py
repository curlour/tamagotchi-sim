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

def prk(avars, asprs, screen, pt, pchr, panit, pcharinfo):
    
    kr = True

    chngsts = False

    ar = True

    ret = 1

    swthr = ["skyd", "skyaf", "skyn"]
    cwthr = ["skydc", "skydc", "skync"]
    wthrbk = [swthr, cwthr, cwthr]

    slake = ["laked", "lakee", "laken"]
    clake = ["lakec", "lakec", "lakecn"]
    lakebk = [slake, clake, clake]

    pgbk = ["pgbk", "pgbks", "pgbka", "pgbkw"]
    
    lkfrbk = ["lakebg", "lakebgs", "lakebga", "lakebgw"]

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

    def outbg():
        bg = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
        a = pygame.image.load("Sprites/Misc/bg/" + pgbk[s] + ".png").convert()
        b = pygame.Surface([240, 160]).convert()
        c = (0, 0, 0)
        if w != 0:
            if w == 2:
                if s == 3:
                    a.blit(snowg, [0, 0])
                else:
                    a.blit(raing, [0, 0])
        if panit < 2:
            a.blit(pygame.image.load("Sprites/Misc/bg/" + prkbg[s] + ".png").convert(), [0, 0])
        elif panit < 5:
            a.blit(city, [0, 12])
        else:
            a.blit(pygame.image.load("Sprites/Misc/bg/" + lkfrbk[s] + ".png").convert(), [0, 0])
            bg.blit(pygame.image.load("Sprites/Misc/bg/" + lakebk[w][tm] + ".png").convert(), [0, 0])
        if w != 0:
            if tm < 2:
                b.fill((204, 204, 204))
                c = (81, 81, 81)
            else:
                b.fill((102, 102, 102))
                c = (40, 40, 40)
            b.set_alpha(102)
            a.blit(b, [0, 0])
        elif tm > 0:
            if tm == 1:
                b.fill((255, 102, 0))
                c = (101, 40, 0)
            else:
                b.fill((0, 0, 102))
                c = (0, 0, 40)
            b.set_alpha(102)
            a.blit(b, [0, 0])
        a.set_colorkey(c)
        bg.blit(a, [0, 0])
        return(bg)

    def arrive():
        flip = False
        pflip = False
        if anifr < 48:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 11
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                if pchr > 0:
                    pcs = 3
            else:
                spr = 13
                spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
                if pchr > 0:
                    pcs = 4
            sprx = (208 - (10 * (anifr // 6))) + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            if pchr > 0:
                pcy = 98 + (32 -  pchrs[pcs].get_height())
        else:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 3
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                if pchr > 0:
                    pcs = 3
                    pcy = 98 + (32 -  pchrs[pcs].get_height())
            else:
                spr = 5
                spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
                if pchr > 0:
                    pcs = 5
                    pcy = 96 + (32 -  pchrs[pcs].get_height())
            sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        if pchr > 0:
            pcx = 86 + ((32 -  pchrs[pcs].get_width()) // 2)
            pflip = True
        if pchr == 0:
            return spr, sprx, spry, flip
        else:
            return spr, sprx, spry, flip, pcs, pcx, pcy, pflip

    def pani():
        flip = False
        pflip = False
        if panit == 0:
            if pchr > 0 and ptlk:
                if anifr < 58:
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 11
                        pcs = 12
                    else:
                        spr = 12
                        pcs = 11
                else:
                    spr = 5
                    pcs = 5
            else:
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    spr = 3
                    if pchr > 0:
                        pcs = 3
                else:
                    spr = 4
                    if pchr > 0:
                        pcs = 4
            sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            if pchr > 0:
                pcy = 98 + (32 -  pchrs[pcs].get_height())
                pcx = 86 + ((32 -  pchrs[pcs].get_width()) // 2)
                pflip = True
        elif panit == 1:
            flip = True
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 16
                pcs = 17
            else:
                spr = 17
                pcs = 16
            sprx = 72 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            pcx = 108 + ((32 -  pchrs[pcs].get_width()) // 2)
            pcy = 98 + (32 -  pchrs[pcs].get_height())
        elif panit == 2:
            if anifr % 16 < 8:
                spr = 17
                pcs = 17
                spry = 83 + (32 - asprs[avars[3][5]][spr].get_height())
                pcy = 83 + (32 -  pchrs[pcs].get_height())
            else:
                if anifr % 32 < 16:
                    spr = 5
                    pcs = 16
                    spry = 68 + (32 - asprs[avars[3][5]][spr].get_height())
                    pcy = 94 + (32 -  pchrs[pcs].get_height())
                else:
                    spr = 16
                    pcs = 5
                    spry = 94 + (32 - asprs[avars[3][5]][spr].get_height())
                    pcy = 68 + (32 -  pchrs[pcs].get_height())
            sprx = 136 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            pcx = 72 + ((32 -  pchrs[pcs].get_width()) // 2)
            pflip = True
        elif panit == 3:
            pflip = True
            if anifr < 32:
                if anifr % 16 < 8:
                    spr = 11
                    pcs = 11
                    sprx = 132 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    pcx = 76 + ((32 -  pchrs[pcs].get_width()) // 2)
                    screen.blit(pygame.transform.flip(sndsnw[(s == 3 and w == 2)][0], 1, 0), [124, 114])
                    screen.blit(sndsnw[(s == 3 and w == 2)][0], [88, 114])
                else:
                    spr = 13
                    pcs = 13
                    sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    pcx = 80 + ((32 -  pchrs[pcs].get_width()) // 2)
                    screen.blit(pygame.transform.flip(sndsnw[(s == 3 and w == 2)][0], 1, 0), [120, 114])
                    screen.blit(sndsnw[(s == 3 and w == 2)][0], [92, 114])
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                pcy = 98 + (32 -  pchrs[pcs].get_height())
            elif anifr < 56:
                if anifr % 16 < 8:
                    spr = 4
                    pcs = 4
                    spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                    pcy = 98 + (32 -  pchrs[pcs].get_height())
                else:
                    spr = 5
                    pcs = 5
                    spry = 94 + (32 - asprs[avars[3][5]][spr].get_height())
                    pcy = 94 + (32 -  pchrs[pcs].get_height())
                sprx = 132 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                pcx = 76 + ((32 -  pchrs[pcs].get_width()) // 2)
                screen.blit(sndsnw[(s == 3 and w == 2)][1], [108, 106])
            else:
                spr = 9
                pcs = 9
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                pcy = 98 + (32 -  pchrs[pcs].get_height())
                sprx = 132 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                pcx = 76 + ((32 -  pchrs[pcs].get_width()) // 2)
                screen.blit(sndsnw[(s == 3 and w == 2)][2], [108, 106])
        elif panit == 4:
            pflip = anifr < 32
            flip = anifr > 31
            if anifr % 32 < 8:
                spr = 5
                pcs = 5
                sprx = 56 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2) + (104 * (anifr < 32))
                pcx = 56 + ((32 -  pchrs[pcs].get_width()) // 2) + (104 * (anifr > 31))
                spry = 66 + (32 - asprs[avars[3][5]][spr].get_height()) + (32 * (anifr < 32))
                pcy = 66 + (32 -  pchrs[pcs].get_height()) + (32 * (anifr > 31))
            elif anifr % 32 < 16:
                spr = 17 - (4 * (anifr < 32))
                pcs = 17 - (4 * (anifr > 31))
                sprx = 84 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2) + (41 * (anifr < 32))
                pcx = 84 + ((32 -  pchrs[pcs].get_width()) // 2) + (41 * (anifr > 31))
                spry = 44 + (32 - asprs[avars[3][5]][spr].get_height()) + (56 * (anifr < 32))
                pcy = 44 + (32 -  pchrs[pcs].get_height()) + (56 * (anifr > 31))
            elif anifr % 32 < 24:
                spr = 16 - (5 * (anifr < 32))
                pcs = 16 - (5 * (anifr > 31))
                sprx = 108 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2) - (18 * (anifr < 32))
                pcx = 108 + ((32 -  pchrs[pcs].get_width()) // 2) - (18 * (anifr > 31))
                spry = 62 + (32 - asprs[avars[3][5]][spr].get_height()) + (38 * (anifr < 32))
                pcy = 62 + (32 -  pchrs[pcs].get_height()) + (38 * (anifr > 31))
            else:
                spr = 17 - (4 * (anifr < 32))
                pcs = 17 - (4 * (anifr > 31))
                sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2) - (64 * (anifr < 32))
                pcx = 128 + ((32 -  pchrs[pcs].get_width()) // 2) - (64 * (anifr > 31))
                spry = 90 + (32 - asprs[avars[3][5]][spr].get_height()) + (10 * (anifr < 32))
                pcy = 90 + (32 -  pchrs[pcs].get_height()) + (10 * (anifr > 31))
        elif panit == 5:
            pflip = True
            if anifr % 16 < 8:
                spr = [10, 6, 4, 6][s]
                pcs = [3, 3, 5, 6][s]
                if s == 1:
                    screen.blit(sweat, [156, 82])
                elif s == 3:
                    screen.blit(shiver, [71, 108])
                    screen.blit(shiver, [155, 108])
            else:
                spr = [3, 3, 5, 6][s]
                pcs = [10, 6, 4, 6][s]
                if s == 1:
                    screen.blit(sweat, [120, 82])
                elif s == 3:
                    screen.blit(shiver, [69, 108])
                    screen.blit(shiver, [157, 108])
            sprx = 122 + ((32 -  pchrs[pcs].get_width()) // 2) + ((s == 3) * ((2 * (anifr % 16 > 7)) - 1))
            pcx = 86 + ((32 -  pchrs[pcs].get_width()) // 2) + ((s == 3) * ((2 * (anifr % 16 < 8)) - 1))
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            pcy = 98 + (32 -  pchrs[pcs].get_height())
        if pchr == 0:
            return spr, sprx, spry, flip
        else:
            return spr, sprx, spry, flip, pcs, pcx, pcy, pflip

    if pt == 0:
        tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)
    else:
        tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 4, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    shiver = pygame.image.load("Sprites/Misc/emo/shiver.png").convert()
    sweat = pygame.image.load("Sprites/Misc/emo/sweat.png").convert()

    prkbg = ["parkbg", "parkbgs", "parkbga" , "parkbgw"]

    city = pygame.image.load("Sprites/Misc/bg/walkbg.png").convert()

    balnc1 = pygame.image.load("Sprites/Misc/obj/prkbal1.png").convert()
    balnc2 = pygame.image.load("Sprites/Misc/obj/prkbal2.png").convert()

    prkpnk = pygame.image.load("Sprites/Misc/bg/prkpnk.png").convert()

    sndbox = pygame.image.load("Sprites/Misc/bg/prksand.png").convert()

    sndsnw = [[pygame.image.load("Sprites/Misc/obj/sandm.png").convert(), pygame.image.load("Sprites/Misc/obj/sandcst.png").convert(), pygame.image.load("Sprites/Misc/obj/sandd.png").convert()],
              [pygame.image.load("Sprites/Misc/obj/snowm.png").convert(), pygame.image.load("Sprites/Misc/obj/snowman.png").convert(), pygame.image.load("Sprites/Misc/obj/snowd.png").convert()]]

    slide = pygame.image.load("Sprites/Misc/obj/slide.png").convert()

    rain = pygame.image.load("Sprites/Misc/bg/rain.png").convert()
    snow = pygame.image.load("Sprites/Misc/bg/snow.png").convert()

    raing = pygame.image.load("Sprites/Misc/bg/rpgb.png").convert()
    snowg = pygame.image.load("Sprites/Misc/bg/spgb.png").convert()

    s, tm , w = weather.chktime(avars)

    obgi = outbg()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    sound = sounds.imprtsnd(avars)

    clock = pygame.time.Clock()

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    ptlk = False

    if pt == 0:
        if int(avars[3][6][:2]) < 12 or int(avars[3][6][:2]) > 18:
            pchr = 0
        else:
            p = randint(1, 4)
            t = [0, 3600, 176400, 435600][p - 1]
            g = randint(0, 4294967295)
            while (format(g, '032b')[16:28]) == (format(avars[avars[3][5]][14], '032b')[16:28]):
                g = randint(0, 4294967295)
            a = randint(1, 8)
            c = ["no", "ma", "ku", "ku", "ma", "me", "me", "no"][a - 1]
            d = [choice(["ku", "ma", "me"]), "ku", "ku", "me", "ma", "me", "ma", "no"][a - 1]
            ov = [[a, 1, 0, (g % 4 > 1), 0, randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), c, c, d, g, 0, 0, 0, randint(1, 99), randint(0, 5), 0, 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 4], [], [], [0, 0, 0, 0, 0, 0]]
            ov = growth.grw(ov)
            while ov[0][1] < p:
                ov[0][1] += 1
                ov = growth.grw(ov)
            pchr = ov[0][15]
            pcharinfo = ["PARK", "", pchr, g, ov[0][13], ov[0][12], ov[0][11], [t, avars[avars[3][5]][2]], 0]
    if pchr > 0:
        pchrs = chsprs(pchr, pcharinfo[3])

    while kr:
        screen.blit(obgi, [0, 0])
        if w == 2:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                y = 0
            else:
                if s < 3:
                    y = 16
                else:
                    y = 8
            if s < 3:
                screen.blit(rain, [0, y])
            else:
                screen.blit(snow, [0, y])
        if ar:
            if anifr < 48 and ((anifr / 12) - (anifr // 12)) == 0.5:
                pygame.mixer.stop()
                sound[6].play()
            elif ((anifr / 12) - (anifr // 12)) == 0.5:
                pygame.mixer.stop()
                sound[9].play()
            if pchr == 0:
                spr, sprx, spry, flip = arrive()
            else:
                spr, sprx, spry, flip, pcs, pcx, pcy, pflip = arrive()
                screen.blit(pygame.transform.flip(pchrs[pcs], pflip, 0), [pcx, pcy])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [sprx, spry])
        else:
            if pt == 0:
                if panit == 0:
                    if pchr == 0:
                        spr, sprx, spry, flip = pani()
                    else:
                        spr, sprx, spry, flip, pcs, pcx, pcy, pflip = pani()
                        screen.blit(pygame.transform.flip(pchrs[pcs], pflip, 0), [pcx, pcy])
                else:
                    spr = 11 + (2 * (anifr % 8 < 4))
                    spry = 98 + (32 - asprs[avars[3][5]][spr].get_height()) - (8 * (anifr % 8 < 4))
                    sprx = (368 - (32 * (anifr // 4))) + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                    flip = False
                    if anifr % 8 < 4:
                        screen.blit(sweat, [(400 - (32 * (anifr // 4))), 74])
            else:
                if panit == 1:
                    screen.blit(prkpnk, [74, 123])
                elif panit == 2:
                    if anifr % 16 < 8:
                        screen.blit(balnc1, [72, 98])
                    else:
                        screen.blit(pygame.transform.flip(balnc2, (anifr % 32 < 16), 0), [72, 98])
                elif panit == 3 and (s < 3 or w < 2):
                    screen.blit(sndbox, [32, 104])
                elif panit == 4:
                    screen.blit(slide, [88, 66])
                spr, sprx, spry, flip, pcs, pcx, pcy, pflip = pani()
                screen.blit(pygame.transform.flip(pchrs[pcs], pflip, 0), [pcx, pcy])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [sprx, spry])
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
                            if pt == 0:
                                return(avars, ret)
                            else:
                                return(avars)
                        elif 212 < mp[0] < 224 and pt == 0:
                            ret = 0
                            sound[4].play()
                            return(avars, ret)
                    if 23 < mp[1] < 136 and not ar and not ptlk and pt == 0 and panit == 0:
                        if pchr > 0:
                            ptlk = True
                            anifr = 33
                            f = avars[avars[3][5]][32]
                            f.append(pcharinfo)
                            avars[avars[3][5]][32] = f
                        else:
                            panit = 5
                            obgi = outbg()
                            anifr = 0
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
                if pt == 0:
                    return(avars, ret)
                else:
                    return(avars)
            chngsts = False
        if anifr < 63:
            anifr += 1
        else:
            anifr = 0
            if panit == 5 and pt == 0:
                if avars[avars[3][5]][18] > 1:
                    avars[avars[3][5]][18] -= 1
            ar = False
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

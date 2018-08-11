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
import growth
import palette
import dirty
import mainscreen

def game(avars, asprs, screen):

    class Mnbx(pygame.sprite.Sprite):

        bxt = []
        
        def __init__(self):
            super().__init__()
            box = pygame.image.load("Sprites/Misc/txtbox/box2.png").convert()

            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (0, 0, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (8, 0, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (16, 0, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (0, 8, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (8, 8, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (16, 8, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (0, 16, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (8, 16, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (16, 16, 8, 8))
            self.bxt.append(image)

            self.image = self.bxt[0]
            self.rect = self.image.get_rect()

        def update(self):
            self.image = self.bxt[tl]
    
    kr = True

    chngsts = False

    vfls = [0, 0, 0, 0]
    vbfl = [0, 0]

    fsel = -1

    scr = 0

    ret = 1
    spret = 0

    tuts = True
    strt = False
    play = False
    end = 0

    def chsprs(chara, dirt, g):
        sprs = []
        bs = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "b.png")
        ss = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "s.png")
        opal = []
        for i in range(32):
            opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
        bs = palette.palch(bs, g, opal)
        if dirt:
            bs = dirty.dirt(bs)
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
        return(sprs)

    def fvals():
        l = [1, 2, 3, 5, 7, 11]
        shuffle(l)
        fls = [[l[0], l[1]], [l[2], l[3]]]
        flss = []
        f = pygame.image.load("Sprites/Misc/obj/labf.png").convert()
        for i in range(4):
            c = pygame.Surface((24, 24)).convert()
            c.fill((0, 255, 255))
            n = [1, 2, 3, 5, 7, 11].index(fls[i // 2][i % 2])
            c.blit(f, [-(24 * (n % 3)), -(24 * (n // 3))])
            c.set_colorkey((0, 255, 255))
            flss.append(c)
        obj = [0, 0]
        for i in [0, 1]:
            obj[i] = randint(1, (max(fls[i]) - 1))
        return(fls, flss, obj)

    def drbx():
        tile = Mnbx()
        tile.update()
        textbox.blit(tile.image, [tx, ty])

    def drhl():
        global tx
        global tl
        tx = 0
        drbx()
        tl += 1
        while tx < 48:
            tx += 8
            drbx()
        tx = 56
        tl += 1
        drbx()

    def dral():
        global ty
        global tl
        while ty < 16:
            tl = 3
            ty += 8
            drhl()

    def aspr():
        if len(avars[0]) > 0:
            sprs0 = chsprs(avars[0][15], (avars[0][30] == 2), avars[0][14])
        else:
            sprs0 = []
        if len(avars[1]) > 0:
            sprs1 = chsprs(avars[1][15], (avars[1][30] == 2), avars[1][14])
        else:
            sprs1 = []
        if len(avars[2]) > 0:
            sprs2 = chsprs(avars[2][15], (avars[2][30] == 2), avars[2][14])
        else:
            sprs2 = []
        asprs = [sprs0, sprs1, sprs2]
        return(asprs)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    tutimg = pygame.image.load("Sprites/Misc/bg/labt.png").convert()

    playbk = pygame.image.load("Sprites/Misc/bg/lab.png").convert()

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    bflsk = []
    a = pygame.image.load("Sprites/Misc/obj/labfb.png").convert()
    for i in [0, 1]:
        b = pygame.Surface((48, 48)).convert()
        b.fill((0, 255, 255))
        b.blit(a, [-(48 * i), 0])
        b.set_colorkey((0, 255, 255))
        bflsk.append(b)

    toobad = pygame.image.load("Sprites/Misc/bg/toobad.png").convert()
    good = pygame.image.load("Sprites/Misc/bg/good.png").convert()
    great = pygame.image.load("Sprites/Misc/bg/great.png").convert()
    excellent = pygame.image.load("Sprites/Misc/bg/excellent.png").convert()

    win = pygame.image.load("Sprites/Misc/emo/happy.png").convert()
    cry = pygame.image.load("Sprites/Misc/emo/cry.png").convert()

    money = pygame.image.load("Sprites/Misc/obj/money.png").convert()
    coin = pygame.image.load("Sprites/Misc/menu/gotchipt.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    textbox = pygame.Surface([240, 64]).convert()
    textbox.fill((0, 255, 255))
    global tl
    global ty
    tl = 0
    ty = 0
    drhl()
    dral()
    tl = 6
    ty = 24
    drhl()
    textbox.set_colorkey((0, 255, 255))

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
            screen.blit(playbk, [0, 0])
            if anifr == 16:
                pygame.mixer.stop()
                sound[11].play()
            if anifr < 16:
                screen.blit(ready, [80, 48])
                spr = 3
            else:
                screen.blit(go, [95, 48])
                spr = 5
            screen.blit(asprs[avars[3][5]][spr], [(104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
        elif play:
            screen.blit(playbk, [0, 0])
            if end < 2:
                spr = 3 + (anifr % 12 > 5)
            else:
                spr = 5 + (2 * (obj != vbfl))
            for i in range(4):
                screen.blit(flss[i], [[8, 56, 160, 208][i], (104- (8 * (i == fsel)))])
            screen.blit(fnt.render("%02d" % obj[0], 1, (0, 0, 100)), [67, 30])
            screen.blit(fnt.render("%02d" % obj[1], 1, (0, 0, 100)), [155, 30])
            screen.blit(bflsk[(end == 2 and (obj != vbfl))], [96, 80])
            screen.blit(asprs[avars[3][5]][spr], [104, 32])
        else:
            screen.blit(playbk, [0, 0])
            if end == 3:
                screen.blit(money, [88, 106])
                if anifr < 8:
                    spr = 11
                else:
                    if anifr == 8:
                        pygame.mixer.stop()
                        sound[13].play()
                    screen.blit(textbox, [94, 64])
                    mntxt = fnt.render(str(scr * 500), 1, (0, 0, 100))
                    screen.blit(mntxt, [(138 - (mntxt.get_width())), 74])
                    screen.blit(coin, [138, 72])
                    if scr > 0:
                        spr = 5
                    else:
                        spr = 6
                screen.blit(asprs[avars[3][5]][spr], [(124 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            elif end == 4:
                if scr < 2:
                    screen.blit(toobad, [71, 48])
                    sy = 98
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 6
                    else:
                        spr = 7
                        screen.blit(cry, [56, 90])
                else:
                    if scr < 4:
                        screen.blit(good, [94, 48])
                    elif scr < 6:
                        screen.blit(great, [85, 48])
                    else:
                        screen.blit(excellent, [51, 48])
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        sy = 98
                        spr = 4
                    else:
                        sy = 90
                        spr = 5
                        screen.blit(win, [136, 82])
                screen.blit(asprs[avars[3][5]][spr], [(104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (sy + (32 - asprs[avars[3][5]][spr].get_height()))])
            elif end == 5:
                if anifr < 6:
                    screen.blit(asprs[avars[3][5]][9], [104, 56])
                screen.blit(bflsk[(anifr > 11)], [96, 80])
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
                    if play and end == 0:
                        if fsel == -1 and (96 < mp[1] < 136) and (mp[0] not in range(96, 144)):
                            pygame.mixer.stop()
                            sound[2].play()
                            if mp[0] < 120:
                                fsel = (mp[0] > 47)
                            else:
                                fsel = 2 + (mp[0] > 191)
                        elif fsel > -1 and (fsel < 2 and mp[0] < 144) or \
                             (fsel > 1 and mp[0] > 95) and (24 < mp[1] < 136):
                            pygame.mixer.stop()
                            sound[3].play()
                            if 96 < mp[1]:
                                if mp[0] not in range(96, 144):
                                    if mp[0] < 120:
                                        a = (mp[0] > 47)
                                    else:
                                        a = 2 + (mp[0] > 191)
                                    if fsel == a:
                                        vfls[fsel] = 0
                                    else:
                                        b = vfls[a] + vfls[fsel]
                                        if b > fls[a // 2][a % 2]:
                                            vfls[a] = fls[a // 2][a % 2]
                                            vfls[fsel] = b - fls[a // 2][a % 2]
                                        else:
                                            vfls[a] = b
                                            vfls[fsel] = 0
                                else:
                                    vbfl[fsel > 1] += vfls[fsel]
                                    vfls[fsel] = 0
                            else:
                                vfls[fsel] = fls[fsel // 2][fsel % 2]
                            end = 1
                            anifr = 17
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
                fls, flss, obj = fvals()
            if play:
                if end == 1:
                    if vbfl.count(0) == 0:
                        end = 2
                        anifr = 12
                        pygame.mixer.stop()
                        sound[9 + (3 * (obj != vbfl))].play()
                    else:
                        end = 0
                    fsel = -1
                elif end == 2:
                    if obj == vbfl:
                        scr += 1
                        end = 0
                        vfls = [0, 0, 0, 0]
                        vbfl = [0, 0]
                        fls, flss, obj = fvals()
                    if end == 2 or scr == 6:
                        end = 3
                        play = False
                        if (avars[3][2] + (scr * 500)) < 99999:
                            avars[3][2] += (scr * 500)
                        else:
                            avars[3][2] = 99999
                        avars[avars[3][5]][5] += scr * 4
            elif end == 3:
                if scr < 6 or avars[avars[3][5]][15] != 217 or avars[avars[3][5]][5] < 1000:
                    if scr < 2:
                        pygame.mixer.stop()
                        sound[14].play()
                    else:
                        pygame.mixer.stop()
                        sound[1].play()
                    end = 4
                else:
                    pygame.mixer.stop()
                    sound[15].play()
                    end = 5
            elif end == 5:
                pygame.mixer.stop()
                sound[1].play()
                avars[avars[3][5]][1] = 5
                avars = growth.grw(avars)
                asprs = aspr()
                spret = 1
                end = 4
            elif end == 4:
                ret = spret
                return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import sounds
import borders
import shelve
import varsup
import statusup
import weather
import growth
import palette
import dirty
import mainscreen

def items(avars, asprs, screen):

    class Txtbx(pygame.sprite.Sprite):

        bxt = []
        
        def __init__(self):
            super().__init__()
            box = pygame.image.load("Sprites/Misc/txtbox/box1.png").convert()

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

    bx = True

    clt = 0

    spclk = False

    swt = False

    inf = False

    happyani = False

    flip = False
 
    scr = 0

    swthr = ["skyd", "skyaf", "skyn"]
    cwthr = ["skydc", "skydc", "skync"]
    wthrbk = [swthr, cwthr, cwthr]

    pgbk = ["pgbk", "pgbks", "pgbka", "pgbkw"]

    chngsts = False

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

    def drbx():
        tile = Txtbx()
        tile.update()
        textbox.blit(tile.image, [tx, ty])

    def drhl():
        global tx
        global tl
        tx = 0
        drbx()
        tl += 1
        while tx < 224:
            tx += 8
            drbx()
        tx = 232
        tl += 1
        drbx()

    def dral():
        global ty
        global tl
        while ty < 96:
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

    def drit():
        global itn
        if len(avars[3][9]) < (24 * (scr + 1)):
            a = len(avars[3][9]) - (24 * scr)
        else:
            a = 24
        while itn < a:
            screen.blit(isprs[(itn + (24 * scr))][0], [(14 + ((itn - (8 * (itn // 8))) * 27)), (44 + (24 * (itn // 8)))])
            screen.blit((lfnt.render(str(avars[3][9][(itn + (24 * scr))][1]), 1, (0, 0, 100))), [(14 + ((itn - (8 * (itn // 8))) * 27)), (44 + (24 * (itn // 8)))])
            itn += 1

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

    def itspr():
        isprs = []
        a = 0
        while a < len(avars[3][9]):
            sl = []
            b = pygame.image.load("Sprites/Misc/item/" + avars[3][9][a][0] + ".png").convert()
            sl.append(b)
            if avars[3][9][a][0] in ["balloon", "blocks", "clay", "rope", "yoyo", "plant", "ufo", "phouse", "book", "pc",
                                     "abac", "bubl", "camera", "makeup", "pinw", "plcrd", "sketch", "wool"]:
                b = pygame.image.load("Sprites/Misc/item/" + avars[3][9][a][0] + "1.png").convert()
                sl.append(b)
                b = pygame.image.load("Sprites/Misc/item/" + avars[3][9][a][0] + "2.png").convert()
                sl.append(b)
                b = pygame.image.load("Sprites/Misc/item/" + avars[3][9][a][0] + "3.png").convert()
                sl.append(b)
            isprs.append(sl)
            a += 1
        return(isprs)

    def ballani():
        flip = False
        if anifr < 12 or 59 < anifr < 72 or 89 < anifr < 114:
            spr = 3
            if anifr < 12:
                sprx = 168 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            elif anifr < 72:
                sprx = 40 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                flip = True
            else:
                sprx = 100 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                if anifr < 102:
                    flip = True
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif anifr < 18 or 53 < anifr < 60 or 71 < anifr < 78 or anifr > 137:
            spr = 5
            if anifr < 18:
                sprx = 156 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                spry = 90 + (32 - asprs[avars[3][5]][spr].get_height())
            elif anifr < 60:
                sprx = 54 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                spry = 94 + (32 - asprs[avars[3][5]][spr].get_height())
            elif anifr < 78:
                sprx = 56 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                spry = 92 + (32 - asprs[avars[3][5]][spr].get_height())
                flip = True
            else:
                sprx = 168 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif anifr < 30 or 77 < anifr < 90:
            spr = 4
            if anifr < 30:
                sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            else:
                sprx = 78 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                flip = True
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif anifr < 36:
            spr = 12
            sprx = 112 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif anifr < 48:
            spr = 11
            sprx = 100 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif anifr < 54 or 125 < anifr < 132:
            spr = 13
            if anifr < 54:
                sprx = 78 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            else:
                sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                flip = True
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif anifr < 126 or 131 < anifr < 138:
            spr = 9
            if anifr < 126:
                sprx = 100 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                if anifr < 120:
                    flip = True
            else:
                sprx = 148 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        itms = 0
        if anifr < 6:
            itmx = 166
            itmy = 76
        elif anifr < 12:
            itmx = 170
            itmy = 82
        elif anifr < 18 or anifr > 137:
            itmx = 136
            itmy = 36
        elif anifr < 24:
            itmx = 112
            itmy = 82
        elif anifr < 30:
            itmx = 86
            itmy = 102
        elif anifr < 36:
            itmx = 52
            itmy = 96
        elif anifr < 42:
            itmx = 24
            itmy = 106
        elif anifr < 66:
            itmx = 20
            itmy = 106
        elif anifr < 72:
            itmx = 52
            itmy = 68
        elif anifr < 78:
            itmx = 84
            itmy = 26
        else:
            itmx = 0
            itmy = 0
        return spr, sprx, spry, itms, itmx, itmy, flip

    def ropeani():
        if anifr % 12 < 6:
            spr = 4
            itms = 1
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        else:
            spr = 5
            itms = 2
            spry = 90 + (32 - asprs[avars[3][5]][spr].get_height())
        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        itmx = 96
        itmy = 82
        return spr, sprx, spry, itms, itmx, itmy

    def plushani():
        itms = 0
        if anifr < 24:
            spr = 10 - (anifr < 12)
            if anifr < 12:
                screen.blit(em, [104, 80])
        elif 59 < anifr < 108:
            spr = 10 // (1 + (anifr % 12 < 6))
            if anifr % 12 < 6:
                screen.blit(heart, [104, 80])
        else:
            spr = 16 + (anifr % 12 < 6)
        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        itmx = 84
        itmy = 106
        return spr, sprx, spry, itms, itmx, itmy

    def yoyoani():
        if anifr % 12 < 6:
            spr = 11
            itms = 1
        else:
            spr = 5 + (7 * (anifr < 72))
            itms = 3 - (anifr < 72)
        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        itmx = sprx - 32
        itmy = 98
        return spr, sprx, spry, itms, itmx, itmy

    def plantani():
        if anifr < 48:
            itms = 0
            itmy = 106
            spr = 3 + (anifr % 12 < 6)
        elif anifr < 96:
            itms = 1
            itmy = 98
            spr = 3 + (anifr % 12 < 6)
        else:
            itms = 3 - (avars[3][9][citn][2] == 4)
            itmy = 98
            spr = 6 + (anifr % 12 < 6) - (2 * (avars[3][9][citn][2] == 4))
            if anifr % 12 < 6:
                screen.blit([cnf, heart][avars[3][9][citn][2] == 4], [152, 80])
        itmx = 84
        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        return spr, sprx, spry, itms, itmx, itmy

    def ufoani():
        if 5 < anifr < 132:
            itms = 2
            spr = 3 + (anifr % 12 < 6)
        else:
            itms = 3
            if anifr < 6:
                spr = 14
                screen.blit(qm, [152, 80])
            else:
                spr = 9
                screen.blit(em, [152, 80])
        if anifr < 6:
            itmx = 80
            itmy =  106
        elif anifr < 18:
            itmx = 80
            itmy =  106 - (6 * (anifr - 6))
        elif anifr < 42:
            itmx = 80 - (6 * (anifr - 18))
            itmy = 34
        elif anifr < 100:
            itmx = 240
            itmy =  160
        elif anifr < 132:
            itmx = 272 - (6 * (anifr - 100))
            itmy = 34
        else:
            itmx = 80
            itmy =  34 + (6 * (anifr - 132))
        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        screen.blit(isprs[citn][1], [(sprx - 24), 106])
        return spr, sprx, spry, itms, itmx, itmy

    def phouseani():
        spr = 14 - (5 * (anifr // 48)) + (anifr % 12 < 6)
        itms = 1 + (anifr // 48)
        itmx = 96
        itmy = 82
        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 94 + ((32 - asprs[avars[3][5]][spr].get_height()) // 2)
        return spr, sprx, spry, itms, itmx, itmy

    def cloneani(movl):
        itms = 0
        if anifr < 6:
            itmx = 84
            itmy = 106
            spr = 14
            screen.blit(qm, [152, 80])
        else:
            itmx = 240
            itmy = 160
            if anifr < 18 or 131 < anifr:
                spr = 9
                screen.blit(em, [152, 80])
            else:
                spr = movl[(anifr - 18) // 6]
        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        if 5 < anifr < 12 or 131 < anifr:
            screen.blit(poof, [80, 98])
        elif anifr > 5:
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], 1, 0), [(sprx - 40), spry])
        return spr, sprx, spry, itms, itmx, itmy

    def woolani(wevo):
        itms = 1 + (anifr % 12 > 5) + (wevo)
        spr = 4 + (5 * (anifr % 12 > 5))
        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        itmx = 104
        itmy = 98
        return spr, sprx, spry, itms, itmx, itmy

    def cameani(isr, wevo):
        sprx = 120 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
        if isr:
            if (anifr < 36) or (71 < anifr < 108):
                itms = 1
                itmx = 84
                itmy = 106
                spr = 11
                if anifr % 12 > 5:
                    screen.blit(shine, [104, 80])
            else:
                itms = 0
                itmx = 240
                itmy = 106
                spr = 4 + ((1 + (4 * wevo)) * (anifr % 12 > 5))
        else:
            spr = 4 + (anifr % 12 > 5)
            itms = (2 * (anifr % 12 > 5))
            itmx = 84
            itmy = 98 + (8 * (anifr % 12 > 5))
            if anifr % 12 > 5:
                screen.blit(shine, [104, 80])
        return spr, sprx, spry, itms, itmx, itmy

    def bublani():
        sprx = 120 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
        itmx = 84
        itmy = 98
        spr = 12 + (3 * (anifr % 12 > 5))
        itms = 1 + (anifr % 12 > 5)
        for i in range(4):
            screen.blit(pygame.transform.flip(isprs[citn][3], 0, ((i % 2) == (anifr % 12 > 5))), [((i * 24) - 12), (98 + (8 * ((i % 2) == (anifr % 12 > 5))))])
        return spr, sprx, spry, itms, itmx, itmy

    def duckani():
        sprx = 240 + ((32 - asprs[avars[3][5]][3].get_width()) // 2) - (16 * (anifr // 6))
        spry = 90 + (32 - asprs[avars[3][5]][3].get_height()) + (8 * (anifr % 12 < 6))
        itmx = 272 - (16 * (anifr // 6))
        itmy = 106
        spr = 11 + (2 * (anifr % 12 > 5))
        itms = 0
        return spr, sprx, spry, itms, itmx, itmy

    def skateani():
        sprx = 240 + ((32 - asprs[avars[3][5]][3].get_width()) // 2) - (16 * (anifr // 6))
        spry = 92 + (32 - asprs[avars[3][5]][3].get_height())
        itmx = 244 - (16 * (anifr // 6))
        itmy = 106
        spr = 11 + (anifr % 12 > 5)
        itms = 0
        return spr, sprx, spry, itms, itmx, itmy

    def dustani():
        itms = 0
        itmx = 240
        itmy = 160
        sprx = 104 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)
        if anifr < 24:
            spr = 3 + (anifr % 12 > 5)
            spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
            screen.blit(shine, [(88 + (48 * (anifr % 12 > 5))), (90 + (24 * (anifr % 12 > 5)))])
        elif anifr < 84:
            spr = 5 + (4 * (anifr % 12 > 5))
            spry = 90 + (32 - asprs[avars[3][5]][3].get_height()) - (8 * (anifr % 12 > 5))
            screen.blit(shine, [(88 + (48 * (anifr % 12 > 5))), (74 + (40 * (anifr % 12 > 5)))])
        else:
            spr = 3 + (6 * (anifr % 12 > 5))
            spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
        return spr, sprx, spry, itms, itmx, itmy

    def bookani(maxs):
        sprx = 120 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
        if maxs == 0:
            itmx = sprx - 16
            itmy = 108
            if anifr % 36 < 6:
                itms = 2
                spr = 3
            else:
                itms = 1
                if anifr % 36 < 24:
                    spr = 6
                    screen.blit(cnf, [152, 80])
                else:
                    spr = 5
                    screen.blit(em, [152, 80])
        elif maxs == 1:
            itmx = sprx - 16
            itmy = 108
            itms = 1
            spr = 5 - (anifr % 12 < 6)
            screen.blit([mn1, mn2][anifr % 12 < 6], [152, 80])
        elif maxs == 2:
            itmx = sprx - 16
            itmy = 108
            itms = 1
            spr = 5 * (1 + (anifr % 12 < 6))
            screen.blit([heart, heart2][anifr % 12 < 6], [152, 80])
        elif maxs == 3:
            itmx = sprx - 16
            itmy = 108
            itms = 1 + (2 * (anifr < 72))
            spr = 4 + (anifr % 12 < 6) + ((anifr % 12 < 6) and (anifr < 72))
            if anifr > 71:
                screen.blit(poo[anifr % 12 < 6], [(sprx - 12), 110])
        elif maxs == 4:
            itmx = sprx - 16
            itmy = 108
            if anifr < 72:
                itms = 1
                spr = 4 - (anifr % 12 < 6)
            else:
                itms = 3
                spr = 5 - (anifr % 12 < 6)
                if anifr % 12 > 5:
                    screen.blit(shine, [152, 80])
        elif maxs == 5:
            itmx = sprx - 16
            itmy = 108 - (32 * (anifr % 12 > 5))
            itms = 3
            spr = 4 * (1 + (anifr % 12 > 5))
        return spr, sprx, spry, itms, itmx, itmy

    def sketani(maxs):
        sprx = 120 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
        itmy = 106
        if anifr < 12:
            itms = 0
            itmx = 84
            spr = 11 - (6 * (anifr % 12 > 5))
        elif anifr < 36 or 71 < anifr < 108:
            itms = 1
            itmx = 83 + (2 * (anifr % 12 > 5))
            spr = 16 + (anifr % 12 > 5)
        else:
            itms = 1
            itmx = 240
            spr = 4 + (anifr % 12 > 5)
            if maxs == 0:
                screen.blit(isprs[citn][3], [84, 106])
            elif maxs == 1:
                screen.blit(isprs[citn][2], [84, 106])
                screen.blit(asprs[avars[3][5]][1], [88, 110])
            else:
                screen.blit(isprs[citn][2], [84, 106])
                screen.blit(heart, [88, 110])
        return spr, sprx, spry, itms, itmx, itmy

    def pcani(maxs):
        sprx = 120 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
        spr = 17 - (anifr % 12 < 6)
        itms = 1 + (anifr % 24 > 5) + (11 < (anifr % 24) < 18)
        itmx = 84
        itmy = 106
        if maxs == 0:
            if anifr % 12 > 5:
                screen.blit([qm, cnf, em][(anifr % 48 > 11) + (23 < (anifr % 48) < 36)], [152, 80])
        elif maxs == 1:
            screen.blit([mn1, mn2][anifr % 12 < 6], [152, 80])
        elif maxs == 2:
            screen.blit([heart, heart2][anifr % 12 < 6], [152, 80])
        elif maxs == 3:
            if anifr % 12 > 5:
                screen.blit([qm, heart, em][(anifr % 48 > 11) + (23 < (anifr % 48) < 36)], [152, 80])
        elif maxs == 4:
            if anifr % 12 > 5:
                screen.blit(shine, [152, 80])
        elif maxs == 5:
            if anifr % 12 > 5:
                screen.blit([em, cnf, em][(anifr % 48 > 11) + (23 < (anifr % 48) < 36)], [152, 80])
        return spr, sprx, spry, itms, itmx, itmy

    def blockani():
        if anifr < 60 or 77 < anifr < 132:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 16
                itmx = 83
            else:
                spr = 17
                itmx = 85
            itms = 0
        elif anifr < 72 or anifr > 131:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 4
            else:
                spr = 5
            if anifr < 72:
                itms = 1
            else:
                itms = 3
            itmx = 84
        else:
            spr = 9
            itms = 2
            itmx = 84
        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        itmy = 106
        return spr, sprx, spry, itms, itmx, itmy

    def trmpani():
        itms = 0
        if anifr < 30 or 71 < anifr < 102:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 11
            else:
                spr = 5
        elif anifr < 36 or 101 < anifr < 108 or 50 < anifr < 57 or 122 < anifr < 129:
            spr = 12
        else:
            spr = 15
        sprx = 116
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        itmx = 92
        if avars[avars[3][5]][1] == 1:
            itmy = 107
        elif avars[avars[3][5]][1] == 2:
            itmy = 105
        elif avars[avars[3][5]][1] == 3:
            itmy = 101
        elif avars[avars[3][5]][1] == 4:
            itmy = 97
        return spr, sprx, spry, itms, itmx, itmy

    def clayani():
        if anifr < 12:
            itms = 0
            itmx = 84
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 11
            else:
                spr = 5
        elif anifr < 36 or 71 < anifr < 108:
            itms = 1
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 16
                itmx = 83
            else:
                spr = 17
                itmx = 85
        elif anifr < 72:
            itms = 2
            itmx = 84
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 4
            else:
                spr = 5
        else:
            itms = 3
            itmx = 84
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 10
                screen.blit(heart, [104, 80])
            else:
                spr = 5
        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        itmy = 106
        return spr, sprx, spry, itms, itmx, itmy
    
    def bloonani():
        if anifr < 108:
            if anifr < 12:
                itms = 1
                if anifr < 6:
                    spr = 5
                else:
                    spr = 11
            elif anifr < 48 or 71 < anifr:
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    spr = 12
                    itms = 1
                else:
                    spr = 15
                    itms = 2
            else:
                itms = 1
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    spr = 6
                else:
                    spr = 8
            itmx = 92
            if avars[avars[3][5]][1] == 1:
                itmy = 107
            elif avars[avars[3][5]][1] == 2:
                itmy = 105
            elif avars[avars[3][5]][1] == 3:
                itmy = 101
            elif avars[avars[3][5]][1] == 4:
                itmy = 97
        else:
            if anifr < 138:
                itms = 0
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    spr = 5
                else:
                    spr = 4
            else:
                itms = 3
                spr = 9
            itmx = 84
            itmy = 106
        sprx = 116
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        return spr, sprx, spry, itms, itmx, itmy

    def mirrorani():
        itms = 0
        if anifr < 36:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 4
            else:
                spr = 5
        elif anifr < 84:
            if ((anifr / 24) - (anifr // 24)) < 0.5:
                spr = 17
                screen.blit(shine, [104, 72])
            else:
                spr = 16
                screen.blit(shine, [86, 88])
        elif anifr < 108:
            spr = 12
        elif anifr < 132:
            spr = 15
        else:
            spr = 4 + (6 * (anifr > 137))
        sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        itmx = 84
        itmy = 106
        return spr, sprx, spry, itms, itmx, itmy

    def wghtani():
        itms = 0
        if anifr < 36:
            itmy = 106
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 4
            else:
                spr = 5
        elif anifr < 60:
            itmy = 106
            spr = 11
        elif anifr < 66:
            itmy = 102
            spr = 12
        elif anifr < 90 or 101 < anifr < 126:
            itmy = 102
            spr = 6
        elif anifr < 102 or 125 < anifr < 138:
            itmy = 98
            spr = 8
        else:
            itmy = 90
            spr = 5
        sprx = 116
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        itmx = 92
        return spr, sprx, spry, itms, itmx, itmy

    def plcani(maxs):
        sprx = 120 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
        itmy = 106
        if anifr < 12:
            itms = 0
            itmx = 84
            spr = 11 - (6 * (anifr % 12 > 5))
        elif anifr < 36 or 71 < anifr < 108:
            itms = 1
            itmx = 83 + (2 * (anifr % 12 > 5))
            spr = 16 + (anifr % 12 > 5)
        else:
            itms = 2 + (maxs > 0)
            itmx = 84
            spr = 4 + (anifr % 12 > 5)
        return spr, sprx, spry, itms, itmx, itmy

    def pinani(maxs):
        sprx = 120 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][3].get_height())
        itmx = 84
        itmy = 102
        itms = (2 * (maxs > 0)) + (anifr % [12, 6][maxs > 0] > [5, 2][maxs > 0])
        spr = 11 + (4 * (anifr % [12, 6][maxs > 0] > [5, 2][maxs > 0]))
        return spr, sprx, spry, itms, itmx, itmy

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 7, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    hpb = pygame.image.load("Sprites/Misc/menu/hpyf.png").convert()

    inti = pygame.image.load("Sprites/Misc/menu/inti.png").convert()
    styi = pygame.image.load("Sprites/Misc/menu/styi.png").convert()
    kndi = pygame.image.load("Sprites/Misc/menu/kndi.png").convert()
    humi = pygame.image.load("Sprites/Misc/menu/humi.png").convert()
    gori = pygame.image.load("Sprites/Misc/menu/gori.png").convert()
    pasi = pygame.image.load("Sprites/Misc/menu/pasi.png").convert()

    try:
        if pygame.image.load(avars[avars[3][5]][23]).get_rect().size == (240, 160):
            rbck = pygame.image.load(avars[avars[3][5]][23]).convert()
        else:
            rbck = pygame.Surface([240, 160]).convert()
            rbck.fill((51, 51, 204))
            rbck.blit(fnt.render("IMAGE SIZE IS", 1, (255, 255, 255)), [8, 34])
            rbck.blit(fnt.render("INCORRECT!!!", 1, (255, 255, 255)), [8, 50])
            rbck.blit(fnt.render("DO NOT MESS", 1, (255, 255, 255)), [8, 66])
            rbck.blit(fnt.render("WITH THE", 1, (255, 255, 255)), [8, 82])
            rbck.blit(fnt.render("GAME FILES!", 1, (255, 255, 255)), [8, 98])
    except pygame.error:
        rbck = pygame.Surface([240, 160]).convert()
        rbck.fill((51, 51, 204))
        rbck.blit(fnt.render("ERROR 404:", 1, (255, 255, 255)), [8, 34])
        rbck.blit(fnt.render("BACKGROUND IMAGE", 1, (255, 255, 255)), [8, 50])
        rbck.blit(fnt.render("NOT FOUND", 1, (255, 255, 255)), [8, 66])

    initml = ['plush', 'yoyo', '!!', 'book', 'wool', 'tamai', 'pc', 'blocks',
              'trumpet', 'clay', 'balloon', 'mirror', 'weights', 'sketch', 'abac', 'gamei',
              'plcrd', 'musb', 'makeup', 'pman', 'dhouse']
    outitml = ['ball', 'rope', 'plant', 'ufo', 'phouse', 'bubl', 'ducki', 'skate', 'dust', 'pinw']

    uplan = ['plush', 'tamai', 'pman', 'dhouse', 'gamei', 'musb']

    uclan = ['clay', 'makeup', 'abac']

    s, tm , w = weather.chktime(avars)
    if w == 2:
        initml.append('camera')
    else:
        outitml.append('camera')

    rain = pygame.image.load("Sprites/Misc/bg/rain.png").convert()
    snow = pygame.image.load("Sprites/Misc/bg/snow.png").convert()

    raing = pygame.image.load("Sprites/Misc/bg/rpgb.png").convert()
    snowg = pygame.image.load("Sprites/Misc/bg/spgb.png").convert()

    mn1 = pygame.image.load("Sprites/Misc/emo/music1.png").convert()
    mn2 = pygame.image.load("Sprites/Misc/emo/music2.png").convert()
    heart = pygame.image.load("Sprites/Misc/emo/heart.png").convert()
    heart2 = pygame.image.load("Sprites/Misc/emo/heart2.png").convert()
    shine = pygame.image.load("Sprites/Misc/emo/shine.png").convert()
    cnf = pygame.image.load("Sprites/Misc/emo/conf.png").convert()
    em = pygame.image.load("Sprites/Misc/emo/em.png").convert()
    qm = pygame.image.load("Sprites/Misc/emo/qm.png").convert()

    poof = pygame.image.load("Sprites/Misc/obj/poof.png").convert()

    poo = [pygame.image.load("Sprites/Misc/poo/bpoo1.png").convert(), pygame.image.load("Sprites/Misc/poo/bpoo2.png").convert()]

    isprs = itspr()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    lfnt = pygame.font.Font("Sprites/Misc/font/Tama1.ttf", 8)

    textbox = pygame.Surface([240, 112]).convert()
    textbox.fill((0, 255, 255))
    global tl
    global ty
    tl = 0
    ty = 0
    drhl()
    dral()
    tl = 6
    ty = 104
    drhl()

    scrli = pygame.image.load("Sprites/Misc/txtbox/scrli.png").convert()

    sound = sounds.imprtsnd(avars)

    clock = pygame.time.Clock()

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if bx or inf:
            screen.blit(textbox, [0, 24])
            if bx:
                screen.blit(scrli, [232, 128])
                global itn
                itn = 0
                drit()
            else:
                screen.blit(isprs[iitn][0], [108, 32])
                if avars[3][9][iitn][2] > 0:
                    screen.blit(hpb, [40, 56])
                    if avars[3][9][iitn][2] > 1:
                        screen.blit(hpb, [88, 56])
                        if avars[3][9][iitn][2] > 2:
                            screen.blit(hpb, [136, 56])
                            if avars[3][9][iitn][2] > 3:
                                screen.blit(hpb, [184, 56])
                if avars[3][9][iitn][3] > 0:
                    screen.blit(inti, [32, 80])
                if avars[3][9][iitn][4] > 0:
                    screen.blit(styi, [64, 80])
                if avars[3][9][iitn][5] > 0:
                    screen.blit(kndi, [96, 80])
                if avars[3][9][iitn][6] > 0:
                    screen.blit(humi, [128, 80])
                if avars[3][9][iitn][7] > 0:
                    screen.blit(gori, [160, 80])
                if avars[3][9][iitn][8] > 0:
                    screen.blit(pasi, [192, 80])
                screen.blit((fnt.render("MOVE", 1, (0, 0, 100))), [95, 98])
                screen.blit((fnt.render("TRASH", 1, (0, 0, 100))), [89, 114])
        else:
            if avars[3][9][citn][0] in outitml:
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
                if avars[3][9][citn][0] == 'ball':
                    spr, sprx, spry, itms, itmx, itmy, flip = ballani()
                elif avars[3][9][citn][0] == 'rope':
                    spr, sprx, spry, itms, itmx, itmy = ropeani()
                elif avars[3][9][citn][0] == 'plant':
                    spr, sprx, spry, itms, itmx, itmy = plantani()
                    if anifr == 48:
                        sound[3].play()
                    elif anifr == 96:
                        sound[12 - (3 * (avars[3][9][citn][2] == 4))].play()
                elif avars[3][9][citn][0] == 'ufo':
                    spr, sprx, spry, itms, itmx, itmy = ufoani()
                    if 5 < anifr < 12 or 17 < anifr < 24 or 111 < anifr < 118:
                        pygame.mixer.stop()
                        sound[2].play()
                    elif anifr == 132:
                        sound[12].play()
                elif avars[3][9][citn][0] == 'phouse':
                    spr, sprx, spry, itms, itmx, itmy = phouseani()
                    if anifr == 48:
                        sound[3].play()
                    elif anifr == 96:
                        sound[9].play()
                elif avars[3][9][citn][0] == 'camera':
                    spr, sprx, spry, itms, itmx, itmy = cameani(0, 0)
                elif avars[3][9][citn][0] == 'bubl':
                    spr, sprx, spry, itms, itmx, itmy = bublani()
                elif avars[3][9][citn][0] == 'ducki':
                    spr, sprx, spry, itms, itmx, itmy = duckani()
                elif avars[3][9][citn][0] == 'skate':
                    spr, sprx, spry, itms, itmx, itmy = skateani()
                elif avars[3][9][citn][0] == 'dust':
                    spr, sprx, spry, itms, itmx, itmy = dustani()
                elif avars[3][9][citn][0] == 'pinw':
                    spr, sprx, spry, itms, itmx, itmy = pinani(maxs)
            elif avars[3][9][citn][0] in initml:
                screen.blit(rbck, [0, 0])
                if avars[3][9][citn][0] in uplan:
                    spr, sprx, spry, itms, itmx, itmy = plushani()
                    if (avars[3][9][citn][0] == 'gamei') and (23 < anifr < 60) and (anifr % 12 > 5):
                        screen.blit([qm, mn1, heart][maxs], [112, 82])
                    if (avars[3][9][citn][0] == 'musb') and (23 < anifr < 60) and (anifr % 12 > 5):
                        screen.blit([mn1, mn2][maxs > 0], [112, 82])
                        if anifr % 12 == 6:
                            if maxs == 0:
                                sound[randint(19, 22)].play()
                            else:
                                sound[[20, 21, 22][(anifr - 24) // 12]].play()
                    if anifr == 60:
                        sound[9].play()
                elif avars[3][9][citn][0] == 'yoyo':
                    spr, sprx, spry, itms, itmx, itmy = yoyoani()
                elif avars[3][9][citn][0] == '!!':
                    spr, sprx, spry, itms, itmx, itmy = cloneani(movl)
                    if anifr == 6 or anifr == 132:
                        sound[9].play()
                elif avars[3][9][citn][0] == 'wool':
                    spr, sprx, spry, itms, itmx, itmy = woolani(wevo)
                elif avars[3][9][citn][0] == 'camera':
                    spr, sprx, spry, itms, itmx, itmy = cameani(1, wevo)
                    if (35 < anifr < 72) or (anifr > 107):
                        screen.blit(isprs[citn][3], [84, 106])
                        if avars[avars[3][5]][15] == 357:
                            screen.blit(paps[1], [88, 110])
                        elif avars[avars[3][5]][15] != 187:
                            screen.blit(asprs[avars[3][5]][1], [88, 110])
                elif avars[3][9][citn][0] == 'book':
                    spr, sprx, spry, itms, itmx, itmy = bookani(maxs)
                elif avars[3][9][citn][0] == 'sketch':
                    spr, sprx, spry, itms, itmx, itmy = sketani(maxs)
                elif avars[3][9][citn][0] == 'pc':
                    spr, sprx, spry, itms, itmx, itmy = pcani(maxs)
                elif avars[3][9][citn][0] == 'blocks':
                    spr, sprx, spry, itms, itmx, itmy = blockani()
                elif avars[3][9][citn][0] == 'trumpet':
                    spr, sprx, spry, itms, itmx, itmy = trmpani()
                    if 35 < anifr < 51 or 56 < anifr < 72 or 107 < anifr < 123 or 128 < anifr:
                        if anifr == 36 or anifr == 57 or anifr == 108 or anifr == 129:
                            sound[18].play()
                        if ((anifr / 6) - (anifr // 6)) < 0.5:
                            screen.blit(mn1, [104, 72])
                        else:
                            screen.blit(mn2, [86, 88])
                elif avars[3][9][citn][0] in uclan:
                    spr, sprx, spry, itms, itmx, itmy = clayani()
                elif avars[3][9][citn][0] == 'balloon':
                    spr, sprx, spry, itms, itmx, itmy = bloonani()
                elif avars[3][9][citn][0] == 'mirror':
                    spr, sprx, spry, itms, itmx, itmy = mirrorani()
                elif avars[3][9][citn][0] == 'weights':
                    spr, sprx, spry, itms, itmx, itmy = wghtani()
                elif avars[3][9][citn][0] == 'plcrd':
                    spr, sprx, spry, itms, itmx, itmy = plcani(maxs)
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [sprx, spry])
            screen.blit(isprs[citn][itms], [itmx, itmy])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
        for event in pygame.event.get():
            if event.type == QUIT:
                varsup.updtvrs(avars)
                kr = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in [303, 304]:
                    spclk = True
            if event.type == KEYUP:
                if event.key in [303, 304]:
                    spclk = False
            if event.type == MOUSEBUTTONDOWN:
                mp = event.pos
                d = (screen.get_size()[0] // 240)
                mp = ((mp[0] // d), (mp[1] // d))
                pb = event.button + (spclk * (1 + (event.button > 2)))
                if pb in [2, 4]:
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if scr != ((len(avars[3][9]) - 1) // 24):
                            scr += 1
                        else:
                            scr = 0
                        clt = 0
                elif pb == 5:
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if scr != 0:
                            scr -= 1
                        else:
                            scr = ((len(avars[3][9]) - 1) // 24)
                        clt = 0
                elif pb == 1:
                    clt = 0
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            sound[4].play()
                            return(avars, happyani)
                    if bx:
                        if 44 < mp[1] < 116 and 14 < mp[0] < 230 and (mp[0] - (14 + (27 * ((mp[0] - 14) // 27)))) < 24:
                            citn = ((mp[0] - 14) // 27) + (8 * ((mp[1] - 44) // 24)) + (scr * 24)
                            if citn < len(avars[3][9]):
                                if not swt:
                                    sound[3].play()
                                    anifr = 143
                                    bx = False
                                    if avars[3][9][citn][0] in outitml:
                                        s, tm , w = weather.chktime(avars)
                                        obgi = outbg()
                                    if avars[3][9][citn][0] == 'plant':
                                        a = randint(0, 1)
                                        if a:
                                            avars[3][9][citn][2] = 4
                                        else:
                                            avars[3][9][citn][2] = 0
                                            avars[avars[3][5]][17] -= (avars[avars[3][5]][17] > 0)
                                    if avars[3][9][citn][0] == '!!':
                                        movl = []
                                        while len(movl) < 19:
                                            movl.append(randint(3, 17))
                                    if avars[3][9][citn][0] in ['book', 'pc']:
                                        l = [avars[avars[3][5]][i] for i in range(5, 11)]
                                        a = max(l)
                                        b = []
                                        for i in range(0, 6):
                                            if l[i] == a:
                                                b.append(i)
                                        maxs = choice(b)
                                        avars[avars[3][5]][maxs + 5] += 5
                                    if avars[3][9][citn][0] in ['sketch', 'gamei']:
                                        l = [(avars[avars[3][5]][5] + avars[avars[3][5]][8]),
                                             (avars[avars[3][5]][6] + avars[avars[3][5]][9]),
                                             (avars[avars[3][5]][7] + avars[avars[3][5]][10])]
                                        a = max(l)
                                        b = []
                                        for i in range(0, 3):
                                            if l[i] == a:
                                                b.append(i)
                                        maxs = choice(b)
                                        avars[avars[3][5]][maxs + 5] += 5
                                        avars[avars[3][5]][maxs + 8] += 5
                                    if avars[3][9][citn][0] == 'plcrd':
                                        maxs = 0
                                        if avars[avars[3][5]][5] < avars[avars[3][5]][8]:
                                            maxs = 3
                                        elif avars[avars[3][5]][5] == avars[avars[3][5]][8]:
                                            maxs = choice([0, 3])
                                        avars[avars[3][5]][maxs + 5] += 2
                                    if avars[3][9][citn][0] == 'musb':
                                        maxs = 0
                                        if avars[avars[3][5]][6] < avars[avars[3][5]][9]:
                                            maxs = 3
                                        elif avars[avars[3][5]][6] == avars[avars[3][5]][9]:
                                            maxs = choice([0, 3])
                                        avars[avars[3][5]][maxs + 6] += 2
                                    if avars[3][9][citn][0] == 'pinw':
                                        maxs = 0
                                        if avars[avars[3][5]][7] < avars[avars[3][5]][10]:
                                            maxs = 3
                                        elif avars[avars[3][5]][7] == avars[avars[3][5]][10]:
                                            maxs = choice([0, 3])
                                        avars[avars[3][5]][maxs + 7] += 2
                                    if avars[3][9][citn][0] == 'makeup':
                                        if (avars[avars[3][5]][15] == 194) and ((avars[avars[3][5]][5] + avars[avars[3][5]][8]) < (avars[avars[3][5]][6] + avars[avars[3][5]][9])):
                                            avars[avars[3][5]][1] = 5
                                            avars = growth.grw(avars)
                                            asprs = aspr()
                                        elif (avars[avars[3][5]][15] == 356) and ((avars[avars[3][5]][5] + avars[avars[3][5]][8]) > (avars[avars[3][5]][6] + avars[avars[3][5]][9])):
                                            avars[avars[3][5]][1] = 4
                                            avars[avars[3][5]][15] = 194
                                            a = avars[avars[3][5]][24]
                                            a.pop(3)
                                            avars[avars[3][5]][24] = a
                                            asprs = aspr()
                                    if avars[3][9][citn][0] == 'wool':
                                        wevo = False
                                        if (avars[avars[3][5]][15] == 193) and ((avars[avars[3][5]][5] + avars[avars[3][5]][8]) < (avars[avars[3][5]][7] + avars[avars[3][5]][10])):
                                            avars[avars[3][5]][1] = 5
                                            avars = growth.grw(avars)
                                            asprs = aspr()
                                            wevo = True
                                        elif (avars[avars[3][5]][15] == 359) and ((avars[avars[3][5]][5] + avars[avars[3][5]][8]) > (avars[avars[3][5]][7] + avars[avars[3][5]][10])):
                                            avars[avars[3][5]][1] = 4
                                            avars[avars[3][5]][15] = 193
                                            a = avars[avars[3][5]][24]
                                            a.pop(3)
                                            avars[avars[3][5]][24] = a
                                            asprs = aspr()
                                            wevo = True
                                    if (avars[3][9][citn][0] == 'camera') and ('camera' in initml):
                                        wevo = False
                                        paps = chsprs(357, (avars[avars[3][5]][30] == 2), avars[avars[3][5]][14])
                                        if (avars[avars[3][5]][15] == 187) and ((avars[avars[3][5]][7] + avars[avars[3][5]][10]) < (avars[avars[3][5]][6] + avars[avars[3][5]][9])):
                                            avars[avars[3][5]][1] = 5
                                            avars = growth.grw(avars)
                                            wevo = True
                                        elif (avars[avars[3][5]][15] == 357) and ((avars[avars[3][5]][7] + avars[avars[3][5]][10]) > (avars[avars[3][5]][6] + avars[avars[3][5]][9])):
                                            avars[avars[3][5]][1] = 4
                                            avars[avars[3][5]][15] = 187
                                            a = avars[avars[3][5]][24]
                                            a.pop(3)
                                            avars[avars[3][5]][24] = a
                                            wevo = True
                                    if avars[3][9][citn][2] > 0:
                                        happyani = True
                                        if (avars[avars[3][5]][17] + avars[3][9][citn][2]) < 6:
                                            avars[avars[3][5]][17] += avars[3][9][citn][2]
                                        else:
                                            avars[avars[3][5]][17] = 6
                                    avars[avars[3][5]][5] += avars[3][9][citn][3]
                                    avars[avars[3][5]][6] += avars[3][9][citn][4]
                                    avars[avars[3][5]][7] += avars[3][9][citn][5]
                                    avars[avars[3][5]][8] += avars[3][9][citn][6]
                                    avars[avars[3][5]][9] += avars[3][9][citn][7]
                                    avars[avars[3][5]][10] += avars[3][9][citn][8]
                                else:
                                    if iitn == citn:
                                        sound[12].play()
                                    else:
                                        sound[3].play()
                                        a = avars[3][9]
                                        a[iitn], a[citn] = a[citn], a[iitn]
                                        avars[3][9] = a
                                        isprs = itspr()
                                    swt = False
                    elif inf:
                        if 32 < mp[1] < 56 and 108 < mp[0] < 132:
                            sound[3].play()
                            inf = False
                            bx = True
                        if 98 < mp[1] < 110 and 95 < mp[0] < 145:
                            sound[3].play()
                            swt = True
                            inf = False
                            bx = True
                        if 114 < mp[1] < 126 and 89 < mp[0] < 153:
                            sound[3].play()
                            avars[3][9][iitn][1] -= 1
                            if avars[3][9][iitn][1] == 0:
                                a = avars[3][9]
                                a.pop(iitn)
                                avars[3][9] = a
                            if len(avars[3][9]) > 0:
                                inf = False
                                bx = True
                                isprs = itspr()
                                if ((len(avars[3][9]) - 1) // 24) < scr:
                                    scr = (len(avars[3][9]) - 1) // 24
                            else:
                                return(avars, happyani)
                if pb == 3:
                    clt = 0
                    if bx:
                        if 44 < mp[1] < 116 and 14 < mp[0] < 230 and (mp[0] - (14 + (27 * ((mp[0] - 14) // 27)))) < 24:
                            iitn = ((mp[0] - 14) // 27) + (8 * ((mp[1] - 44) // 24)) + (scr * 24)
                            if iitn < len(avars[3][9]):
                                sound[3].play()
                                anifr = 23
                                bx = False
                                inf = True
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
                if bx:
                    clt += 1
        if chngsts:
            avars = statusup.chngsts(avars)
            if avars[avars[3][5]][20] or not avars[avars[3][5]][21]:
                return(avars, happyani)
            chngsts = False
        if anifr < 143:
            anifr += 1
        else:
            anifr = 0
        if clt > 29:
            return(avars, happyani)
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

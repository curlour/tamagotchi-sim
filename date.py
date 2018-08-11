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
import palette
import growth
import mainscreen
import marryseq

def fdt(avars, asprs, screen):

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

    bx = False

    scr = 0

    ret = 1

    chngsts = False

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

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    heart = pygame.image.load("Sprites/Misc/emo/heart.png").convert()
    hear2 = pygame.image.load("Sprites/Misc/emo/heart2.png").convert()

    backg = pygame.image.load("Sprites/Misc/bg/dateplin.png").convert()

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

    book = []
    for i in [0, 1]:
        a = pygame.Surface((24, 24))
        a.blit(backg, [-(24 * i), 0])
        a.set_colorkey((0, 255, 255))
        a.convert()
        book.append(a)

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    marrtx = fnt.render("MARRY?", 1, (0, 0, 100))
    yest = fnt.render("YES", 1, (0, 0, 100))
    notx = fnt.render("NO", 1, (0, 0, 100))

    sound = sounds.imprtsnd(avars)

    clock = pygame.time.Clock()

    anifr = 0
    
    p = [4, 6][randint(1, 4) == 4]
    t = 435600
    g = randint(0, 4294967295)
    a = randint(1, 8)
    c = ["no", "ma", "ku", "ku", "ma", "me", "me", "no"][a - 1]
    d = [choice(["ku", "ma", "me"]), "ku", "ku", "me", "ma", "me", "ma", "no"][a - 1]
    ov = [[a, 1, 0, (g % 4 > 1), 0, randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), c, c, d, g, 0, 0, 0, randint(1, 99), randint(0, 5), 0, 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 4], [], [], [0, 0, 0, 0, 0, 0]]
    ov = growth.grw(ov)
    while ov[0][1] < p:
        ov[0][1] += 1
        if ov[0][1] == 5:
            ov[0][1] = 6
        ov = growth.grw(ov)
    pchr = ov[0][15]
    pcharinfo = ["PARK", "", pchr, g, ov[0][13], ov[0][12], ov[0][11], [t, avars[avars[3][5]][2]], 0]
    pchrs = chsprs(pchr, pcharinfo[3])

    matc = [randint(379, 384), randint(379, 380), randint(381, 382), randint(383, 384)][["no", "ma", "me", "ku"].index(c)]
    mats = chsprs(matc, [4027187200, 16384000][matc == 381])

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        screen.blit(backg, [0, 0])
        if scr == 0 and not bx:
            if anifr < 48:
                screen.blit(pygame.transform.flip(mats[3 + (anifr % 12 > 5)], 1, 0), [104, 35])
                screen.blit(book[0], [136, 43])
                screen.blit(asprs[avars[3][5]][11 + (2 * (anifr % 12 > 5))], [(224 - (12 * (anifr // 6))), (98 - (2 * (anifr % 12 > 5)))])
            elif anifr < 54:
                if anifr == 48:
                    pygame.mixer.stop()
                    sound[9].play()
                screen.blit(pygame.transform.flip(mats[5], 1, 0), [104, 35])
                screen.blit(book[0], [136, 43])
                screen.blit(asprs[avars[3][5]][5], [128, 98])
            elif anifr < 78:
                screen.blit(pygame.transform.flip(mats[11 + (anifr % 12 > 5)], 1, 0), [104, 35])
                screen.blit(book[anifr % 12 > 5], [136, 43])
                screen.blit(asprs[avars[3][5]][3 + (anifr % 12 > 5)], [128, 98])
            elif anifr < 84:
                if anifr == 78:
                    pygame.mixer.stop()
                    sound[9].play()
                screen.blit(mats[5], [104, 35])
                screen.blit(book[0], [136, 43])
                screen.blit(asprs[avars[3][5]][9], [128, 98])
            elif anifr < 132:
                screen.blit(mats[3 + (anifr % 12 > 5)], [104, 35])
                screen.blit(book[0], [136, 43])
                screen.blit(asprs[avars[3][5]][3 + (7 * (anifr % 12 > 5))], [128, 98])
                screen.blit(pygame.transform.flip(pchrs[11 + (2 * (anifr % 12 > 5))], 1, 0), [(-16 + (12 * ((anifr - 84) // 6))), (98 - (2 * (anifr % 12 > 5)))])
            else:
                if anifr == 132:
                    pygame.mixer.stop()
                    sound[9].play()
                screen.blit(mats[4 + (anifr % 12 > 5)], [104, 35])
                screen.blit(book[0], [136, 43])
                screen.blit(asprs[avars[3][5]][10], [128, 98])
                screen.blit(pygame.transform.flip(pchrs[10], 1, 0), [80, 98])
        elif bx:
            screen.blit(textbox, [0, 24])
            screen.blit(marrtx, [8, 66])
            screen.blit(yest, [107, 82])
            screen.blit(notx, [164, 82])
        elif scr == 1:
            if anifr < 96:
                screen.blit(mats[8], [104, 35])
                screen.blit(book[0], [136, 43])
                screen.blit(asprs[avars[3][5]][6], [128, 98])
                screen.blit(pygame.transform.flip(pchrs[7], 1, 0), [80, 98])
            else:
                screen.blit(pygame.transform.flip(mats[11 + (anifr % 12 > 5)], 1, 0), [104, 35])
                screen.blit(book[anifr % 12 > 5], [136, 43])
                screen.blit(asprs[avars[3][5]][6], [128, 98])
                screen.blit(pchrs[11 + (2 * (anifr % 12 > 5))], [(68 - (12 * ((anifr - 96) // 6))), (98 - (2 * (anifr % 12 > 5)))])
        elif scr == 2:
            screen.blit(mats[5 + (5 * (anifr % 12 > 5))], [104, 35])
            screen.blit(book[0], [136, 43])
            if anifr < 72:
                screen.blit(asprs[avars[3][5]][5 + (5 * (anifr % 12 > 5))], [128, 98])
                screen.blit(pygame.transform.flip(pchrs[3], 1, 0), [80, 98])
                screen.blit([hear2, heart][anifr % 12 > 5], [160, 82])
            elif anifr < 96:
                screen.blit(asprs[avars[3][5]][3], [128, 98])
                screen.blit(pygame.transform.flip(pchrs[5 + (5 * (anifr % 12 > 5))], 1, 0), [80, 98])
                screen.blit([hear2, heart][anifr % 12 > 5], [64, 82])
            elif anifr < 120:
                screen.blit(asprs[avars[3][5]][11 + (anifr > 107)], [124, 98])
                screen.blit(pygame.transform.flip(pchrs[11 + (anifr > 107)], 1, 0), [84, 98])
            else:
                if anifr == 120:
                    pygame.mixer.stop()
                    sound[9].play()
                screen.blit(asprs[avars[3][5]][15], [120, 98])
                screen.blit(pygame.transform.flip(pchrs[15], 1, 0), [88, 98])
                screen.blit([hear2, heart][anifr % 12 > 5], [64, (74 + (4 * (anifr % 12 > 5)))])
                screen.blit([hear2, heart][anifr % 12 < 6], [112, (74 + (4 * (anifr % 12 < 6)))])
                screen.blit([hear2, heart][anifr % 12 > 5], [160, (74 + (4 * (anifr % 12 > 5)))])
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
                    if bx and 80 < mp[1] < 96:
                        if 164 < mp[0] < 188:
                            pygame.mixer.stop()
                            sound[12].play()
                            bx = False
                            scr = 1
                            anifr = 83
                        elif 107 < mp[0] < 139:
                            pygame.mixer.stop()
                            sound[9].play()
                            bx = False
                            scr = 2
                            anifr = 47
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
        if anifr < 143:
            anifr += 1
        else:
            anifr = 0
            if scr == 0 and not bx:
                bx = True
            elif scr == 1:
                scr = 0
                anifr = 78
                p = [4, 6][randint(1, 4) == 4]
                t = 435600
                g = randint(0, 4294967295)
                a = [choice([1, 2, 5, 8]), choice([1, 6, 7, 8]), choice([1, 3, 4, 8])][(matc - 379) // 2]
                c = ["no", "ma", "ku", "ku", "ma", "me", "me", "no"][a - 1]
                d = [choice(["ku", "ma", "me"]), "ku", "ku", "me", "ma", "me", "ma", "no"][a - 1]
                ov = [[a, 1, 0, (g % 4 > 1), 0, randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), c, c, d, g, 0, 0, 0, randint(1, 99), randint(0, 5), 0, 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 4], [], [], [0, 0, 0, 0, 0, 0]]
                ov = growth.grw(ov)
                while ov[0][1] < p:
                    ov[0][1] += 1
                    if ov[0][1] == 5:
                        ov[0][1] = 6
                    ov = growth.grw(ov)
                pchr = ov[0][15]
                pcharinfo = ["PARK", "", pchr, g, ov[0][13], ov[0][12], ov[0][11], [t, avars[avars[3][5]][2]], 0]
                pchrs = chsprs(pchr, pcharinfo[3])
            elif scr == 2:
                avars = marryseq.wed(avars, asprs, pchrs, pcharinfo, screen)
                return(avars, ret)
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

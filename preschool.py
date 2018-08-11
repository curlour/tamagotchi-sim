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
import jumprope
import statues

def pres(avars, asprs, screen):

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

    clt = 0

    chngsts = False

    tch = randint(0, 3)

    ret = 1

    cret = True

    def chsprs(chara):
        sprs = []
        bs = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "b.png")
        ss = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "s.png")
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

    def preani(tch):
        if ((anifr / 12) - (anifr // 12)) == 0 and anifr > 0:
            tch = randint(0, 3)
        if ((anifr / 12) - (anifr // 12)) < 0.5:
            mfs = 0
            if tch == 0:
                spr = 17
                pcs1 = 16
                pcs2 = 16
                pcs3 = 16
            elif tch == 1:
                spr = 16
                pcs1 = 17
                pcs2 = 16
                pcs3 = 16
            elif tch == 2:
                spr = 16
                pcs1 = 16
                pcs2 = 17
                pcs3 = 16
            else:
                spr = 16
                pcs1 = 16
                pcs2 = 16
                pcs3 = 17
        else:
            mfs = 1
            spr = 16
            pcs1 = 16
            pcs2 = 16
            pcs3 = 16
        return spr, pcs1, pcs2, pcs3, mfs, tch

    def gradani():
        if ((anifr / 12) - (anifr // 12)) < 0.5:
            spr = 6
        else:
            spr = 8
        mfs = 3
        return spr, mfs

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()
    
    presin = pygame.image.load("Sprites/Misc/bg/presin.png").convert()

    grad = pygame.image.load("Sprites/Misc/obj/graduation.png").convert()
    schoolen = pygame.image.load("Sprites/Misc/mail/schoolen.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

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

    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    pchr1 = randint(17, 48)
    psps1 = chsprs(pchr1)
    
    pchr2 = randint(17, 48)
    psps2 = chsprs(pchr2)
    
    pchr3 = randint(17, 48)
    psps3 = chsprs(pchr3)

    g = avars[avars[3][5]][14]
    if g < 0:
        g = 4294967296 + g
    a = format(g, '032b')

    t = ["MsFrill", "MsApron"][(a.count("1") % 2)]

    mfsps = []
    s = pygame.image.load("Sprites/NPC/" + t + ".png").convert()
    for i in range(4):
        a = pygame.Surface([32, 32]).convert()
        a.fill((0, 255, 255))
        a.blit(s, [-(32 * (i % 2)), -(32 * (i // 2))])
        a.set_colorkey((0, 255, 255))
        mfsps.append(a)

    while kr:
        if not bx and avars[avars[3][5]][1] == 2:
            screen.blit(presin, [0, 0])
            spr, pcs1, pcs2, pcs3, mfs, tch = preani(tch)
            screen.blit(mfsps[mfs], [104, 54])
            screen.blit(pygame.transform.flip(psps1[pcs1], 1, 0), [42, 94])
            screen.blit(pygame.transform.flip(psps2[pcs2], 1, 0), [50, 106])
            screen.blit(psps3[pcs3], [174, 94])
            screen.blit(asprs[avars[3][5]][spr], [166, 106])
        elif avars[avars[3][5]][1] > 2 and not bx:
            avars[avars[3][5]][31] = 2
            screen.blit(presin, [0, 0])
            screen.blit(grad, [0, 26])
            spr, mfs = gradani()
            screen.blit(pygame.transform.flip(mfsps[mfs], 1, 0), [87, 98])
            screen.blit(asprs[avars[3][5]][spr], [129, 106])
        elif avars[avars[3][5]][1] == 3:
            screen.blit(schoolen, [0, 0])
        else:
            screen.blit(textbox, [0, 24])
            screen.blit((fnt.render("JUMP ROPE", 1, (0, 0, 100))), [8, 34])
            screen.blit((fnt.render("STATUES", 1, (0, 0, 100))), [8, 50])
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
                    clt = 0
                    if 138 < mp[1] < 158 and cret:
                        if 228 < mp[0] < 240:
                            pygame.mixer.stop()
                            sound[4].play()
                            return(avars, ret)
                        elif 212 < mp[0] < 224:
                            pygame.mixer.stop()
                            sound[4].play()
                            ret = 0
                            return(avars, ret)
                    if not bx and (24 < mp[1] < 136 and 0 < mp[0] < 240):
                        pygame.mixer.stop()
                        sound[3].play()
                        bx = True
                    elif bx and avars[avars[3][5]][1] == 2:
                        if (32 < mp[1] < 48) and (8 < mp[0] < 116):
                            avars, ret = jumprope.game(avars, asprs, screen, pchr1, psps1, pchr2, psps2, pchr3, psps3, mfsps)
                            cret = 0
                            anifr = 19
                            if ret:
                                return(avars, ret)
                        elif (48 < mp[1] < 64) and (8 < mp[0] < 98):
                            avars, ret = statues.game(avars, asprs, screen, pchr1, psps1, pchr2, psps2, pchr3, psps3, mfsps)
                            cret = 0
                            anifr = 19
                            if ret:
                                return(avars, ret)
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
                return(avars)
            chngsts = False
        if anifr < 23:
            anifr += 1
        else:
            anifr = 0
            cret = 1
            ret = 1
        if clt > 29:
            return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

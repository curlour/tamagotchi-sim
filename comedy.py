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

    scr = 0

    ret = 1
    spret = 0

    act = -1
    typ = randint(0, 1)

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

    tutimg = pygame.image.load("Sprites/Misc/bg/comedyt.png").convert()

    playbk = pygame.image.load("Sprites/Misc/bg/comedy.png").convert()

    poof = pygame.image.load("Sprites/Misc/obj/poof.png").convert()

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    pals = chsprs(choice([223, 224, 235, 236, 253, 254, 355, 365, 366]), 0, 65536)
    fan = pygame.transform.flip(pygame.image.load("Sprites/Misc/obj/fan2.png").convert(), 1, 0)

    emo = [pygame.image.load("Sprites/Misc/emo/heart.png").convert(),
           pygame.image.load("Sprites/Misc/emo/em.png").convert(),
           pygame.image.load("Sprites/Misc/emo/qm.png").convert(),
           pygame.image.load("Sprites/Misc/emo/conf.png").convert(),
           pygame.image.load("Sprites/Misc/emo/ang.png").convert(),
           pygame.image.load("Sprites/Misc/emo/music1.png").convert(),
           pygame.image.load("Sprites/Misc/emo/happy.png").convert()]

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
            if end == 0:
                spr = 11 + (anifr % 12 > 5)
                psp = 11 + (anifr % 12 < 6)
            if end == 1:
                if anifr < 12:
                    spr, psp = 6, 6
                    screen.blit(emo[2], [112, 90])
                elif anifr < 24:
                    spr = 9
                    psp = [10, 5][typ]
                    screen.blit(emo[typ], [112, 90])
                else:
                    if typ == act:
                        spr = [5, 8][act]
                        psp = [5, 9][act]
                        if act == 1:
                            screen.blit(fan, [96, 90])
                    else:
                        spr, psp = 7, 7
                    for i in range(15):
                        screen.blit(emo[3 + (2 * (typ == act)) + (i % 2)], [(16 * i), (32 + (16 * ((i % 2) == (anifr % 12 > 5))))])
            screen.blit(pygame.transform.flip(pals[psp], 1, 0), [80, 98])
            screen.blit(asprs[avars[3][5]][spr], [128, 98])
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
                    mntxt = fnt.render(str(scr * 125), 1, (0, 0, 100))
                    screen.blit(mntxt, [(138 - (mntxt.get_width())), 74])
                    screen.blit(coin, [138, 72])
                    if scr > 0:
                        spr = 5
                    else:
                        spr = 6
                screen.blit(asprs[avars[3][5]][spr], [(124 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            elif end == 4:
                if scr < 8:
                    screen.blit(toobad, [71, 48])
                    sy = 98
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 6
                    else:
                        spr = 7
                        screen.blit(cry, [56, 90])
                else:
                    if scr < 16:
                        screen.blit(good, [94, 48])
                    elif scr < 24:
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
                screen.blit(playbk, [0, 0])
                if anifr < 6:
                    screen.blit(asprs[avars[3][5]][5], [104, 98])
                    screen.blit(pals[5], [144, 98])
                else:
                    screen.blit(poof, [104, 98])
                    screen.blit(pals[9], [144, 98])
                for i in range(15):
                    screen.blit(emo[5 + (i % 2)], [(16 * i), (32 + (16 * ((i % 2) == (anifr % 12 > 5))))])
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
                if pb in [1, 3] and (24 < mp[1] < 136) and end == 1 and anifr < 24:
                    act = pb // 2
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
        if anifr < (23 + (12 * (end == 1))):
            anifr += 1
            if end == 1 and anifr == 24:
                pygame.mixer.stop()
                sound[12 - (3 * (typ == act))].play()
        else:
            anifr = 0
            if strt:
                play = True
                strt = False
            elif play:
                if end == 0:
                    end = 1
                    pygame.mixer.stop()
                    sound[2].play()
                else:
                    if typ == act:
                        end = 0
                        scr += 1
                        act = -1
                        typ = randint(0, 1)
                    if end == 1 or scr == 24:
                        end = 3
                        play = False
                        if (avars[3][2] + (scr * 125)) < 99999:
                            avars[3][2] += (scr * 125)
                        else:
                            avars[3][2] = 99999
                        avars[avars[3][5]][8] += scr
            elif end == 3:
                if scr < 24 or avars[avars[3][5]][15] != 253 or avars[avars[3][5]][8] < 1000:
                    if scr < 8:
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

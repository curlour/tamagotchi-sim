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

    gmprt = 0

    sec = []

    dopt = (pygame.image.load("Sprites/Misc/bg/ddown.png").convert(), pygame.image.load("Sprites/Misc/bg/dleft.png").convert(),
            pygame.image.load("Sprites/Misc/bg/dright.png").convert(), pygame.image.load("Sprites/Misc/bg/dup.png").convert())

    tprs = 0

    prsb = 4
    dwin = 0

    tuts = True
    strt = False
    play = False
    end = 0

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

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    tutimg = pygame.image.load("Sprites/Misc/bg/dancet.png").convert()

    gamebk = pygame.image.load("Sprites/Misc/bg/gamecenter.png").convert()

    playbk = pygame.image.load("Sprites/Misc/bg/dance.png").convert()

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    readyb = pygame.image.load("Sprites/Misc/bg/readyb.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()
    gob = pygame.image.load("Sprites/Misc/bg/gob.png").convert()

    toobad = pygame.image.load("Sprites/Misc/bg/toobad.png").convert()
    good = pygame.image.load("Sprites/Misc/bg/good.png").convert()
    great = pygame.image.load("Sprites/Misc/bg/great.png").convert()
    excellent = pygame.image.load("Sprites/Misc/bg/excellent.png").convert()

    win = pygame.image.load("Sprites/Misc/emo/happy.png").convert()
    cry = pygame.image.load("Sprites/Misc/emo/cry.png").convert()

    con1 = pygame.image.load("Sprites/Misc/bg/congrt1.png").convert()
    con2 = pygame.image.load("Sprites/Misc/bg/congrt2.png").convert()
    con3 = pygame.image.load("Sprites/Misc/bg/congrt3.png").convert()

    money = pygame.image.load("Sprites/Misc/obj/money.png").convert()
    coin = pygame.image.load("Sprites/Misc/menu/gotchipt.png").convert()

    dw = pygame.image.load("Sprites/Misc/bg/dwrong.png").convert()
    dc = pygame.image.load("Sprites/Misc/bg/dcorrect.png").convert()

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

    sndsec = [11, 4, 6, 9]

    while kr:
        if tuts:
            screen.blit(tutimg, [0, 0])
        elif strt:
            screen.blit(gamebk, [0, 0])
            if anifr == 16:
                pygame.mixer.stop()
                sound[11].play()
            if anifr < 16:
                screen.blit(readyb, [0, 0])
                screen.blit(ready, [80, 48])
                spr = 3
            else:
                screen.blit(gob, [0, 0])
                screen.blit(go, [95, 48])
                spr = 5
            screen.blit(asprs[avars[3][5]][spr], [(104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
        elif play:
            screen.blit(playbk, [0, 0])
            screen.blit((fnt.render((str(scr)), 1, (0, 0, 100))), [56, 48])
            if gmprt == 0:
                spr = 3
                sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                spry = 84 + (32 - asprs[avars[3][5]][spr].get_height())
                if anifr == 0:
                    for i in range(4):
                        a = choice(dopt)
                        sec.append(a)
                if anifr % 6 < 4:
                    screen.blit(sec[(anifr // 6)], [100, 46])
            if gmprt == 1:
                if tprs > 0:
                    if prsb != 4:
                        screen.blit(sec[(tprs - 1)], [100, 46])
                        if prsb == 3:
                            spr = 5
                            sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                            spry = 76 + (32 - asprs[avars[3][5]][spr].get_height())
                        elif prsb == 0:
                            spr = 9
                            sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
                        elif prsb == 2:
                            spr = 15
                            sprx = 132 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                            spry = 84 + (32 - asprs[avars[3][5]][spr].get_height())
                        elif prsb == 1:
                            spr = 11
                            sprx = 76 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                            spry = 84 + (32 - asprs[avars[3][5]][spr].get_height())
                    else:
                        sprx = 104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
                        spry = 84 + (32 - asprs[avars[3][5]][spr].get_height())
                        if dwin == 0:
                            screen.blit(dw, [100, 46])
                            spr = 7
                        elif dwin == 2:
                            screen.blit(dc, [100, 46])
                            spr = 5
                        else:
                            spr = 3
                else:
                    spr = 3
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], (spr == 15), 0), [sprx, spry])
        else:
            screen.blit(gamebk, [0, 0])
            if end == 3:
                screen.blit(money, [88, 106])
                if anifr < 8:
                    spr = 11
                else:
                    if anifr == 8:
                        pygame.mixer.stop()
                        sound[13].play()
                    screen.blit(textbox, [94, 64])
                    mntxt = fnt.render(str(scr * 20), 1, (0, 0, 100))
                    screen.blit(mntxt, [(134 - (mntxt.get_width())), 74])
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
                if anifr < 12:
                    screen.blit(con1, [0, 24])
                    spr = 3
                elif anifr < 16:
                    screen.blit(con2, [0, 24])
                    spr = 9
                else:
                    screen.blit(con3, [0, 24])
                    spr = 10
                screen.blit(asprs[avars[3][5]][spr], [(104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
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
                if gmprt == 0:
                    gmprt = 1
                    dwin = 1
                elif tprs < 4 and dwin == 1:
                    tprs += 1
                    p = pygame.mouse.get_pos()
                    d = (screen.get_size()[0] // 240)
                    p = ((p[0] // d), (p[1] // d))
                    prsb = (2 * ((2 * p[0]) > (3 * p[1]))) + ((480 - (2 * p[0])) > (3 * p[1]))
                    pygame.mixer.stop()
                    sound[sndsec[prsb]].play()
                    if dopt[prsb] != sec[(tprs - 1)]:
                        dwin = 0
                    elif tprs == 4:
                        dwin = 2
                elif prsb < 4:
                    prsb = 4
                else:
                    if dwin == 0:
                        end = 1
                    elif dwin == 2:
                        scr += 1
                        if scr < 6:
                            gmprt = 0
                            tprs = 0
                            sec = []
                        else:
                            end = 1
            if end == 1:
                play = False
                end = 3
                if (avars[avars[3][5]][17] + (scr // 2)) < 6:
                    avars[avars[3][5]][17] += (scr // 2)
                else:
                    avars[avars[3][5]][17] = 6
                if (avars[3][2] + (scr * 20)) < 99999:
                    avars[3][2] += (scr * 20)
                else:
                    avars[3][2] = 99999
                if (avars[avars[3][5]][18] - (scr // 2)) > 1:
                    avars[avars[3][5]][18] -= (scr // 2)
                else:
                    avars[avars[3][5]][18] = 1
                avars[avars[3][5]][6] += (scr // 2)
            elif end == 3:
                if scr < 6:
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
                end = 4
            elif end == 4:
                ret = 0
                return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

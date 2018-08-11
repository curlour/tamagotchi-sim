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

    gpos = 0

    chh = 0

    ret = 1

    clk = False

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

    tutimg = pygame.image.load("Sprites/Misc/bg/whackafoolt.png").convert()

    gamebk = pygame.image.load("Sprites/Misc/bg/gamecenter.png").convert()

    fan1 = pygame.image.load("Sprites/Misc/obj/fan1.png").convert()
    fan2 = pygame.image.load("Sprites/Misc/obj/fan2.png").convert()

    fool1 = pygame.image.load("Sprites/Misc/obj/fool1.png").convert()
    fool2 = pygame.image.load("Sprites/Misc/obj/fool2.png").convert()

    poop1 = pygame.image.load("Sprites/Misc/obj/poop1.png").convert()
    poop2 = pygame.image.load("Sprites/Misc/obj/poop2.png").convert()

    playbk = pygame.image.load("Sprites/Misc/bg/whackafool.png").convert()

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

    sprlst = pygame.sprite.Group()

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
            if anifr > 3:
                if objl[0] < 16:
                    if gpos == 2 and chh == objl[0]:
                        screen.blit(fool2, [(66 + (28 * (4 * ((objl[0] / 4) - (objl[0] // 4))))), (40 + (24 * (objl[0] // 4)))])
                    else:
                        screen.blit(fool1, [(66 + (28 * (4 * ((objl[0] / 4) - (objl[0] // 4))))), (40 + (24 * (objl[0] // 4)))])
                if objl[1] < 16:
                    if gpos == 2 and chh == objl[1]:
                        screen.blit(fool2, [(66 + (28 * (4 * ((objl[1] / 4) - (objl[1] // 4))))), (40 + (24 * (objl[1] // 4)))])
                    else:
                        screen.blit(fool1, [(66 + (28 * (4 * ((objl[1] / 4) - (objl[1] // 4))))), (40 + (24 * (objl[1] // 4)))])
                if objl[2] < 16:
                    if gpos == 3 and chh == objl[2]:
                        screen.blit(poop2, [(66 + (28 * (4 * ((objl[2] / 4) - (objl[2] // 4))))), (40 + (24 * (objl[2] // 4)))])
                    else:
                        screen.blit(poop1, [(66 + (28 * (4 * ((objl[2] / 4) - (objl[2] // 4))))), (40 + (24 * (objl[2] // 4)))])
                if objl[3] < 16:
                    if gpos == 3 and chh == objl[3]:
                        screen.blit(poop2, [(66 + (28 * (4 * ((objl[3] / 4) - (objl[3] // 4))))), (40 + (24 * (objl[3] // 4)))])
                    else:
                        screen.blit(poop1, [(66 + (28 * (4 * ((objl[3] / 4) - (objl[3] // 4))))), (40 + (24 * (objl[3] // 4)))])
                if objl[4] < 16:
                    if gpos == 3 and chh == objl[4]:
                        screen.blit(poop2, [(66 + (28 * (4 * ((objl[4] / 4) - (objl[4] // 4))))), (40 + (24 * (objl[4] // 4)))])
                    else:
                        screen.blit(poop1, [(66 + (28 * (4 * ((objl[4] / 4) - (objl[4] // 4))))), (40 + (24 * (objl[4] // 4)))])
            if gpos == 0:
                spr = 3
                sprx = 30
                fanx = 6
            elif gpos == 1:
                spr = 13
                sprx = 30 + (((42 + (28 * (4 * ((chh / 4) - (chh // 4))))) - 30) // 2)
                spry = spry + (((((32 + (24 * (chh // 4))))) - spry) // 2)
                fanx = 6 + (((42 + (28 * (4 * ((chh / 4) - (chh // 4))))) - 30) // 2)
                fany = spry + (((((40 + (24 * (chh // 4))))) - spry) // 2)
                if chh in objl:
                    if objl.index(chh) < 2:
                        gpos = 2
                        pygame.mixer.stop()
                        sound[6].play()
                    else:
                        gpos = 3
                        anifr = 17
                        pygame.mixer.stop()
                        sound[6].play()
                else:
                    gpos = 3
                    anifr = 17
            elif gpos == 2:
                spr = 5
                if chh in objl:
                    sprx = 42 + (28 * (4 * ((chh / 4) - (chh // 4))))
                    spry = 32 + (24 * (chh // 4))
                    fanx = 66 + (28 * (4 * ((chh / 4) - (chh // 4))))
                    fany = 40 + (24 * (chh // 4))
                    objl[objl.index(chh)] = 16
                else:
                    gpos = 4
                    if objl.count(16) == 2:
                        anifr = 0
                        scr += 1
            elif gpos == 3:
                spr = 9
                sprx = 42 + (28 * (4 * ((chh / 4) - (chh // 4))))
                spry = 32 + (24 * (chh // 4))
                fanx = 66 + (28 * (4 * ((chh / 4) - (chh // 4))))
                fany = 40 + (24 * (chh // 4))
            else:
                spr = 13
                sprx = 30 + ((sprx - 30) // 2)
                fanx = 62 + ((fanx - 30) // 2)
                gpos = 0
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], (gpos > 0 or sprx == 30), 0), [(sprx + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (spry + (32 - asprs[avars[3][5]][spr].get_height()))])
            if gpos == 2 or gpos == 3:
                screen.blit(fan2, [fanx, fany])
            else:
                screen.blit(fan1, [fanx, fany])
            screen.blit((fnt.render(("%02d" % scr), 1, (0, 0, 100))), [219, 64])
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
                    mntxt = fnt.render(str(scr * 10), 1, (0, 0, 100))
                    screen.blit(mntxt, [(134 - (mntxt.get_width())), 74])
                    screen.blit(coin, [138, 72])
                    if scr > 0:
                        spr = 5
                    else:
                        spr = 6
                screen.blit(asprs[avars[3][5]][spr], [(124 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            elif end == 4:
                if scr < 4:
                    screen.blit(toobad, [71, 48])
                    sy = 98
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 6
                    else:
                        spr = 7
                        screen.blit(cry, [56, 90])
                else:
                    if scr < 8:
                        screen.blit(good, [94, 48])
                    elif scr < 12:
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
                    elif 64 < mp[0] < 176 and 40 < mp[1] < 136 and gpos == 0 and play:
                        chh = (4 * ((mp[1] - 40) // 24)) + ((mp[0] - 64) // 28)
                        gpos = 1
                        if objl.count(16) == 1:
                            anifr = 6
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
            if play:
                if anifr == 4:
                    if scr < 12:
                        a = randint(0, 15)
                        b = a
                        while b == a:
                            b = randint(0, 15)
                        c = a
                        while c == a or c == b:
                            c = randint(0, 15)
                        d = a
                        while d == a or d == b or d == c:
                            d = randint(0, 15)
                        e = a
                        while e == a or e == b or e == c or e == d:
                            e = randint(0, 15)
                        f = a
                        while f == a or f == b or f == c or f == d or f == e:
                            f = randint(0, 15)
                        objl = [a, b, c, d, e, f]
                    else:
                        objl = [16, 16, 16, 16, 16, 16]
                        anifr = 23
        else:
            anifr = 0
            if strt:
                play = True
                objl = [16, 16, 16, 16, 16]
                strt = False
                spry = 80
                fany = 88
            elif play:
                play = False
                end = 3
                if (avars[avars[3][5]][17] + (scr // 4)) < 6:
                    avars[avars[3][5]][17] += (scr // 4)
                else:
                    avars[avars[3][5]][17] = 6
                if (avars[3][2] + (scr * 10)) < 99999:
                    avars[3][2] += (scr * 10)
                else:
                    avars[3][2] = 99999
                if (avars[avars[3][5]][18] - (scr // 4)) > 1:
                    avars[avars[3][5]][18] -= (scr // 4)
                else:
                    avars[avars[3][5]][18] = 1
                avars[avars[3][5]][8] += (scr // 4)
            elif end == 3:
                if scr < 12:
                    if scr < 4:
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
        if play:
            clock.tick(8)
        else:
            clock.tick(16)
        pygame.display.update()

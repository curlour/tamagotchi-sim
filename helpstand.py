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

    chpos = 0

    cos1 = []
    cos2= []

    tuts = True
    strt = False
    play = False
    end = 0

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

    tutimg = pygame.image.load("Sprites/Misc/bg/helpstandt.png").convert()

    gamebk = pygame.image.load("Sprites/Misc/bg/gamecenter.png").convert()

    playbk = pygame.image.load("Sprites/Misc/bg/helpstand.png").convert()

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

    ball = pygame.image.load("Sprites/Misc/item/ball.png").convert()
    s = pygame.image.load("Sprites/Food/IceCream.png").convert()
    icec = pygame.Surface([24, 24]).convert()
    icec.fill((0, 255, 255))
    icec.blit(s, [0, 0])
    icec.set_colorkey((0, 255, 255))
    balli = pygame.image.load("Sprites/Misc/bg/hsab.png").convert()
    iceci = pygame.image.load("Sprites/Misc/bg/hsai.png").convert()

    obj = [icec, ball]

    obji = [iceci, balli]

    msprs = []
    s = pygame.image.load("Sprites/NPC/Market.png").convert()
    for i in range(4):
        a = pygame.Surface([32, 32]).convert()
        a.fill((0, 255, 255))
        a.blit(s, [-(32 * (i % 2)), -(32 * (i // 2))])
        a.set_colorkey((0, 255, 255))
        msprs.append(a)

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
            if len(cos2) > 0:
                if cos2[2] == 114:
                    if chpos < 2:
                        if anifr < 4:
                            cos2s = 12
                            screen.blit(obji[cos2[1]], [122, 80])
                        else:
                            cos2s = 11
                    elif chpos == 2:
                        cos2s = 5
                    else:
                        cos2s = 8
                else:
                    if ((anifr / 8) - (anifr // 8)) < 0.5:
                        cos2s = 11
                    else:
                        cos2s = 13
                screen.blit(pygame.transform.flip(cos2sp[cos2s], (cos2[2] != 114 and cos2[4] == 1), 0), [(cos2[2] + ((32 - cos2sp[cos2s].get_width()) // 2)), (cos2[3] + (32 - cos2sp[cos2s].get_height()))])
            if len(cos1) > 0:
                if cos1[2] == 114:
                    if chpos < 2:
                        if anifr < 4:
                            cos1s = 12
                            screen.blit(obji[cos1[1]], [122, 80])
                        else:
                            cos1s = 11
                    elif chpos == 2:
                        cos1s = 5
                    else:
                        cos1s = 8
                else:
                    if ((anifr / 8) - (anifr // 8)) < 0.5:
                        cos1s = 11
                    else:
                        cos1s = 13
                screen.blit(pygame.transform.flip(cos1sp[cos1s], (cos1[2] != 114 and cos1[4] == 1), 0), [(cos1[2] + ((32 - cos1sp[cos1s].get_width()) // 2)), (cos1[3] + (32 - cos1sp[cos1s].get_height()))])
            if chpos == 0:
                spr = 11
                mspr = 0
            elif chpos == 1:
                if anifr == 19:
                    pygame.mixer.stop()
                    sound[9].play()
                    chpos = 2
                    scr += 1
                spr = 12
                mspr = 1
                if len(cos1) > 0:
                    screen.blit(obj[cos1[1]], [56, 80])
                elif len(cos2) > 0:
                    screen.blit(obj[cos2[1]], [56, 80])
            elif chpos == 2:
                spr = 5
                mspr = 2
                if len(cos1) > 0:
                    screen.blit(obj[cos1[1]], [98, 80])
                elif len(cos2) > 0:
                    screen.blit(obj[cos2[1]], [98, 80])
            else:
                spr = 7
                mspr = 3
            screen.blit(msprs[mspr], [16, 98])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], (spr != 12), 0), [(74 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit((fnt.render(("%02d" % scr), 1, (0, 0, 100))), [48, 31])
        else:
            screen.blit(gamebk, [0, 0])
            if end == 3:
                screen.blit(money, [88, 106])
                if anifr < 8:
                    if anifr == 0:
                        if (avars[avars[3][5]][17] + (scr // 4)) < 6:
                            avars[avars[3][5]][17] += (scr // 4)
                        else:
                            avars[avars[3][5]][17] = 6
                        if (avars[3][2] + (scr * 10)) < 99999:
                            avars[3][2] += (scr * 10)
                        else:
                            avars[3][2] = 99999
                        avars[avars[3][5]][7] += (scr // 4)
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
                if len(cos1) > 0 and 100 < mp[1] < 132 and 114 < mp[0] < 146 and chpos == 0:
                    if (pb == 1 and cos1[1] == 0) or (pb == 3 and cos1[1] == 1):
                        chpos = 1
                        anifr = 15
                    elif (pb == 1 and cos1[1] == 1) or (pb == 3 and cos1[1] == 0):
                        pygame.mixer.stop()
                        sound[12].play()
                        chpos = 3
                        anifr = 15
                if len(cos2) > 0 and 90 < mp[1] < 122 and 114 < mp[0] < 146 and chpos == 0:
                    if (pb == 1 and cos2[1] == 0) or (pb == 3 and cos2[1] == 1):
                        chpos = 1
                        anifr = 15
                    elif (pb == 1 and cos2[1] == 1) or (pb == 3 and cos2[1] == 0):
                        pygame.mixer.stop()
                        sound[12].play()
                        chpos = 3
                        anifr = 15
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
                if end == 0:
                    if ((anifr / 4) - (anifr // 4)) == 0:
                        if len(cos1) > 0 and cos1[(len(cos1) // 2)] > 114:
                            cos1[2] += ((36 * cos1[4]) - 18)
                        if len(cos2) > 0 and cos2[(len(cos2) // 2)] > 114:
                            cos2[2] += ((36 * cos2[4]) - 18)
        else:
            anifr = 0
            if strt:
                play = True
                strt = False
            elif play:
                if len(cos1) == 0:
                    if len(cos2) == 0:
                        cos1 = [(randint(1, 132)), (randint(0, 1)), 208, 100, 0]
                        cos1sp = chsprs(cos1[0])
                    elif cos2[2] == 114:
                        if chpos == 0:
                            chpos = 3
                            anifr = 16
                        elif chpos == 2:
                            chpos = 0
                            cos2[4] = 1
                            cos2[2] += 18
                            if scr < 12:
                                cos1 = [(randint(1, 132)), (randint(0, 1)), 208, 100, 0]
                                cos1sp = chsprs(cos1[0])
                        else:
                            play = False
                            end = 3
                    else:
                        play = False
                        end = 3
                else:
                    if cos1[2] == 114:
                        if chpos == 0:
                            chpos = 3
                            anifr = 16
                        elif chpos == 2:
                            chpos = 0
                            cos1[4] = 1
                            cos1[2] += 18
                            cos2 = [(randint(1, 132)), (randint(0, 1)), 208, 90, 0]
                            cos2sp = chsprs(cos2[0])
                        else:
                            play = False
                            end = 3
                    elif cos1[4]:
                        cos1 = []
                        cos2[2] = 114
                    else:
                        cos1[2] = 114
                        if len(cos2) > 0:
                            cos2 = []
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
        clock.tick(16)
        pygame.display.update()

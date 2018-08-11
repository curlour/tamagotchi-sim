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

    class Card(pygame.sprite.Sprite):

        crdfr = []

        def __init__(self):
            super().__init__()

            image = pygame.image.load("Sprites\Misc\card\c1.png").convert()
            self.crdfr.append(image)
            image = pygame.image.load("Sprites\Misc\card\c2.png").convert()
            self.crdfr.append(image)
            image = pygame.image.load("Sprites\Misc\card\c3.png").convert()
            self.crdfr.append(image)
            image = pygame.image.load("Sprites\Misc\card\c4.png").convert()
            self.crdfr.append(image)
            image = pygame.image.load("Sprites\Misc\card\c5.png").convert()
            self.crdfr.append(image)
            
            self.image = self.crdfr[0]
            self.rect = self.image.get_rect()

        def update(self):
            self.image = self.crdfr[cfr]
    
    kr = True

    chngsts = False

    scr = 0

    ret = 1

    gmprt = 0

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

    tutimg = pygame.image.load("Sprites/Misc/bg/cardshut.png").convert()

    gamebk = pygame.image.load("Sprites/Misc/bg/gamecenter.png").convert()

    playbk = pygame.image.load("Sprites/Misc/bg/cards.png").convert()

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

    poo = pygame.image.load("Sprites/Misc/poo/spoo1.png").convert()

    con1 = pygame.image.load("Sprites/Misc/bg/congrt1.png").convert()
    con2 = pygame.image.load("Sprites/Misc/bg/congrt2.png").convert()
    con3 = pygame.image.load("Sprites/Misc/bg/congrt3.png").convert()

    crdd = pygame.image.load("Sprites/Misc/card/c1.png").convert()
    crdu = pygame.image.load("Sprites/Misc/card/c5.png").convert()
    poof = pygame.image.load("Sprites/Misc/obj/poof.png").convert()

    xlst = (24, 56, 88, 128, 160, 192)

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

    cha = asprs[avars[3][5]][1]

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
            if gmprt == 0:
                if anifr < 8:
                    if anifr < 4:
                        spr = 9
                        screen.blit(asprs[avars[3][5]][spr], [(52 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (76 + ((32 - asprs[avars[3][5]][spr].get_height()) // 2))])
                    else:
                        screen.blit(poof, [52, 76])
                elif anifr < 10:
                    cfr = anifr - 6
                    crdn = 0
                    while crdn < 24:
                        crd1 = Card()
                        crd1.rect.x = xlst[(crdn - (6 * (crdn // 6)))]
                        crd1.rect.y = 32 + (24 * (crdn // 6))
                        sprlst.add(crd1)
                        sprlst.update()
                        sprlst.draw(screen)
                        sprlst.empty()
                        crdn += 1
                    screen.blit(crdu, [56, 80])
                    screen.blit(cha, [(60 + ((16 - cha.get_width()) // 2)), (84 + ((16 - cha.get_height()) // 2))])
                elif anifr < 16:
                    crdn = 0
                    while crdn < 24:
                        screen.blit(crdu, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                    crdn = 0
                    while crdn < 24:
                        screen.blit(poo, [(xlst[(crdn - (6 * (crdn // 6)))] + 4), (36 + (24 * (crdn // 6)))])
                        crdn += 1
                    screen.blit(crdu, [56, 80])
                    screen.blit(cha, [(60 + ((16 - cha.get_width()) // 2)), (84 + ((16 - cha.get_height()) // 2))])
                elif anifr < 19:
                    cfr = 19 - anifr
                    crdn = 0
                    while crdn < 24:
                        crd1 = Card()
                        crd1.rect.x = xlst[(crdn - (6 * (crdn // 6)))]
                        crd1.rect.y = 32 + (24 * (crdn // 6))
                        sprlst.add(crd1)
                        sprlst.update()
                        sprlst.draw(screen)
                        sprlst.empty()
                        crdn += 1
                else:
                    crdn = 0
                    while crdn < 24:
                        screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                    if anifr == 23:
                        gmprt = 1
                        ccrd = 13
            elif gmprt == 1:
                if (((anifr - 1) / 3) - ((anifr - 1) // 3)) == 0:
                    c1 = ccrd
                    if c1 == 0:
                        c2 = randint((c1 + 1), 23)
                    elif c1 == 23:
                        c2 = randint(0, (c1 - 1))
                    else:
                        c2 = choice((randint(0, (c1 - 1)), randint((c1 + 1), 23)))
                    ccrd = c2
                    cl = [c1, c2]
                    cl.sort()
                    crdn = 0
                    while crdn < cl[0]:
                        screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                    crdn += 1
                    while crdn < cl[1]:
                        screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                    crdn += 1
                    while crdn < 24:
                        screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                    screen.blit(crdd, [(((xlst[(c1 - (6 * (c1 // 6)))]) + (xlst[(c2 - (6 * (c2 // 6)))])) // 2), (((32 + (24 * (c1 // 6))) + (32 + (24 * (c2 // 6)))) // 2)])
                else:
                    crdn = 0
                    while crdn < 24:
                        screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                    if anifr == 23:
                        gmprt = 2
            elif gmprt == 2:
                crdn = 0
                while crdn < 24:
                    screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                    crdn += 1
            elif gmprt == 3:
                crdn = 0
                if anifr < 12:
                    while crdn < chcrd:
                        screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                    crdn += 1
                    while crdn < 24:
                        screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                elif anifr < 16:
                    while crdn < ccrd:
                        screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                    crdn += 1
                    while crdn < 24:
                        screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                        crdn += 1
                if anifr < 3:
                    cfr = anifr + 1
                    crd1 = Card()
                    crd1.rect.x = xlst[(chcrd - (6 * (chcrd // 6)))]
                    crd1.rect.y = 32 + (24 * (chcrd // 6))
                    sprlst.add(crd1)
                    sprlst.update()
                    sprlst.draw(screen)
                    sprlst.empty()
                elif anifr < 12:
                    screen.blit(crdu, [xlst[(chcrd - (6 * (chcrd // 6)))], (32 + (24 * (chcrd // 6)))])
                    if chcrd == ccrd:
                        screen.blit(cha, [((xlst[(chcrd - (6 * (chcrd // 6)))] + 4) + ((16 - cha.get_width()) // 2)), ((36 + (24 * (chcrd // 6))) + ((16 - cha.get_height()) // 2))])
                    else:
                        screen.blit(poo, [(xlst[(chcrd - (6 * (chcrd // 6)))] + 4), (36 + (24 * (chcrd // 6)))])
                elif anifr < 16:
                    if anifr < 14:
                        screen.blit(poof, [(xlst[(ccrd - (6 * (ccrd // 6)))] - 4), (28 + (24 * (ccrd // 6)))])
                    else:
                        if chcrd == ccrd:
                            spr = 5
                        else:
                            spr = 8
                        screen.blit(asprs[avars[3][5]][spr], [((xlst[(ccrd - (6 * (ccrd // 6)))] - 4) + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), ((28 + (24 * (ccrd // 6))) + ((32 - asprs[avars[3][5]][spr].get_height()) // 2))])
                    if chcrd != ccrd:
                        screen.blit(crdu, [xlst[(chcrd - (6 * (chcrd // 6)))], (32 + (24 * (chcrd // 6)))])
                        screen.blit(poo, [(xlst[(chcrd - (6 * (chcrd // 6)))] + 4), (36 + (24 * (chcrd // 6)))])
                    if anifr == 15:
                        if chcrd == ccrd:
                            scr += 1
                            if scr == 6:
                                end = 1
                        else:
                            end = 1
                else:
                    if end == 1:
                        crdn = 0
                        if anifr < 18:
                            while crdn < ccrd:
                                screen.blit(poof, [(xlst[(crdn - (6 * (crdn // 6)))] - 4), (28 + (24 * (crdn // 6)))])
                                crdn += 1
                            crdn += 1
                            while crdn < 24:
                                screen.blit(poof, [(xlst[(crdn - (6 * (crdn // 6)))] - 4), (28 + (24 * (crdn // 6)))])
                                crdn += 1
                        if chcrd == ccrd:
                            spr = 5
                        else:
                            spr = 8
                        screen.blit(asprs[avars[3][5]][spr], [((xlst[(ccrd - (6 * (ccrd // 6)))] - 4) + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), ((28 + (24 * (ccrd // 6))) + ((32 - asprs[avars[3][5]][spr].get_height()) // 2))])
                    else:
                        while crdn < ccrd:
                            screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                            crdn += 1
                        crdn += 1
                        while crdn < 24:
                            screen.blit(crdd, [xlst[(crdn - (6 * (crdn // 6)))], (32 + (24 * (crdn // 6)))])
                            crdn += 1
                        if anifr < 18:
                            screen.blit(poof, [(xlst[(chcrd - (6 * (chcrd // 6)))] - 4), (28 + (24 * (chcrd // 6)))])
                        elif anifr < 20:
                            screen.blit(crdu, [xlst[(chcrd - (6 * (chcrd // 6)))], (32 + (24 * (chcrd // 6)))])
                            screen.blit(cha, [((xlst[(chcrd - (6 * (chcrd // 6)))] + 4) + ((16 - cha.get_width()) // 2)), ((36 + (24 * (chcrd // 6))) + ((16 - cha.get_height()) // 2))])
                        else:
                            cfr = 23 - anifr
                            crd1 = Card()
                            crd1.rect.x = xlst[(chcrd - (6 * (chcrd // 6)))]
                            crd1.rect.y = 32 + (24 * (chcrd // 6))
                            sprlst.add(crd1)
                            sprlst.update()
                            sprlst.draw(screen)
                            sprlst.empty()
                        if anifr == 23:
                            gmprt = 1
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
                    if gmprt == 2:
                        if 32 < mp[1] < 128:
                            a = 6 * ((mp[1] - 32) // 24)
                            b = -1
                            if 20 < mp[0] < 116:
                                b = (mp[0] - 20) // 32
                            elif 124 < mp[0] < 220:
                                b = ((mp[0] - 124) // 32) + 3
                            if b > -1:
                                chcrd = a + b
                                gmprt = 3
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
                avars[avars[3][5]][5] += (scr // 2)
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

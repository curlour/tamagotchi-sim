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

def game(avars, asprs, screen, fsprs, ywn):

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

    gmst = 0

    strt = True
    play = False

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

    def monani():
        if gmst < 2:
            if anifr % 12 < 6:
                spr = 3
                frs = 3
            else:
                spr = 4
                frs = 4
        else:
            if anifr < 12:
                spr = 11
                frs = 11
            else:
                spr = 7 - (2 * ywn)
                frs = 5 + (2 * ywn)
        return(spr, frs)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 4, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    lfnt = pygame.font.Font("Sprites/Misc/font/Tama1.ttf", 16)
    
    bck = pygame.image.load("Sprites/Misc/bg/congamesbg.png").convert()
    bck.blit(asprs[avars[3][5]][1], [(193 + ((16 - asprs[avars[3][5]][1].get_width()) // 2)), (69 + ((16 - asprs[avars[3][5]][1].get_height()) // 2))])
    bck.blit(fsprs[1], [(31 + ((16 - fsprs[1].get_width()) // 2)), (47 + ((16 - fsprs[1].get_height()) // 2))])

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    wint = pygame.image.load("Sprites/Misc/bg/win.png").convert()
    loset = pygame.image.load("Sprites/Misc/bg/lose.png").convert()

    money = pygame.image.load("Sprites/Misc/obj/money.png").convert()
    coin = pygame.image.load("Sprites/Misc/menu/gotchipt.png").convert()

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
        
    pygame.mixer.stop()
    sound[10].play()

    while kr:
        screen.blit(bck, [0, 0])
        if strt:
            if anifr == 16:
                pygame.mixer.stop()
                sound[11].play()
            if anifr < 16:
                screen.blit(ready, [80, 48])
                spr = 3
            else:
                screen.blit(go, [95, 48])
                spr = 5
            screen.blit(asprs[avars[3][5]][spr], [(136 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit(fsprs[spr], [(72 + ((32 - fsprs[spr].get_width()) // 2)), (98 + (32 - fsprs[spr].get_height()))])
        elif play:
            spr, frs = monani()
            if gmst == 0:
                screen.blit(money, [112, 102])
                screen.blit(money, [108, 106])
                screen.blit(coin, [(98 + (8 * (anifr % 12 > 5))), (90 + (8 * (anifr % 12 > 5)))])
                screen.blit(coin, [(132 - (8 * (anifr % 12 > 5))), (90 + (8 * (anifr % 12 > 5)))])
            elif gmst == 1:
                screen.blit(money, [(104 + (8 * (anifr % 12 < 6))), 106])
                screen.blit(money, [(112 - (8 * (anifr % 12 < 6))), 106])
            elif gmst == 2:
                screen.blit(money, [46, 106])
                screen.blit(money, [170, 106])
                if anifr > 11:
                    screen.blit(textbox, [52, 64])
                    mntxt = fnt.render(str((not ywn) * 200), 1, (0, 0, 100))
                    screen.blit(mntxt, [(92 - (mntxt.get_width())), 74])
                    screen.blit(coin, [96, 72])
                    screen.blit(textbox, [176, 64])
                    mntxt = fnt.render(str(ywn * 200), 1, (0, 0, 100))
                    screen.blit(mntxt, [(216 - (mntxt.get_width())), 74])
                    screen.blit(coin, [220, 72])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], gmst > 1, 0), [(148 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit(pygame.transform.flip(fsprs[frs], gmst < 2, 0), [(60 + ((32 - fsprs[frs].get_width()) // 2)), (98 + (32 - fsprs[frs].get_height()))])
        else:
            if ywn:
                screen.blit(wint, [78, 48])
            else:
                screen.blit(loset, [65, 48])
            if anifr % 12 < 6:
                spr = 6 - (2 *  ywn)
                frs = 4 + (2 *  ywn)
            else:
                spr = 7 - (2 *  ywn)
                frs = 5 + (2 *  ywn)
            screen.blit(asprs[avars[3][5]][spr], [(136 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            screen.blit(fsprs[frs], [(72 + ((32 - fsprs[frs].get_width()) // 2)), (98 + (32 - fsprs[frs].get_height()))])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
        for event in pygame.event.get():
            if event.type == QUIT:
                varsup.updtvrs(avars)
                kr = False
                pygame.quit()
                sys.exit()
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
            if play and gmst == 2 and anifr == 12:
                pygame.mixer.stop()
                sound[13].play()
        else:
            anifr = 0
            if strt:
                play = True
                strt = False
            elif play:
                if gmst < 2:
                    gmst += 1
                    if gmst == 2:
                        pygame.mixer.stop()
                        sound[9].play()
                else:
                    play = False
                    if ywn:
                        if (avars[3][2] + 100) < 99999:
                            avars[3][2] += 100
                        else:
                            avars[3][2] = 99999
                    else:
                        avars[3][2] -= 100
                    pygame.mixer.stop()
                    sound[14 - (13 * ywn)].play()
            else:
                return(avars)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

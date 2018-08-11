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
import maths
import gradient
import water
import clean
import acting
import wipe

def school(avars, asprs, screen):

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

    bx = avars[avars[3][5]][2] < 691200

    grad = avars[avars[3][5]][2] > 691199

    clt = 0

    skcls = 0

    tani = True

    chngsts = False

    scr = 0

    ret = 1
    cret = 1

    def teachersp(n):
        sprs = []
        s = pygame.image.load("Sprites/NPC/" + n + ".png").convert()
        for i in range(4):
            a = pygame.Surface([32, 32]).convert()
            a.fill((0, 255, 255))
            a.blit(s, [-(32 * (i % 2)), -(32 * (i // 2))])
            a.set_colorkey((0, 255, 255))
            sprs.append(a)
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

    classbk = [pygame.image.load("Sprites/Misc/bg/intclass.png").convert(),
               pygame.image.load("Sprites/Misc/bg/styclass.png").convert(),
               pygame.image.load("Sprites/Misc/bg/kndclass.png").convert(),
               pygame.image.load("Sprites/Misc/bg/humclass.png").convert(),
               pygame.image.load("Sprites/Misc/bg/gorclass.png").convert(),
               pygame.image.load("Sprites/Misc/bg/pasclass.png").convert()]

    classbkg = [[pygame.image.load("Sprites/Misc/bg/intclass1.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/intclass2.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/intclass3.png").convert()],
                [pygame.image.load("Sprites/Misc/bg/styclass1.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/styclass2.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/styclass3.png").convert()],
                [pygame.image.load("Sprites/Misc/bg/kndclass1.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/kndclass2.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/kndclass3.png").convert()],
                [pygame.image.load("Sprites/Misc/bg/humclass1.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/humclass2.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/humclass3.png").convert()],
                [pygame.image.load("Sprites/Misc/bg/gorclass1.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/gorclass2.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/gorclass3.png").convert()],
                [pygame.image.load("Sprites/Misc/bg/pasclass1.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/pasclass2.png").convert(),
                 pygame.image.load("Sprites/Misc/bg/pasclass3.png").convert()]]

    gradbg = pygame.image.load("Sprites/Misc/bg/schoolg.png").convert()
    gradl = pygame.image.load("Sprites/Misc/mail/joben.png").convert()

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

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

    intct = fnt.render("LOGIC", 1, (0, 128, 255))
    styct = fnt.render("ARTISTRY", 1, (255, 128, 51))
    kndct = fnt.render("KINDNESS", 1, (102, 255, 51))
    humct = fnt.render("HUMOUR", 1, (153, 128, 0))
    gorct = fnt.render("BEAUTY", 1, (0, 153, 128))
    pasct = fnt.render("PASSION", 1, (204, 0, 153))

    inti = pygame.image.load("Sprites/Misc/menu/inti.png").convert()
    styi = pygame.image.load("Sprites/Misc/menu/styi.png").convert()
    kndi = pygame.image.load("Sprites/Misc/menu/kndi.png").convert()
    humi = pygame.image.load("Sprites/Misc/menu/humi.png").convert()
    gori = pygame.image.load("Sprites/Misc/menu/gori.png").convert()
    pasi = pygame.image.load("Sprites/Misc/menu/pasi.png").convert()

    if avars[avars[3][5]][2] > 691199:
        tsprs = teachersp("Mimizu")
        avars[avars[3][5]][31] = 3

    teachn = [["MrTurtle", "ProfFlask", "MrRobomecha"],
              ["MsFlower", "MsMusicatchi", "MsModetchi"],
              ["MrCanvas", "MsHoutaiko", "Marutentchi"],
              ["MrFukuwarai", "MrKokuban", "Grippatchi"],
              ["MsBlonde", "Classictchi", "MrCombBowie"],
              ["MrKarate", "MrOkkana", "MrMicchi"]]

    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if avars[avars[3][5]][2] < 691200:
            if bx:
                screen.blit(textbox, [0, 24])
                screen.blit(intct, [8, 34])
                screen.blit(inti, [216, 32])
                screen.blit(styct, [8, 50])
                screen.blit(styi, [216, 48])
                screen.blit(kndct, [8, 66])
                screen.blit(kndi, [216, 64])
                screen.blit(humct, [8, 82])
                screen.blit(humi, [216, 80])
                screen.blit(gorct, [8, 98])
                screen.blit(gori, [216, 96])
                screen.blit(pasct, [8, 114])
                screen.blit(pasi, [216, 112])
            else:
                screen.blit(classbk[skcls], [0, 0])
                if tani and 5 < anifr:
                    screen.blit(classbkg[skcls][(anifr - 6) // 6], [72, 51])
                    if anifr == 18:
                        pygame.mixer.stop()
                        sound[9].play()
                elif not tani:
                    screen.blit(classbkg[skcls][2], [72, 51])
                screen.blit(tsprs[(anifr % 12 < 6) + (2 * (tani and anifr > 17))], [180, 72])
        else:
            if grad < 3:
                screen.blit(gradbg, [0, 0])
                if grad == 1:
                    tsp = (anifr % 12 < 6) + (2 * (anifr > 17))
                    spr = 5 + (8 * (anifr % 12 < 6))
                    if anifr == 18:
                        pygame.mixer.stop()
                        sound[9].play()
                else:
                    tsp = 3
                    spr = 5 + (5 * (anifr % 12 < 6))
                screen.blit(tsprs[tsp], [86, 88])
                if anifr > 11 or grad == 2:
                    screen.blit(asprs[avars[3][5]][spr], [(122 + (46 * (anifr < 18 and grad == 1))), 88])
            else:
                screen.blit(gradl, [0, 0])
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
                            if bx or grad > 0:
                                ret = 0
                                return(avars, ret)
                            else:
                                bx = True
                    if bx:
                        if 32 < mp[1] < 128 and 8 < mp[0] < 232:
                            pygame.mixer.stop()
                            sound[3].play()
                            skcls = (mp[1] - 32) // 16
                            g = avars[avars[3][5]][14]
                            if g < 0:
                                g = 4294967296 + g
                            a = format(g, '032b')
                            tsprs = teachersp(teachn[skcls][(a.count("1") % 3)])
                            bx = False
                            tani = True
                            anifr = 0
                    elif not tani:
                        if 24 < mp[1] < 136:
                            if skcls == 0:
                                avars, ret = maths.game(avars, asprs, screen, tsprs)
                            elif skcls == 1:
                                avars, ret = gradient.game(avars, asprs, screen, tsprs)
                            elif skcls == 2:
                                avars, ret = water.game(avars, asprs, screen, tsprs)
                            elif skcls == 3:
                                avars, ret = clean.game(avars, asprs, screen, tsprs)
                            elif skcls == 4:
                                avars, ret = acting.game(avars, asprs, screen, tsprs)
                            elif skcls == 5:
                                avars, ret = wipe.game(avars, asprs, screen, tsprs)
                            cret = 0
                            anifr = 19
                            if ret:
                                return(avars, ret)
                    elif grad == 2:
                        pygame.mixer.stop()
                        sound[3].play()
                        grad = 3
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
                return(avars, ret)
            chngsts = False
        if anifr < 23:
            anifr += 1
        else:
            anifr = 0
            cret = 1
            ret = 1
            if not bx and grad == 0:
                tani = False
            elif grad == 1:
                grad = 2
        if clt > 29:
            return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

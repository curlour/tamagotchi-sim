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

def job(avars, asprs, screen):

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

    scr = 0

    chngsts = False

    ret = 1
    cret = 1

    intt = 0

    jch = 0

    jreq = [[[(avars[avars[3][5]][5] > 125), (avars[avars[3][5]][5] > 250), (avars[avars[3][5]][5] > 500)], [(avars[avars[3][5]][5] > 125), (avars[avars[3][5]][5] > 250), (avars[avars[3][5]][9] > 125)], #L
             [(avars[avars[3][5]][5] > 125), (avars[avars[3][5]][5] > 250), (avars[avars[3][5]][10] > 125)], [(avars[avars[3][5]][5] > 125), (avars[avars[3][5]][5] > 250), (avars[avars[3][5]][7] > 125)],
             [(avars[avars[3][5]][5] > 125), (avars[avars[3][5]][5] > 250), (avars[avars[3][5]][6] > 125)], [(avars[avars[3][5]][5] > 125), (avars[avars[3][5]][9] > 75), (avars[avars[3][5]][10] > 75)]],
            [[(avars[avars[3][5]][6] > 125), (avars[avars[3][5]][6] > 250), (avars[avars[3][5]][6] > 500)], [(avars[avars[3][5]][6] > 125), (avars[avars[3][5]][6] > 250), (avars[avars[3][5]][10] > 125)], #A
             [(avars[avars[3][5]][6] > 125), (avars[avars[3][5]][6] > 250), (avars[avars[3][5]][8] > 125)], [(avars[avars[3][5]][6] > 125), (avars[avars[3][5]][6] > 250), (avars[avars[3][5]][5] > 125)],
             [(avars[avars[3][5]][6] > 125), (avars[avars[3][5]][6] > 250), (avars[avars[3][5]][7] > 125)], [(avars[avars[3][5]][6] > 125), (avars[avars[3][5]][8] > 75), (avars[avars[3][5]][10] > 75)]],
            [[(avars[avars[3][5]][7] > 125), (avars[avars[3][5]][7] > 250), (avars[avars[3][5]][7] > 500)], [(avars[avars[3][5]][7] > 125), (avars[avars[3][5]][7] > 250), (avars[avars[3][5]][8] > 125)], #K
             [(avars[avars[3][5]][7] > 125), (avars[avars[3][5]][7] > 250), (avars[avars[3][5]][9] > 125)], [(avars[avars[3][5]][7] > 125), (avars[avars[3][5]][7] > 250), (avars[avars[3][5]][5] > 125)],
             [(avars[avars[3][5]][7] > 125), (avars[avars[3][5]][7] > 250), (avars[avars[3][5]][6] > 125)], [(avars[avars[3][5]][7] > 125), (avars[avars[3][5]][9] > 75), (avars[avars[3][5]][8] > 75)]],
            [[(avars[avars[3][5]][8] > 125), (avars[avars[3][5]][8] > 250), (avars[avars[3][5]][8] > 500)], [(avars[avars[3][5]][8] > 125), (avars[avars[3][5]][8] > 250), (avars[avars[3][5]][6] > 125)], #H
             [(avars[avars[3][5]][8] > 125), (avars[avars[3][5]][8] > 250), (avars[avars[3][5]][7] > 125)], [(avars[avars[3][5]][8] > 125), (avars[avars[3][5]][8] > 250), (avars[avars[3][5]][10] > 125)],
             [(avars[avars[3][5]][8] > 125), (avars[avars[3][5]][8] > 250), (avars[avars[3][5]][9] > 125)], [(avars[avars[3][5]][8] > 125), (avars[avars[3][5]][6] > 75), (avars[avars[3][5]][7] > 75)]],
            [[(avars[avars[3][5]][9] > 125), (avars[avars[3][5]][9] > 250), (avars[avars[3][5]][9] > 500)], [(avars[avars[3][5]][9] > 125), (avars[avars[3][5]][9] > 250), (avars[avars[3][5]][7] > 125)], #B
             [(avars[avars[3][5]][9] > 125), (avars[avars[3][5]][9] > 250), (avars[avars[3][5]][5] > 125)], [(avars[avars[3][5]][9] > 125), (avars[avars[3][5]][9] > 250), (avars[avars[3][5]][10] > 125)],
             [(avars[avars[3][5]][9] > 125), (avars[avars[3][5]][9] > 250), (avars[avars[3][5]][8] > 125)], [(avars[avars[3][5]][9] > 125), (avars[avars[3][5]][7] > 75), (avars[avars[3][5]][5] > 75)]],
            [[(avars[avars[3][5]][10] > 125), (avars[avars[3][5]][10] > 250), (avars[avars[3][5]][10] > 500)], [(avars[avars[3][5]][10] > 125), (avars[avars[3][5]][10] > 250), (avars[avars[3][5]][5] > 125)], #P
             [(avars[avars[3][5]][10] > 125), (avars[avars[3][5]][10] > 250), (avars[avars[3][5]][6] > 125)], [(avars[avars[3][5]][10] > 125), (avars[avars[3][5]][10] > 250), (avars[avars[3][5]][8] > 125)],
             [(avars[avars[3][5]][10] > 125), (avars[avars[3][5]][10] > 250), (avars[avars[3][5]][9] > 125)], [(avars[avars[3][5]][10] > 125), (avars[avars[3][5]][6] > 75), (avars[avars[3][5]][5] > 75)]]]

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

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    intb = pygame.image.load("Sprites/Misc/bg/interview.png").convert()

    lsig = [pygame.image.load("Sprites/Misc/bg/interc.png").convert(),
            pygame.image.load("Sprites/Misc/bg/interd.png").convert()]
    bsig = [pygame.image.load("Sprites/Misc/bg/interb.png").convert(),
            pygame.image.load("Sprites/Misc/bg/intera.png").convert()]

    empl = [["ProfFlask", "Jidoutchi", "Guide",
             "MsHoutaiko", "Ginkotchi", "MrTurtle"],
            ["Gulasantchi", "MsModetchi", "King",
             "MrCombBowie", "MsFlower", "MsMusicatchi"],
            ["Morikami", "MsFrill", "Guide",
             "King", "King", "Marutentchi"],
            ["MrFukuwarai", "Dancho", "Market",
             "MrKokuban", "Santa", "Grippatchi"],
            ["Classictchi", "MrCanvas", "King",
             "MrMicchi", "Dancho", "MsBlonde"],
            ["King", "King", "MrKarate",
             "King", "Daiku", "MrOkkana"]]

    emot = [pygame.image.load("Sprites/Misc/emo/conf.png").convert(),
            pygame.image.load("Sprites/Misc/emo/music1.png").convert(),
            pygame.image.load("Sprites/Misc/emo/heart.png").convert(),
            pygame.image.load("Sprites/Misc/emo/em.png").convert(),
            pygame.image.load("Sprites/Misc/emo/shine.png").convert(),
            pygame.image.load("Sprites/Misc/emo/sweat.png").convert()]

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

    scrli = pygame.image.load("Sprites/Misc/txtbox/scrli.png").convert()

    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if bx:
            screen.blit(textbox, [0, 24])
            screen.blit(scrli, [232, 128])
            if scr == 0:
                screen.blit((fnt.render("SCIENTIST", 1, (0, 128, 255))), [8, 34])
                screen.blit((fnt.render("LIBRARIAN", 1, (0, 128, 255))), [8, 50])
                screen.blit((fnt.render("ANNOUNCER", 1, (0, 128, 255))), [8, 66])
                screen.blit((fnt.render("DOCTOR", 1, (0, 128, 255))), [8, 82])
                screen.blit((fnt.render("BANK CLERK", 1, (0, 128, 255))), [8, 96])
                screen.blit((fnt.render("L. TEACHER", 1, (0, 128, 255))), [8, 112])
            elif scr == 1:
                screen.blit((fnt.render("MUSIC STAR", 1, (255, 128, 51))), [8, 34])
                screen.blit((fnt.render("FASHION DESIGNER", 1, (255, 128, 51))), [8, 50])
                screen.blit((fnt.render("BAKER", 1, (255, 128, 51))), [8, 66])
                screen.blit((fnt.render("HAIR STYLIST", 1, (255, 128, 51))), [8, 82])
                screen.blit((fnt.render("FLORIST", 1, (255, 128, 51))), [8, 96])
                screen.blit((fnt.render("A. TEACHER", 1, (255, 128, 51))), [8, 112])
            elif scr == 2:
                screen.blit((fnt.render("SPRINGS ATTENDANT", 1, (102, 255, 51))), [8, 34])
                screen.blit((fnt.render("PRESCHOOL T.", 1, (102, 255, 51))), [8, 50])
                screen.blit((fnt.render("TRAVEL GUIDE", 1, (102, 255, 51))), [8, 66])
                screen.blit((fnt.render("POLICEMAN", 1, (102, 255, 51))), [8, 82])
                screen.blit((fnt.render("CHEF", 1, (102, 255, 51))), [8, 96])
                screen.blit((fnt.render("K. TEACHER", 1, (102, 255, 51))), [8, 112])
            elif scr == 3:
                screen.blit((fnt.render("COMEDIAN", 1, (153, 128, 0))), [8, 34])
                screen.blit((fnt.render("CIRCUS MEMBER", 1, (153, 128, 0))), [8, 50])
                screen.blit((fnt.render("FESTIVAL WORKER", 1, (153, 128, 0))), [8, 66])
                screen.blit((fnt.render("COMIC WRITER", 1, (153, 128, 0))), [8, 82])
                screen.blit((fnt.render("TOY MAKER", 1, (153, 128, 0))), [8, 96])
                screen.blit((fnt.render("H. TEACHER", 1, (153, 128, 0))), [8, 112])
            elif scr == 4:
                screen.blit((fnt.render("ENKA SINGER", 1, (0, 153, 128))), [8, 34])
                screen.blit((fnt.render("ART CRITIC", 1, (0, 153, 128))), [8, 50])
                screen.blit((fnt.render("JEWELER", 1, (0, 153, 128))), [8, 66])
                screen.blit((fnt.render("DANCER", 1, (0, 153, 128))), [8, 82])
                screen.blit((fnt.render("MAGICIAN", 1, (0, 153, 128))), [8, 96])
                screen.blit((fnt.render("B. TEACHER", 1, (0, 153, 128))), [8, 112])
            elif scr == 5:
                screen.blit((fnt.render("BODY BUILDER", 1, (204, 0, 153))), [8, 34])
                screen.blit((fnt.render("ADVENTURER", 1, (204, 0, 153))), [8, 50])
                screen.blit((fnt.render("MARTIAL ARTIST", 1, (204, 0, 153))), [8, 66])
                screen.blit((fnt.render("FIREMAN", 1, (204, 0, 153))), [8, 82])
                screen.blit((fnt.render("CARPENTER", 1, (204, 0, 153))), [8, 96])
                screen.blit((fnt.render("P. TEACHER", 1, (204, 0, 153))), [8, 112])
        elif intt < 3:
            screen.blit(intb, [0, 0])
            if intt == 0:
                isp = anifr % 12 > 5
                spr = [[6, 12, 10, 9, 4, 8][scr], 5][anifr % 12 > 5]
                if anifr % 12  < 6:
                    screen.blit(emot[scr], [140, 100])
            elif intt == 1:
                isp = anifr % 12 > 5
                spr = 3 + (anifr % 12 > 5)
                for i in [0, 1]:
                    if anifr > ((8 * (i + 1)) - 1):
                        screen.blit(lsig[jreq[scr][jch][i]], [(4 + (80 * i)), 62])
            else:
                isp = 3 - (sum(jreq[scr][jch]) == 3)
                spr = 7 - (2 * (sum(jreq[scr][jch]) == 3))
                for i in [0, 1, 2]:
                    screen.blit(lsig[jreq[scr][jch][i]], [(4 + (80 * i)), 62])
                screen.blit(bsig[sum(jreq[scr][jch]) == 3], [38, 80])
            screen.blit(intwrs[isp], [104, 26])
            screen.blit(asprs[avars[3][5]][spr], [104, 102])
        else:
            screen.blit(jobltr, [0, 0])
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
                if pb in [2, 4] and bx:
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if scr < 5:
                            scr += 1
                        else:
                            scr = 0
                        clt = 0
                elif pb == 5 and bx:
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if scr > 0:
                            scr -= 1
                        else:
                            scr = 5
                        clt = 0
                elif pb == 1:
                    clt = 0
                    if 138 < mp[1] < 158 and cret and (bx or intt == 3):
                        if 228 < mp[0] < 240:
                            pygame.mixer.stop()
                            sound[4].play()
                            return(avars, ret)
                        elif 212 < mp[0] < 224:
                            pygame.mixer.stop()
                            sound[4].play()
                            ret = 0
                            return(avars, ret)
                    if bx and 32 < mp[1] < 128 and 8 < mp[0] < 232:
                        pygame.mixer.stop()
                        sound[3].play()
                        jch = ((mp[1] - 32) // 16)
                        bx = False
                        intt = 0
                        anifr = -1
                        intwrs = teachersp(empl[scr][jch])
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
            if not bx and intt < 2:
                intt += 1
                if intt == 2:
                    pygame.mixer.stop()
                    sound[12 - (3 * (sum(jreq[scr][jch]) == 3))].play()
            elif not bx and intt == 2:
                if sum(jreq[scr][jch]) == 3:
                    intt = 3
                    avars[avars[3][5]][31] = (4 + (6 * scr) + jch)
                    jobltr = pygame.image.load("Sprites/Misc/mail/job_" + str(1 + (6 * scr) + jch) + ".png").convert()
                else:
                    bx = True
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

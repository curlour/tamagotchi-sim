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
import weather
import mainscreen
import tamadepa
import park
import preschool
import tamaschool
import jobhnt
import lab
import libr
import tamax
import hospital
import bank
import lclass
import concert
import fashion
import bakery
import hair
import florist
import aclass
import springs
import prest
import station
import police
import chef
import kclass
import comedy
import circus
import festival
import mangaka
import toy
import hclass
import enka
import art
import jewel
import dancer
import magic
import bclass
import builder
import adventure
import martial
import fire
import carpenter
import pclass
import date
import parent
import eggad
import makkaka
import mamec
import gurut
import patchif
import uratama

def door(avars, asprs, screen):

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

    scr = 0

    clt = 0

    spclk = False

    walk = False

    dest = 0

    chngsts = False

    ret = 1

    swthr = ["skyd", "skyaf", "skyn"]
    cwthr = ["skydc", "skydc", "skync"]
    wthrbk = [swthr, cwthr, cwthr]

    jloc = ["PRESCHOOL", "SCHOOL", "JOB HUNT", "LABORATORY", "LIBRARY", "TAMAX TV",
            "HOSPITAL", "GOTCHI BANK", "LOGIC CLASS", "CONCERT", "TAILORING STUDIO", "BAKERY",
            "HAIR SALON", "FLOWER SHOP", "ARTISTRY CLASS", "HOT SPRINGS", "PRESCHOOL", "GOTCHI STATION",
            "POLICE STATION", "RESTAURANT", "KINDNESS CLASS", "COMEDY SHOW", "CIRCUS", "FESTIVAL",
            "COMIC STUDIO", "TOY FACTORY", "HUMOUR CLASS", "AUDITORIUM", "GALLERY", "JEWELRY SHOP",
            "DANCE STUDIO", "MAGIC SHOW", "BEAUTY CLASS", "GYM", "ADVENTURE", "DOJO",
            "FIRE STATION", "CARPENTRY SHOP", "PASSION CLASS"]

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

    def walkani():
        global bkx
        global wthy
        global sprxy
        global spr
        if ((anifr / 12) - (anifr // 12)) < 0.5:
            wthy = 0
            bkx = -8
            spr = 11
            sprxy = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        else:
            if s == 3:
                wthy = 8
            else:
                wthy = 16
            bkx = 0
            spr = 13
            sprxy = 96 + (32 - asprs[avars[3][5]][spr].get_height())

    def arrive():
        global wthy
        global sprx
        global spry
        global spr
        if anifr < 48:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                wthy = 0
                spr = 11
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            else:
                if s == 3:
                    wthy = 8
                else:
                    wthy = 16
                spr = 13
                spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
        else:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                wthy = 0
                spr = 3
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            else:
                if s == 3:
                    wthy = 8
                else:
                    wthy = 16
                spr = 5
                spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
        if 0 <= anifr < 6:
            sprx = 208 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        elif 6 <= anifr < 12:
            sprx = 198 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        elif 12 <= anifr < 18:
            sprx = 188 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        elif 18 <= anifr < 24:
            sprx = 178 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        elif 24 <= anifr < 30:
            sprx = 168 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        elif 30 <= anifr < 36:
            sprx = 158 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        elif 36 <= anifr < 42:
            sprx = 148 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        elif 42 <= anifr < 48:
            sprx = 138 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        else:
            sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()
    
    wlkbk = pygame.image.load("Sprites/Misc/bg/walkbg.png").convert()
    wlkfr = pygame.image.load("Sprites/Misc/bg/walkfg.png").convert()

    rain = pygame.image.load("Sprites/Misc/bg/rain.png").convert()
    snow = pygame.image.load("Sprites/Misc/bg/snow.png").convert()

    tamadepabk = pygame.image.load("Sprites/Misc/bg/tamadepa.png").convert()
    
    presbk = pygame.image.load("Sprites/Misc/bg/presen.png").convert()

    schbk = [pygame.image.load("Sprites/Misc/bg/schoolen.png").convert(),
             pygame.image.load("Sprites/Misc/bg/schoolens.png").convert(),
             pygame.image.load("Sprites/Misc/bg/schoolena.png").convert(),
             pygame.image.load("Sprites/Misc/bg/schoolenw.png").convert()]

    datepl = pygame.image.load("Sprites/Misc/bg/dateplen.png").convert()

    eggado = pygame.image.load("Sprites/Misc/bg/eggout.png").convert()
    
    parents = pygame.image.load("Sprites/Misc/bg/parento.png").convert()

    if avars[avars[3][5]][31] > 3:
        jobpbk = pygame.Surface((240, 160)).convert()
        s = pygame.image.load("Sprites/Misc/bg/job_1.png").convert()
        jobpbk.blit(s, [-(240 * ((avars[avars[3][5]][31] - 4) % 6)), -(160 * ((avars[avars[3][5]][31] - 4) // 6))])

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
                screen.blit((fnt.render("TAMADEPA", 1, (0, 0, 100))), [8, 34])
                screen.blit((fnt.render("PARK", 1, (0, 0, 100))), [8, 50])
                if avars[avars[3][5]][31] == 0 or avars[avars[3][5]][31] > 39:
                    screen.blit((fnt.render("? ? ? ? ?", 1, (102, 102, 255))), [8, 66])
                else:
                    if 8 < int(avars[3][6][:2]) < 17:
                        screen.blit((fnt.render(jloc[avars[avars[3][5]][31] - 1], 1, (0, 0, 100))), [8, 66])
                    else:
                        screen.blit((fnt.render(jloc[avars[avars[3][5]][31] - 1], 1, (102, 102, 255))), [8, 66])
                if avars[avars[3][5]][2] > 691199:
                    screen.blit((fnt.render("DATE PLACE", 1, (0, 0, 100))), [8, 82])
                else:
                    screen.blit((fnt.render("DATE PLACE", 1, (102, 102, 255))), [8, 82])
                if avars[avars[3][5]][2] > 691199:
                    screen.blit((fnt.render("EGG ADOPTION", 1, (0, 0, 100))), [8, 98])
                else:
                    screen.blit((fnt.render("EGG ADOPTION", 1, (102, 102, 255))), [8, 98])
                if (8 < int(avars[3][6][:2]) < 17) and (avars[avars[3][5]][1] < 6) and (avars[avars[3][5]][3] > 1):
                    screen.blit((fnt.render("PARENTS", 1, (0, 0, 100))), [8, 114])
                else:
                    screen.blit((fnt.render("PARENTS", 1, (102, 102, 255))), [8, 114])
            elif scr == 1:
                if (avars[3][14][0] == '1') and (avars[3][14][7] == '1'):
                    screen.blit((fnt.render("MAKKAKKA TOWN", 1, (255, 102, 0))), [8, 34])
                else:
                    screen.blit((fnt.render("? ? ? ? ?", 1, (102, 102, 255))), [8, 34])
                if (avars[3][14][1] == '1') and (avars[3][14][4] == '1'):
                    screen.blit((fnt.render("MAME CITY", 1, (102, 102, 204))), [8, 50])
                else:
                    screen.blit((fnt.render("? ? ? ? ?", 1, (102, 102, 255))), [8, 50])
                if (avars[3][14][5] == '1') and (avars[3][14][6] == '1'):
                    screen.blit((fnt.render("GURUGURU TOWN", 1, (204, 102, 102))), [8, 66])
                else:
                    screen.blit((fnt.render("? ? ? ? ?", 1, (102, 102, 255))), [8, 66])
                if (avars[3][14][2] == '1') and (avars[3][14][3] == '1'):
                    screen.blit((fnt.render("PATCHI FOREST", 1, (102, 204, 102))), [8, 82])
                else:
                    screen.blit((fnt.render("? ? ? ? ?", 1, (102, 102, 255))), [8, 82])
                if avars[3][14].count('0') == 0:
                    screen.blit((fnt.render("URA TAMATOWN", 1, (0, 153, 238))), [8, 98])
                else:
                    screen.blit((fnt.render("? ? ? ? ?", 1, (102, 102, 255))), [8, 98])
        elif walk:
            if ((anifr / 12) - (anifr // 12)) == 0.5:
                pygame.mixer.stop()
                sound[6].play()
            screen.blit(wlkwb, [0, 0])
            screen.blit(wlkbk, [0, 0])
            walkani()
            screen.blit(wlkfr, [bkx, 24])
            screen.blit(asprs[avars[3][5]][spr], [sprxy, sprxy])
            if w == 2:
                screen.blit(wprec, [0, wthy])
        else:
            if dest == 0:
                screen.blit(tamadepabk, [0, 0])
            elif dest == 2:
                screen.blit(wlkwb, [0, 0])
                screen.blit(presbk, [0, 0])
            elif dest == 3:
                screen.blit(wlkwb, [0, 0])
                screen.blit(schbk[s], [0, 0])
            elif 4 < dest < 41:
                screen.blit(jobpbk, [0, 0])
            elif dest == 41:
                screen.blit(datepl, [0, 0])
            elif dest == 42:
                screen.blit(eggado, [0, 0])
            elif dest == 43:
                screen.blit(wlkwb, [0, 0])
                screen.blit(parents, [0, 0])
            if anifr < 48 and ((anifr / 12) - (anifr // 12)) == 0.5:
                pygame.mixer.stop()
                sound[6].play()
            elif ((anifr / 12) - (anifr // 12)) == 0.5:
                pygame.mixer.stop()
                sound[9].play()
            arrive()
            screen.blit(asprs[avars[3][5]][spr], [sprx, spry])
            if w == 2 and dest not in [10, 16, 22, 28, 34, 40]:
                screen.blit(wprec, [0, wthy])
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
                pb = event.button + (spclk * (1 + (event.button > 2)))
                if pb in [2, 4]:
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if scr != 1:
                            scr += 1
                        else:
                            scr = 0
                        clt = 0
                elif pb == 5:
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if scr != 0:
                            scr -= 1
                        else:
                            scr = 1
                        clt = 0
                elif pb == 1:
                    clt = 0
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            pygame.mixer.stop()
                            sound[4].play()
                            return(avars)
                    if bx:
                        if scr == 0:
                            if (32 < mp[1] < 48) and (8 < mp[0] < 112):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 0
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                            if (48 < mp[1] < 64) and (8 < mp[0] < 58):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 1
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                            if (64 < mp[1] < 80) and (8 < mp[0] < 232) and (8 < int(avars[3][6][:2]) < 17) and 0 < avars[avars[3][5]][31] < 40:
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = avars[avars[3][5]][31] + 1
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                            if (80 < mp[1] < 96) and (8 < mp[0] < 232) and (avars[avars[3][5]][2] > 691199):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 41
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                            if (96 < mp[1] < 112) and (8 < mp[0] < 232) and (avars[avars[3][5]][2] > 691199):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 42
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                            if (112 < mp[1] < 128) and (8 < mp[0] < 232) and (8 < int(avars[3][6][:2]) < 17) and (avars[avars[3][5]][1] < 6) and (avars[avars[3][5]][3] > 1):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 43
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                        elif scr == 1:
                            if (32 < mp[1] < 48) and (8 < mp[0] < 232) and (avars[3][14][0] == '1') and (avars[3][14][7] == '1'):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 44
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                            if (48 < mp[1] < 64) and (8 < mp[0] < 232) and (avars[3][14][1] == '1') and (avars[3][14][4] == '1'):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 45
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                            if (64 < mp[1] < 80) and (8 < mp[0] < 232) and (avars[3][14][5] == '1') and (avars[3][14][6] == '1'):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 46
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                            if (80 < mp[1] < 90) and (8 < mp[0] < 232) and (avars[3][14][2] == '1') and (avars[3][14][3] == '1'):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 47
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                            if (96 < mp[1] < 112) and (8 < mp[0] < 232) and (avars[3][14].count('0') == 0):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 48
                                walk = True
                                s, tm , w = weather.chktime(avars)
                                wlkwb = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
                                if s < 3:
                                    wprec = rain
                                else:
                                    wprec = snow
                                anifr = -1
                    elif anifr > 3:
                        if 24 < mp[1] < 136:
                            pygame.mixer.stop()
                            sound[3].play()
                            anifr = 63
                            walk = False
                if pb == 3 and bx and (64 < mp[1] < 80) and (8 < mp[0] < 232) and (8 < int(avars[3][6][:2]) < 17) and avars[avars[3][5]][31] > 3:
                    pygame.mixer.stop()
                    sound[4].play()
                    avars[avars[3][5]][31] = 3
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
        if anifr < 63:
            anifr += 1
        else:
            anifr = 0
            if not bx:
                if dest == 0 and (not walk):
                    avars, ret = tamadepa.depa(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 1:
                    avars, ret = park.prk(avars, asprs, screen, 0, 0, 0, [])
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 2 and (not walk):
                    avars, ret = preschool.pres(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 3 and (not walk):
                    avars, ret = tamaschool.school(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 4:
                    avars, ret = jobhnt.job(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                    if avars[avars[3][5]][31] > 3:
                        jobpbk = pygame.Surface((240, 160)).convert()
                        s = pygame.image.load("Sprites/Misc/bg/job_1.png").convert()
                        jobpbk.blit(s, [-(240 * ((avars[avars[3][5]][31] - 4) % 6)), -(160 * ((avars[avars[3][5]][31] - 4) // 6))])
                elif dest == 5 and (not walk):
                    avars, ret = lab.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 6 and (not walk):
                    avars, ret = libr.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 7 and (not walk):
                    avars, ret = tamax.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 8 and (not walk):
                    avars, ret = hospital.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 9 and (not walk):
                    avars, ret = bank.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 10 and (not walk):
                    avars, ret = lclass.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 11 and (not walk):
                    avars, ret = concert.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 12 and (not walk):
                    avars, ret = fashion.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 13 and (not walk):
                    avars, ret = bakery.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 14 and (not walk):
                    avars, ret = hair.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 15 and (not walk):
                    avars, ret = florist.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 16 and (not walk):
                    avars, ret = aclass.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 17 and (not walk):
                    avars, ret = springs.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 18 and (not walk):
                    avars, ret = prest.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 19 and (not walk):
                    avars, ret = station.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 20 and (not walk):
                    avars, ret = police.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 21 and (not walk):
                    avars, ret = chef.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 22 and (not walk):
                    avars, ret = kclass.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 23 and (not walk):
                    avars, ret = comedy.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 24 and (not walk):
                    avars, ret = circus.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 25 and (not walk):
                    avars, ret = festival.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 26 and (not walk):
                    avars, ret = mangaka.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 27 and (not walk):
                    avars, ret = toy.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 28 and (not walk):
                    avars, ret = hclass.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 29 and (not walk):
                    avars, ret = enka.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 30 and (not walk):
                    avars, ret = art.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 31 and (not walk):
                    avars, ret = jewel.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 32 and (not walk):
                    avars, ret = dancer.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 33 and (not walk):
                    avars, ret = magic.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 34 and (not walk):
                    avars, ret = bclass.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 35 and (not walk):
                    avars, ret = builder.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 36 and (not walk):
                    avars, ret = adventure.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 37 and (not walk):
                    avars, ret = martial.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 38 and (not walk):
                    avars, ret = fire.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 39 and (not walk):
                    avars, ret = carpenter.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 40 and (not walk):
                    avars, ret = pclass.game(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 41 and (not walk):
                    avars, ret = date.fdt(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 42 and (not walk):
                    avars, ret = eggad.adop(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 43 and (not walk):
                    avars, ret = parent.phom(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 44:
                    avars, ret = makkaka.prk(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 45:
                    avars, ret = mamec.prk(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 46:
                    avars, ret = gurut.prk(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 47:
                    avars, ret = patchif.prk(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
                elif dest == 48:
                    avars, ret = uratama.prk(avars, asprs, screen)
                    if ret:
                        return(avars)
                    bx = True
            walk = False
        if clt > 29:
            return(avars)
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

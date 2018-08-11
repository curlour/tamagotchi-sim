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
import palette
import growth
import mainscreen
import coincatch
import cranegame
import darts
import slots
import cardshuffle
import whsuits
import counts
import addcard
import dance
import tones
import soundblk
import colours
import helpstand
import separate
import hrtrain
import cloudbrk
import whackafool
import balance
import hitbloon
import tower
import orderdiamonds
import mimic
import clrjw
import memory
import boxing
import running
import dash
import catch

def depa(avars, asprs, screen):

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

    spclk = False

    dest = 0

    chngsts = False

    scr = 0

    fscr = 0
    iscr = 0
    bscr = 0

    bty = -1

    amrm = 1

    sfd = -1
    sit = -1
    srm = 0
    smd = 0

    mrktm = 0

    ishpm = 0

    remm = 0
    
    medm = 0

    ret = 1
    cret = 1

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

    def drth(lst, tscr):
        tn = 0
        if len(lst) < (16 * (tscr + 1)):
            a = len(lst) - (16 * tscr)
        else:
            a = 16
        while tn < a:
            screen.blit(lst[(tn + (16 * tscr))], [(14 + ((tn - (8 * (tn // 8))) * 27)), (36 + (28 * (tn // 8)))])
            tn += 1

    def arrive():
        global sprx
        global spry
        global spr
        if anifr < 48:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 11
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            else:
                spr = 13
                spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
        else:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 3
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            else:
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

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    gamebk = pygame.image.load("Sprites/Misc/bg/gamecenter.png").convert()
    marketbk = pygame.image.load("Sprites/Misc/bg/market.png").convert()
    ishopbk = pygame.image.load("Sprites/Misc/bg/ishop.png").convert()
    rembk = pygame.image.load("Sprites/Misc/bg/remodelbg.png").convert()
    phabk = pygame.image.load("Sprites/Misc/bg/pharma.png").convert()

    fdlst = [['Rice', 1, 0, 1, 10, 0, 0, 0, 0, 0, 0], ['Apple', 1, 1, 1, 20, 0, 0, 0, 0, 0, 0], ['Mandarin', 1, 2, 1, 35, 0, 0, 0, 0, 0, 0],
             ['Meat', 3, 0, 5, 150, 0, 0, 0, 0, 0, 0], ['Milk', 1, 1, 2, 100, 0, 0, 0, 0, 0, 0], ['IceCream', 1, 2, 3, 100, 0, 0, 0, 0, 0, 0],
             ['Cake', 1, 1, 4, 50, 0, 0, 0, 0, 0, 0], ['Sake', 1, 1, 2, 100, 0, 0, 0, 0, 0, 0], ['Scone', 2, 1, 2, 125, 0, 0, 0, 0, 0, 0],
             ['Pasta', 2, 0, 3, 150, 0, 0, 0, 0, 0, 0], ['SandW', 2, 1, 2, 100, 0, 0, 0, 0, 0, 0], ['Melon', 3, 4, 6, 500, 0, 0, 0, 0, 0, 0],
             ['DrumS', 2, 0, 5, 125, 0, 0, 0, 0, 0, 0], ['Fries', 2, 1, 4, 125, 0, 0, 0, 0, 0, 0], ['Burger', 2, 1, 5, 150, 0, 0, 0, 0, 0, 0],
             ['Steak', 4, 3, 10, 500, 0, 0, 0, 0, 0, 0], ['Bread', 1, 0, 1, 15, 0, 0, 0, 0, 0, 0], ['Pear', 1, 1, 1, 25, 0, 0, 0, 0, 0, 0],
             ['Juice', 1, 2, 1, 50, 0, 0, 0, 0, 0, 0], ['Fish', 3, 0, 5, 175, 0, 0, 0, 0, 0, 0], ['ChMlk', 1, 1, 2, 125, 0, 0, 0, 0, 0, 0],
             ['Choco', 1, 2, 3, 125, 0, 0, 0, 0, 0, 0], ['Donut', 1, 1, 4, 75, 0, 0, 0, 0, 0, 0], ['Wine', 1, 2, 2, 150, 0, 0, 0, 0, 0, 0],
             ['BCheese', 2, 1, 2, 150, 0, 0, 0, 0, 0, 0], ['Tacos', 2, 0, 3, 175, 0, 0, 0, 0, 0, 0], ['Hotdog', 2, 1, 2, 125, 0, 0, 0, 0, 0, 0],
             ['WMelon', 3, 4, 6, 750, 0, 0, 0, 0, 0, 0], ['BBQ', 2, 0, 5, 150, 0, 0, 0, 0, 0, 0], ['PopCorn', 2, 2, 4, 150, 0, 0, 0, 0, 0, 0],
             ['Pizza', 2, 1, 5, 175, 0, 0, 0, 0, 0, 0], ['Sushi', 4, 3, 10, 750, 0, 0, 0, 0, 0, 0], ['Omurice', 2, 0, 3, 120, 1, 0, 0, 0, 0, 0],
             ['Cupcake', 1, 1, 4, 120, 0, 1, 0, 0, 0, 0], ['Corn', 2, 0, 2, 120, 0, 0, 1, 0, 0, 0], ['Bananas', 2, 0, 2, 120, 0, 0, 0, 1, 0, 0],
             ['Slush', 1, 1, 4, 120, 0, 0, 0, 0, 1, 0], ['Sausage', 2, 0, 6, 120, 0, 0, 0, 0, 0, 1], ['Maki', 2, 1, 3, 200, 3, 0, 0, 0, 0, 0],
             ['Dango', 1, 2, 4, 150, 1, 0, 0, 1, 0, 0], ['OcSaus', 2, 1, 4, 200, 0, 0, 0, 3, 0, 0], ['ChCake', 2, 2, 4, 200, 0, 3, 0, 0, 0, 0],
             ['SwCndy', 1, 2, 3, 150, 0, 1, 0, 0, 1, 0], ['Kakigori', 1, 2, 4, 200, 0, 0, 0, 0, 3, 0], ['Onigiri', 2, 1, 3, 200, 0, 0, 3, 0, 0, 0],
             ['Tea', 1, 2, 2, 150, 0, 0, 1, 0, 0, 1], ['Curry', 2, 1, 6, 200, 0, 0, 0, 0, 0, 3], ['Yogurt', 2, 3, 10, 600, 2, 2, 2, 2, 2, 2]]

    a = 0
    fdspr = []
    while a < len(fdlst):
        s = pygame.image.load("Sprites/Food/" + fdlst[a][0] + ".png").convert()
        b = pygame.Surface([24, 24])
        b.fill((0, 255, 255))
        b.blit(s, [0, 0])
        b.set_colorkey((0, 255, 255))
        b.convert()
        fdspr.append(b)
        a += 1

    for file in os.listdir("CFood"):
        if file.endswith(".png"):
            if (pygame.image.load("CFood/" + file).get_rect().size == (72, 24)) and os.path.isfile("CFood/" + file[:(len(file) - 4)] + ".txt"):
                n = open(("CFood/" + file[:(len(file) - 4)] + ".txt"), 'r')
                t = n.read()
                t = t.split('-')
                for i in range(len(t)):
                    t[i] = int(t[i])
                    if (i < 2) and (t[i] > 4):
                        t[i] = 4
                    elif (i == 2) and (t[i] > 15):
                        t[i] = 15
                    elif (i > 2) and (t[i] > 3):
                        t[i] = 3
                p = (sum(t[:2]) + (2 * sum(t[3:]))) * 10
                fdlst.append([file[:(len(file) - 4)], t[0], t[1], t[2], p, t[3], t[4], t[5], t[6], t[7], t[8]])
                s = pygame.image.load("CFood/" + file).convert()
                b = pygame.Surface([24, 24])
                b.fill((0, 255, 255))
                b.blit(s, [0, 0])
                b.set_colorkey((0, 255, 255))
                b.convert()
                fdspr.append(b)

    itlst = [['ball', 100, 1, 0, 0, 0, 0, 0, 0], ['rope', 100, 1, 0, 0, 0, 0, 0, 0], ['plush', 120, 1, 0, 0, 0, 0, 0, 0],
             ['yoyo', 100, 1, 0, 0, 0, 0, 0, 0], ['plant', 200, 0, 0, 0, 0, 0, 0, 0], ['ufo', 250, 2, 0, 0, 0, 0, 0, 0],
             ['phouse', 250, 2, 0, 0, 0, 0, 0, 0], ['!!', 500, 3, 0, 0, 0, 0, 0, 0], ['wool', 120, 1, 0, 0, 0, 0, 0, 0],
             ['camera', 250, 2, 0, 0, 0, 0, 0, 0], ['tamai', 120, 3, 0, 0, 0, 0, 0, 0], ['bubl', 100, 1, 0, 0, 0, 0, 0, 0],
             ['ducki', 250, 2, 0, 0, 0, 0, 0, 0], ['skate', 200, 2, 0, 0, 0, 0, 0, 0], ['dhouse', 500, 3, 0, 0, 0, 0, 0, 0],
             ['dust', 500, 3, 0, 0, 0, 0, 0, 0], ['book', 250, 1, 0, 0, 0, 0, 0, 0], ['sketch', 500, 1, 0, 0, 0, 0, 0, 0],
             ['abac', 250, 1, 3, 0, 0, 0, 0, 0], ['trumpet', 250, 1, 0, 3, 0, 0, 0, 0], ['clay', 250, 1, 0, 0, 3, 0, 0, 0],
             ['balloon', 250, 1, 0, 0, 0, 3, 0, 0], ['mirror', 250, 1, 0, 0, 0, 0, 3, 0], ['weights', 250, 1, 0, 0, 0, 0, 0, 3],
             ['pc', 1000, 1, 3, 3, 3, 3, 3, 3], ['gamei', 1000, 1, 3, 3, 3, 3, 3, 3], ['plcrd', 500, 1, 2, 0, 0, 2, 0, 0],
             ['blocks', 500, 1, 3, 0, 0, 3, 0, 0], ['musb', 500, 1, 0, 2, 0, 0, 2, 0], ['makeup', 500, 1, 0, 3, 0, 0, 3, 0],
             ['pinw', 500, 1, 0, 0, 2, 0, 0, 2], ['pman', 500, 1, 0, 0, 3, 0, 0, 3]]

    a = 0
    itspr = []
    while a < len(itlst):
        itspr.append(pygame.image.load("Sprites/Misc/item/" + itlst[a][0] + ".png").convert())
        a += 1

    bklst = ["Sprites/Misc/bg/room1.png", 10000, "Sprites/Misc/bg/room2.png", 10000, "Sprites/Misc/bg/room3.png", 10000,
             "Sprites/Misc/bg/room4.png", 10000, "Sprites/Misc/bg/roomo.png", 7500, "Sprites/Misc/bg/roomm.png", 7500,
             "Sprites/Misc/bg/roomn.png", 7500, "Sprites/Misc/bg/roomp.png", 7500]

    for file in os.listdir("Backgrounds"):
        if file.endswith(".png"):
            if pygame.image.load("Backgrounds/" + file).get_rect().size == (240, 160):
                bklst.append("Backgrounds/" + file)
                a = ((os.path.getsize("Backgrounds/" + file)) // 100)
                if a > 15:
                    a = 15
                bklst.append(a * 1000)

    if avars[avars[3][5]][23] in bklst:
        a = bklst.index(avars[avars[3][5]][23])
        bklst.pop(a)
        bklst.pop(a)

    bkspr = []
    a = 0
    while a < len(bklst):
        s = pygame.image.load(bklst[a]).convert()
        ns = pygame.Surface([224, 64]).convert()
        ns.blit(s, [-8, -32])
        bkspr.append(ns)
        a += 2

    kbklst = ["Sprites/Misc/bg/kitchen.png", 10000, "Sprites/Misc/bg/kitchen2.png", 10000]

    for file in os.listdir("Kitchen/BG"):
        if file.endswith(".png"):
            if pygame.image.load("Kitchen/BG/" + file).get_rect().size == (240, 160):
                kbklst.append("Kitchen/BG/" + file)
                a = ((os.path.getsize("Kitchen/BG/" + file)) // 100)
                if a > 15:
                    a = 15
                kbklst.append(a * 1000)

    if avars[3][15] in kbklst:
        a = kbklst.index(avars[3][15])
        kbklst.pop(a)
        kbklst.pop(a)

    kbkspr = []
    a = 0
    while a < len(kbklst):
        s = pygame.image.load(kbklst[a]).convert()
        ns = pygame.Surface([224, 64]).convert()
        ns.blit(s, [-8, -32])
        kbkspr.append(ns)
        a += 2

    tables = ["Sprites/Misc/obj/table.png", 5000, "Sprites/Misc/obj/table2.png", 5000]

    for file in os.listdir("Kitchen/Tables"):
        if file.endswith(".png"):
            if pygame.image.load("Kitchen/Tables/" + file).get_rect().size == (64, 32):
                tables.append("Kitchen/Tables/" + file)
                a = ((os.path.getsize("Kitchen/Tables/" + file)) // 100)
                if a > 10:
                    a = 10
                tables.append(a * 1000)

    if avars[3][16] in tables:
        a = tables.index(avars[3][16])
        tables.pop(a)
        tables.pop(a)

    tablespr = []
    a = 0
    while a < len(tables):
        tablespr.append(pygame.image.load(tables[a]).convert())
        a += 2

    chair = ["Sprites/Misc/obj/chair.png", 5000, "Sprites/Misc/obj/chair2.png", 5000]

    for file in os.listdir("Kitchen/Chairs"):
        if file.endswith(".png"):
            if pygame.image.load("Kitchen/Chairs/" + file).get_rect().size == (32, 32):
                chair.append("Kitchen/Chairs/" + file)
                a = ((os.path.getsize("Kitchen/Chairs/" + file)) // 100)
                if a > 10:
                    a = 10
                chair.append(a * 1000)

    if avars[3][17] in chair:
        a = chair.index(avars[3][17])
        chair.pop(a)
        chair.pop(a)

    chairspr = []
    a = 0
    while a < len(chair):
        chairspr.append(pygame.image.load(chair[a]).convert())
        a += 2

    tbklst = ["Sprites/Misc/bg/toilet1.png", 15000, "Sprites/Misc/bg/toilet2.png", 15000]

    for file in os.listdir("WC/BG"):
        if file.endswith(".png"):
            if pygame.image.load("WC/BG/" + file).get_rect().size == (240, 160):
                tbklst.append("WC/BG/" + file)
                a = ((os.path.getsize("WC/BG/" + file)) // 100)
                if a > 15:
                    a = 15
                tbklst.append(a * 1000)

    if avars[3][18] in tbklst:
        a = tbklst.index(avars[3][18])
        tbklst.pop(a)
        tbklst.pop(a)

    tbkspr = []
    a = 0
    while a < len(tbklst):
        s = pygame.image.load(tbklst[a]).convert()
        ns = pygame.Surface([224, 64]).convert()
        ns.blit(s, [-8, -32])
        tbkspr.append(ns)
        a += 2

    toilet = ["Sprites/Misc/obj/toilet.png", 10000, "Sprites/Misc/obj/toilet2.png", 10000]

    for file in os.listdir("WC/Toilet"):
        if file.endswith(".png"):
            if pygame.image.load("WC/Toilet/" + file).get_rect().size == (48, 48):
                toilet.append("WC/Toilet/" + file)
                a = ((os.path.getsize("WC/Toilet/" + file)) // 100)
                if a > 10:
                    a = 10
                toilet.append(a * 1000)

    if avars[3][19] in toilet:
        a = toilet.index(avars[3][19])
        toilet.pop(a)
        toilet.pop(a)

    toiletspr = []
    a = 0
    while a < len(toilet):
        toiletspr.append(pygame.image.load(toilet[a]).convert())
        a += 2

    btoilet = ["Sprites/Misc/obj/babytoilet.png", 5000, "Sprites/Misc/obj/babytoilet2.png", 5000]

    for file in os.listdir("WC/BabyToilet"):
        if file.endswith(".png"):
            if pygame.image.load("WC/BabyToilet/" + file).get_rect().size == (32, 32):
                btoilet.append("WC/BabyToilet/" + file)
                a = ((os.path.getsize("WC/BabyToilet/" + file)) // 100)
                if a > 10:
                    a = 10
                btoilet.append(a * 1000)

    if avars[3][20] in btoilet:
        a = btoilet.index(avars[3][20])
        btoilet.pop(a)
        btoilet.pop(a)

    btoiletspr = []
    a = 0
    while a < len(btoilet):
        btoiletspr.append(pygame.image.load(btoilet[a]).convert())
        a += 2

    bbklst = ["Sprites/Misc/bg/bathroom.png", 15000, "Sprites/Misc/bg/bathroom2.png", 15000]

    for file in os.listdir("Bathroom/BG"):
        if file.endswith(".png"):
            if pygame.image.load("Bathroom/BG/" + file).get_rect().size == (240, 160):
                bbklst.append("Bathroom/BG/" + file)
                a = ((os.path.getsize("Bathroom/BG/" + file)) // 100)
                if a > 15:
                    a = 15
                bbklst.append(a * 1000)

    if avars[3][21] in bbklst:
        a = bbklst.index(avars[3][21])
        bbklst.pop(a)
        bbklst.pop(a)

    bbkspr = []
    a = 0
    while a < len(bbklst):
        s = pygame.image.load(bbklst[a]).convert()
        ns = pygame.Surface([224, 64]).convert()
        ns.blit(s, [-8, -32])
        bbkspr.append(ns)
        a += 2

    bath = ["Sprites/Misc/obj/bath.png", 10000, "Sprites/Misc/obj/bath2.png", 10000]

    for file in os.listdir("Bathroom/Bath"):
        if file.endswith(".png"):
            if pygame.image.load("Bathroom/Bath/" + file).get_rect().size == (64, 32):
                bath.append("Bathroom/Bath/" + file)
                a = ((os.path.getsize("Bathroom/Bath/" + file)) // 100)
                if a > 10:
                    a = 10
                bath.append(a * 1000)

    if avars[3][22] in bath:
        a = bath.index(avars[3][22])
        bath.pop(a)
        bath.pop(a)

    bathspr = []
    a = 0
    while a < len(bath):
        bathspr.append(pygame.image.load(bath[a]).convert())
        a += 2

    rembr = pygame.image.load("Sprites/Misc/bg/bkbrd.png").convert()

    mkspr = []
    s = pygame.image.load("Sprites/NPC/Market.png").convert()
    for i in range(4):
        a = pygame.Surface([32, 32]).convert()
        a.fill((0, 255, 255))
        a.blit(s, [-(32 * (i % 2)), -(32 * (i // 2))])
        a.set_colorkey((0, 255, 255))
        mkspr.append(a)

    dpspr = []
    s = pygame.image.load("Sprites/NPC/Depa.png").convert()
    for i in range(4):
        a = pygame.Surface([32, 32]).convert()
        a.fill((0, 255, 255))
        a.blit(s, [-(32 * (i % 2)), -(32 * (i // 2))])
        a.set_colorkey((0, 255, 255))
        dpspr.append(a)

    rmspr = []
    s = pygame.image.load("Sprites/NPC/Daiku.png").convert()
    for i in range(4):
        a = pygame.Surface([32, 32]).convert()
        a.fill((0, 255, 255))
        a.blit(s, [-(32 * (i % 2)), -(32 * (i // 2))])
        a.set_colorkey((0, 255, 255))
        rmspr.append(a)

    phaspr = []
    s = pygame.image.load("Sprites/NPC/ProfFlask.png").convert()
    for i in range(4):
        a = pygame.Surface([32, 32]).convert()
        a.fill((0, 255, 255))
        a.blit(s, [-(32 * (i % 2)), -(32 * (i // 2))])
        a.set_colorkey((0, 255, 255))
        a = pygame.transform.flip(a, 1, 0)
        phaspr.append(a)
    
    heart = pygame.image.load("Sprites/Misc/menu/hpyf.png").convert()
    heate = pygame.image.load("Sprites/Misc/menu/hpye.png").convert()
    inti = pygame.image.load("Sprites/Misc/menu/inti.png").convert()
    styi = pygame.image.load("Sprites/Misc/menu/styi.png").convert()
    kndi = pygame.image.load("Sprites/Misc/menu/kndi.png").convert()
    humi = pygame.image.load("Sprites/Misc/menu/humi.png").convert()
    gori = pygame.image.load("Sprites/Misc/menu/gori.png").convert()
    pasi = pygame.image.load("Sprites/Misc/menu/pasi.png").convert()

    eskill = []
    for i in range(6):
        a = pygame.image.load("Sprites/Misc/menu/" + ["inti", "styi", "kndi", "humi", "gori", "pasi"][i] + ".png")
        a.set_palette_at([2, 1, 2, 2, 2, 1][i], (255, 255, 255, 255))
        b = [(224, 224, 255, 255), (255, 224, 224, 255), (224, 255, 224, 255),
             (255, 255, 176, 255), (176, 255, 255, 255), (255, 176, 255, 255)][i]
        a.set_palette_at([0, 2, 0, 1, 1, 2][i], b)
        a.convert()
        eskill.append(a)

    coin = pygame.image.load("Sprites/Misc/menu/gotchipt.png").convert()

    barrow = pygame.image.load("Sprites/Misc/txtbox/arrow2.png").convert()
    earrow = pygame.image.load("Sprites/Misc/txtbox/arrow1.png").convert()

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

    unkt = fnt.render("? ? ? ? ?", 1, (102, 102, 255))
    unktn = fnt.render("? ? ? ? ?", 1, (204, 204, 204)) #temp

    mont = fnt.render("MONEY", 1, (0, 0, 100))
    prct = fnt.render("PRICE", 1, (0, 0, 100))

    phatt = [fnt.render("GENETIC ANALYSIS", 1, (0, 0, 100)),
             fnt.render("PLUS LOGIC", 1, (0, 128, 255)),
             fnt.render("PLUS ARTISTRY", 1, (255, 128, 51)),
             fnt.render("PLUS KINDNESS", 1, (102, 255, 51)),
             fnt.render("PLUS HUMOUR", 1, (153, 128, 0)),
             fnt.render("PLUS BEAUTY", 1, (0, 153, 128)),
             fnt.render("PLUS PASSION", 1, (204, 0, 153)),
             fnt.render("PLUS HEALTH", 1, (0, 0, 100)),
             fnt.render("MIN. WEIGHT", 1, (0, 0, 100)),
             fnt.render("BEST WEIGHT", 1, (0, 0, 100)),
             fnt.render("MAX. WEIGHT", 1, (0, 0, 100)),
             fnt.render("REJUVENATE", 1, (0, 0, 100))]

    rltr = [fnt.render("R", 1, (224, 255, 255)), fnt.render("R", 1, (255, 0, 0))]
    gltr = [fnt.render("G", 1, (255, 224, 255)), fnt.render("G", 1, (0, 255, 0))]
    bltr = [fnt.render("B", 1, (255, 255, 224)), fnt.render("B", 1, (0, 0, 255))]
    oltr = [fnt.render("O", 1, (255, 102, 0)), fnt.render("O", 1, (0, 153, 238))]

    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if bx:
            screen.blit(textbox, [0, 24])
            if scr == 2:
                if mrktm == 0:
                    screen.blit(mkspr[0], [28, 94])
                elif mrktm == 1:
                    screen.blit(mkspr[2], [28, 94])
                else:
                    screen.blit(mkspr[3], [28, 94])
            elif scr == 3:
                if ishpm == 0:
                    screen.blit(dpspr[0], [28, 94])
                elif ishpm == 1:
                    screen.blit(dpspr[2], [28, 94])
                else:
                    screen.blit(dpspr[3], [28, 94])
            elif scr == 5:
                if remm == 0:
                    screen.blit(rmspr[0], [28, 94])
                elif remm == 1:
                    screen.blit(rmspr[2], [28, 94])
                else:
                    screen.blit(rmspr[3], [28, 94])
            elif scr == 6:
                if medm == 0:
                    screen.blit(phaspr[0], [28, 94])
                elif medm == 1:
                    screen.blit(phaspr[2], [28, 94])
                else:
                    screen.blit(phaspr[3], [28, 94])
            elif scr == 7:
                for i in range(4):
                    screen.blit(rltr[int(genl[i])], [(18 + (16 * i)), 42])
                for i in range(4):
                    screen.blit(gltr[int(genl[i + 4])], [(18 + (16 * i)), 58])
                for i in range(4):
                    screen.blit(bltr[int(genl[i + 8])], [(18 + (16 * i)), 74])
                for i in range(4):
                    screen.blit(oltr[int(genl[i + 12])], [(18 + (16 * i)), 90])
                if avars[avars[3][5]][1] < 6:
                    i = (avars[avars[3][5]][1] < 4) + (avars[avars[3][5]][1] < 2)
                    j = (avars[avars[3][5]][1] < 3)
                    screen.blit(asprs[avars[3][5]][3], [(112 + (4 * i)), (64 + (4 * i))])
                    screen.blit(earrow, [152, 76])
                    screen.blit(prds, [(168 + (4 * j)), (64 + (4 * j))])
                else:
                    screen.blit(prds, [140, 64])
                if genl[9:11] + genl[16:18] == '1111':
                    screen.blit(inti, [88, 40])
                else:
                    screen.blit(eskill[0], [88, 40])
                if genl[1:3] + genl[18:20] == '1111':
                    screen.blit(styi, [112, 40])
                else:
                    screen.blit(eskill[1], [112, 40])
                if genl[5:7] + genl[20:22] == '1111':
                    screen.blit(kndi, [136, 40])
                else:
                    screen.blit(eskill[2], [136, 40])
                if genl[3:5] + genl[22:24] == '1111':
                    screen.blit(humi, [160, 40])
                else:
                    screen.blit(eskill[3], [160, 40])
                if genl[7:9] + genl[24:26] == '1111':
                    screen.blit(gori, [184, 40])
                else:
                    screen.blit(eskill[4], [184, 40])
                if genl[0] + genl[11] + genl[26:28] == '1111':
                    screen.blit(pasi, [208, 40])
                else:
                    screen.blit(eskill[5], [208, 40])
                screen.blit(heart, [24, 108])
                screen.blit(fdspr[lkfd], [48, 104])
                screen.blit(heate, [168, 108])
                screen.blit(fdspr[htfd], [192, 104])
            if scr == 0:
                screen.blit((fnt.render("GAME CENTER", 1, (0, 0, 100))), [8, 34])
                screen.blit((fnt.render("MARKET", 1, (0, 0, 100))), [8, 50])
                screen.blit((fnt.render("ITEM SHOP", 1, (0, 0, 100))), [8, 66])
                screen.blit((fnt.render("REMODEL", 1, (0, 0, 100))), [8, 82])
                screen.blit((fnt.render("PHARMACY", 1, (0, 0, 100))), [8, 98])
            elif scr == 1:
                screen.blit(scrli, [232, 128])
                if gms == 0:
                    screen.blit(heart, [8, 32])
                    screen.blit(heart, [216, 32])
                    screen.blit(heart, [8, 112])
                    screen.blit(heart, [216, 112])
                    screen.blit((fnt.render("COIN CATCH", 1, (0, 0, 100))), [24, 50])
                    if avars[avars[3][5]][1] < 2:
                        screen.blit(unkt, [24, 66])
                    else:
                        screen.blit((fnt.render("CRANE GAME", 1, (0, 0, 100))), [24, 66])
                    if avars[avars[3][5]][1] < 3:
                        screen.blit(unkt, [24, 82])
                    else:
                        screen.blit((fnt.render("DARTS", 1, (0, 0, 100))), [24, 82])
                    if avars[avars[3][5]][1] < 4:
                        screen.blit(unkt, [24, 98])
                    else:
                        if avars[3][2] < 10:
                            screen.blit((fnt.render("SLOTS", 1, (102, 102, 255))), [24, 98])
                        else:
                            screen.blit((fnt.render("SLOTS", 1, (0, 0, 100))), [24, 98])
                if gms == 1:
                    screen.blit(inti, [8, 32])
                    screen.blit(inti, [216, 32])
                    screen.blit(inti, [8, 112])
                    screen.blit(inti, [216, 112])
                    if avars[avars[3][5]][5] == 0:
                        screen.blit(unkt, [24, 50])
                    else:
                        screen.blit((fnt.render("CARD SHUFFLE", 1, (0, 128, 255))), [24, 50])
                    if avars[avars[3][5]][5] < 25:
                        screen.blit(unkt, [24, 66])
                    else:
                        screen.blit((fnt.render("WHICH SUITS?", 1, (0, 128, 255))), [24, 66])
                    if avars[avars[3][5]][5] < 100:
                        screen.blit(unkt, [24, 82])
                    else:
                        screen.blit((fnt.render("COUNT", 1, (0, 128, 255))), [24, 82])
                    if avars[avars[3][5]][5] < 250:
                        screen.blit(unkt, [24, 98])
                    else:
                        screen.blit((fnt.render("ADD CARDS", 1, (0, 128, 255))), [24, 98])
                if gms == 2:
                    screen.blit(styi, [8, 32])
                    screen.blit(styi, [216, 32])
                    screen.blit(styi, [8, 112])
                    screen.blit(styi, [216, 112])
                    if avars[avars[3][5]][6] == 0:
                        screen.blit(unkt, [24, 50])
                    else:
                        screen.blit((fnt.render("DANCE", 1, (255, 128, 51))), [24, 50])
                    if avars[avars[3][5]][6] < 25:
                        screen.blit(unkt, [24, 66])
                    else:
                        screen.blit((fnt.render("TONES", 1, (255, 128, 51))), [24, 66])
                    if avars[avars[3][5]][6] < 100:
                        screen.blit(unkt, [24, 82])
                    else:
                        screen.blit((fnt.render("SOUND BLOCK", 1, (255, 128, 51))), [24, 82])
                    if avars[avars[3][5]][6] < 250:
                        screen.blit(unkt, [24, 98])
                    else:
                        screen.blit((fnt.render("COLOURS", 1, (255, 128, 51))), [24, 98])
                if gms == 3:
                    screen.blit(kndi, [8, 32])
                    screen.blit(kndi, [216, 32])
                    screen.blit(kndi, [8, 112])
                    screen.blit(kndi, [216, 112])
                    if avars[avars[3][5]][7] == 0:
                        screen.blit(unkt, [24, 50])
                    else:
                        screen.blit((fnt.render("HELP AT STAND", 1, (102, 255, 51))), [24, 50])
                    if avars[avars[3][5]][7] < 25:
                        screen.blit(unkt, [24, 66])
                    else:
                        screen.blit((fnt.render("SEPARATE", 1, (102, 255, 51))), [24, 66])
                    if avars[avars[3][5]][7] < 100:
                        screen.blit(unkt, [24, 82])
                    else:
                        screen.blit((fnt.render("HEART RAIN", 1, (102, 255, 51))), [24, 82])
                    if avars[avars[3][5]][7] < 250:
                        screen.blit(unkt, [24, 98])
                    else:
                        screen.blit((fnt.render("CLOUD BREAK", 1, (102, 255, 51))), [24, 98])
                if gms == 4:
                    screen.blit(humi, [8, 32])
                    screen.blit(humi, [216, 32])
                    screen.blit(humi, [8, 112])
                    screen.blit(humi, [216, 112])
                    if avars[avars[3][5]][8] == 0:
                        screen.blit(unkt, [24, 50])
                    else:
                        screen.blit((fnt.render("WHACK A FOOL", 1, (153, 128, 0))), [24, 50])
                    if avars[avars[3][5]][8] < 25:
                        screen.blit(unkt, [24, 66])
                    else:
                        screen.blit((fnt.render("BALANCE", 1, (153, 128, 0))), [24, 66])
                    if avars[avars[3][5]][8] < 100:
                        screen.blit(unkt, [24, 82])
                    else:
                        screen.blit((fnt.render("HIT THE BALLOON", 1, (153, 128, 0))), [24, 82])
                    if avars[avars[3][5]][8] < 250:
                        screen.blit(unkt, [24, 98])
                    else:
                        screen.blit((fnt.render("TOWER", 1, (153, 128, 0))), [24, 98])
                if gms == 5:
                    screen.blit(gori, [8, 32])
                    screen.blit(gori, [216, 32])
                    screen.blit(gori, [8, 112])
                    screen.blit(gori, [216, 112])
                    if avars[avars[3][5]][9] == 0:
                        screen.blit(unkt, [24, 50])
                    else:
                        screen.blit((fnt.render("ORDER DIAMONDS", 1, (0, 153, 128))), [24, 50])
                    if avars[avars[3][5]][9] < 25:
                        screen.blit(unkt, [24, 66])
                    else:
                        screen.blit((fnt.render("MIMIC", 1, (0, 153, 128))), [24, 66])
                    if avars[avars[3][5]][9] < 100:
                        screen.blit(unkt, [24, 82])
                    else:
                        screen.blit((fnt.render("COLOURED JEWELS", 1, (0, 153, 128))), [24, 82])
                    if avars[avars[3][5]][9] < 250:
                        screen.blit(unkt, [24, 98])
                    else:
                        screen.blit((fnt.render("MEMORY", 1, (0, 153, 128))), [24, 98])
                if gms == 6:
                    screen.blit(pasi, [8, 32])
                    screen.blit(pasi, [216, 32])
                    screen.blit(pasi, [8, 112])
                    screen.blit(pasi, [216, 112])
                    if avars[avars[3][5]][10] == 0:
                        screen.blit(unkt, [24, 50])
                    else:
                        screen.blit((fnt.render("BOXING", 1, (204, 0, 153))), [24, 50])
                    if avars[avars[3][5]][10] < 25:
                        screen.blit(unkt, [24, 66])
                    else:
                        screen.blit((fnt.render("RUNNING", 1, (204, 0, 153))), [24, 66])
                    if avars[avars[3][5]][10] < 100:
                        screen.blit(unkt, [24, 82])
                    else:
                        screen.blit((fnt.render("DASH", 1, (204, 0, 153))), [24, 82])
                    if avars[avars[3][5]][10] < 250:
                        screen.blit(unkt, [24, 98])
                    else:
                        screen.blit((fnt.render("CATCH", 1, (204, 0, 153))), [24, 98])
            elif scr == 4:
                if bty == -1:
                    screen.blit((fnt.render("ROOM", 1, (0, 0, 100))), [8, 34])
                    screen.blit((fnt.render("KITCHEN", 1, (0, 0, 100))), [8, 50])
                    screen.blit((fnt.render("WC", 1, (0, 0, 100))), [8, 66])
                    screen.blit((fnt.render("BATHROOM", 1, (0, 0, 100))), [8, 82])
                elif bty == 1:
                    screen.blit((fnt.render("ROOM", 1, (0, 0, 100))), [8, 34])
                    screen.blit((fnt.render("TABLE", 1, (0, 0, 100))), [8, 50])
                    screen.blit((fnt.render("CHAIR", 1, (0, 0, 100))), [8, 66])
                elif bty == 2:
                    screen.blit((fnt.render("ROOM", 1, (0, 0, 100))), [8, 34])
                    screen.blit((fnt.render("TOILET", 1, (0, 0, 100))), [8, 50])
                    screen.blit((fnt.render("BABY TOILET", 1, (0, 0, 100))), [8, 66])
                elif bty == 3:
                    screen.blit((fnt.render("ROOM", 1, (0, 0, 100))), [8, 34])
                    screen.blit((fnt.render("BATH", 1, (0, 0, 100))), [8, 50])
            elif scr == 2 or scr == 3 or scr == 5 or scr == 6:
                screen.blit(scrli, [232, 128])
                screen.blit(mont, [68, 114])
                screen.blit((fnt.render(str(avars[3][2]), 1, (0, 0, 100))), [(188 - (10 * (len(str(avars[3][2]))))), 114])
                screen.blit(coin, [196, 112])
                if scr == 2:
                    drth(fdspr, fscr)
                elif scr == 3:
                    drth(itspr, iscr)
                elif scr == 5:
                    if bty in [0, 4, 7, 10]:
                        if bty == 0:
                            screen.blit(bkspr[srm], [8, 32])
                        if bty == 4:
                            screen.blit(kbkspr[srm], [8, 32])
                        if bty == 7:
                            screen.blit(tbkspr[srm], [8, 32])
                        if bty == 10:
                            screen.blit(bbkspr[srm], [8, 32])
                        screen.blit(rembr, [8, 32])
                    else:
                        if bty == 5:
                            screen.blit(tablespr[srm], [88, 48])
                        if bty == 6:
                            screen.blit(chairspr[srm], [104, 48])
                        if bty == 8:
                            screen.blit(toiletspr[srm], [96, 40])
                        if bty == 9:
                            screen.blit(btoiletspr[srm], [104, 48])
                        if bty == 11:
                            screen.blit(bathspr[srm], [88, 48])
                if (sfd > -1 and scr == 2) or (sit > -1 and scr == 3):
                    screen.blit(prct, [68, 98])
                    if scr == 2:
                        screen.blit((fnt.render(str(fdlst[sfd][4]), 1, (0, 0, 100))), [(178 - (10 * (len(str(fdlst[sfd][4]))))), 98])
                        screen.blit(barrow, [(22 + ((sfd - (8 * (sfd // 8))) * 27)), (58 + (28 * ((sfd % 16) // 8)))])
                    else:
                        screen.blit((fnt.render(str(itlst[sit][1]), 1, (0, 0, 100))), [(178 - (10 * (len(str(itlst[sit][1]))))), 98])
                        screen.blit(barrow, [(22 + ((sit - (8 * (sit // 8))) * 27)), (58 + (28 * ((sit % 16) // 8)))])
                    screen.blit(coin, [186, 96])
                elif scr == 5:
                    n = bty - (3 * (bty > 0))
                    a = [bklst, kbklst, tables, chair, tbklst, toilet, btoilet,
                         bbklst, bath][n]
                    screen.blit(prct, [68, 98])
                    screen.blit((fnt.render(str(a[(2 * srm) + 1]), 1, (0, 0, 100))), [(178 - (10 * (len(str(a[(2 * srm) + 1]))))), 98])
                    screen.blit(coin, [186, 96])
                elif scr == 6:
                    screen.blit(phatt[smd], [8, 66])####
                    screen.blit(prct, [68, 98])
                    screen.blit((fnt.render(str(1250 * ((smd > 0) + (2 * (smd == 11)) + 1)), 1, (0, 0, 100))), [138, 98])
                    screen.blit(coin, [186, 96])
        else:
            if anifr < 48 and ((anifr / 12) - (anifr // 12)) == 0.5:
                pygame.mixer.stop()
                sound[6].play()
            elif ((anifr / 12) - (anifr // 12)) == 0.5:
                pygame.mixer.stop()
                sound[9].play()
            if dest == 0:
                screen.blit(gamebk, [0, 0])
            elif dest == 1:
                screen.blit(marketbk, [0, 0])
                if 54 <= anifr < 60:
                    screen.blit(mkspr[2], [80, 96])
                elif ((anifr / 12) - (anifr // 12)) < 0.5:
                    screen.blit(mkspr[0], [80, 98])
                else:
                    screen.blit(mkspr[1], [80, 98])
            elif dest == 2:
                screen.blit(ishopbk, [0, 0])
                if 54 <= anifr < 60:
                    screen.blit(dpspr[2], [80, 96])
                elif ((anifr / 12) - (anifr // 12)) < 0.5:
                    screen.blit(dpspr[0], [80, 98])
                else:
                    screen.blit(dpspr[1], [80, 98])
            elif dest == 3:
                screen.blit(rembk, [0, 0])
                if 54 <= anifr < 60:
                    screen.blit(rmspr[2], [80, 96])
                elif ((anifr / 12) - (anifr // 12)) < 0.5:
                    screen.blit(rmspr[0], [80, 98])
                else:
                    screen.blit(rmspr[1], [80, 98])
            elif dest == 4:
                screen.blit(phabk, [0, 0])
                if 54 <= anifr < 60:
                    screen.blit(phaspr[2], [80, 96])
                elif ((anifr / 12) - (anifr // 12)) < 0.5:
                    screen.blit(phaspr[0], [80, 98])
                else:
                    screen.blit(phaspr[1], [80, 98])
            arrive()
            screen.blit(asprs[avars[3][5]][spr], [sprx, spry])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
        for event in pygame.event.get():
            if event.type == QUIT:
                varsup.updtvrs(avars)
                kr = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in [303, 304]:
                    spclk = True
            if event.type == KEYUP:
                if event.key in [303, 304]:
                    spclk = False
            if event.type == MOUSEBUTTONDOWN:
                mp = event.pos
                d = (screen.get_size()[0] // 240)
                mp = ((mp[0] // d), (mp[1] // d))
                pb = event.button + (spclk * (1 + (event.button > 2)))
                if pb in [2, 4]:
                    clt = 0
                    if scr == 1:
                        pygame.mixer.stop()
                        sound[2].play()
                        if gms != 6:
                            gms += 1
                        else:
                            gms = 0
                    elif scr == 2:
                        pygame.mixer.stop()
                        sound[2].play()
                        if fscr != ((len(fdlst) - 1) // 16):
                            fscr += 1
                        else:
                            fscr = 0
                        sfd = -1
                    elif scr == 3:
                        pygame.mixer.stop()
                        sound[2].play()
                        if iscr != ((len(itlst) - 1) // 16):
                            iscr += 1
                        else:
                            iscr = 0
                        sit = -1
                    elif scr == 5 and remm == 0:
                        pygame.mixer.stop()
                        sound[2].play()
                        if srm != amrm:
                            srm += 1
                        else:
                            srm = 0
                    elif scr == 6 and medm == 0:
                        pygame.mixer.stop()
                        sound[2].play()
                        if smd != 11:
                            smd += 1
                        else:
                            smd = 0
                elif pb == 5:
                    clt = 0
                    if scr == 1:
                        pygame.mixer.stop()
                        sound[2].play()
                        if gms != 0:
                            gms -= 1
                        else:
                            gms = 6
                    elif scr == 2:
                        pygame.mixer.stop()
                        sound[2].play()
                        if fscr != 0:
                            fscr -= 1
                        else:
                            fscr = ((len(fdlst) - 1) // 16)
                        sfd = -1
                    elif scr == 3:
                        pygame.mixer.stop()
                        sound[2].play()
                        if iscr != 0:
                            iscr -= 1
                        else:
                            iscr = ((len(itlst) - 1) // 16)
                        sit = -1
                    elif scr == 5 and remm == 0:
                        pygame.mixer.stop()
                        sound[2].play()
                        if srm != 0:
                            srm -= 1
                        else:
                            srm = amrm
                    elif scr == 6 and medm == 0:
                        pygame.mixer.stop()
                        sound[2].play()
                        if smd != 0:
                            smd -= 1
                        else:
                            smd = 11
                elif pb == 1:
                    clt = 0
                    if 138 < mp[1] < 158 and cret:
                        if 228 < mp[0] < 240:
                            pygame.mixer.stop()
                            sound[4].play()
                            return(avars, ret)
                        elif 212 < mp[0] < 224:
                            if bx:
                                pygame.mixer.stop()
                                sound[4].play()
                                if scr == 0:
                                    ret = 0
                                    return(avars, ret)
                                else:
                                    if scr != 5:
                                        scr = 0
                                        fscr = 0
                                        iscr = 0
                                        bscr = 0
                                        bty = -1
                                        sfd = -1
                                        sit = -1
                                        srm = 0
                                        mrktm = 0
                                        ishpm = 0
                                        remm = 0
                                    elif scr == 5:
                                        scr = 4
                                        bty = -1
                                        remm = 0
                                        srm = 0
                                        bscr = 0
                    if bx:
                        if scr == 0:
                            if (32 < mp[1] < 48) and (8 < mp[0] < 232):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 0
                                anifr = 0
                            if (48 < mp[1] < 64) and (8 < mp[0] < 232):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 1
                                anifr = 0
                            if (64 < mp[1] < 80) and (8 < mp[0] < 232):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 2
                                anifr = 0
                            if (80 < mp[1] < 96) and (8 < mp[0] < 232):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 3
                                anifr = 0
                            if (96 < mp[1] < 112) and (8 < mp[0] < 232):
                                pygame.mixer.stop()
                                sound[3].play()
                                bx = False
                                dest = 4
                                anifr = 0
                        if scr == 1:
                            if gms == 0:
                                if 48 < mp[1] < 64 and 24 < mp[0] < 138:
                                    avars, ret = coincatch.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 64 < mp[1] < 80 and 24 < mp[0] < 144 and avars[avars[3][5]][1] > 1:
                                    avars, ret = cranegame.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 80 < mp[1] < 96 and 24 < mp[0] < 88 and avars[avars[3][5]][1] > 2:
                                    avars, ret = darts.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 96 < mp[1] < 112 and 24 < mp[0] < 86 and avars[avars[3][5]][1] > 3 and avars[3][2] > 9:
                                    avars, ret = slots.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                            elif gms == 1:
                                if 48 < mp[1] < 64 and 24 < mp[0] < 170 and avars[avars[3][5]][5] > 0:
                                    avars, ret = cardshuffle.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 64 < mp[1] < 80 and 24 < mp[0] < 158 and avars[avars[3][5]][5] > 24:
                                    avars, ret = whsuits.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 80 < mp[1] < 96 and 24 < mp[0] < 88 and avars[avars[3][5]][5] > 99:
                                    avars, ret = counts.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 96 < mp[1] < 112 and 24 < mp[0] < 132 and avars[avars[3][5]][5] > 249:
                                    avars, ret = addcard.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                            elif gms == 2:
                                if 48 < mp[1] < 64 and 24 < mp[0] < 88 and avars[avars[3][5]][6] > 0:
                                    avars, ret = dance.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 64 < mp[1] < 80 and 24 < mp[0] < 88 and avars[avars[3][5]][6] > 24:
                                    avars, ret = tones.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 80 < mp[1] < 96 and 24 < mp[0] < 156 and avars[avars[3][5]][6] > 99:
                                    avars, ret = soundblk.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 96 < mp[1] < 112 and 24 < mp[0] < 112 and avars[avars[3][5]][6] > 249:
                                    avars, ret = colours.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                            elif gms == 3:
                                if 48 < mp[1] < 64 and 24 < mp[0] < 174 and avars[avars[3][5]][7] > 0:
                                    avars, ret = helpstand.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 64 < mp[1] < 80 and 24 < mp[0] < 126 and avars[avars[3][5]][7] > 24:
                                    avars, ret = separate.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 80 < mp[1] < 96 and 24 < mp[0] < 138 and avars[avars[3][5]][7] > 99:
                                    avars, ret = hrtrain.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 96 < mp[1] < 112 and 24 < mp[0] < 156 and avars[avars[3][5]][7] > 249:
                                    avars, ret = cloudbrk.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                            elif gms == 4:
                                if 48 < mp[1] < 64 and 24 < mp[0] < 160 and avars[avars[3][5]][8] > 0:
                                    avars, ret = whackafool.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 64 < mp[1] < 80 and 24 < mp[0] < 112 and avars[avars[3][5]][8] > 24:
                                    avars, ret = balance.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 80 < mp[1] < 96 and 24 < mp[0] < 194 and avars[avars[3][5]][8] > 99:
                                    avars, ret = hitbloon.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 96 < mp[1] < 112 and 24 < mp[0] < 88 and avars[avars[3][5]][8] > 249:
                                    avars, ret = tower.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                            elif gms == 5:
                                if 48 < mp[1] < 64 and 24 < mp[0] < 190 and avars[avars[3][5]][9] > 0:
                                    avars, ret = orderdiamonds.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 64 < mp[1] < 80 and 24 < mp[0] < 76 and avars[avars[3][5]][9] > 24:
                                    avars, ret = mimic.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 80 < mp[1] < 96 and 24 < mp[0] < 208 and avars[avars[3][5]][9] > 99:
                                    avars, ret = clrjw.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 96 < mp[1] < 112 and 24 < mp[0] < 100 and avars[avars[3][5]][9] > 249:
                                    avars, ret = memory.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                            elif gms == 6:
                                if 48 < mp[1] < 64 and 24 < mp[0] < 94 and avars[avars[3][5]][10] > 0:
                                    avars, ret = boxing.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 64 < mp[1] < 80 and 24 < mp[0] < 108 and avars[avars[3][5]][10] > 24:
                                    avars, ret = running.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 80 < mp[1] < 96 and 24 < mp[0] < 74 and avars[avars[3][5]][10] > 99:
                                    avars, ret = dash.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                                if 96 < mp[1] < 112 and 24 < mp[0] < 88 and avars[avars[3][5]][10] > 249:
                                    avars, ret = catch.game(avars, asprs, screen)
                                    cret = 0
                                    anifr = 59
                                    if ret:
                                        return(avars, ret)
                        elif scr == 4 and bty == -1 and 32 < mp[1] < 96 and 8 < mp[0] < 134:
                            pygame.mixer.stop()
                            sound[3].play()
                            bty = (mp[1] - 32) // 16
                            if bty == 0:
                                scr = 5
                                amrm = ((len(bklst) - 1) // 2)
                        elif scr == 4 and bty == 1 and 32 < mp[1] < 80 and 8 < mp[0] < 134:
                            pygame.mixer.stop()
                            sound[3].play()
                            bty = 4
                            bty += (mp[1] - 32) // 16
                            scr = 5
                            amrm = ((len([kbklst, tables, chair][bty - 4]) - 1) // 2)
                        elif scr == 4 and bty == 2 and 32 < mp[1] < 80 and 8 < mp[0] < 134:
                            pygame.mixer.stop()
                            sound[3].play()
                            bty = 7
                            bty += (mp[1] - 32) // 16
                            scr = 5
                            amrm = ((len([tbklst, toilet, btoilet][bty - 7]) - 1) // 2)
                        elif scr == 4 and bty == 3 and 32 < mp[1] < 64 and 8 < mp[0] < 134:
                            pygame.mixer.stop()
                            sound[3].play()
                            bty = 10
                            bty += (mp[1] - 32) // 16
                            scr = 5
                            amrm = ((len([bbklst, bath][bty - 10]) - 1) // 2)
                        elif scr == 5 and remm == 0 and 36 < mp[1] < 88:
                            n = bty - (3 * (bty > 0))
                            a = [bklst, kbklst, tables, chair, tbklst, toilet, btoilet,
                                 bbklst, bath][n]
                            if a[(2 * srm) + 1] <= avars[3][2]:
                                avars[3][2] -= a[(2 * srm) + 1]
                                if n == 0:
                                    avars[avars[3][5]][23] = a[2 * srm]
                                else:
                                    avars[3][14 + n] = a[2 * srm]
                                anifr = 0
                                remm = 1
                                pygame.mixer.stop()
                                sound[13].play()
                            else:
                                anifr = 0
                                remm = 2
                                pygame.mixer.stop()
                                sound[12].play()
                        elif scr == 6 and medm == 0 and 36 < mp[1] < 88:
                            if smd == 0:
                                if 1250 <= avars[3][2]:
                                    avars[3][2] -= 1250
                                    scr = 7
                                    g = avars[avars[3][5]][14]
                                    if g < 0:
                                        g = 4294967296 + g
                                    genl = format(g, '032b')
                                    lkfd = int((genl[16:19] + genl[28]), 2) + (16 * int(genl[30]))
                                    htfd = int((genl[20:23] + genl[29]), 2) + (16 * (int(genl[30]) == 0))
                                    if avars[avars[3][5]][1] < 6:
                                        ov = [[], [], [], [0, 0, 0, 0, 0, 0]]
                                        for i in range(len(avars[avars[3][5]])):
                                            if i != 24:
                                                ov[0].append(avars[avars[3][5]][i])
                                            else:
                                                ov[0].append([])
                                        ov[0][1] += 1
                                        if ov[0][1] == 5: ov[0][1] += 1
                                        ov = growth.grw(ov)
                                        try:
                                            bs = pygame.image.load("Sprites/Characters/chara_" + str(ov[0][15]) + "b.png")
                                            ss = pygame.image.load("Sprites/Characters/chara_" + str(ov[0][15]) + "s.png")
                                            opal = []
                                            for i in range(32):
                                                opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                                            bs = palette.palch(bs, g, opal)
                                            ss = palette.palch(ss, g, opal)
                                        except:
                                            bs = pygame.image.load("Sprites/NPC/Nazotchi.png")
                                            ss = pygame.image.load("Sprites/NPC/Nazo.png")
                                            opal = []
                                            for i in range(32):
                                                opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                                            bs = palette.palch(bs, g, opal)
                                            ss = palette.palch(ss, g, opal)
                                        p = (bs.get_width() // 4)
                                        prds = pygame.Surface([p, p]).convert()
                                        prds.fill((0, 255, 255))
                                        prds.blit(bs, [0, 0])
                                        prds.set_colorkey((0, 255, 255))
                                    else:
                                        prds = asprs[avars[3][5]][6]
                                    pygame.mixer.stop()
                                    sound[13].play()
                                else:
                                    anifr = 0
                                    medm = 2
                                    pygame.mixer.stop()
                                    sound[12].play()
                            elif smd in range(1, 7):
                                if 2500 <= avars[3][2]:
                                    avars[3][2] -= 2500
                                    anifr = 0
                                    medm = 1
                                    avars[avars[3][5]][4 + smd] += 250
                                    pygame.mixer.stop()
                                    sound[13].play()
                                else:
                                    anifr = 0
                                    medm = 2
                                    pygame.mixer.stop()
                                    sound[12].play()
                            elif smd == 7:
                                if (2500 <= avars[3][2]) and (avars[avars[3][5]][19] > 0):
                                    avars[3][2] -= 2500
                                    anifr = 0
                                    medm = 1
                                    avars[avars[3][5]][19] -= 1
                                    pygame.mixer.stop()
                                    sound[13].play()
                                else:
                                    anifr = 0
                                    medm = 2
                                    pygame.mixer.stop()
                                    sound[12].play()
                            elif smd in range(8, 11):
                                if 2500 <= avars[3][2]:
                                    avars[3][2] -= 2500
                                    anifr = 0
                                    medm = 1
                                    b = 15 + (5 * (avars[avars[3][5]][1] > 1)) + (10 * (avars[avars[3][5]][1] > 2)) + (20 * (avars[avars[3][5]][1] > 3))
                                    avars[avars[3][5]][18] = [1, b, 99][smd - 8]
                                    pygame.mixer.stop()
                                    sound[13].play()
                                else:
                                    anifr = 0
                                    medm = 2
                                    pygame.mixer.stop()
                                    sound[12].play()
                            elif smd == 11:
                                if (5000 <= avars[3][2]) and (avars[avars[3][5]][2] > 691199):
                                    avars[3][2] -= 5000
                                    anifr = 0
                                    medm = 1
                                    avars[avars[3][5]][2] = [691200, 1382400][avars[avars[3][5]][1] == 6]
                                    pygame.mixer.stop()
                                    sound[13].play()
                                else:
                                    anifr = 0
                                    medm = 2
                                    pygame.mixer.stop()
                                    sound[12].play()
                        elif scr == 2 or scr == 3:
                            if 36 < mp[1] < 88 and 14 < mp[0] < 227:
                                if scr == 2:
                                    if sfd == ((mp[0] - 14) // 27) + (8 * ((mp[1] - 36) // 28)) + (fscr * 16):
                                        if fdlst[sfd][4] <= avars[3][2]:
                                            avars[3][2] -= fdlst[sfd][4]
                                            h = False
                                            a = 0
                                            for f in avars[3][4]:
                                                if f[0] == fdlst[sfd][0]:
                                                    if f[4] < 255:
                                                        h = True
                                                        break
                                                a += 1
                                            if h:
                                                avars[3][4][a][4] += 1
                                            else:
                                                n = []
                                                for i in range(11):
                                                    if i != 4:
                                                        n.append(fdlst[sfd][i])
                                                    else:
                                                        n.append(1)
                                                a = avars[3][4]
                                                a.append(n)
                                                avars[3][4] = a
                                            anifr = 0
                                            mrktm = 1
                                            pygame.mixer.stop()
                                            sound[13].play()
                                        else:
                                            anifr = 0
                                            mrktm = 2
                                            pygame.mixer.stop()
                                            sound[12].play()
                                    else:
                                        sfd = ((mp[0] - 14) // 27) + (8 * ((mp[1] - 36) // 28)) + (fscr * 16)
                                        if sfd > (len(fdlst) - 1):
                                            sfd = -1
                                else:
                                    if sit == ((mp[0] - 14) // 27) + (8 * ((mp[1] - 36) // 28)) + (iscr * 16):
                                        if itlst[sit][1] <= avars[3][2]:
                                            avars[3][2] -= itlst[sit][1]
                                            h = False
                                            a = 0
                                            for f in avars[3][9]:
                                                if f[0] == itlst[sit][0]:
                                                    if f[1] < 255:
                                                        h = True
                                                        break
                                                a += 1
                                            if h:
                                                avars[3][9][a][1] += 1
                                            else:
                                                n = []
                                                for i in range(9):
                                                    if i != 1:
                                                        n.append(itlst[sit][i])
                                                    else:
                                                        n.append(1)
                                                a = avars[3][9]
                                                a.append(n)
                                                avars[3][9] = a
                                            anifr = 0
                                            ishpm = 1
                                            pygame.mixer.stop()
                                            sound[13].play()
                                        else:
                                            anifr = 0
                                            ishpm = 2
                                            pygame.mixer.stop()
                                            sound[12].play()
                                    else:
                                        sit = ((mp[0] - 14) // 27) + (8 * ((mp[1] - 36) // 28)) + (iscr * 16)
                                        if sit > (len(itlst) - 1):
                                            sit = -1
                    elif anifr > 3:
                        pygame.mixer.stop()
                        sound[3].play()
                        anifr = 63
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
                if bx and (scr != 7):
                    clt += 1
        if chngsts:
            avars = statusup.chngsts(avars)
            if avars[avars[3][5]][20] or not avars[avars[3][5]][21]:
                return(avars, ret)
            chngsts = False
        if anifr < 63:
            anifr += 1
            if bx and (scr == 2 or scr == 3 or scr == 6) and anifr == 5:
                mrktm = 0
                ishpm = 0
                medm = 0
            elif bx and scr == 5 and anifr == 5:
                if remm == 1:
                    ret = 1
                    return(avars, ret)
                else:
                    remm = 0
        else:
            anifr = 0
            cret = 1
            ret = 1
            if not bx:
                bx = True
                if dest == 0:
                    gms = 0
                    scr = 1
                elif dest == 1:
                    sfd = -1
                    scr = 2
                elif dest == 2:
                    sit = -1
                    scr = 3
                elif dest == 3:
                    srm = 0
                    scr = 4
                elif dest == 4:
                    smd = 0
                    scr = 6
        if clt > 29:
            return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

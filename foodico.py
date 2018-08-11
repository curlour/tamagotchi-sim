import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import sounds
import borders
import shelve
import varsup
import statusup
import growth
import palette
import dirty
import mainscreen

def kitchen(avars, asprs, screen):

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

    inf = False

    swt = False
 
    scr = 0

    etng = 0

    fname = ''
    
    frms = 0

    chngsts = False

    foodl = [['Rice', 'Apple', 'Mandarin', 'Meat',
             'Milk', 'IceCream', 'Cake', 'Sake',
             'Scone', 'Pasta', 'SandW', 'Melon',
             'DrumS', 'Fries', 'Burger', 'Steak'],
             ['Bread', 'Pear', 'Juice', 'Fish',
             'ChMlk', 'Choco', 'Donut', 'Wine',
             'BCheese', 'Tacos', 'Hotdog', 'WMelon',
             'BBQ', 'PopCorn', 'Pizza', 'Sushi']]
    
    g = avars[avars[3][5]][14]
    if g < 0:
        g = 4294967296 + g
    a = format(g, '032b')

    l = int((a[16:19] + a[28]), 2)
    d = int((a[20:23] + a[29]), 2)

    #print(l)
    #print(d)
    #print(a[30])

    likes = [foodl[int(a[30])][l], foodl[int(a[30]) == 0][d]]

    alcohol = ['Wine', 'Sake']

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

    def drfd():
        global fdn
        if len(avars[3][4]) < (24 * (scr + 1)):
            a = len(avars[3][4]) - (24 * scr)
        else:
            a = 24
        while fdn < a:
            screen.blit(fsprs[(fdn + (24 * scr))][0], [(14 + ((fdn - (8 * (fdn // 8))) * 27)), (44 + (24 * (fdn // 8)))])
            screen.blit((lfnt.render(str(avars[3][4][(fdn + (24 * scr))][4]), 1, (0, 0, 100))), [(14 + ((fdn - (8 * (fdn // 8))) * 27)), (44 + (24 * (fdn // 8)))])
            fdn += 1

    def fdspr():
        fsprs = []
        a = 0
        while a < len(avars[3][4]):
            sl = []
            try:
                s = pygame.image.load("Sprites/Food/" + avars[3][4][a][0] + ".png").convert()
            except:
                s = pygame.image.load("CFood/" + avars[3][4][a][0] + ".png").convert()
            for i in range(3):
                b = pygame.Surface([24, 24])
                b.fill((0, 255, 255))
                b.blit(s, [-(24 * (i)), 0])
                b.set_colorkey((0, 255, 255))
                b.convert()
                sl.append(b)
            fsprs.append(sl)
            a += 1
        return(fsprs)

    def eatanim():
        flip = False
        if etng == 1:
            screen.blit(tbl, [88, 95])
            screen.blit(chair, [160, 95])
            if frms == 0:
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    spr = 16
                else:
                    spr = 17
            else:
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    spr = 16
                elif ((anifr / 24) - (anifr // 24)) < 0.5:
                    spr = 17
                else:
                    spr = 16
            if frms == 0:
                if ((anifr / 24) - (anifr // 24)) < 0.5:
                    screen.blit(fsprs[efdn][0], [123, 86])
                else:
                    screen.blit(fsprs[efdn][1], [123, 86])
            else:
                if ((anifr / 24) - (anifr // 24)) < 0.5:
                    screen.blit(fsprs[efdn][2], [123, 86])
            screen.blit(asprs[avars[3][5]][spr], [(156 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (84 + (32 - asprs[avars[3][5]][spr].get_height()))])
        elif etng == 2:
            if avars[avars[3][5]][1] > 3:
                spr = 9 + (anifr % 12 < 6)
                if anifr % 12 > 5:
                    screen.blit(cnf, [136, 82])
            else:
                if frms == 0:
                    spr = 9 - (3 * (anifr % 12 < 6))
                    if anifr % 12 > 5:
                        screen.blit(cnf, [136, 82])
                elif frms == 1:
                    spr = 8 + (6 * (anifr < 12))
                    if anifr > 11:
                        screen.blit(puke, [88, 114])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [(104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
        elif etng == 3:
            if likes[0] == fname:
                spr = 4 + (anifr % 12 < 6)
                if anifr % 12 < 6:
                    screen.blit(ht, [136, 82])
            else:
                spr = 6 + (2 * (anifr % 12 < 6))
                if anifr % 12 < 6:
                    screen.blit(ang, [136, 82])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [(104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
        else:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                spr = 14
            else:
                spr = 14
                flip = True
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [(104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 1, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()
    
    ang = pygame.image.load("Sprites/Misc/emo/ang.png").convert()
    cnf = pygame.image.load("Sprites/Misc/emo/conf.png").convert()
    ht = pygame.image.load("Sprites/Misc/emo/heart.png").convert()

    puke = pygame.image.load("Sprites/Misc/sick/puke.png").convert()

    hnb = pygame.image.load("Sprites/Misc/menu/hngf.png").convert()
    hpb = pygame.image.load("Sprites/Misc/menu/hpyf.png").convert()

    inti = pygame.image.load("Sprites/Misc/menu/inti.png").convert()
    styi = pygame.image.load("Sprites/Misc/menu/styi.png").convert()
    kndi = pygame.image.load("Sprites/Misc/menu/kndi.png").convert()
    humi = pygame.image.load("Sprites/Misc/menu/humi.png").convert()
    gori = pygame.image.load("Sprites/Misc/menu/gori.png").convert()
    pasi = pygame.image.load("Sprites/Misc/menu/pasi.png").convert()
    
    try:
        bck = pygame.image.load(avars[3][15]).convert()
        if bck.get_size() != (240, 160):
            raise Exception("Wrong size!")
    except pygame.error:
        bck = pygame.Surface([240, 160]).convert()
        bck.fill((51, 51, 204))
    try:
        tbl = pygame.image.load(avars[3][16]).convert()
        if tbl.get_size() != (64, 32):
            raise Exception("Wrong size!")
    except pygame.error:
        tbl = pygame.Surface([64, 32]).convert()
        tbl.fill((51, 51, 204))
    try:
        chair = pygame.image.load(avars[3][17]).convert()
        if chair.get_size() != (32, 32):
            raise Exception("Wrong size!")
    except pygame.error:
        chair = pygame.Surface([32, 32]).convert()
        chair.fill((51, 51, 204))

    fsprs = fdspr()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    lfnt = pygame.font.Font("Sprites/Misc/font/Tama1.ttf", 8)

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

    sound = sounds.imprtsnd(avars)

    clock = pygame.time.Clock()

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        screen.blit(bck, [0, 0])
        if bx or inf:
            screen.blit(textbox, [0, 24])
            if bx:
                screen.blit(scrli, [232, 128])
                global fdn
                fdn = 0
                drfd()
            else:
                screen.blit(fsprs[cfdn][0], [108, 32])
                screen.blit(hnb, [16, 56])
                if avars[3][4][cfdn][1] > 1:
                    screen.blit(hnb, [40, 56])
                    if avars[3][4][cfdn][1] > 2:
                        screen.blit(hnb, [64, 56])
                        if avars[3][4][cfdn][1] > 3:
                            screen.blit(hnb, [88, 56])
                if avars[3][4][cfdn][2] > 0:
                    screen.blit(hpb, [136, 56])
                    if avars[3][4][cfdn][2] > 1:
                        screen.blit(hpb, [160, 56])
                        if avars[3][4][cfdn][2] > 2:
                            screen.blit(hpb, [184, 56])
                            if avars[3][4][cfdn][2] > 3:
                                screen.blit(hpb, [208, 56])
                if avars[3][4][cfdn][5] > 0:
                    screen.blit(inti, [32, 80])
                if avars[3][4][cfdn][6] > 0:
                    screen.blit(styi, [64, 80])
                if avars[3][4][cfdn][7] > 0:
                    screen.blit(kndi, [96, 80])
                if avars[3][4][cfdn][8] > 0:
                    screen.blit(humi, [128, 80])
                if avars[3][4][cfdn][9] > 0:
                    screen.blit(gori, [160, 80])
                if avars[3][4][cfdn][10] > 0:
                    screen.blit(pasi, [192, 80])
                screen.blit((fnt.render("MOVE", 1, (0, 0, 100))), [95, 98])
                screen.blit((fnt.render("TRASH", 1, (0, 0, 100))), [89, 114])
        else:
            eatanim()
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
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if scr != ((len(avars[3][4]) - 1) // 24):
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
                            scr = ((len(avars[3][4]) - 1) // 24)
                        clt = 0
                elif pb == 1:
                    clt = 0
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            sound[4].play()
                            return(avars)
                    if bx:
                        if 44 < mp[1] < 116 and 14 < mp[0] < 230 and (mp[0] - (14 + (27 * ((mp[0] - 14) // 27)))) < 24:
                            efdn = ((mp[0] - 14) // 27) + (8 * ((mp[1] - 44) // 24)) + (scr * 24)
                            if efdn < len(avars[3][4]):
                                if not swt:
                                    sound[3].play()
                                    anifr = 23
                                    bx = False
                                    frms = -1
                                    if avars[avars[3][5]][16] < 6 and (avars[avars[3][5]][1] > 2 or avars[3][4][efdn][0] not in alcohol):
                                        etng = 1
                                        h = avars[avars[3][5]][17]
                                        if (avars[avars[3][5]][1] > 3 or avars[3][4][efdn][0] not in alcohol):
                                            if (avars[avars[3][5]][16] + avars[3][4][efdn][1]) < 6:
                                                avars[avars[3][5]][16] += avars[3][4][efdn][1]
                                            else:
                                                avars[avars[3][5]][16] = 6
                                            if (avars[avars[3][5]][17] + avars[3][4][efdn][2]) < 6:
                                                avars[avars[3][5]][17] += avars[3][4][efdn][2]
                                            else:
                                                avars[avars[3][5]][17] = 6
                                            if (avars[avars[3][5]][18] + avars[3][4][efdn][3]) < 99:
                                                avars[avars[3][5]][18] += avars[3][4][efdn][3]
                                            else:
                                                avars[avars[3][5]][18] = 99
                                        avars[avars[3][5]][5] += avars[3][4][efdn][5]
                                        avars[avars[3][5]][6] += avars[3][4][efdn][6]
                                        avars[avars[3][5]][7] += avars[3][4][efdn][7]
                                        avars[avars[3][5]][8] += avars[3][4][efdn][8]
                                        avars[avars[3][5]][9] += avars[3][4][efdn][9]
                                        avars[avars[3][5]][10] += avars[3][4][efdn][10]
                                        fname = avars[3][4][efdn][0]
                                        if likes[0] == fname:
                                            if (avars[avars[3][5]][17] + 2) < 6:
                                                avars[avars[3][5]][17] += 2
                                            else:
                                                avars[avars[3][5]][17] = 6
                                        elif likes[1] == fname:
                                            avars[avars[3][5]][17] = h
                                            if (avars[avars[3][5]][17] - 2) > 0:
                                                avars[avars[3][5]][17] -= 2
                                            else:
                                                avars[avars[3][5]][17] = 0
                                        if (avars[avars[3][5]][15] == 163) and (len(avars[avars[3][5]][25]) > 0) and (len(avars[avars[3][5]][26]) > 0) and (avars[3][4][efdn][0] == 'Sake'):
                                            if ([avars[avars[3][5]][25][1], avars[avars[3][5]][26][1]] in [[379, 380], [380, 379]]) and (avars[avars[3][5]][24][2] == 57):
                                                avars[avars[3][5]][1] = 5
                                                avars = growth.grw(avars)
                                                asprs = aspr()
                                        if (avars[avars[3][5]][15] == 167) and (len(avars[avars[3][5]][25]) > 0) and (len(avars[avars[3][5]][26]) > 0) and (avars[3][4][efdn][0] == 'Tea'):
                                            if ([avars[avars[3][5]][25][1], avars[avars[3][5]][26][1]] in [[383, 384], [384, 383]]) and ((avars[avars[3][5]][7] + avars[avars[3][5]][10]) > 999):
                                                avars[avars[3][5]][1] = 5
                                                avars = growth.grw(avars)
                                                asprs = aspr()
                                        if (avars[avars[3][5]][15] == 204) and (avars[avars[3][5]][10] < 100) and (avars[avars[3][5]][7] > 500) and (avars[3][4][efdn][0] == 'Cake'):
                                            avars[avars[3][5]][1] = 5
                                            avars = growth.grw(avars)
                                            asprs = aspr()
                                        avars[3][4][efdn][4] -= 1
                                        if avars[3][4][efdn][4] == 0:
                                            a = avars[3][4]
                                            a.pop(efdn)
                                            avars[3][4] = a
                                else:
                                    if efdn == cfdn:
                                        sound[12].play()
                                    else:
                                        sound[3].play()
                                        a = avars[3][4]
                                        a[efdn], a[cfdn] = a[cfdn], a[efdn]
                                        avars[3][4] = a
                                    swt = False
                                    fsprs = fdspr()
                    elif inf:
                        if 32 < mp[1] < 56 and 108 < mp[0] < 132:
                            sound[3].play()
                            inf = False
                            bx = True
                        if 98 < mp[1] < 110 and 95 < mp[0] < 145:
                            sound[3].play()
                            swt = True
                            inf = False
                            bx = True
                        if 114 < mp[1] < 126 and 89 < mp[0] < 153:
                            sound[3].play()
                            avars[3][4][cfdn][4] -= 1
                            if avars[3][4][cfdn][4] == 0:
                                a = avars[3][4]
                                a.pop(cfdn)
                                avars[3][4] = a
                            if len(avars[3][4]) > 0:
                                inf = False
                                bx = True
                                fsprs = fdspr()
                                if ((len(avars[3][4]) - 1) // 24) < scr:
                                    scr = (len(avars[3][4]) - 1) // 24
                            else:
                                return(avars)
                    elif frms != 0:
                        if len(avars[3][4]) > 0:
                            etng = 0
                            bx = True
                            frms = 0
                            fname = ''
                            fsprs = fdspr()
                        else:
                            return(avars)
                if pb == 3:
                    clt = 0
                    if bx:
                        if 44 < mp[1] < 116 and 14 < mp[0] < 230 and (mp[0] - (14 + (27 * ((mp[0] - 14) // 27)))) < 24:
                            cfdn = ((mp[0] - 14) // 27) + (8 * ((mp[1] - 44) // 24)) + (scr * 24)
                            if cfdn < len(avars[3][4]):
                                sound[3].play()
                                anifr = 23
                                bx = False
                                inf = True
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
        if anifr < 23:
            anifr += 1
        else:
            if not bx and not inf:
                frms += 1
                if frms == 2:
                    if (etng == 1 and (fname not in alcohol) and (fname not in likes)) or etng == 0 or etng == 3 or (etng == 2 and (fname not in likes)):
                        if len(avars[3][4]) > 0:
                            etng = 0
                            bx = True
                            frms = 0
                            fname = ''
                            fsprs = fdspr()
                            if ((len(avars[3][4]) - 1) // 24) < scr:
                                scr = (len(avars[3][4]) - 1) // 24
                        else:
                            return(avars)
                    elif etng == 1 and (fname in alcohol):
                        sound[5].play()
                        frms = 0
                        etng = 2
                    else:
                        sound[12 - (3 * (likes[0] == fname))].play()
                        frms = 0
                        etng = 3
            anifr = 0
        if clt > 29:
            return(avars)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

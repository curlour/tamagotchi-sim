import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import shelve
import pyperclip
import sounds
import varsup
import borders
import growth
import palette
import statusup
from random import *
import dirty
import mainscreen
import parentg

def phom(avars, asprs, screen):

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

    bx = False
    name = False

    scr = (format(avars[avars[3][5]][14], '032b')[30] == '0')
    sibin = 0
    if len(avars[avars[3][5]][26]) > 0:
        for a in avars[avars[3][5]][32][2:]:
            if (format(a[3], '032b')[16:28]) == (format(avars[avars[3][5]][14], '032b')[16:28]):
                sibin = avars[avars[3][5]][32].index(a)
                if avars[avars[3][5]][32][sibin][8] < 80:
                    avars[avars[3][5]][32][sibin][8] += 1
                if avars[avars[3][5]][32][sibin][0] == avars[3][0]:
                    for i in [0, 1, 2]:
                        if len(avars[i]) > 0:
                            if avars[i][14] == avars[avars[3][5]][32][sibin][3]:
                                if avars[i][32][0][8] < 80:
                                    avars[i][32][0][8] += 1
                                if avars[i][32][1][8] < 80:
                                    avars[i][32][1][8] += 1
                                for b in avars[i][32][2:]:
                                    if b[3] == avars[avars[3][5]][14]:
                                        c = avars[i][32].index(b)
                                        if avars[i][32][c][8] < 80:
                                            avars[i][32][c][8] += 1
                scr = 1

    chngsts = False

    ret = 1

    def chsprs(chara, dirt, g):
        sprs = []
        if chara > 0:
            try:
                bs = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "b.png")
                ss = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "s.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, g, opal)
                if dirt:
                    bs = dirty.dirt(bs)
                ss = palette.palch(ss, g, opal)
            except:
                bs = pygame.image.load("Sprites/NPC/Nazotchi.png")
                ss = pygame.image.load("Sprites/NPC/Nazo.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, g, opal)
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
        else:
            bs = pygame.image.load("Sprites/Eggs/egg_" + str(-chara) + "b.png")
            ss = pygame.image.load("Sprites/Eggs/egg_" + str(-chara) + "s.png")
            for i in range(2):
                a = pygame.Surface([16, 16])
                a.fill((0, 255, 255))
                a.blit(ss, [-(16 * (i % 2)), 0])
                a.set_colorkey((0, 255, 255))
                a.convert()
                sprs.append(a)
            for i in range(4):
                spr = pygame.Surface([24, 24]).convert()
                spr.fill((0, 255, 255))
                spr.blit(bs, [-(24 * (i % 2)), -(24 * (i // 2))])
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

    def nchild():
        negg = []
        if len(avars[avars[3][5]][26]) > 0:
            l = [choice([avars[avars[3][5]][25][4], avars[avars[3][5]][25][5]]),
                 choice([avars[avars[3][5]][26][2], avars[avars[3][5]][26][3]])]
        else:
            l = [avars[avars[3][5]][12], avars[avars[3][5]][13]]
        if avars[avars[3][5]][0] < 9:
            if "no" in l:
                if l.count("no") == 2:
                    negg.append(8)
                else:
                    negg.append(1)
                negg.append(l.pop(l.index("no")))
                negg.append(l[0])
            elif "ma" in l:
                if l.count("ma") == 2:
                    negg.append(5)
                    negg.append(l.pop(l.index("ma")))
                else:
                    if "me" in l:
                        negg.append(7)
                        negg.append(l.pop(l.index("me")))
                    else:
                        negg.append(2)
                        negg.append(l.pop(l.index("ma")))
                negg.append(l[0])
            elif "me" in l:
                if l.count("me") == 2:
                    negg.append(6)
                    negg.append(l.pop(l.index("me")))
                else:
                    negg.append(4)
                    negg.append(l.pop(l.index("ku")))
                negg.append(l[0])
            else:
                negg.append(3)
                negg.append(l.pop(l.index("ku")))
                negg.append(l[0])
        else:
            negg.append(avars[avars[3][5]][0])
            negg.append(ced[str(avars[avars[3][5]][0])])
            negg.append(0)
        y = format(avars[avars[3][5]][25][0], '032b')
        m = format(avars[avars[3][5]][26][0], '032b')
        a = (int(y[:16], 2) & int(m[:16], 2))
        b = ((int(y[:16], 2) ^ int(m[:16], 2)) & randint(0, 65535))
        r = format((a | b), '016b') + format((int(y[16:28], 2) ^ int(m[16:28], 2)), '012b') + format(randint(0, 15), '04b')
        #print('%08x' % int(y, 2))
        #print('%08x' % int(m, 2))
        #print('%08x' % int(r, 2))
        negg.append(int(r, 2))
        return(negg)
    
    ced = {}
    for f in os.listdir("CCharacters"):
        if f.endswith(".txt") and (f != ("Names.txt")):
            n = open(("CCharacters/" + f), 'r')
            t = n.read()
            i = t.index('/')
            j = int(t[:i])
            if os.path.isfile("Sprites/Eggs/egg_" + str(j) + "b.png") and os.path.isfile("Sprites/Eggs/egg_" + str(j) + "s.png") and (8 < j < 16):
                ced.update({str(j): f[:(len(f) - 4)]})

    def impvrs():
        d = shelve.open('save_db')
        if ('egg1' in d):
            var1 = [d['egg1'], d['charag1'], d['time1'], d['gene1'], d['poo1'], d['int1'], d['sty1'], d['knd1'], d['hum1'], d['gor1'], d['pas1'], d['grp1'], d['grpf1'],
                    d['grpm1'], d['gender1'], d['chara1'], d['hungry1'], d['happy1'], d['weight1'], d['caremiss1'], d['sick1'], d['awake1'], d['chname1'], d['room1'],
                    d['stages1'], d['parent1'], d['pspouse1'], d['gparent1'], d['gpspouse1'], d['agen1'], d['dirty1'], d['edu1'], d['frnd1'], d['pttrain1']]
        else:
            var1 = []

        if ('egg2' in d):
            var2 = [d['egg2'], d['charag2'], d['time2'], d['gene2'], d['poo2'], d['int2'], d['sty2'], d['knd2'], d['hum2'], d['gor2'], d['pas2'], d['grp2'], d['grpf2'],
                    d['grpm2'], d['gender2'], d['chara2'], d['hungry2'], d['happy2'], d['weight2'], d['caremiss2'], d['sick2'], d['awake2'], d['chname2'], d['room2'],
                    d['stages2'], d['parent2'], d['pspouse2'], d['gparent2'], d['gpspouse2'], d['agen2'], d['dirty2'], d['edu2'], d['frnd2'], d['pttrain2']]
        else:
            var2 = []

        if ('egg3' in d):
            var3 = [d['egg3'], d['charag3'], d['time3'], d['gene3'], d['poo3'], d['int3'], d['sty3'], d['knd3'], d['hum3'], d['gor3'], d['pas3'], d['grp3'], d['grpf3'],
                    d['grpm3'], d['gender3'], d['chara3'], d['hungry3'], d['happy3'], d['weight3'], d['caremiss3'], d['sick3'], d['awake3'], d['chname3'], d['room3'],
                    d['stages3'], d['parent3'], d['pspouse3'], d['gparent3'], d['gpspouse3'], d['agen3'], d['dirty3'], d['edu3'], d['frnd3'], d['pttrain3']]
        else:
            var3 = []

        gvar = [d['uname'], d['bday'], d['money'], d['speed'], d['food'], d['selchara'], d['hour'], d['secs'], d['vol'], d['item'], d['grave'], d['mail'],
                d['lstdt'], d['border'], d['chegg'], d['kitchen'], d['table'], d['chair'], d['wc'], d['toilet'], d['btoilet'], d['bathr'], d['bath'], d['dex']]

        avars = [var1, var2, var3, gvar]
        d.close()
        return(avars)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    house = pygame.image.load("Sprites/Misc/bg/parenti.png").convert()

    if (avars[avars[3][5]][2] - avars[avars[3][5]][32][0][7][1] + avars[avars[3][5]][32][0][7][0]) > 1382400 and avars[avars[3][5]][32][0][2] < 379:
        a = 6
        gn = avars[avars[3][5]][3] - 1
        l = [0, 0, 0, 0, 0, 0]
        l[int(format(avars[avars[3][5]][14], '032b')[16:28], 2) % 6] += 500
        ov = [[0, a, 0, gn, 0, l[0], l[1], l[2], l[3], l[4], l[5], avars[avars[3][5]][32][0][6], avars[avars[3][5]][32][0][5], avars[avars[3][5]][32][0][4], avars[avars[3][5]][32][0][3], \
               avars[avars[3][5]][32][0][2], 0, 0, 22, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 4], [], [], [0, 0, 0, 0, 0, 0]]
        ov = growth.grw(ov)
        avars[avars[3][5]][32][0][2] = ov[0][15]
        avars[avars[3][5]][32][0][5] = ov[0][12]
        avars[avars[3][5]][32][0][4] = ov[0][13]
    if avars[avars[3][5]][32][0][8] < 80:
        avars[avars[3][5]][32][0][8] += 1

    if len(avars[avars[3][5]][26]) > 0:
        if (avars[avars[3][5]][2] - avars[avars[3][5]][32][1][7][1] + avars[avars[3][5]][32][1][7][0]) > 1382400 and avars[avars[3][5]][32][1][2] < 379:
            a = 6
            gn = avars[avars[3][5]][3] - 1
            l = [0, 0, 0, 0, 0, 0]
            l[int(format(avars[avars[3][5]][14], '032b')[16:28], 2) % 6] += 500
            ov = [[0, a, 0, gn, 0, l[0], l[1], l[2], l[3], l[4], l[5], avars[avars[3][5]][32][1][6], avars[avars[3][5]][32][1][5], avars[avars[3][5]][32][1][4], avars[avars[3][5]][32][1][3], \
                   avars[avars[3][5]][32][1][2], 0, 0, 22, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 4], [], [], [0, 0, 0, 0, 0, 0]]
            ov = growth.grw(ov)
            avars[avars[3][5]][32][1][2] = ov[0][15]
            avars[avars[3][5]][32][1][5] = ov[0][12]
            avars[avars[3][5]][32][1][4] = ov[0][13]
        if avars[avars[3][5]][32][1][8] < 80:
            avars[avars[3][5]][32][1][8] += 1

    eggs = chsprs(-avars[avars[3][5]][0], 0, 0)
    parents = chsprs(avars[avars[3][5]][32][0][2], 0, avars[avars[3][5]][25][0])
    aparents = chsprs(avars[avars[3][5]][25][1], 0, avars[avars[3][5]][25][0])
    if len(avars[avars[3][5]][26]) > 0:
        spouses = chsprs(avars[avars[3][5]][32][1][2], 0, avars[avars[3][5]][26][0])
        aspouses = chsprs(avars[avars[3][5]][26][1], 0, avars[avars[3][5]][26][0])
    if sibin > 0:
        sibls = chsprs(avars[avars[3][5]][32][sibin][2], 0, avars[avars[3][5]][32][sibin][3])

    if scr == 0:
        negg = nchild()
        #print(negg)
        e = avars[3][14]
        e = e[:(negg[0] - 1)] + '1' + e[(negg[0]):]
        avars[3][14] = e
        neggs = chsprs(-negg[0], 0, 0)
        babd = [[negg[0], 1, 0, avars[avars[3][5]][3], 0, 0, 0, 0, 0, 0, 0, negg[1], negg[1], negg[2], negg[3], \
               0, 0, 0, 5, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0], [], [], [0, 0, 0, 0, 0, 0]]
        babd = growth.grw(babd)
        babs = chsprs(babd[0][15], 0, babd[0][14])

    frame = pygame.Surface((24, 24)).convert()
    frame.blit(house, [0, 0])

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    keeptx = fnt.render("KEEP?", 1, (0, 0, 100))
    nametx = fnt.render("NAME:", 1, (0, 0, 100))
    yest = fnt.render("YES", 1, (0, 0, 100))
    notx = fnt.render("NO", 1, (0, 0, 100))
    nw = ""
    nmwr = fnt.render(nw, 1, (0, 0, 100))
    ne = False

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

    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if not bx:
            screen.blit(house, [0, 0])
            screen.blit(aparents[1], [13, 62])
            screen.blit(eggs[0], [29, 62])
            if len(avars[avars[3][5]][26]) > 0:
                screen.blit(aspouses[1], [45, 62])
            screen.blit(frame, [32, 28])
            screen.blit(asprs[avars[3][5]][1], [36, 32])
            if sibin > 0:
                screen.blit(frame, [56, 28])
                screen.blit(sibls[1], [60, 32])
            if scr == 0:
                if anifr < 24:
                    screen.blit(pygame.transform.flip(spouses[4 + (anifr % 12 > 5)], 1, 0), [80, 90])
                    screen.blit(pygame.transform.flip(parents[4 + (anifr % 12 < 6)], 1, 0), [56, 98])
                    screen.blit(asprs[avars[3][5]][4 + (5 * (anifr % 12 > 5))], [(152 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][3].get_height()))])
                    screen.blit(neggs[2 + (anifr % 12 > 5)], [108, 106])
                elif anifr < 96:
                    if anifr == 24:
                        pygame.mixer.stop()
                        sound[7].play()
                    screen.blit(pygame.transform.flip(spouses[4 + (5 * (anifr % 12 > 5))], 1, 0), [80, 90])
                    screen.blit(pygame.transform.flip(parents[4 + (5 * (anifr % 12 < 6))], 1, 0), [56, 98])
                    screen.blit(asprs[avars[3][5]][4 + (5 * (anifr % 12 > 5))], [(152 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][3].get_height()))])
                    screen.blit(neggs[4], [(107 + (2 * (anifr % 12 > 5))), 106])
                elif anifr < 120:
                    if anifr == 96:
                        pygame.mixer.stop()
                        sound[8].play()
                    screen.blit(pygame.transform.flip(spouses[5], 1, 0), [80, 90])
                    screen.blit(pygame.transform.flip(parents[5], 1, 0), [56, 98])
                    screen.blit(asprs[avars[3][5]][5], [(152 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][3].get_height()))])
                    screen.blit(babs[5], [112, 107])
                    screen.blit(neggs[5], [108, 106])
                else:
                    screen.blit(pygame.transform.flip(spouses[11 + (anifr % 12 > 5)], 1, 0), [80, 90])
                    screen.blit(pygame.transform.flip(parents[11 + (anifr % 12 < 6)], 1, 0), [56, 98])
                    screen.blit(asprs[avars[3][5]][11 + (anifr % 12 > 5)], [(152 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][3].get_height()))])
                    screen.blit(babs[6 + (anifr % 12 > 5)], [112, 114])
            elif scr == 1:
                if len(avars[avars[3][5]][26]) > 0:
                    screen.blit(pygame.transform.flip(spouses[4 + (anifr % 12 > 5)], 1, 0), [80, 90])
                if sibin > 0:
                    screen.blit(sibls[4 + (anifr % 12 < 6)], [(128 + ((32 - sibls[3].get_width()) // 2)), (90 + (32 - sibls[3].get_height()))])
                screen.blit(pygame.transform.flip(parents[4 + (anifr % 12 < 6)], 1, 0), [56, 98])
                screen.blit(asprs[avars[3][5]][4 + (anifr % 12 > 5)], [(152 + ((32 - asprs[avars[3][5]][3].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][3].get_height()))])
        else:
            screen.blit(textbox, [0, 24])
            if not name:
                screen.blit(keeptx, [8, 66])
                screen.blit(yest, [107, 82])
                screen.blit(notx, [164, 82])
            else:
                screen.blit(nametx, [8, 66])
                screen.blit(nmwr, [8, 82])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
        for event in pygame.event.get():
            if event.type == QUIT:
                varsup.updtvrs(avars)
                kr = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if name and bx:
                    if pygame.K_a <= event.key <= pygame.K_z:
                        ltr = chr(event.key)
                        if len(nw) < 8:
                            nw = (nw + str(ltr)).upper()
                        nmwr = fnt.render(nw, 1, (0, 0, 100))
                        ne = True
                    if event.key == pygame.K_BACKSPACE:
                        if len(nw) != 0:
                            if len(nw) == 1:
                                ne = False
                            nw = nw[:len(nw) - 1]
                            nmwr = fnt.render(nw, 1, (0, 0, 100))
                    if event.key == pygame.K_RETURN:
                        if ne:
                            pygame.mixer.stop()
                            sound[0].play()
                            pcharinfo = [avars[3][0], nw, babd[0][15], babd[0][14], babd[0][13], babd[0][12], babd[0][11], [0, avars[avars[3][5]][2]], 0]
                            f = avars[avars[3][5]][32]
                            f.append(pcharinfo)
                            avars[avars[3][5]][32] = f
                            x = avars[3][23]
                            x = format(x, '0384b')
                            x = x[:(babd[0][15] - 1)] + '1' + x[babd[0][15]:]
                            avars[3][23] = int(x, 2)
                            y = [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14], \
                                 avars[avars[3][5]][13], avars[avars[3][5]][12], avars[avars[3][5]][11], avars[avars[3][5]][2], 0]
                            varsup.updtvrs(avars)
                            d = shelve.open('save_db')
                            if (not ('egg1' in d)) or d['egg1'] == None:
                                for file in os.listdir("Sprites/Misc/mail/tm1"):
                                    os.remove("Sprites/Misc/mail/tm1/" + file)
                                d['egg1'] = babd[0][0]
                                d['charag1'] = babd[0][1]
                                d['time1'] = 0
                                d['gene1'] = babd[0][3]
                                d['poo1'] = 0
                                d['int1'] = babd[0][5]
                                d['sty1'] = babd[0][6]
                                d['knd1'] = babd[0][7]
                                d['hum1'] = babd[0][8]
                                d['gor1'] = babd[0][9]
                                d['pas1'] = babd[0][10]
                                d['grp1'] = babd[0][11]
                                d['grpf1'] = babd[0][12]
                                d['grpm1'] = babd[0][13]
                                d['gender1'] = babd[0][14]
                                d['chara1'] = babd[0][15]
                                d['hungry1'] = 0
                                d['happy1'] = 0
                                d['weight1'] = 5
                                d['caremiss1'] = 0
                                d['sick1'] = False
                                d['awake1'] = True
                                d['chname1'] = nw
                                d['stages1'] = []
                                d['parent1'] = avars[avars[3][5]][25]
                                d['pspouse1'] = avars[avars[3][5]][26]
                                d['gparent1'] = avars[avars[3][5]][27]
                                d['gpspouse1'] = avars[avars[3][5]][28]
                                d['agen1'] = avars[avars[3][5]][29]
                                d['dirty1'] = 0
                                d['edu1'] = 0
                                d['frnd1'] = [avars[avars[3][5]][32][0], avars[avars[3][5]][32][1], y]
                                d['pttrain1'] = 0
                                d['selchara'] = 0
                            elif (not ('egg2' in d)):
                                for file in os.listdir("Sprites/Misc/mail/tm2"):
                                    os.remove("Sprites/Misc/mail/tm2/" + file)
                                d['egg2'] = babd[0][0]
                                d['charag2'] = babd[0][1]
                                d['time2'] = 0
                                d['gene2'] = babd[0][3]
                                d['poo2'] = 0
                                d['int2'] = babd[0][5]
                                d['sty2'] = babd[0][6]
                                d['knd2'] = babd[0][7]
                                d['hum2'] = babd[0][8]
                                d['gor2'] = babd[0][9]
                                d['pas2'] = babd[0][10]
                                d['grp2'] = babd[0][11]
                                d['grpf2'] = babd[0][12]
                                d['grpm2'] = babd[0][13]
                                d['gender2'] = babd[0][14]
                                d['chara2'] = babd[0][15]
                                d['hungry2'] = 0
                                d['happy2'] = 0
                                d['weight2'] = 5
                                d['caremiss2'] = 0
                                d['sick2'] = False
                                d['awake2'] = True
                                d['chname2'] = nw
                                d['stages2'] = []
                                d['parent2'] = avars[avars[3][5]][25]
                                d['pspouse2'] = avars[avars[3][5]][26]
                                d['gparent2'] = avars[avars[3][5]][27]
                                d['gpspouse2'] = avars[avars[3][5]][28]
                                d['agen2'] = avars[avars[3][5]][29]
                                d['dirty2'] = 0
                                d['edu2'] = 0
                                d['frnd2'] = [avars[avars[3][5]][32][0], avars[avars[3][5]][32][1], y]
                                d['pttrain2'] = 0
                                d['selchara'] = 1
                            elif (not ('egg3' in d)):
                                for file in os.listdir("Sprites/Misc/mail/tm3"):
                                    os.remove("Sprites/Misc/mail/tm3/" + file)
                                d['egg3'] = babd[0][0]
                                d['charag3'] = babd[0][1]
                                d['time3'] = 0
                                d['gene3'] = babd[0][3]
                                d['poo3'] = 0
                                d['int3'] = babd[0][5]
                                d['sty3'] = babd[0][6]
                                d['knd3'] = babd[0][7]
                                d['hum3'] = babd[0][8]
                                d['gor3'] = babd[0][9]
                                d['pas3'] = babd[0][10]
                                d['grp3'] = babd[0][11]
                                d['grpf3'] = babd[0][12]
                                d['grpm3'] = babd[0][13]
                                d['gender3'] = babd[0][14]
                                d['chara3'] = babd[0][15]
                                d['hungry3'] = 0
                                d['happy3'] = 0
                                d['weight3'] = 5
                                d['caremiss3'] = 0
                                d['sick3'] = False
                                d['awake3'] = True
                                d['chname3'] = nw
                                d['stages3'] = []
                                d['parent3'] = avars[avars[3][5]][25]
                                d['pspouse3'] = avars[avars[3][5]][26]
                                d['gparent3'] = avars[avars[3][5]][27]
                                d['gpspouse3'] = avars[avars[3][5]][28]
                                d['agen3'] = avars[avars[3][5]][29]
                                d['dirty3'] = 0
                                d['edu3'] = 0
                                d['frnd3'] = [avars[avars[3][5]][32][0], avars[avars[3][5]][32][1], y]
                                d['pttrain3'] = 0
                                d['selchara'] = 2
                            d.close()
                            avars = impvrs()
                            return(avars, ret)
            if event.type == MOUSEBUTTONDOWN:
                mp = event.pos
                d = (screen.get_size()[0] // 240)
                mp = ((mp[0] // d), (mp[1] // d))
                pb = event.button
                if pb == 1:
                    if 138 < mp[1] < 158 and scr == 1:
                        if 228 < mp[0] < 240:
                            pygame.mixer.stop()
                            sound[4].play()
                            return(avars, ret)
                        elif 212 < mp[0] < 224:
                            pygame.mixer.stop()
                            sound[4].play()
                            ret = 0
                            return(avars, ret)
                    if 24 < mp[1] < 136 and scr == 1:
                        fsps = [parents]
                        if len(avars[avars[3][5]][26]) > 0:
                            fsps.append(spouses)
                            if sibin > 0:
                                fsps.append(sibls)
                        avars, ret = parentg.game(avars, asprs, screen, fsps)
                        return(avars, ret)
                    if bx and not name and 80 < mp[1] < 96:
                        if 164 < mp[0] < 188:
                            pygame.mixer.stop()
                            sound[4].play()
                            pcharinfo = ["PARK", "", babd[0][15], babd[0][14], babd[0][13], babd[0][12], babd[0][11], [0, avars[avars[3][5]][2]], 0]
                            f = avars[avars[3][5]][32]
                            f.append(pcharinfo)
                            avars[avars[3][5]][32] = f
                            return(avars, ret)
                        elif 107 < mp[0] < 139:
                            pygame.mixer.stop()
                            sound[3].play()
                            name = True
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
            if avars[avars[3][5]][20] or not avars[avars[3][5]][21]:
                return(avars, ret)
            chngsts = False
        if anifr < 143:
            anifr += 1
        else:
            anifr = 0
            if scr == 0 and not bx:
                if not (len(avars[0]) > 0 and len(avars[1]) > 0 and len(avars[2]) > 0):
                    bx = True
                else:
                    pygame.mixer.stop()
                    sound[4].play()
                    pcharinfo = ["PARK", "", babd[0][15], babd[0][14], babd[0][13], babd[0][12], babd[0][11], [0, avars[avars[3][5]][2]], 0]
                    f = avars[avars[3][5]][32]
                    f.append(pcharinfo)
                    avars[avars[3][5]][32] = f
                    return(avars, ret)
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

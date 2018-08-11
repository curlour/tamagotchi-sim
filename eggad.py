import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import shelve
import pyperclip
import sounds
import borders
import varsup
import palette
import statusup
from random import *
import dirty
import palette
import nextgen
import mainscreen

def adop(avars, asprs, screen):

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

    spclk = False

    ret = 1

    scr = 0
    sure = False
    cen = 0

    chngsts = False

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

    def nchild(cen):
        negg = [eggl[cen]]
        if eggl[cen] < 9:
            negg.append(["no", "ma", "ku", "ku", "ma", "me", "me", "no"][eggl[cen] - 1])
            negg.append([choice(["ku", "me", "ma"]), "ku", "ku", "me", "ma", "me", "ma", "no"][eggl[cen] - 1])
        else:
            negg.append(ced[str(eggl[cen])])
            negg.append("")
        r = format(randint(0, 4294967295), '032b')
        r = r[:30] + '0' + r[31]
        negg.append(int(r, 2))
        return(negg)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    eggl = []
    ced = {}
    for i in range(8):
        if avars[3][14][i] == '1':
            eggl.append(i + 1)
    for f in os.listdir("CCharacters"):
        if f.endswith(".txt") and (f != ("Names.txt")):
            n = open(("CCharacters/" + f), 'r')
            t = n.read()
            i = t.index('/')
            j = int(t[:i])
            if os.path.isfile("Sprites/Eggs/egg_" + str(j) + "b.png") and os.path.isfile("Sprites/Eggs/egg_" + str(j) + "s.png") and (8 < j < 16):
                eggl.append(j)
                ced.update({str(j): f[:(len(f) - 4)]})

    eggs = []
    for e in eggl:
        s = chsprs(-e, 0, 0)
        eggs.append(s)

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    suretx = fnt.render("SURE?", 1, (0, 0, 100))
    yest = fnt.render("YES", 1, (0, 0, 100))
    notx = fnt.render("NO", 1, (0, 0, 100))

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
        screen.blit(textbox, [0, 24])
        if not sure:
            screen.blit(scrli, [232, 128])
            for i in eggs[(scr * 24):((scr + 1) * 24)]:
                j = eggs.index(i) % 24
                screen.blit(i[2], [(14 + (27 * (j % 8))), (44 + (24 * (j // 8)))])
        else:
            screen.blit(suretx, [8, 66])
            screen.blit(yest, [107, 82])
            screen.blit(notx, [164, 82])
            screen.blit(eggs[cen][2], [108, 96])
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
                    pygame.mixer.stop()
                    sound[2].play()
                    if scr != ((len(eggl) - 1) // 24):
                        scr += 1
                    else:
                        scr = 0
                elif pb == 5:
                    pygame.mixer.stop()
                    sound[2].play()
                    if scr != 0:
                        scr -= 1
                    else:
                        scr = ((len(eggl) - 1) // 24)
                elif pb == 1:
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
                    if not sure:
                        if (14 < mp[0] < 221) and (((mp[0] - 14) % 27) < 24) and (44 < mp[1] < 116):
                            cen = ((mp[0] - 14) // 27) + (((mp[1] - 44) // 24) * 8) + (scr * 24)
                            if cen < len(eggl):
                                pygame.mixer.stop()
                                sound[3].play()
                                sure = True
                    elif 80 < mp[1] < 96:
                        if 164 < mp[0] < 188:
                            pygame.mixer.stop()
                            sound[4].play()
                            sure = False
                        elif 107 < mp[0] < 139:
                            pygame.mixer.stop()
                            sound[3].play()
                            negg = nchild(cen)
                            mate = []
                            avars = nextgen.bir(avars, asprs, mate, negg, screen)
                            return(avars, ret)
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
        if anifr < 24:
            anifr += 1
        else:
            anifr = 0
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

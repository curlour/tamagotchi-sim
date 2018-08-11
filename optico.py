import pygame, sys
import os
import shutil
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
import mainscreen
import eggsel
import shutil

def options(avars, asprs, screen):

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

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 9, 0)

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

    scrli = pygame.image.load("Sprites/Misc/txtbox/scrli.png").convert()

    clock = pygame.time.Clock()

    brdlst = ["Sprites/Misc/bg/borders1.png", "Sprites/Misc/bg/borderso.png", "Sprites/Misc/bg/bordersm.png",
             "Sprites/Misc/bg/bordersn.png", "Sprites/Misc/bg/bordersp.png"]

    for file in os.listdir("Borders"):
        if file.endswith(".png"):
            if pygame.image.load("Borders/" + file).get_rect().size == (240, 72):
                brdlst.append("Borders/" + file)

    bordn = 0

    if avars[3][13] in brdlst:
        bordn = brdlst.index(avars[3][13])

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

    def aspr():
        if len(avars[0]) > 0:
            if avars[0][1] > 0:
                sprs0 = chsprs(avars[0][15], (avars[0][30] == 2), avars[0][14])
            else:
                sprs0 = chsprs(0 - avars[0][0], 0, 0)
        else:
            sprs0 = []
        if len(avars[1]) > 0:
            if avars[1][1] > 0:
                sprs1 = chsprs(avars[1][15], (avars[1][30] == 2), avars[1][14])
            else:
                sprs1 = chsprs(0 - avars[1][0], 0, 0)
        else:
            sprs1 = []
        if len(avars[2]) > 0:
            if avars[2][1] > 0:
                sprs2 = chsprs(avars[2][15], (avars[2][30] == 2), avars[2][14])
            else:
                sprs2 = chsprs(0 - avars[2][0], 0, 0)
        else:
            sprs2 = []
        asprs = [sprs0, sprs1, sprs2]
        return(asprs)

    anifr = 0

    sound = sounds.imprtsnd(avars)

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if bx:
            screen.blit(textbox, [0, 24])
            if scr == 0:
                screen.blit(scrli, [232, 128])
                if not (len(avars[0]) > 0 and len(avars[1]) > 0 and len(avars[2]) > 0):
                    screen.blit((fnt.render("CHOOSE EGG", 1, (0, 0, 100))), [8, 34])
                else:
                    screen.blit((fnt.render("CHOOSE EGG", 1, (102, 102, 255))), [8, 34])
                screen.blit((fnt.render("ABANDON", 1, (0, 0, 100))), [8, 50])
                screen.blit((fnt.render("IMPORT CHARACTERS", 1, (0, 0, 100))), [8, 114])
            elif scr == 1:
                screen.blit(scrli, [232, 128])
                screen.blit((fnt.render("CHANGE TIME MODE", 1, (0, 0, 100))), [8, 34])
                screen.blit((fnt.render("CHANGE BORDER", 1, (0, 0, 100))), [8, 50])
                screen.blit((fnt.render("SOUND:", 1, (0, 0, 100))), [8, 66])
                if avars[3][8] == "1.0":
                    screen.blit((fnt.render("ON", 1, (204, 0, 100))), [107, 66])
                    screen.blit((fnt.render("OFF", 1, (102, 102, 255))), [164, 66])
                else:
                    screen.blit((fnt.render("ON", 1, (102, 102, 255))), [107, 66])
                    screen.blit((fnt.render("OFF", 1, (204, 0, 100))), [164, 66])
                screen.blit((fnt.render("DELETE SAVE FILE", 1, (0, 0, 100))), [8, 114])
            else:
                screen.blit((fnt.render("ARE YOU SURE?", 1, (0, 0, 100))), [8, 66])
                screen.blit((fnt.render("YES", 1, (0, 0, 100))), [107, 82])
                screen.blit((fnt.render("NO", 1, (0, 0, 100))), [164, 82])
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
                if pb in [2, 4, 5] and 24 < mp[1] < 136:
                        sound[2].play()
                        scr = not scr
                        clt = 0
                elif pb == 1:
                    clt = 0
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            pygame.mixer.stop()
                            sound[4].play()
                            return avars, asprs
                    if scr == 0:
                        if not (len(avars[0]) > 0 and len(avars[1]) > 0 and len(avars[2]) > 0):
                            if 32 < mp[1] < 48 and 8 < mp[0] < 128:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 2
                                afw = 0
                        if 48 < mp[1] < 64 and 8 < mp[0] < 98:
                            pygame.mixer.stop()
                            sound[3].play()
                            scr = 2
                            afw = 1
                        if 112 < mp[1] < 128 and 8 < mp[0] < 232:
                            pygame.mixer.stop()
                            sound[3].play()
                            for f in os.listdir("CCharacters"):
                                #print(f)
                                if f.endswith(".png"):
                                    #print(f[:6])
                                    if f[:6] == "chara_":
                                        #print(f[:(len(f) - 5)] + "s.png")
                                        try:
                                            a = int(f[6:(len(f) - 5)])
                                            if (384 < a < 65536) and (f[len(f) - 5] == 'b'):
                                                if os.path.isfile("CCharacters/" + f[:(len(f) - 5)] + "s.png"):
                                                    shutil.copyfile(("CCharacters/" + f), ("Sprites/Characters/chara_" + str(a) + "b.png"))
                                                    shutil.copyfile(("CCharacters/" + f[:(len(f) - 5)] + "s.png"), ("Sprites/Characters/chara_" + str(a) + "s.png"))
                                        except:
                                            pass
                                    elif f[:4] == "egg_":
                                        try:
                                            a = int(f[4:(len(f) - 5)])
                                            if (8 < a < 16) and (f[len(f) - 5] == 'b'):
                                                if os.path.isfile("CCharacters/" + f[:(len(f) - 5)] + "s.png"):
                                                    shutil.copyfile(("CCharacters/" + f), ("Sprites/Eggs/egg_" + str(a) + "b.png"))
                                                    shutil.copyfile(("CCharacters/" + f[:(len(f) - 5)] + "s.png"), ("Sprites/Eggs/egg_" + str(a) + "s.png"))
                                        except:
                                            pass
                    elif scr == 1:
                        if 32 < mp[1] < 48 and 8 < mp[0] < 192:
                            pygame.mixer.stop()
                            sound[3].play()
                            avars[3][3] = not avars[3][3]
                        if 48 < mp[1] < 64 and 8 < mp[0] < 168:
                            pygame.mixer.stop()
                            sound[3].play()
                            bordn = (bordn + 1) % len(brdlst)
                            avars[3][13] = brdlst[bordn]
                            tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 9, 0)
                        if 64 < mp[1] < 80 and 107 < mp[0] < 131:
                            avars[3][8] = "1.0"
                            sound = sounds.imprtsnd(avars)
                            pygame.mixer.stop()
                            sound[3].play()
                        if 64 < mp[1] < 80 and 164 < mp[0] < 201:
                            avars[3][8] = "0.0"
                            sound = sounds.imprtsnd(avars)
                        if 112 < mp[1] < 128 and 8 < mp[0] < 190:
                            scr = 2
                            afw = 2
                    else:
                        if 80 < mp[1] < 96:
                            if 107 < mp[0] < 139:
                                if afw == 0:
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    varsup.updtvrs(avars)
                                    eggsel.crdani(screen)
                                    avars = impvrs()
                                    asprs = aspr()
                                    return avars, asprs
                                elif afw == 1:
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    varsup.updtvrs(avars)
                                    d = shelve.open('save_db')
                                    if d['selchara'] == 0:
                                        del d['egg1']
                                    elif d['selchara'] == 1:
                                        del d['egg2']
                                    elif d['selchara'] == 2:
                                        del d['egg3']
                                    if ('egg1' in d):
                                        d['selchara'] = 0
                                    elif ('egg2' in d) > 0:
                                        d['selchara'] = 1
                                    elif ('egg3' in d) > 0:
                                        d['selchara'] = 2
                                    else:
                                        d['egg1'] = None
                                        d.close()
                                        eggsel.crdani(screen)
                                    d.close()
                                    avars = impvrs()
                                    asprs = aspr()
                                    return avars, asprs
                                else:
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    varsup.updtvrs(avars)
                                    if os.path.isfile("save_db.dat"):
                                        os.remove('save_db.dat')
                                    if os.path.isfile("save_db.bak"):
                                        os.remove('save_db.bak')
                                    if os.path.isfile("save_db.dir"):
                                        os.remove('save_db.dir')
                                    for file in os.listdir("Sprites/Misc/mail/tm1"):
                                        if file.endswith(".png"):
                                            os.remove("Sprites/Misc/mail/tm1/" + file)
                                    for file in os.listdir("Sprites/Misc/mail/tm2"):
                                        if file.endswith(".png"):
                                            os.remove("Sprites/Misc/mail/tm2/" + file)
                                    for file in os.listdir("Sprites/Misc/mail/tm3"):
                                        if file.endswith(".png"):
                                            os.remove("Sprites/Misc/mail/tm3/" + file)
                                    if os.path.isfile("Sprites/Misc/mail/news.png"):
                                        os.remove("Sprites/Misc/mail/news.png")
                                    kr = False
                                    pygame.quit()
                                    sys.exit()
                            elif 164 < mp[0] < 188:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = (afw == 2)
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
                clt += 1
        if chngsts:
            avars = statusup.chngsts(avars)
            chngsts = False
        if anifr < 23:
            anifr += 1
        else:
            anifr = 0
        if clt > 29:
            return avars, asprs
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

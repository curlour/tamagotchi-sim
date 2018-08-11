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
from random import *
import dirty
import mainscreen

def bir(avars, asprs, mate, negg, screen):
    
    kr = True

    scr = 0
    name = False
    ne = False

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

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    
    nw = ""
    nmwr = fnt.render(nw, 1, (0, 0, 100))

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    boytxt = fnt.render("BOY", 1, (204, 204, 255))

    girltxt = fnt.render("GIRL", 1, (255, 204, 204))

    wrttxt = fnt.render("WRITE", 1, (102, 102, 255))

    clock = pygame.time.Clock()

    def impvrs():
        d = shelve.open('save_db')
        if ('egg1' in d):
            var1 = [d['egg1'], d['charag1'], d['time1'], d['gene1'], d['poo1'], d['int1'], d['sty1'], d['knd1'], d['hum1'], d['gor1'], d['pas1'], d['grp1'], d['grpf1'],
                    d['grpm1'], d['gender1'], d['chara1'], d['hungry1'], d['happy1'], d['weight1'], d['caremiss1'], d['sick1'], d['awake1'], d['chname1'], d['room1'],
                    d['stages1'], d['parent1'], d['pspouse1'], d['gparent1'], d['gpspouse1'] ,d['agen1'], d['dirty1'], d['edu1'], d['frnd1'], d['pttrain1']]
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

    if len(mate) > 0:
        if mate[0] == avars[3][0]:
            try:
                a = avars[0][14]
            except:
                a = 0
            try:
                b = avars[1][14]
            except:
                b = 0
            try:
                c = avars[2][14]
            except:
                c = 0
            l = [a, b, c]
            if mate[3] in l:
                varsup.updtvrs(avars)
                d = shelve.open('save_db')
                if mate[3] == l[0]:
                    del d['egg1']
                elif mate[3] == l[1]:
                    del d['egg2']
                elif mate[3] == l[2]:
                    del d['egg3']
                d.close()
                avars = impvrs()

    tpborder, btborder = borders.getborders(avars[3][13], 0, 0, 0)

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

    def drawbg():
        try:
            if pygame.image.load(avars[avars[3][5]][23]).get_rect().size == (240, 160):
                bgi = pygame.image.load(avars[avars[3][5]][23]).convert()
            else:
                bgi = pygame.Surface([240, 160]).convert()
                bgi.fill((51, 51, 204))
                bgi.blit(fnt.render("IMAGE SIZE IS", 1, (255, 255, 255)), [8, 34])
                bgi.blit(fnt.render("INCORRECT!!!", 1, (255, 255, 255)), [8, 50])
                bgi.blit(fnt.render("DO NOT MESS", 1, (255, 255, 255)), [8, 66])
                bgi.blit(fnt.render("WITH THE", 1, (255, 255, 255)), [8, 82])
                bgi.blit(fnt.render("GAME FILES!", 1, (255, 255, 255)), [8, 98])
        except pygame.error:
            bgi = pygame.Surface([240, 160]).convert()
            bgi.fill((51, 51, 204))
            bgi.blit(fnt.render("ERROR 404:", 1, (255, 255, 255)), [8, 34])
            bgi.blit(fnt.render("BACKGROUND IMAGE", 1, (255, 255, 255)), [8, 50])
            bgi.blit(fnt.render("NOT FOUND", 1, (255, 255, 255)), [8, 66])
        if int(time.strftime("%m")) == 12 and int(time.strftime("%d")) > 19:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/xmasbg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 1 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/newyearbg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 3 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/girlsbg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 4 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/hanamibg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 5 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/boysbg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 7 and int(time.strftime("%d")) < 11:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/tanabatabg.png").convert(), [0, 0])
        elif int(time.strftime("%m")) == 8 and 10 < int(time.strftime("%d")) < 21:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/firewkbg.png").convert(), [0, 0])
        elif (int(time.strftime("%m")) == 10 and int(time.strftime("%d")) > 25) or (int(time.strftime("%m")) == 11 and int(time.strftime("%d")) < 5):
            bgi.blit(pygame.image.load("Sprites/Misc/bg/haweenbg.png").convert(), [0, 0])
        if (time.strftime("%m") + time.strftime("%d")) == avars[3][1]:
            bgi.blit(pygame.image.load("Sprites/Misc/bg/bdaybg.png").convert(), [0, 0])
        return(bgi)

    bgi = drawbg()

    eggs = chsprs(-(negg[0]), 0, 0)

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        screen.blit(bgi, [0, 0])
        if scr == 0:
            screen.blit(eggs[2 + (anifr % 12 > 5)], [108, 106])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][16], 1, 0), [72, 98])
        elif scr == 1:
            if anifr < 132:
                screen.blit(eggs[4], [(107 + (2 * (anifr % 6 > 2))), 106])
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][4 + (5 * (anifr % 12 > 5))], 1, 0), [72, 98])
            else:
                if anifr == 132:
                    pygame.mixer.stop()
                    sound[8].play()
                screen.blit(babys[5], [112, 107])
                screen.blit(eggs[5], [108, 106])
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][5], 1, 0), [72, 98])
        elif scr == 2:
            screen.blit(babys[11 + (anifr % 12 > 5)], [112, 114])
            screen.blit(pygame.transform.flip(asprs[avars[3][5]][6], 1, 0), [72, 98])
        elif scr == 3:
            if anifr < 24:
                screen.blit(babys[5 + (5 * (anifr % 12 > 5))], [104, 106])
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][5 + (10 * (anifr % 12 > 5))], 1, 0), [72, 98])
            elif anifr < 48:
                screen.blit(babys[4 + (2 * (anifr % 12 > 5))], [112, 114])
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][3 + (anifr % 12 > 5)], 1, 0), [72, 98])
            elif anifr < 60:
                screen.blit(babys[18], [112, 114])
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][12], 1, 0), [72, 98])
            elif anifr < 108:
                screen.blit(babys[18], [112, 114])
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][6 + (anifr % 12 > 5)], 1, 0), [72, 98])
            elif anifr < 132:
                screen.blit(babys[18], [112, 114])
                screen.blit(asprs[avars[3][5]][11 + (2 * (anifr % 12 < 6))], [(48 - (24 * ((anifr - 108) // 6))), (98 - (2 * (anifr % 12 < 6)))])
            else:
                screen.blit(babys[9], [112, 114])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, 0, fnt, name, anifr, hn, hp, sk, sl)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.stop()
                sound[12].play()
            if event.type == pygame.KEYDOWN:
                if name and scr == 2:
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
                            avars[avars[3][5]][2] = 0
                            avars[avars[3][5]][22] = nw
                            anifr = 0
                            scr = 3
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
        if name and scr == 2:
            genbk= pygame.Surface([240, 24]).convert()
            if avars[avars[3][5]][14] % 2 == 0:
                genbk.fill((0, 0, 100))
                genbk.blit(boytxt, [102, 4])
            else:
                genbk.fill((100, 0, 0))
                genbk.blit(girltxt, [96, 4])
            screen.blit(genbk, [0, 24])
            screen.blit(nmwr, [67, 6])
            if not ne:
                screen.blit(wrttxt, [67, 6])
        else:
            screen.blit((fnt.render(avars[avars[3][5]][22], 1, (0, 0, 100))), [67, 6])
        if anifr < 143:
            anifr += 1
        else:
            anifr = 0
            if scr == 0:
                scr = 1
                name = True
                #print(negg)
                #print(avars[avars[3][5]][11])
                #print(avars[avars[3][5]][12])
                #print(avars[avars[3][5]][13])
                #print(avars[avars[3][5]][14])
                p = ["PARK", avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14], avars[avars[3][5]][13], avars[avars[3][5]][12], avars[avars[3][5]][11], [avars[avars[3][5]][2], 0], 0]
                avars[avars[3][5]][27] = avars[avars[3][5]][25]
                avars[avars[3][5]][28] = avars[avars[3][5]][26]
                avars[avars[3][5]][25] = [avars[avars[3][5]][14],
                                          avars[avars[3][5]][15],
                                          avars[avars[3][5]][22],
                                          avars[avars[3][5]][24],
                                          avars[avars[3][5]][12],
                                          avars[avars[3][5]][13]]
                if len(mate) > 0:
                    q = ["PARK", mate[1], mate[2], mate[3], mate[4], mate[5], mate[6], [avars[avars[3][5]][2], 0], 0]
                    avars[avars[3][5]][26] = [mate[3],
                                              mate[2],
                                              mate[4],
                                              mate[5]]
                else:
                    avars[avars[3][5]][26] = []
                a = avars[avars[3][5]][29]
                a.append([avars[avars[3][5]][14],
                          avars[avars[3][5]][15],
                          avars[avars[3][5]][24]])
                avars[avars[3][5]][0] = negg[0]
                avars[avars[3][5]][1] = 1
                avars[avars[3][5]][2] = 0
                avars[avars[3][5]][3] += 1
                avars[avars[3][5]][4] = 0
                avars[avars[3][5]][5] = 0
                avars[avars[3][5]][6] = 0
                avars[avars[3][5]][7] = 0
                avars[avars[3][5]][8] = 0
                avars[avars[3][5]][9] = 0
                avars[avars[3][5]][10] = 0
                avars[avars[3][5]][11] = negg[1]
                if negg[0] < 9:
                    avars[avars[3][5]][12] = negg[1]
                    avars[avars[3][5]][13] = negg[2]
                avars[avars[3][5]][14] = negg[3]
                avars[avars[3][5]][15] = 0
                avars[avars[3][5]][16] = 0
                avars[avars[3][5]][17] = 0
                avars[avars[3][5]][18] = 5
                avars[avars[3][5]][19] = 0
                avars[avars[3][5]][20] = False
                avars[avars[3][5]][21] = True
                avars[avars[3][5]][22] = ""
                avars[avars[3][5]][24] = []
                avars[avars[3][5]][30] = 0
                avars[avars[3][5]][31] = 0
                if len(mate) > 0:
                    avars[avars[3][5]][32] = [p, q]
                else:
                    avars[avars[3][5]][32] = [p]
                avars[avars[3][5]][33] = 0
                avars = growth.grw(avars)
                babys = chsprs(avars[avars[3][5]][15], 0, avars[avars[3][5]][14])
                #print(avars[avars[3][5]][11])
                #print(avars[avars[3][5]][12])
                #print(avars[avars[3][5]][13])
                #print(avars[avars[3][5]][14])
                pygame.mixer.stop()
                sound[7].play()
            elif scr == 1:
                scr = 2
            elif scr == 3:
                #print(avars[avars[3][5]][25])
                #print(avars[avars[3][5]][26])
                #print(avars[avars[3][5]][27])
                #print(avars[avars[3][5]][28])
                #print(avars[avars[3][5]][29])
                pygame.mixer.stop()
                sound[0].play()
                return(avars)
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

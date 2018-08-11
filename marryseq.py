import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import shelve
import pyperclip
import sounds
import varsup
import palette
import statusup
from random import *
import weather
import dirty
import nextgen
import mainscreen

def wed(avars, asprs, fsprs, mate, screen):
    
    kr = True

    scr = 0

    chngsts = False

    def chsprs(chara, g):
        try:
            sprs = []
            if chara > 0:
                bs = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "b.png")
                ss = pygame.image.load("Sprites/Characters/chara_" + str(chara) + "s.png")
            else:
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
        except:
            sprs = chsprs(0, g)
        return(sprs)

    def nchild():
        negg = []
        l = [choice([avars[avars[3][5]][12], avars[avars[3][5]][13]]),
             choice([mate[4], mate[5]])]
        if ((mate[6] != avars[avars[3][5]][0]) and (mate[6] != avars[avars[3][5]][11])) or (mate[6] in ['no', 'ma', 'me', 'ku']):
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
        y = format(avars[avars[3][5]][14], '032b')
        m = format(mate[3], '032b')
        a = (int(y[:16], 2) & int(m[:16], 2))
        b = ((int(y[:16], 2) ^ int(m[:16], 2)) & randint(0, 65535))
        r = format((a | b), '016b') + format((int(y[16:28], 2) ^ int(m[16:28], 2)), '012b') + format(randint(0, 15), '04b')
        if (mate[0] != "PARK") and (mate[0] != avars[3][0]):
            r = r[:30] + '0' + r[31]
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

    ht = pygame.image.load("Sprites/Misc/emo/heart.png").convert()
    ht2 = pygame.image.load("Sprites/Misc/emo/heart2.png").convert()

    walk = pygame.image.load("Sprites/Misc/bg/marrwlk.png").convert()

    s, tm , w = weather.chktime(avars)

    mbk = pygame.image.load("Sprites/Misc/bg/marrsc.png").convert()

    scn = pygame.Surface([240, 160]).convert()
    scn.fill((0, 255, 255))
    scn.blit(mbk, [-(240 * s), -160])
    scn.set_colorkey((0, 255, 255))

    sky = []
    for i in [0, 1, 2, 3]:
        c = pygame.Surface([240, 160]).convert()
        c.blit(mbk, [-(240 * i), 0])
        sky.append(c)

    prevs = []
    for i in avars[avars[3][5]][24]:
        c = chsprs(i, avars[avars[3][5]][14])
        prevs.append(c)
    
    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if scr == 0:
            screen.blit(walk, [0, 0])
            if anifr < 60:
                screen.blit(prevs[anifr // (60 // len(prevs))][11 + (2 * (anifr % 12 > 5))], [(240 - ((anifr // 6) * 20)), \
                                                                                              ((8 * (((anifr // (60 // len(prevs))) < 3) + ((anifr // (60 // len(prevs))) < 1))) \
                                                                                               + 98 + (2 * (anifr % 12 < 6)))])
                if (anifr % (60 // len(prevs))) == 0:
                    pygame.mixer.stop()
                    sound[3].play()
            elif anifr < 108:
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][5 * (1 + (anifr % 12 > 5))], 1, 0), [20, 100])
                screen.blit(fsprs[11 + (2 * (anifr % 12 > 5))], [(240 - (((anifr - 60) // 6) * 20)), (98 + (2 * (anifr % 12 < 6)))])
            elif anifr < 120:
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][15], 1, 0), [20, 100])
                screen.blit(fsprs[15], [52, 100])
                if anifr == 108:
                    pygame.mixer.stop()
                    sound[9].play()
            else:
                screen.blit(asprs[avars[3][5]][11 + (2 * (anifr % 12 > 5))], [(20 - (((anifr - 120) // 6) * 20)), (98 + (2 * (anifr % 12 < 6)))])
                screen.blit(fsprs[11 + (2 * (anifr % 12 > 5))], [(52 - (((anifr - 120) // 6) * 20)), (98 + (2 * (anifr % 12 < 6)))])
        else:
            if anifr < 24:
                screen.blit(sky[0], [0, 0])
                screen.blit(scn, [0, 0])
                screen.blit([ht, ht2][anifr < 6], [112, 82])
                if anifr == 6:
                    pygame.mixer.stop()
                    sound[9].play()
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][(15 - (3 * (anifr < 6)))], 1, 0), [88, 104])
                screen.blit(fsprs[(15 - (3 * (anifr < 6)))], [120, 104])
            elif anifr < 84:
                i = (anifr - 24) / 6
                screen.blit(sky[1], [0, ((16 * i) - 160)])
                screen.blit(sky[0], [0, (16 * i)])
                screen.blit(scn, [0, (32 * i)])
                screen.blit(ht, [112, (82 + (32 * i))])
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][15], 1, 0), [88, (104 + (32 * i))])
                screen.blit(fsprs[15], [120, (104 + (32 * i))])
            elif anifr < 96:
                screen.blit(sky[1], [0, 0])
            elif anifr < 102:
                if anifr == 96:
                    pygame.mixer.stop()
                    sound[3].play()
                screen.blit(sky[2], [0, 0])
            else:
                if anifr % 6 == 0:
                    pygame.mixer.stop()
                    sound[9].play()
                screen.blit(pygame.transform.flip(sky[3], (anifr % 12 < 6), 0), [0, 0])
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
        if anifr < 143:
            anifr += 1
        else:
            anifr = 0
            if scr == 0:
                scr = 1
            else:
                negg = nchild()
                #print(negg)
                e = avars[3][14]
                e = e[:(negg[0] - 1)] + '1' + e[(negg[0]):]
                avars[3][14] = e
                avars = nextgen.bir(avars, asprs, mate, negg, screen)
                return(avars)
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

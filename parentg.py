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
import mainscreen

def game(avars, asprs, screen, fsps):
    
    kr = True

    chngsts = False

    scr = 0

    ret = 1

    tuts = True
    strt = False
    play = False
    end = 0

    cardn = list(range(0, 51))
    shuffle(cardn)
    ycl = cardn[:7]
    pcl = cardn[7:14]
    cardn = cardn[14:]

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    cards = [pygame.image.load("Sprites/Misc/card/c1.png").convert(),
             pygame.image.load("Sprites/Misc/card/c5.png").convert()]

    tutimg = pygame.image.load("Sprites/Misc/bg/parentgt.png").convert()

    gamebk = pygame.image.load("Sprites/Misc/bg/parenti.png").convert()

    playbk = pygame.image.load("Sprites/Misc/bg/parentg.png").convert()

    suits = []
    for i in [0, 1, 2, 3]:
        a = pygame.Surface((24, 24))
        a.blit(playbk, [-(24 * i), 0])
        a.set_colorkey((0, 255, 255))
        a.convert()
        suits.append(a)

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    wint = pygame.image.load("Sprites/Misc/bg/win.png").convert()
    loset = pygame.image.load("Sprites/Misc/bg/lose.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    lfnt = pygame.font.Font("Sprites/Misc/font/Tama1.ttf", 8)

    cardt = []
    for i in ["A", "2", "3", "4", "5", "6",
              "7", "8", "9", "10", "J", "Q", "K"]:
        cardt.append(lfnt.render(i, 1, (0, 0, 100)))

    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if tuts:
            screen.blit(tutimg, [0, 0])
        elif strt:
            screen.blit(gamebk, [0, 0])
            if anifr == 16:
                pygame.mixer.stop()
                sound[11].play()
            if anifr < 16:
                screen.blit(ready, [80, 48])
                spr = 3
            else:
                screen.blit(go, [95, 48])
                spr = 5
            screen.blit(fsps[0][spr], [48, 98])
            if len(fsps) > 1:
                screen.blit(fsps[1][spr], [88, 98])
            screen.blit(asprs[avars[3][5]][spr], [(128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            if len(fsps) == 3:
                screen.blit(fsps[2][spr], [(168 + ((32 - fsps[2][spr].get_width()) // 2)), (98 + (32 - fsps[2][spr].get_height()))])
        elif play:
            screen.blit(playbk, [0, 0])
            if end == 0:
                spr = 3 + (anifr % 12 > 5)
                ps = 6
            elif end == 1:
                spr = 6
                ps = 3 + (anifr % 12 > 5)
            else:
                spr = 5 + (2 * (len(pcl) < len(ycl)))
                ps = 7 - (2 * (len(pcl) < len(ycl)))
            screen.blit(cards[1], [108, 68])
            screen.blit(cardt[cardn[len(cardn) - 1] % 13], [110, 70])
            screen.blit(suits[cardn[len(cardn) - 1] // 13], [108, 68])
            for n in range(len(pcl)):
                screen.blit(cards[0], [(36 + (24 * n)), (48 - (24 * (n % 2)))])
            for n in range(len(ycl)):
                screen.blit(cards[1], [(36 + (24 * n)), (88 + (24 * (n % 2)))])
                screen.blit(cardt[ycl[(7 * scr):][n] % 13], [(38 + (24 * n)), (90 + (24 * (n % 2)))])
                screen.blit(suits[ycl[(7 * scr):][n] // 13], [(36 + (24 * n)), (88 + (24 * (n % 2)))])
            screen.blit(fsps[0][ps], [0, 24])
            if len(fsps) > 1:
                screen.blit(fsps[1][ps], [208, 24])
            screen.blit(asprs[avars[3][5]][spr], [((32 - asprs[avars[3][5]][spr].get_width()) // 2), (104 + (32 - asprs[avars[3][5]][spr].get_height()))])
            if len(fsps) == 3:
                screen.blit(fsps[2][spr], [(208 + ((32 - fsps[2][spr].get_width()) // 2)), (104 + (32 - fsps[2][spr].get_height()))])
        else:
            screen.blit(gamebk, [0, 0])
            if (len(pcl) >= len(ycl)):
                screen.blit(wint, [78, 48])
            else:
                screen.blit(loset, [65, 48])
            if anifr % 12 < 6:
                spr = 6 - (2 *  (len(pcl) >= len(ycl)))
                ps = 4 + (2 *  (len(pcl) >= len(ycl)))
            else:
                spr = 7 - (2 *  (len(pcl) >= len(ycl)))
                ps = 5 + (2 *  (len(pcl) >= len(ycl)))
            screen.blit(fsps[0][ps], [48, 98])
            if len(fsps) > 1:
                screen.blit(fsps[1][ps], [88, 98])
            screen.blit(asprs[avars[3][5]][spr], [(128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            if len(fsps) == 3:
                screen.blit(fsps[2][spr], [(168 + ((32 - fsps[2][spr].get_width()) // 2)), (98 + (32 - fsps[2][spr].get_height()))])
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
                    if (24 < mp[1] < 136) and tuts:
                        pygame.mixer.stop()
                        sound[10].play()
                        tuts = False
                        strt = True
                        anifr = -1
                if end == 1 and play:
                    if pb == 1 and ((88 < mp[1] < 136) and (36 < mp[0] < 204)):
                        i = cardn[len(cardn) - 1] % 13
                        w = [i, (i + 13), (i + 26), (i + 39)]
                        w.pop(w.index(cardn[len(cardn) - 1]))
                        w.append((13 * (cardn[len(cardn) - 1] // 13)) + ((cardn[len(cardn) - 1] + 1) % 13))
                        w.append((13 * (cardn[len(cardn) - 1] // 13)) + ((cardn[len(cardn) - 1] + 12) % 13))
                        p = (mp[0] - 36) // 24
                        if p < len(ycl):
                            if ycl[p] in w:
                                cardn.append(ycl[p])
                                ycl.pop(p)
                                end = 2 * (len(ycl) == 0)
                                pygame.mixer.stop()
                                sound[3 + (6 * (len(ycl) == 0))].play()
                                anifr = -1
                            else:
                                pygame.mixer.stop()
                                sound[12].play()
                    elif pb == 3 and ((88 < mp[1] < 136) and (36 < mp[0] < 204)):
                        i = cardn[len(cardn) - 1] % 13
                        w = [i, (i + 13), (i + 26), (i + 39)]
                        w.pop(w.index(cardn[len(cardn) - 1]))
                        w.append((13 * (cardn[len(cardn) - 1] // 13)) + ((cardn[len(cardn) - 1] + 1) % 13))
                        w.append((13 * (cardn[len(cardn) - 1] // 13)) + ((cardn[len(cardn) - 1] + 12) % 13))
                        p = ((mp[0] - 36) // 24) + (7 * scr)
                        l = True
                        for j in w:
                            if j in ycl:
                                l = False
                        if l:
                            l = True
                            for j in w:
                                if j in pcl:
                                    l = False
                            pygame.mixer.stop()
                            sound[3 + ((6 + (3 * (len(pcl) < len(ycl)))) * l)].play()
                            end = 2 * l
                            anifr = -1
                        else:
                            pygame.mixer.stop()
                            sound[12].play()
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
        if anifr < 23:
            anifr += 1
        else:
            anifr = 0
            if strt:
                play = True
                strt = False
            elif play:
                if end == 0:
                    i = cardn[len(cardn) - 1] % 13
                    w = [i, (i + 13), (i + 26), (i + 39)]
                    w.pop(w.index(cardn[len(cardn) - 1]))
                    w.append((13 * (cardn[len(cardn) - 1] // 13)) + ((cardn[len(cardn) - 1] + 1) % 13))
                    w.append((13 * (cardn[len(cardn) - 1] // 13)) + ((cardn[len(cardn) - 1] + 12) % 13))
                    l = []
                    for j in w:
                        if j in pcl:
                            l.append(j)
                    if len(l) == 0:
                        l = []
                        for j in w:
                            if j in ycl:
                                l.append(j)
                        end = 1 + (len(l) == 0)
                        pygame.mixer.stop()
                        sound[3 + ((6 + (3 * (len(pcl) < len(ycl)))) * (len(l) == 0))].play()
                    else:
                        l.sort()
                        j = l[0]
                        pcl.pop(pcl.index(j))
                        cardn.append(j)
                        end = 1 + (len(pcl) == 0)
                        pygame.mixer.stop()
                        sound[3 + (9 * (len(pcl) == 0))].play()
                elif end == 2:
                    end = 3
                    play = False
                    if len(pcl) >= len(ycl):
                        avars[avars[3][5]][17] = 6
                    pygame.mixer.stop()
                    sound[1 + (13 * (len(pcl) < len(ycl)))].play()
            elif end == 3:
                return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

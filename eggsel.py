import pygame, sys
from pygame.locals import *
import os
from random import *
import time
import shelve
import mainscreen

def crdani(screen):

    kr= True

    bk = pygame.image.load("Sprites/Misc/bg/selscr.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)
    
    chegglb = pygame.image.load("Sprites/Misc/bg/chooseegg.png").convert()
    
    bbbeep = pygame.mixer.Sound("Sound/bb.ogg")

    flp = True
    cfr = -4

    chcard = 0

    ncrd = pygame.image.load("Sprites\Misc\card\c6.png").convert()

    crds = [pygame.image.load("Sprites\Misc\card\c5.png").convert(),
            pygame.image.load("Sprites\Misc\card\c4.png").convert(),
            pygame.image.load("Sprites\Misc\card\c3.png").convert(),
            pygame.image.load("Sprites\Misc\card\c2.png").convert(),
            pygame.image.load("Sprites\Misc\card\c1.png").convert()]

    eggs = []
    for i in range(1, 9):
        bs = pygame.image.load("Sprites/Eggs/egg_" + str(i) + "b.png")
        eg = pygame.Surface([24, 24]).convert()
        eg.fill((0, 255, 255))
        eg.blit(bs, [0, 0])
        eg.set_colorkey((0, 255, 255))
        eggs.append(eg)

    clock = pygame.time.Clock()

    d = shelve.open('save_db')

    ctc = d['chegg']

    d.close()

    while kr:
        screen.blit(bk, [0,0])
        screen.blit(chegglb, [((240 - chegglb.get_width()) // 2), 2])
        for i in range(8):
            if int(ctc[i]):
                if flp:
                    screen.blit(crds[abs(cfr)], [(36 + (48 * (i % 4))), (64 + (48 * (i // 4)))])
                    if cfr == 0:
                        screen.blit(eggs[i], [(36 + (48 * (i % 4))), (63 + (48 * (i // 4)))])
                elif chcard == 0 or (chcard > 0 and ((i + 1) != chcard)):
                    screen.blit(crds[4], [(36 + (48 * (i % 4))), (64 + (48 * (i // 4)))])
                elif cfr > 0:
                    screen.blit(crds[cfr], [(36 + (48 * (i % 4))), (64 + (48 * (i // 4)))])
                else:
                    screen.blit(crds[0], [(36 + (48 * (i % 4))), (64 + (48 * (i // 4)))])
                    screen.blit(eggs[i], [(36 + (48 * (i % 4))), (63 + (48 * (i // 4)))])
            else:
                screen.blit(ncrd, [(36 + (48 * (i % 4))), (64 + (48 * (i // 4)))])
        for event in pygame.event.get():
            if event.type == QUIT:
                d = shelve.open('save_db')
                if ('egg1' in d) or ('egg2' in d) or ('egg3' in d):
                    d.close()
                else:
                    d.close()
                    if os.path.isfile("save_db.dat"):
                        os.remove('save_db.dat')
                    if os.path.isfile("save_db.bak"):
                        os.remove('save_db.bak')
                    if os.path.isfile("save_db.dir"):
                        os.remove('save_db.dir')
                kr = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mp = event.pos
                d = (screen.get_size()[0] // 240)
                mp = ((mp[0] // d), (mp[1] // d))
                pb = event.button
                if pb == 1 and not flp and chcard == 0 and \
                   ((64 < mp[1] < 136) and (((mp[1] - 64) // 24) != 1)) and \
                   ((36 < mp[0] < 204) and ((((mp[0] - 36) // 24) % 2) != 1)):
                    chcard = ((mp[0] - 24) // 48) + (4 * (mp[1] > 100))
                    if int(ctc[chcard]):
                        chcard += 1
                        bbbeep.play()
                    else:
                        chcard = 0
        if flp:
            cfr += 1
            if cfr == 4:
                flp = False
        elif chcard > 0:
            cfr -= 1
            if cfr == -8:
                d = shelve.open('save_db')
                frstt = False
                if not (('egg1' in d) or ('egg2' in d) or ('egg3' in d)):
                    if d['speed'] == 0:
                        d['hour'] = time.strftime("%H:%M")
                        d['secs'] = 0
                        d['lstdt'] = time.strftime("%Y/%m/%d")
                    else:
                        d['hour'] = "08:59"
                        d['secs'] = 0
                        d['lstdt'] = time.strftime("%Y/%m/%d")
                    frstt = True
                if (not ('egg1' in d)) or d['egg1'] == None:
                    for file in os.listdir("Sprites/Misc/mail/tm1"):
                        os.remove("Sprites/Misc/mail/tm1/" + file)
                    d['egg1'] = chcard
                    d['charag1'] = 0
                    d['time1'] = 0
                    d['gene1'] = 1
                    d['poo1'] = 0
                    d['int1'] = 0
                    d['sty1'] = 0
                    d['knd1'] = 0
                    d['hum1'] = 0
                    d['gor1'] = 0
                    d['pas1'] = 0
                    d['grp1'] = ["no", "ma", "ku", "ku", "ma", "me", "me", "no"][chcard - 1]
                    d['grpf1'] = ["no", "ma", "ku", "ku", "ma", "me", "me", "no"][chcard - 1]
                    d['grpm1'] = [choice(["ku", "me", "ma"]), "ku", "ku", "me", "ma", "me", "ma", "no"][chcard - 1]
                    d['gender1'] = randint(0, 4294967295)
                    d['chara1'] = 0
                    d['hungry1'] = 0
                    d['happy1'] = 0
                    d['weight1'] = 5
                    d['caremiss1'] = 0
                    d['sick1'] = False
                    d['awake1'] = True
                    d['chname1'] = ""
                    d['stages1'] = []
                    d['parent1'] = []
                    d['pspouse1'] = []
                    d['gparent1'] = []
                    d['gpspouse1'] = []
                    d['agen1'] = []
                    d['dirty1'] = 0
                    d['edu1'] = 0
                    d['frnd1'] = []
                    d['pttrain1'] = 0
                    d['selchara'] = 0
                elif (not ('egg2' in d)):
                    for file in os.listdir("Sprites/Misc/mail/tm2"):
                        os.remove("Sprites/Misc/mail/tm2/" + file)
                    d['egg2'] = chcard
                    d['charag2'] = 0
                    d['time2'] = 0
                    d['gene2'] = 1
                    d['poo2'] = 0
                    d['int2'] = 0
                    d['sty2'] = 0
                    d['knd2'] = 0
                    d['hum2'] = 0
                    d['gor2'] = 0
                    d['pas2'] = 0
                    d['grp2'] = ["no", "ma", "ku", "ku", "ma", "me", "me", "no"][chcard - 1]
                    d['grpf2'] = ["no", "ma", "ku", "ku", "ma", "me", "me", "no"][chcard - 1]
                    d['grpm2'] = [choice(["ku", "me", "ma"]), "ku", "ku", "me", "ma", "me", "ma", "no"][chcard - 1]
                    d['gender2'] = randint(0, 4294967295)
                    d['chara2'] = 0
                    d['hungry2'] = 0
                    d['happy2'] = 0
                    d['weight2'] = 5
                    d['caremiss2'] = 0
                    d['sick2'] = False
                    d['awake2'] = True
                    d['chname2'] = ""
                    d['stages2'] = []
                    d['parent2'] = []
                    d['pspouse2'] = []
                    d['gparent2'] = []
                    d['gpspouse2'] = []
                    d['agen2'] = []
                    d['dirty2'] = 0
                    d['edu2'] = 0
                    d['frnd2'] = []
                    d['pttrain2'] = 0
                    d['selchara'] = 1
                elif (not ('egg3' in d)):
                    for file in os.listdir("Sprites/Misc/mail/tm3"):
                        os.remove("Sprites/Misc/mail/tm3/" + file)
                    d['egg3'] = chcard
                    d['charag3'] = 0
                    d['time3'] = 0
                    d['gene3'] = 1
                    d['poo3'] = 0
                    d['int3'] = 0
                    d['sty3'] = 0
                    d['knd3'] = 0
                    d['hum3'] = 0
                    d['gor3'] = 0
                    d['pas3'] = 0
                    d['grp3'] = ["no", "ma", "ku", "ku", "ma", "me", "me", "no"][chcard - 1]
                    d['grpf3'] = ["no", "ma", "ku", "ku", "ma", "me", "me", "no"][chcard - 1]
                    d['grpm3'] = [choice(["ku", "me", "ma"]), "ku", "ku", "me", "ma", "me", "ma", "no"][chcard - 1]
                    d['gender3'] = randint(0, 4294967295)
                    d['chara3'] = 0
                    d['hungry3'] = 0
                    d['happy3'] = 0
                    d['weight3'] = 5
                    d['caremiss3'] = 0
                    d['sick3'] = False
                    d['awake3'] = True
                    d['chname3'] = ""
                    d['stages3'] = []
                    d['parent3'] = []
                    d['pspouse3'] = []
                    d['gparent3'] = []
                    d['gpspouse3'] = []
                    d['agen3'] = []
                    d['dirty3'] = 0
                    d['edu3'] = 0
                    d['frnd3'] = []
                    d['pttrain3'] = 0
                    d['selchara'] = 2
                d.close()
                if frstt:
                    mainscreen.mnscr()
                else:
                    return;
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

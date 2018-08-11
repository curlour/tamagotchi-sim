import pygame, sys
import os
from pygame.locals import *
import eggsel
import shelve

def init():

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

    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    screen = pygame.display.set_mode((240, 160))
    pygame.display.set_caption('Tamagotchi PC')
    pygame.display.set_icon(pygame.image.load("Sprites/Misc/icon/icon.png").convert())

    def drbx():
        tile = Txtbx()
        tile.update()
        textbox.blit(tile.image, [tx, ty])

    def drhl():
        global tx
        global tl
        tx = 8
        drbx()
        tl += 1
        while tx < 216:
            tx += 8
            drbx()
        tx = 224
        tl += 1
        drbx()

    def dral():
        global ty
        global tl
        while ty < 80:
            tl = 3
            ty += 8
            drhl()

    kr = True

    bk = pygame.image.load("Sprites/Misc/bg/selscr.png").convert()

    global nw
    global bw

    nw = ""
    bw = ""

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
    ty = 88
    drhl()
    textbox.set_colorkey((0, 255, 255))
    
    tptxt = pygame.image.load("Sprites/Misc/bg/fillin.png").convert()
    nmtxt = fnt.render("NAME:", 1, (0, 0, 100))
    nmwr = fnt.render(nw, 1, (0, 0, 100))
    bdtxt = fnt.render("BIRTHDAY: M:     D:", 1, (0, 0, 100))
    bdmwr = fnt.render(bw[:2], 1, (0, 0, 100))
    bddwr = fnt.render(bw[2:], 1, (0, 0, 100))
    sptxt = fnt.render("SPEED:  REAL  FAST", 1, (0, 0, 100))

    arw = pygame.image.load("Sprites/Misc/txtbox/arrow1.png")

    abbeep = pygame.mixer.Sound("Sound/ab.ogg")
    bbbeep = pygame.mixer.Sound("Sound/bb.ogg")
    cbbeep = pygame.mixer.Sound("Sound/cb.ogg")

    global ne
    global be
    global se
    global wrt

    wrt = 0
    ne = False
    be = False
    se = 0

    clock = pygame.time.Clock()

    d = shelve.open(os.path.join(os.path.dirname("save.txt"), 'save_db'))

    while kr:
        for event in pygame.event.get():
            if event.type == QUIT:
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if wrt < 2:
                        abbeep.play()
                        wrt += 1
                if event.key == pygame.K_UP:
                    if wrt > 0:
                        abbeep.play()
                        wrt -= 1
                if (pygame.K_a <= event.key <= pygame.K_z) and wrt == 0:
                    ltr = chr(event.key)
                    ne = True
                    if len(nw) < 8:
                        nw = (nw + str(ltr)).upper()
                    nmwr = fnt.render(nw, 1, (0, 0, 100))
                if (pygame.K_0 <= event.key <= pygame.K_9) and wrt == 1:
                    num = chr(event.key)
                    if len(bw) < 4:
                        bw += str(num)
                    if len(bw) == 4:
                        be = True
                    bdmwr = fnt.render(bw[:2], 1, (0, 0, 100))
                    bddwr = fnt.render(bw[2:], 1, (0, 0, 100))
                if event.key == pygame.K_BACKSPACE:
                    if wrt == 0:
                        if len(nw) != 0:
                            if len(nw) == 1:
                                ne = False
                            nw = nw[:len(nw) - 1]
                            nmwr = fnt.render(nw, 1, (0, 0, 100))
                    if wrt == 1:
                        if len(bw) != 0:
                            if len(bw) == 4:
                                be = False
                            bw = bw[:len(bw) - 1]
                            bdmwr = fnt.render(bw[:2], 1, (0, 0, 100))
                            bddwr = fnt.render(bw[2:], 1, (0, 0, 100))
                if wrt == 2:
                    if event.key == pygame.K_RIGHT:
                        se = 1
                        abbeep.play()
                    if event.key == pygame.K_LEFT:
                        se = 0
                        abbeep.play()
                if event.key == pygame.K_RETURN:
                    if ne and be and int(bw[:2]) <= 12 and (((int(bw[:2]) == 1 or int(bw[:2]) == 3 or int(bw[:2]) == 5 or int(bw[:2]) == 7 or int(bw[:2]) == 8 or int(bw[:2]) == 10 or int(bw[:2]) == 12) and int(bw[2:]) <= 31) or \
                                                            ((int(bw[:2]) == 4 or int(bw[:2]) == 6 or int(bw[:2]) == 9 or int(bw[:2]) == 11) and int(bw[2:]) <= 30) or (int(bw[:2]) == 2 and int(bw[2:]) <= 29)) and int(bw[:2]) != 0 and \
                                                            int(bw[2:]) != 0 and nw != "PARK":
                        d['uname'] = nw
                        d['bday'] = bw
                        d['money'] = 0
                        d['speed'] = se
                        d['room1'] = "Sprites/Misc/bg/room1.png"
                        d['room2'] = "Sprites/Misc/bg/room2.png"
                        d['room3'] = "Sprites/Misc/bg/room3.png"
                        d['food'] = [['Rice', 1, 0, 1, 4, 0, 0, 0, 0, 0, 0],
                                     ['Cake', 1, 1, 4, 4, 0, 0, 0, 0, 0, 0]]
                        d['vol'] = "1.0"
                        d['item'] = []
                        d['grave'] = []
                        d['mail'] = -1
                        d['border'] = "Sprites/Misc/bg/borders1.png"
                        d['chegg'] = '00000001'
                        d['kitchen'] = "Sprites/Misc/bg/kitchen.png"
                        d['table'] = "Sprites/Misc/obj/table.png"
                        d['chair'] = "Sprites/Misc/obj/chair.png"
                        d['wc'] = "Sprites/Misc/bg/toilet1.png"
                        d['toilet'] = "Sprites/Misc/obj/toilet.png"
                        d['btoilet'] = "Sprites/Misc/obj/babytoilet.png"
                        d['bathr'] = "Sprites/Misc/bg/bathroom.png"
                        d['bath'] = "Sprites/Misc/obj/bath.png"
                        d['dex'] = 0
                        d.close()
                        bbbeep.play()
                        eggsel.crdani(screen)
        screen.blit(bk, [0, 0])
        screen.blit(textbox, [0, 48])
        screen.blit(arw, [14, 62 + (32 * wrt)])
        screen.blit(tptxt, [((240 - tptxt.get_width()) // 2), 2])
        screen.blit(nmtxt, [24, 60])
        screen.blit(nmwr, [96, 60])
        screen.blit(bdtxt, [24, 92])
        screen.blit(bdmwr, [152, 92])
        screen.blit(bddwr, [194, 92])
        screen.blit(sptxt, [24, 124])
        screen.blit(arw, [94 + (60 * se), 126])
        clock.tick(128)
        pygame.display.update()

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
import growth
import statusup
import dirty
import weather
import mailico
import eatcon
import popballoon
import moneyg
import conball
import conrope
import mainscreen
import park
import marryseq

def com(avars, asprs, screen):

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

    cclk = True

    online = False

    marrag = False

    comt = 0

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

    chnamelst = ("BABYTCHI",
                 "SHIROBABYTCHI",
                 "PETITCHI",
                 "SHIROPETITCHI",
                 "PUCHITELETCHI",
                 "MIMIFUWATCHI",
                 "MAMEOTCHI",
                 "MAMEKOTCHI",
                 "PUCHICHOCOTCHI",
                 "OMUTUTCHI",
                 "MEMEOTCHI",
                 "MEMEPUTCHI",
                 "FUTABATCHI",
                 "KURITCHI",
                 "KUCHIOTCHI",
                 "KUCHIKOTCHI",
                 "TAMATCHI",
                 "KUCHITAMATCHI",
                 "HYURUTCHI",
                 "MARUTCHI",
                 "KINAKOMOTCHI",
                 "HOSHITCHI",
                 "TONGARITCHI",
                 "HASHITAMATCHI",
                 "HARUTCHI",
                 "PUCHITCHI",
                 "MIZUTAMATCHI",
                 "HITODETCHI",
                 "KURIBOTCHI",
                 "MOHITAMATCHI",
                 "MAMEBOTCHI",
                 "MOUSETCHI",
                 "MIMIPETCHI",
                 "SAKURAMOTCHI",
                 "SHIPPOTCHI",
                 "SHIPPOKOTCHI",
                 "MEMEBOTCHI",
                 "AHIRUKUTCHI",
                 "MEMEPETCHI",
                 "BELLTCHI",
                 "HANEOTCHI",
                 "HANEKOTCHI",
                 "KUCHIBOTCHI",
                 "MATTARITCHI",
                 "KUCHIPETCHI",
                 "TOROROTCHI",
                 "TSUNOOTCHI",
                 "TSUNOKOTCHI",
                 "OBOTCHI",
                 "OJYOTCHI",
                 "PIRORIROTCHI",
                 "PIRORINTCHI",
                 "MONAPATCHI",
                 "MERUHETCHI",
                 "KILALATCHI",
                 "MAYUMARUTCHI",
                 "Y. OYAJITCHI",
                 "CHUCHUTCHI",
                 "PROPELLERTCHI",
                 "BATABATCHI",
                 "Y. MAMETCHI",
                 "Y. MIMITCHI",
                 "HINOTAMATCHI",
                 "ICHIGOTCHI",
                 "ONIONTCHI",
                 "NIKATCHI",
                 "MAIMAITCHI",
                 "PAINAPUTCHI",
                 "HAWAINOTCHI",
                 "HAWAIKOTCHI",
                 "DARUMATCHI",
                 "TOMATCHI",
                 "MORITCHI",
                 "MORUTCHI",
                 "DAIYATCHI",
                 "MIKAZUKITCHI",
                 "NONOPOTCHI",
                 "SHIRIPURITCHI",
                 "COSMOTCHI",
                 "RINGOTCHI",
                 "Y. ANDROTCHI",
                 "U. Y. MAROTCHI",
                 "MAMEKATCHI",
                 "TERUTERUKOTCHI",
                 "P. TAMAKOKO",
                 "HIKOTCHI",
                 "UFOTCHI",
                 "RAKUGOTCHI",
                 "HINENEOTCHI",
                 "BENZATCHI",
                 "OHIGETCHI",
                 "CHAMAMETCHI",
                 "KIKITCHI",
                 "NOKOBOTCHI",
                 "HAPPABOUYATCHI",
                 "SABOSABOTCHI",
                 "KURIOTCHI",
                 "PYUKITCHI",
                 "DONGURITCHI",
                 "YAKANTCHI",
                 "U. Y. MAMETCHI",
                 "ZOURITCHI",
                 "CRACKERTCHI",
                 "KABOTCHI",
                 "GOURMETCHI",
                 "Y. MEMETCHI",
                 "BAKUTCHI",
                 "IMOTCHI",
                 "KIZATCHI",
                 "HIYAYATCHI",
                 "HANIKAMITCHI",
                 "LOVESORATCHI",
                 "RIONETCHI",
                 "KUJAKUTCHI",
                 "U. Y. VIOLETCHI",
                 "BOKUHOSHITCHI",
                 "NEOTCHI",
                 "BOXERTCHI",
                 "PUTCHICAKETCHI",
                 "U. Y. MEMETCHI",
                 "Y. KUCHIPATCHI",
                 "Y. DOROTCHI",
                 "KOROKOTCHI",
                 "SHELLTCHI",
                 "TENDOTCHI",
                 "GOROGOROTCHI",
                 "FUYOFUYOTCHI",
                 "POKAPOKATCHI",
                 "PANNAKOTCHI",
                 "KOMETCHI",
                 "U. Y. YATTATCHI",
                 "HINATCHI",
                 "PYONCHITCHI",
                 "PYONKOTCHI",
                 "ZATCHI",
                 "OHIMETCHI",
                 "KIWITCHI",
                 "KIKOTCHI",
                 "BILL",
                 "HASHIZOUTCHI",
                 "BILLOTCHI",
                 "BILLKOTCHI",
                 "SEKITORITCHI",
                 "CHARITCHI",
                 "MASKUTCHI",
                 "ARUKOTCHI",
                 "CHOMAMETCHI",
                 "CHOHIMETCHI",
                 "GINJIROTCHI",
                 "OSHAMATCHI",
                 "POCHITCHI",
                 "NYATCHI",
                 "KEROPYONTCHI",
                 "KURITEN",
                 "HIRATCHI",
                 "PIRATCHI",
                 "BUNBUNTCHI",
                 "BUNKOTCHI",
                 "MEGATCHI",
                 "GANKOTCHI",
                 "KABUTCHI",
                 "PIPOTCHI",
                 "ZUCCITCHI",
                 "TAKOTCHI",
                 "KABUTOTCHI",
                 "GHOST DEVILTCHI",
                 "NYOROTCHI",
                 "KUSATCHI",
                 "FURIKOTCHI",
                 "LOVEZUKINTCHI",
                 "MAIKUTCHI",
                 "ONPUTCHI",
                 "NEMUTCHI",
                 "YONEPATCHI",
                 "TAMAGOTCHI",
                 "CAPSULETCHI",
                 "MUMUTCHI",
                 "RIBOTCHI",
                 "BURGERTCHI",
                 "OMURATCHI",
                 "HATUGATCHI",
                 "HANATCHI",
                 "UHYOTCHI",
                 "WATATCHI",
                 "MUKUGETCHI",
                 "POTETCHI",
                 "DOROTCHI",
                 "DECOTCHI",
                 "MIMIYORITCHI",
                 "BUTTERFLYTCHI",
                 "TORATCHI",
                 "HOHOTCHI",
                 "KUROKOTCHI",
                 "MASKTCHI",
                 "HIDATCHI",
                 "FLOWERTCHI",
                 "TENGUTCHI",
                 "WHALETCHI",
                 "TEKETCHI",
                 "TSUNOTCHI",
                 "WARUSOTCHI",
                 "KAERUTCHI",
                 "GOZARUTCHI",
                 "KUNOITCHI",
                 "MARUMIMITCHI",
                 "MIMIKOTCHI",
                 "SUNNYTCHI",
                 "ROSETCHI",
                 "TAMASTATCHI",
                 "ASHITCHI",
                 "MAGICTCHI",
                 "GOSUTCHI",
                 "PHARAOTCHI",
                 "JEWELTCHI",
                 "SUNOPOTCHI",
                 "POMPOMTCHI",
                 "MAMETCHI",
                 "MIMITCHI",
                 "ZUKYUTCHI",
                 "MAIDTCHI",
                 "ANDROTCHI",
                 "MAROTCHI",
                 "KABUKITCHI",
                 "MELODYTCHI",
                 "KNIGHTTCHI",
                 "YUMEMITCHI",
                 "RIGHTTCHI",
                 "SHIGUREHIMETCHI",
                 "SMARTOTCHI",
                 "NACHURATCHI",
                 "GOTCHIMOTCHI",
                 "AMAKUTCHI",
                 "GURIGURITCHI",
                 "CHOUCHOTCHI",
                 "BUSHINOSUKETCHI",
                 "MAJOKKOTCHI",
                 "ACCHITCHI",
                 "SHINOBINYATCHI",
                 "SPACYTCHI",
                 "GYPSYTCHI",
                 "PIPOSPETCHI",
                 "PICHIPITCHI",
                 "WASHIKITCHI",
                 "ANESANTCHI",
                 "NANDETCHI",
                 "HARPTCHI",
                 "TENSAITCHI JR.",
                 "CHANTOTCHI",
                 "KUROMAMETCHI",
                 "KIRARITCHI",
                 "WAGASSIERTCHI",
                 "PEROTCHI",
                 "URA MAMETCHI",
                 "HOROYOTCHI",
                 "SAMURAITCHI",
                 "TSUKKOMITCHI",
                 "MATSURITCHI",
                 "URA ZUKYUTCHI",
                 "EIYUUTCHI",
                 "MEGAMITCHI",
                 "KINBATCHI",
                 "UWASATCHI",
                 "NECKTIETCHI",
                 "TROPICATCHI",
                 "SHINSHITCHI",
                 "YUKINKOTCHI",
                 "BOKUTCHI",
                 "CHOKOMAKATCHI",
                 "MOJAMOJATCHI",
                 "NEENETCHI",
                 "SHIMAGURUTCHI",
                 "HIMETCHI",
                 "KARAKUTCHI",
                 "HOSHIGIRLTCHI",
                 "TOSAKATCHI",
                 "PONYTCHI",
                 "TOGETCHI",
                 "MEMETCHI",
                 "SHIMASHIMATCHI",
                 "VIOLETCHI",
                 "PIEROTCHI",
                 "P. TAMAKO",
                 "SUKATCHI",
                 "JULIETCHI",
                 "SHOOTOTCHI",
                 "MADONNATCHI",
                 "DOYATCHI",
                 "MIRAITCHI",
                 "HEROTCHI",
                 "AGETCHI",
                 "DREAMITCHI",
                 "DAZZILITCHI",
                 "PAINTOTCHI",
                 "WALTZTCHI",
                 "AKASPETCHI",
                 "GIRAGIRATCHI",
                 "ORCHESTROTCHI",
                 "HIMESPETCHI",
                 "MOTETCHI",
                 "LOVELITCHI",
                 "OTOGITCHI",
                 "NIJIFUWATCHI",
                 "CELEBTCHI",
                 "PRIMATCHI",
                 "YASAGURETCHI",
                 "URA MEMETCHI",
                 "URA TOGETCHI",
                 "URA VIOLETCHI",
                 "RINKURUTCHI",
                 "PIANITCHI",
                 "GLASSTCHI",
                 "CHANDELITCHI",
                 "STARTCHI",
                 "CLULUTCHI",
                 "MAISUTATCHI",
                 "COFFRETCHI",
                 "MOGUMOGUTCHI",
                 "FURIFURITCHI",
                 "TACTTCHI",
                 "MORIRITCHI",
                 "MINOTCHI",
                 "PUKATCHI",
                 "TARAKOTCHI",
                 "SEBIRETCHI",
                 "KUCHIPATCHI",
                 "YATTATCHI",
                 "SPEPLANETCHI",
                 "KOTOHIMETCHI",
                 "YOTSUBATCHI",
                 "HIMEBARATCHI",
                 "SHIRIMOTCHI",
                 "MOMOTCHI",
                 "KUISHINBOTCHI",
                 "WATAWATATCHI",
                 "MONAKATCHI",
                 "RAINBOWTCHI",
                 "ORENETCHI",
                 "CANDY PAKUPAKU",
                 "DEBATCHI",
                 "SHITEKITCHI",
                 "CHARATCHI",
                 "AMIAMITCHI",
                 "P. TAMAHIKO",
                 "HOTTEATCHI",
                 "TENPATCHI",
                 "URA DEBATCHI",
                 "TOUGYUTCHI",
                 "DECORATCHI",
                 "URA KUCHIPATCHI",
                 "URA YATTATCHI",
                 "MORIJIKATCHI",
                 "PATITCHI",
                 "PIKAGOROTCHI",
                 "PEKOPEKOTCHI",
                 "OYAJITCHI",
                 "ANTOINETCHI",
                 "PAPARATCHI",
                 "DEVILTCHI",
                 "WOOLTCHI",
                 "CLIONE DEVILTCHI",
                 "RYOUTCHI",
                 "KURONEKOTCHI",
                 "TENSAITCHI",
                 "CHIETCHI",
                 "HYOTTOKOTCHI",
                 "MUTSUKITCHI",
                 "HAMJATCHI",
                 "MAKIKO",
                 "NIYANIYATCHI",
                 "HANAGATATCHI",
                 "NONBIRITCHI",
                 "BEBICAPPUTCHI",
                 "MUKIMUKITCHI",
                 "KISEKITCHI",
                 "OSUMOTCHI",
                 "PUDDINGTCHI",
                 "PUCHIPUTCHI",
                 "MODELTCHI",
                 "OJITCHI",
                 "OTOKITCHI",
                 "REXITCHI",
                 "DANGO OBATCHI",
                 "RYUJIJITCHI",
                 "KIBABATCHI")

    extrchn = {}
    n = open(("CCharacters/Names.txt"), 'r')
    t = n.read().splitlines()
    for i in t:
        i = i.split(":")
        extrchn.update({i[0]: i[1].upper()})

    ret = 1

    swthr = ["skyd", "skyaf", "skyn"]
    cwthr = ["skydc", "skydc", "skync"]
    wthrbk = [swthr, cwthr, cwthr]

    pgbk = ["pgbk", "pgbks", "pgbka", "pgbkw"]

    def otspr(t):
        osprs = []
        a = 0
        while a < len(avars[3][4 + (5 * t)]):
            if t == 0:
                try:
                    s = pygame.image.load("Sprites/Food/" + avars[3][4][a][0] + ".png").convert()
                except:
                    s = pygame.image.load("CFood/" + avars[3][4][a][0] + ".png").convert()
                b = pygame.Surface([24, 24])
                b.fill((0, 255, 255))
                b.blit(s, [0, 0])
                b.set_colorkey((0, 255, 255))
                b.convert()
            else:
                b = pygame.image.load("Sprites/Misc/item/" + avars[3][9][a][0] + ".png").convert()
            osprs.append(b)
            a += 1
        return(osprs)

    def drawobj():
        if len(osprs) < (24 * (oscr + 1)):
            a = len(osprs) - (24 * oscr)
        else:
            a = 24
        n = 0
        while n < a:
            screen.blit(osprs[(n + (24 * oscr))], [(14 + ((n - (8 * (n // 8))) * 27)), (44 + (24 * (n // 8)))])
            n += 1

    def outbg():
        bg = pygame.image.load("Sprites/Misc/bg/" + wthrbk[w][tm] + ".png").convert()
        a = pygame.image.load("Sprites/Misc/bg/" + pgbk[s] + ".png").convert()
        b = pygame.Surface([240, 160]).convert()
        c = (0, 0, 0)
        if w != 0:
            if w == 2:
                if s == 3:
                    a.blit(snowg, [0, 0])
                else:
                    a.blit(raing, [0, 0])
            if tm < 2:
                b.fill((204, 204, 204))
                c = (81, 81, 81)
            else:
                b.fill((102, 102, 102))
                c = (40, 40, 40)
            b.set_alpha(102)
            a.blit(b, [0, 0])
        elif tm > 0:
            if tm == 1:
                b.fill((255, 102, 0))
                c = (101, 40, 0)
            else:
                b.fill((0, 0, 102))
                c = (0, 0, 40)
            b.set_alpha(102)
            a.blit(b, [0, 0])
        a.set_colorkey(c)
        bg.blit(a, [0, 0])
        return(bg)

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

    def meet():
        flip = False
        fflip = True
        if anifr < 132:
            if anifr % 12 < 6:
                if anifr % 12 == 0:
                    pygame.mixer.stop()
                    sound[6].play()
                spr = 4
                fsp = 11
                fsy = 98 + (32 - fsprs[fsp].get_height())
            else:
                spr = 3
                fsp = 13
                fsy = 96 + (32 - fsprs[fsp].get_height())
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            fsx = ((32 - fsprs[fsp].get_width()) // 2) + (20 * ((anifr - 102) // 6))
        else:
            if anifr % 12 < 6:
                spr = 4
                fsp = 4
                fsy = 98 + (32 - fsprs[fsp].get_height())
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            else:
                if anifr % 12 == 6:
                    pygame.mixer.stop()
                    sound[9].play()
                spr = 5
                fsp = 5
                fsy = 96 + (32 - fsprs[fsp].get_height())
                spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
            fsx = ((32 - fsprs[fsp].get_width()) // 2) + 80
        sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        return spr, sprx, spry, flip, fsp, fsx, fsy, fflip

    def intro():
        flip = False
        fflip = True
        if anifr % 12 < 6:
            spr = 12
            fsp = 11
        else:
            spr = 11
            fsp = 12
        sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        fsx = ((32 - fsprs[fsp].get_width()) // 2) + 80
        fsy = 98 + (32 - fsprs[fsp].get_height())
        return spr, sprx, spry, flip, fsp, fsx, fsy, fflip

    def upfrd():
        if avars[avars[3][5]][32][frn][1] == avars[0][22]:
            for b in avars[0][32]:
                if b[0] == avars[3][0] and b[1] == avars[avars[3][5]][22]:
                    a = avars[0][32]
                    n = a.index(b)
                    if b[8] < 80:
                        b[8] += 1
                    if avars[avars[3][5]][1] != b[7]:
                        b[7] = avars[avars[3][5]][1]
                        b[2] = avars[avars[3][5]][15]
                    avars[0][32][n] = b
            if avars[avars[3][5]][32][frn][7] != avars[0][1]:
                avars[avars[3][5]][32][frn][7] = avars[0][1]
                avars[avars[3][5]][32][frn][2] = avars[0][15]
        elif avars[avars[3][5]][32][frn][1] == avars[1][22]:
            for b in avars[1][32]:
                if b[0] == avars[3][0] and b[1] == avars[avars[3][5]][22]:
                    a = avars[1][32]
                    n = a.index(b)
                    if b[8] < 80:
                        b[8] += 1
                    if avars[avars[3][5]][1] != b[7]:
                        b[7] = avars[avars[3][5]][1]
                        b[2] = avars[avars[3][5]][15]
                    avars[1][32][n] = b
            if avars[avars[3][5]][32][frn][7] != avars[1][1]:
                avars[avars[3][5]][32][frn][7] = avars[1][1]
                avars[avars[3][5]][32][frn][2] = avars[1][15]
        elif avars[avars[3][5]][32][frn][1] == avars[2][22]:
            for b in avars[2][32]:
                if b[0] == avars[3][0] and b[1] == avars[avars[3][5]][22]:
                    a = avars[2][32]
                    n = a.index(b)
                    if b[8] < 80:
                        b[8] += 1
                    if avars[avars[3][5]][1] != b[7]:
                        b[7] = avars[avars[3][5]][1]
                        b[2] = avars[avars[3][5]][15]
                    avars[2][32][n] = b
            if avars[avars[3][5]][32][frn][7] != avars[2][1]:
                avars[avars[3][5]][32][frn][7] = avars[2][1]
                avars[avars[3][5]][32][frn][2] = avars[2][15]

    def visit():
        flip = False
        fflip = True
        if avars[avars[3][5]][32][frn][8] < 14:
            if anifr % 12 < 6:
                spr = 12
                fsp = 11
            else:
                spr = 11
                fsp = 12
        elif avars[avars[3][5]][32][frn][8] < 41:
            if vst:
                if anifr < 114:
                    if anifr % 12 < 6:
                        spr = 4
                        fsp = 11
                    else:
                        spr = 3
                        fsp = 12
                elif anifr < 120:
                    spr = 9
                    fsp = 12
                    screen.blit(em, [112, 78])
                elif anifr < 126:
                    spr = 11
                    fsp = 3
                elif anifr < 132:
                    spr = 12
                    fsp = 10
                elif anifr < 138:
                    spr = 5
                    fsp = 5
                    screen.blit(sn, [112, 78])
                else:
                    spr = 4
                    fsp = 4
            else:
                if anifr < 132:
                    if anifr % 12 < 6:
                        spr = 4
                        fsp = 5
                        screen.blit(m1, [64, 74])
                        screen.blit(m2, [112, 78])
                        screen.blit(m1, [160, 74])
                    else:
                        spr = 5
                        fsp = 4
                        screen.blit(m2, [64, 78])
                        screen.blit(m1, [112, 74])
                        screen.blit(m2, [160, 78])
                elif anifr < 138:
                    spr = 5
                    fsp = 5
                    screen.blit(sn, [112, 78])
                else:
                    spr = 4
                    fsp = 4
        elif avars[avars[3][5]][32][frn][8] < 68:
            if vst:
                if anifr < 108:
                    if anifr % 12 < 6:
                        spr = 4
                        fsp = 11
                    else:
                        spr = 10
                        fsp = 12
                elif anifr < 132:
                    if anifr % 12 < 6:
                        spr = 11
                        fsp = 4
                    else:
                        spr = 12
                        fsp = 10
                elif anifr < 138:
                    spr = 5
                    fsp = 5
                    screen.blit(sn, [112, 78])
                else:
                    spr = 10
                    fsp = 10
            else:
                if anifr < 132:
                    if anifr % 12 < 6:
                        spr = 4
                        fsp = 5
                        screen.blit(m1, [64, 74])
                        screen.blit(m2, [112, 78])
                        screen.blit(m1, [160, 74])
                    else:
                        spr = 5
                        fsp = 4
                        screen.blit(m2, [64, 78])
                        screen.blit(m1, [112, 74])
                        screen.blit(m2, [160, 78])
                elif anifr < 138:
                    spr = 5
                    fsp = 5
                    screen.blit(sn, [112, 78])
                else:
                    spr = 4
                    fsp = 4
        else:
            if vst:
                if anifr < 108:
                    if anifr % 12 < 6:
                        spr = 4
                        fsp = 11
                    else:
                        spr = 10
                        fsp = 12
                elif anifr < 132:
                    if anifr % 12 < 6:
                        spr = 11
                        fsp = 4
                    else:
                        spr = 12
                        fsp = 10
                elif anifr < 138:
                    spr = 5
                    fsp = 5
                    screen.blit(sn, [112, 78])
                else:
                    spr = 10
                    fsp = 10
            else:
                if anifr < 132:
                    if anifr % 12 < 6:
                        spr = 10
                        fsp = 15
                        screen.blit(ht2, [64, 74])
                        screen.blit(ht, [112, 78])
                        screen.blit(ht2, [160, 74])
                    else:
                        spr = 15
                        fsp = 10
                        screen.blit(ht, [64, 78])
                        screen.blit(ht2, [112, 74])
                        screen.blit(ht, [160, 78])
                elif anifr < 138:
                    spr = 5
                    fsp = 5
                    screen.blit(sn, [112, 78])
                else:
                    spr = 10
                    fsp = 10
        sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        fsx = ((32 - fsprs[fsp].get_width()) // 2) + 80
        fsy = 98 + (32 - fsprs[fsp].get_height())
        return spr, sprx, spry, flip, fsp, fsx, fsy, fflip

    def gprs():
        flip = False
        fflip = True
        a = [4, 3, 9, 10, 5, 4, 3, 4, 5, 4]
        spr = a[(anifr - 84) // 6]
        a = [4, 3, 10, 4, 5, 4, 3, 4, 5, 4]
        fsp = a[(anifr - 84) // 6]
        a = [84, 94, 104, 104, 104, 104, 124, 144, 144, 144]
        px = a[(anifr - 84) // 6]
        sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        if (89 < anifr < 96) or (119 < anifr < 126):
            fsx = ((32 - fsprs[fsp].get_width()) // 2) + 76
        elif 95 < anifr < 120:
            fsx = ((32 - fsprs[fsp].get_width()) // 2) + 72
        else:
            fsx = ((32 - fsprs[fsp].get_width()) // 2) + 80
        if spr == 5:
            spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
            fsy = 96 + (32 - fsprs[fsp].get_height())
            screen.blit(sn, [112, 78])
        elif spr == 9:
            spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
            fsy = 98 + (32 - fsprs[fsp].get_height())
            screen.blit(em, [112, 78])
        else:
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            fsy = 98 + (32 - fsprs[fsp].get_height())
        screen.blit(press, [px, 106])
        return spr, sprx, spry, flip, fsp, fsx, fsy, fflip

    def marrani():
        flip = False
        fflip = True
        a = [10, 3, 10, 3, 10, 10, 5, 10, 15, 15, 15, 15]
        spr = a[(anifr - 72) // 6]
        a = [4, 6, 4, 6, 9, 9, 10, 5, 15, 15, 15, 15]
        fsp = a[(anifr - 72) // 6]
        spry = 98 + (32 - asprs[avars[3][5]][spr].get_height()) - (4 * (spr in [5, 9]))
        fsy = 98 + (32 - fsprs[fsp].get_height()) - (4 * (fsp in [5, 9]))
        if anifr < 120:
            sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            fsx = ((32 - fsprs[fsp].get_width()) // 2) + 80
        else:
            sprx = 120 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
            fsx = ((32 - fsprs[fsp].get_width()) // 2) + 88
        if 95 < anifr < 108:
            screen.blit(ring, [112, 104])
        if anifr < 96:
            if anifr % 12 < 6:
                screen.blit(sh, [112, 80])
            else:
                screen.blit(qm, [64, 80])
        elif anifr < 108:
            screen.blit(em, [64, 80])
        else:
            screen.blit([ht2, ht][anifr % 12 > 5], [64, [74, 78][anifr % 12 > 5]])
            screen.blit([ht, ht2][anifr % 12 > 5], [112, [78, 74][anifr % 12 > 5]])
            screen.blit([ht2, ht][anifr % 12 > 5], [160, [74, 78][anifr % 12 > 5]])
        if anifr in [96, 120]:
            pygame.mixer.stop()
            sound[9].play()
        return spr, sprx, spry, flip, fsp, fsx, fsy, fflip

    def bye():
        flip = False
        if anifr < 90:
            fflip = True
            if anifr == 84:
                pygame.mixer.stop()
                sound[9].play()
            spr = 5
            fsp = 5
            fsy = 96 + (32 - fsprs[fsp].get_height())
            spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
            fsx = ((32 - fsprs[fsp].get_width()) // 2) + 80
        else:
            fflip = False
            if anifr % 12 < 6:
                spr = 3
                fsp = 13
                fsy = 96 + (32 - fsprs[fsp].get_height())
            else:
                if anifr % 12 == 6:
                    pygame.mixer.stop()
                    sound[6].play()
                spr = 4
                fsp = 11
                fsy = 98 + (32 - fsprs[fsp].get_height())
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            fsx = 80 + ((32 - fsprs[fsp].get_width()) // 2) - (20 * ((anifr - 90) // 6))
        sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        return spr, sprx, spry, flip, fsp, fsx, fsy, fflip

    def opre():
        flip = False
        if anifr < 24:
            if anifr % 12 < 6:
                spr = 6
                screen.blit(qm, [120, 78])
            else:
                spr = 11
            screen.blit(press, [104, 106])
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif anifr < 36:
            spr = 12
            screen.blit(pygame.transform.flip(poof, (anifr % 12 < 6), 0), [100, 102])
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif anifr < 48:
            if anifr == 36:
                if pst == 0:
                    pygame.mixer.stop()
                    sound[12].play()
                else:
                    pygame.mixer.stop()
                    sound[9].play()
            spr = 9
            n = prl[pst].index(prs)
            screen.blit(prsl[pst][n], [(104 + ((24 - prsl[pst][n].get_width()) // 2)), (98 + (32 - prsl[pst][n].get_height()))])
            screen.blit(em, [120, 78])
            spry = 94 + (32 - asprs[avars[3][5]][spr].get_height())
        elif prs == "fly" or prs == "poo":
            if anifr % 12 < 6:
                spr = 6
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            else:
                spr = 8
                spry = 96 + (32 - asprs[avars[3][5]][spr].get_height())
                screen.blit(ang, [120, 78])
            if prs == "fly":
                if anifr == 48:
                    global fx
                    fx = [randint(48, 176), randint(48, 176), randint(48, 176), randint(48, 176)]
                    global fy
                    fy = [randint(32, 114), randint(32, 114), randint(32, 114), randint(32, 114)]
                screen.blit(pygame.transform.flip(fly, (anifr % 24 < 12), (anifr % 12 < 6)), [fx[((anifr - 48) // 6) % 4], fy[((anifr - 48) // 6) % 4]])
            else:
                if anifr % 12 < 6:
                    screen.blit(poo1, [108, 114])
                else:
                    screen.blit(poo2, [108, 114])
        elif prs in ["skull", "heart"]:
            if anifr < 60:
                spr = 9
                if prs == "skull":
                    screen.blit(sickbg, [0, -24])
                    screen.blit(skull, [110, 98])
                    screen.blit(skull, [122, 90])
                    screen.blit(skull, [134, 98])
                else:
                    screen.blit(ht, [110, 98])
                    screen.blit(ht, [122, 90])
                    screen.blit(ht, [134, 98])
            else:
                if anifr == 60:
                    if prs == "skull":
                        pygame.mixer.stop()
                        sound[14].play()
                    else:
                        pygame.mixer.stop()
                        sound[1].play()
                if anifr % 12 < 6:
                    spr = 6 + (4 * (prs == "heart"))
                else:
                    spr = 7 - (2 * (prs == "heart"))
                if prs == "skull":
                    screen.blit(sickbg, [0, 0])
                    screen.blit(skull, [112, (82 - ((anifr % 12 < 6) * 4))])
                    screen.blit(skull, [136, (66 + ((anifr % 12 < 6) * 4))])
                    screen.blit(skull, [160, (82 - ((anifr % 12 < 6) * 4))])
                else:
                    screen.blit(ht, [112, (82 - ((anifr % 12 < 6) * 4))])
                    screen.blit(ht, [136, (66 + ((anifr % 12 < 6) * 4))])
                    screen.blit(ht, [160, (82 - ((anifr % 12 < 6) * 4))])
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif prs == "sbox":
            if anifr < 96:
                if anifr % 12 < 6:
                    spr = 6
                    screen.blit(qm, [120, 78])
                else:
                    spr = 3
                screen.blit(sbx1, [104, 98])
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
            elif anifr < 108:
                if anifr == 96:
                    pygame.mixer.stop()
                    sound[8].play()
                spr = 9
                screen.blit(em, [120, 78])
                screen.blit(sbx2, [104, 98])
                spry = 90 + (32 - asprs[avars[3][5]][spr].get_height())
            else:
                if anifr % 12 < 6:
                    spr = 6
                else:
                    spr = 7
                screen.blit(sbx2, [104, 98])
                spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif prs in ["flower", "cake", "cream", "chht"]:
            if anifr < 54:
                spr = 11
            elif anifr < 60:
                if prs == "chht":
                    spr = 10
                    screen.blit(ht, [120, 78])
                else:
                    spr = 5
                    screen.blit(sn, [120, 78])
            else:
                if anifr % 12 < 6:
                    spr = 16
                else:
                    spr = 17
                    if anifr > 101:
                        if prs == "chht":
                            screen.blit(ht, [120, 78])
                        else:
                            screen.blit(sn, [120, 78])
            if prs == "flower":
                screen.blit(flw, [104, 106])
            elif prs == "cake":
                if anifr < 72:
                    screen.blit(ck1, [104, 106])
                elif anifr < 84:
                    screen.blit(ck2, [104, 106])
                elif anifr < 96:
                    screen.blit(ck3, [104, 106])
            elif prs == "cream":
                if anifr < 72:
                    screen.blit(ic1, [104, 106])
                elif anifr < 84:
                    screen.blit(ic2, [104, 106])
                elif anifr < 96:
                    screen.blit(ic3, [104, 106])
            elif prs == "chht":
                if anifr < 72:
                    screen.blit(ch1, [104, 106])
                elif anifr < 84:
                    screen.blit(ch2, [104, 106])
                elif anifr < 96:
                    screen.blit(ch3, [104, 106])
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height())
        elif prs in ["ball", "rope", "letter", "fb", "copre"]:
            if anifr < 54:
                spr = 11
            elif anifr < 60:
                spr = 5
                if prs in ["ball", "rope"]:
                    screen.blit(sn, [120, 78])
                else:
                    screen.blit(ht, [120, 78])
            else:
                if anifr == 60:
                    pygame.mixer.stop()
                    sound[1].play()
                if anifr % 12 < 6:
                    if prs in ["ball", "rope"]:
                        spr = 4
                    else:
                        spr = 10
                else:
                    spr = 5
                    if prs in ["ball", "rope"]:
                        screen.blit(sn, [120, 78])
                    else:
                        screen.blit(ht, [120, 78])
            n = prl[pst].index(prs)
            screen.blit(prsl[pst][n], [(104 + ((24 - prsl[pst][n].get_width()) // 2)), (106 + (24 - prsl[pst][n].get_height()))])
            spry = 98 + (32 - asprs[avars[3][5]][spr].get_height()) - (4 * (anifr > 59 and spr == 5))
        sprx = 128 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)
        return spr, sprx, spry, flip

    ltrbase = pygame.image.load("Sprites/Misc/txtbox/box3.png").convert()

    def addmail():
        fltr = pygame.Surface([240, 160]).convert()
        fltr.fill((0, 255, 255))
        fltr.blit(ltrbase, [0, 0])
        if avars[avars[3][5]][32][frn][0] == avars[3][0]:
            fltr.blit(fnt.render(avars[avars[3][5]][32][frn][1], 1, (0, 0, 100)), [16, 114])
        else:
            if avars[avars[3][5]][32][frn][2] < 385:
                fltr.blit(fnt.render(chnamelst[(avars[avars[3][5]][32][frn][2] - 1)], 1, (0, 0, 100)), [16, 114])
            else:
                try:
                    screen.blit((fnt.render(extrchn[str(avars[avars[3][5]][32][frn][2])], 1, (0, 0, 100))), [16, 114])
                except:
                    screen.blit((fnt.render("???", 1, (0, 0, 100))), [16, 114])
        if avars[avars[3][5]][32][frn][8] < 14:
            fltr.blit(lfnt.render(("TO " + avars[avars[3][5]][22] + ":"), 1, (0, 0, 100)), [8, 31])
            fltr.blit(cnf, [176, 88])
            fltr.blit(fsprs[6], [(((32 - fsprs[3].get_width()) // 2) + 200), (96 + (32 - fsprs[3].get_height()))])
            fltr.blit(lfnt.render("FROM...", 1, (0, 0, 100)), [8, 95])
            if avars[avars[3][5]][32][frn][0] == avars[3][0]:
                t = ["",
                     "I HAVE  NO IDEA WHY I AM WRITING A LETTER TO",
                     "YOU, GIVEN THAT WE  LIVE  IN THE  SAME  HOUSE...",
                     "",
                     "IT IS ALSO A BIT STRANGE  THAT WE  RARELY GET",
                     "TO SEE  EACH OTHER, TOO..."]
            else:
                t = ["",
                     "UH... SORRY... I DO NOT REALLY KNOW WHAT TO",
                     "WRITE  TO YOU...",
                     "",
                     "WE  DO NOT REALLY KNOW EACH OTHER TOO MUCH",
                     "YET, DO WE?"]
        elif avars[avars[3][5]][32][frn][8] < 41:
            fltr.blit(lfnt.render(("DEAR " + avars[avars[3][5]][22] + ","), 1, (0, 0, 100)), [8, 31])
            fltr.blit(fsprs[3], [(((32 - fsprs[3].get_width()) // 2) + 200), (96 + (32 - fsprs[3].get_height()))])
            fltr.blit(lfnt.render("GOODBYE!", 1, (0, 0, 100)), [8, 95])
            if avars[avars[3][5]][32][frn][0] == avars[3][0]:
                t = ["",
                     "HOW ARE YOU DOING TODAY?",
                     "WELL, I  GUESS I  COULD JUST GO TO YOUR  ROOM",
                     "AND CHECK IT, MYSELF...",
                     "",
                     "WHY AM I  EVEN WASTING PAPER  ON THIS?"]
            else:
                t = ["",
                     "HOW ARE YOU DOING TODAY?",
                     "I HOPE  YOU ARE  FINE.",
                     "",
                     "I WOULD REALLY LIKE  TO MEET YOU AGAIN",
                     "SOMETIME SOON..."]
        elif avars[avars[3][5]][32][frn][8] < 68:
            fltr.blit(lfnt.render(("HELLO, " + avars[avars[3][5]][22] + ","), 1, (0, 0, 100)), [8, 31])
            fltr.blit(sn, [176, 88])
            fltr.blit(fsprs[5], [(((32 - fsprs[3].get_width()) // 2) + 200), (96 + (32 - fsprs[3].get_height()))])
            fltr.blit(lfnt.render("SEE YOU!", 1, (0, 0, 100)), [8, 95])
            if avars[avars[3][5]][32][frn][0] == avars[3][0]:
                t = ["",
                     "...UH...",
                     "",
                     "HOW IS THIS EASIER THAN GOING TO YOUR  ROOM,",
                     "WHICH IS LITERALLY IN THE  SAME  HOUSE AS ME?",
                     "WE  SHOULD JUST MEET IN PERSON!  :P"]
            else:
                t = ["",
                     "IS EVERYTHING OK?",
                     "",
                     "WE  MEET SO OFTEN THAT WRITING A LETTER  TO",
                     "YOU FEELS WIERD.",
                     "I WOULD RATHER SEE YOU IN  PERSON, INSTEAD.  :)"]
        else:
            fltr.blit(lfnt.render(("HI, " + avars[avars[3][5]][22] + "!"), 1, (0, 0, 100)), [8, 31])
            fltr.blit(ht, [176, 88])
            fltr.blit(fsprs[10], [(((32 - fsprs[3].get_width()) // 2) + 200), (96 + (32 - fsprs[3].get_height()))])
            fltr.blit(lfnt.render("BYE!!!", 1, (0, 0, 100)), [8, 95])
            if avars[avars[3][5]][32][frn][0] == avars[3][0]:
                t = ["   00   00",
                     "0      0      0",
                     "0   I <3   0",
                     "   0   U   0",
                     "      0   0",
                     "         0"]
            else:
                t = ["",
                     "I  DO NOT REALLY WANT TO WRITE  A LETTER...",
                     "",
                     "I WANT TO SEE  YOU IN PERSON!",
                     "",
                     "<3"]
        fltr.blit(lfnt.render(t[0], 1, (0, 0, 100)), [8, 39])
        fltr.blit(lfnt.render(t[1], 1, (0, 0, 100)), [8, 47])
        fltr.blit(lfnt.render(t[2], 1, (0, 0, 100)), [8, 55])
        fltr.blit(lfnt.render(t[3], 1, (0, 0, 100)), [8, 63])
        fltr.blit(lfnt.render(t[4], 1, (0, 0, 100)), [8, 71])
        fltr.blit(lfnt.render(t[5], 1, (0, 0, 100)), [8, 79])
        a = str(len([n for n in os.listdir("Sprites/Misc/mail/tm" + str(avars[3][5] + 1))]))
        pygame.image.save(fltr, "Sprites/Misc/mail/tm" + str(avars[3][5] + 1) + "/frnd_ltr_" + a + ".png")

    def encode(etyp, data):
        u = ''
        for i in data[0]:
            u = u + format((i.encode('ascii')[0] - 64), '05b')
        while len(u) < 40:
            u = u + '0'
        n = ''
        for i in data[1]:
            n = n + format((i.encode('ascii')[0] - 64), '05b')
        while len(n) < 40:
            n = n + '0'
        if etyp == 0:
            c = format(data[2], '016b')
            u = u + c[8:]
            n = n + c[:8]
            if data[3] < 0:
                data[3] = 4294967296 + data[3]
            iv = format(data[3], '032b')
            iv = iv + format(['no', 'ma', 'me', 'ku'].index(data[4]), '02b') + format(['no', 'ma', 'me', 'ku'].index(data[5]), '02b')
            if data[6] in ['no', 'ma', 'me', 'ku']:
                iv = iv + format(['no', 'ma', 'me', 'ku'].index(data[6]), '04b')
            else:
                iv = iv + format(data[6], '04b')
            iv = iv + format((data[7] // 86400), '08b')
            code = '%036x' % int((u + n + iv), 2)
        else:
            mkv = 0
            for i in range(5):
                mkv += (int(u[(i * 8):((i * 8) + 8)], 2) ^ int(n[(i * 8):((i * 8) + 8)], 2))
            mkv = mkv % 256
            c = format(data[2], '016b')
            if data[3] < 0:
                data[3] = 4294967296 + data[3]
            iv = format(data[3], '032b')
            iv = format(int(iv[:16], 2) ^ int(iv[16:], 2), '016b')
            iv = iv + c + format((data[4] // 86400), '08b')
            cod = '%012x' % int((iv + format(data[5], '04b') + format(data[6], '04b')), 2)
            if data[5] == 0 or (data[5] == 3 and (0 < data[6] < 4)):
                cod = cod + ('%02x' % int(format(data[7], '08b'), 2))
            elif data[5] == 3 and data[6] == 4:
                on = ''
                i = 0
                for l in data[7][0]:
                    on = on + format((l.encode('ascii')[0]), '08b')
                    i += 1
                if len(data[7]) == 11:
                    on = on + '11111111'
                else:
                    on = on + '11111110'
                a = '%0' + str((i * 2) + 2) + 'x'
                cod = cod + (a % int(on, 2))
                lval = ''
                i = 1
                if len(data[7]) == 11:
                    while i < 3:
                        lval = lval + format(data[7][i], '03b')
                        i += 1
                    lval = lval + format(data[7][3], '04b')
                    i = 4
                lval = lval + '00'
                i += 1
                if len(data[7]) == 9:
                    lval = lval + format(data[7][i], '02b')
                    i += 1
                for j in range(6):
                    lval = lval + format(data[7][i + j], '02b')
                #print(lval)
                if len(data[7]) == 11:
                    cod = cod + ('%06x' % int(lval, 2))
                else:
                    cod = cod + ('%04x' % int(lval, 2))
                #print(cod)
            elif data[5] == 4 and data[6] == 1:
                txt = ''
                for l in range(6):
                    for i in data[7][l]:
                        if i != " ":
                            txt = txt + format((i.encode('ascii')[0] - 64), '05b')
                        else:
                            txt = txt + '00000'
                    txt = txt + '11111'
                txt = txt + format((data[8] - 3), '04b')
                while len(txt) % 8 != 0:
                    txt = txt + '0'
                a = '%0' + str(len(txt) // 4) + 'x'
                cod = cod + (a % int(txt, 2))
            elif data[5] == 5:
                a = ['no', 'ma', 'me', 'ku'].index(data[7][0])
                b = ['no', 'ma', 'me', 'ku'].index(data[7][1])
                cod = cod + str(a) + str(b)
            code = ''
            for i in range(len(cod) // 2):
                code = code + ('%02x' % (int(cod[(i * 2):((i * 2) + 2)], 16) ^ mkv))
        return(code)

    def decode(code, frd):
        if len(code) == 36:
            un = ""
            und = format(int(code[:10], 16), '040b')
            for i in range(8):
                if und[(5 * i):((5 * i) + 5)] == '00000':
                    break
                else:
                    un = un + bytes([int(und[(5 * i):((5 * i) + 5)], 2) + 64]).decode('ascii')
            cn = ""
            cnd = format(int(code[12:22], 16), '040b')
            for i in range(8):
                if cnd[(5 * i):((5 * i) + 5)] == '00000':
                    break
                else:
                    cn = cn + bytes([int(cnd[(5 * i):((5 * i) + 5)], 2) + 64]).decode('ascii')
            ct = int(code[22:24] + code[10:12], 16)
            iv = int(code[24:32], 16)
            fd = format(int(code[32:34], 16), '08b')
            f1 = ['no', 'ma', 'me', 'ku'][int(fd[:2], 2)]
            f2 = ['no', 'ma', 'me', 'ku'][int(fd[2:4], 2)]
            if int(fd[4:], 2) < 4:
                fg = ['no', 'ma', 'me', 'ku'][int(fd[4:], 2)]
            else:
                fg = int(fd[4:], 2)
            lt = int(code[34:36], 16) * 86400
            return(un, cn, ct, iv, f1, f2, fg, lt)
        else:
            u = ''
            for i in frd[0]:
                u = u + format((i.encode('ascii')[0] - 64), '05b')
            while len(u) < 40:
                u = u + '0'
            n = ''
            for i in frd[1]:
                n = n + format((i.encode('ascii')[0] - 64), '05b')
            while len(n) < 40:
                n = n + '0'
            mkv = 0
            for i in range(5):
                mkv += (int(u[(i * 8):((i * 8) + 8)], 2) ^ int(n[(i * 8):((i * 8) + 8)], 2))
            mkv = mkv % 256
            rcode = ''
            for i in range(len(code) // 2):
                rcode = rcode + ('%02x' % (int(code[(i * 2):((i * 2) + 2)], 16) ^ mkv))
            if frd[3] < 0:
                frd[3] = 4294967296 + frd[3]
            iv = format(frd[3], '032b')
            iv = format(int(iv[:16], 2) ^ int(iv[16:], 2), '016b')
            if int(iv, 2) != int(rcode[:4], 16):
                raise Exception("Wrong code!")
            ct = int(rcode[4:8], 16)
            lt = int(rcode[8:10], 16) * 86400
            cnt = int(rcode[10], 16)
            st = int(rcode[11], 16)
            if cnt == 0 or (cnt == 3 and (0 < st < 4)):
                ed = int(rcode[12:], 16)
            elif cnt in [1, 2] or (cnt in [3, 4] and st == 0):
                ed = 0
            elif cnt == 3 and st == 4:
                ed = []
                on = ""
                i = 12
                while rcode[i:(i + 2)] not in ['ff', 'fe']:
                    on = on + bytes([int(rcode[i:(i + 2)], 16)]).decode('ascii')
                    i += 2
                ed.append(on)
                ot = ['ff', 'fe'].index(rcode[i:(i + 2)])
                if ot == 0:
                    lval = format(int(rcode[(i + 2):], 16), '024b')
                else:
                    lval = format(int(rcode[(i + 2):], 16), '016b')
                i = 0
                if ot == 0:
                    while i < 6:
                        ed.append(int(lval[i:(i + 3)], 2))
                        i += 3
                    ed.append(int(lval[6:10], 2))
                    i = 10
                ed.append(1)
                i += 2
                if ot == 1:
                    ed.append(int(lval[i:(i + 2)], 2))
                    i += 2
                for j in range(6):
                    ed.append(int(lval[(i + (2 * j)):((i + (2 * j)) + 2)], 2))
            elif cnt == 4 and st == 1:
                ed = [["", "", "", "", "", ""]]
                a = '0' + str((len(rcode) - 12) * 4) + 'b'
                tdat = format(int(rcode[12:], 16), a)
                l = 0
                for i in range(6):
                    while tdat[l:(l + 5)] != '11111':
                        if tdat[l:(l + 5)] != '00000':
                            ed[0][i] = ed[0][i] + bytes([int(tdat[l:(l + 5)], 2) + 64]).decode('ascii')
                        else:
                            ed[0][i] = ed[0][i] + " "
                        l += 5
                    l += 5
                ed.append(int(tdat[l:(l + 4)], 2) + 3)
            elif cnt == 5:
                ed = [['no', 'ma', 'me', 'ku'][int(rcode[12])], ['no', 'ma', 'me', 'ku'][int(rcode[13])]]
            return(ct, lt, cnt, st, ed)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 4, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    sn = pygame.image.load("Sprites/Misc/emo/happy.png").convert()
    ht = pygame.image.load("Sprites/Misc/emo/heart.png").convert()
    ht2 = pygame.image.load("Sprites/Misc/emo/heart2.png").convert()
    em = pygame.image.load("Sprites/Misc/emo/em.png").convert()
    qm = pygame.image.load("Sprites/Misc/emo/qm.png").convert()
    m1 = pygame.image.load("Sprites/Misc/emo/music1.png").convert()
    m2 = pygame.image.load("Sprites/Misc/emo/music2.png").convert()
    sh = pygame.image.load("Sprites/Misc/emo/shine.png").convert()
    ang = pygame.image.load("Sprites/Misc/emo/ang.png").convert()
    cnf = pygame.image.load("Sprites/Misc/emo/conf.png").convert()

    cons = pygame.image.load("Sprites/Misc/menu/cons.png").convert()

    press = pygame.image.load("Sprites/Misc/obj/present.png").convert()

    ring = pygame.image.load("Sprites/Misc/obj/mring.png").convert()

    prl = [["fly", "poo", "skull", "sbox"], ["flower", "cake", "cream", "ball", "rope"], ["heart", "letter", "fb", "chht"]]

    poof = pygame.image.load("Sprites/Misc/obj/poof.png").convert()

    fly = pygame.image.load("Sprites/Misc/obj/fly.png").convert()
    poo1 = pygame.image.load("Sprites/Misc/poo/bpoo1.png").convert()
    poo2 = pygame.image.load("Sprites/Misc/poo/bpoo2.png").convert()
    skull = pygame.image.load("Sprites/Misc/sick/skull.png").convert()
    sbx1 = pygame.image.load("Sprites/Misc/obj/sbox1.png").convert()
    sbx2 = pygame.image.load("Sprites/Misc/obj/sbox2.png").convert()

    sickbg = pygame.image.load("Sprites/Misc/bg/sick.png").convert()
    sickbg.set_alpha(204)

    flw = pygame.image.load("Sprites/Misc/obj/flower.png").convert()
    s = pygame.image.load("Sprites/Food/Cake.png").convert()
    ck1 = pygame.Surface([24, 24]).convert()
    ck1.fill((0, 255, 255))
    ck1.blit(s, [0, 0])
    ck1.set_colorkey((0, 255, 255))
    ck2 = pygame.Surface([24, 24]).convert()
    ck2.fill((0, 255, 255))
    ck2.blit(s, [-24, 0])
    ck2.set_colorkey((0, 255, 255))
    ck3 = pygame.Surface([24, 24]).convert()
    ck3.fill((0, 255, 255))
    ck3.blit(s, [-48, 0])
    ck3.set_colorkey((0, 255, 255))
    s = pygame.image.load("Sprites/Food/IceCream.png").convert()
    ic1 = pygame.Surface([24, 24]).convert()
    ic1.fill((0, 255, 255))
    ic1.blit(s, [0, 0])
    ic1.set_colorkey((0, 255, 255))
    ic2 = pygame.Surface([24, 24]).convert()
    ic2.fill((0, 255, 255))
    ic2.blit(s, [-24, 0])
    ic2.set_colorkey((0, 255, 255))
    ic3 = pygame.Surface([24, 24]).convert()
    ic3.fill((0, 255, 255))
    ic3.blit(s, [-48, 0])
    ic3.set_colorkey((0, 255, 255))
    ball = pygame.image.load("Sprites/Misc/item/ball.png").convert()
    rope = pygame.image.load("Sprites/Misc/item/rope.png").convert()

    llt = pygame.image.load("Sprites/Misc/obj/lletter.png").convert()
    fb = pygame.image.load("Sprites/Misc/obj/flb.png").convert()
    s = pygame.image.load("Sprites/Food/ChocoH.png").convert()
    ch1 = pygame.Surface([24, 24]).convert()
    ch1.fill((0, 255, 255))
    ch1.blit(s, [0, 0])
    ch1.set_colorkey((0, 255, 255))
    ch2 = pygame.Surface([24, 24]).convert()
    ch2.fill((0, 255, 255))
    ch2.blit(s, [-24, 0])
    ch2.set_colorkey((0, 255, 255))
    ch3 = pygame.Surface([24, 24]).convert()
    ch3.fill((0, 255, 255))
    ch3.blit(s, [-48, 0])
    ch3.set_colorkey((0, 255, 255))

    ballit = ['ball', 1, 1, 0, 0, 0, 0, 0, 0]
    ropeit =  ['rope', 1, 1, 0, 0, 0, 0, 0, 0]

    prsot = True
    
    prsl = [[fly, poo1, skull, sbx1], [flw, ck1, ic1, ball, rope], [ht, llt, fb, ch1]]

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

    inbox = []
    
    for file in os.listdir("Inbox"):
        if file.endswith(".png"):
            if pygame.image.load("Inbox/" + file).get_rect().size == (240, 160):
                inbox.append(pygame.image.load("Inbox/" + file).convert())

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

    rain = pygame.image.load("Sprites/Misc/bg/rain.png").convert()
    snow = pygame.image.load("Sprites/Misc/bg/snow.png").convert()

    pfl = []
    for a in avars[avars[3][5]][32]:
        if a[0] == "PARK":
            pfl.append(a)

    hfb = []
    hfn = []
    if len(avars[0]) > 0 and avars[3][5] != 0:
        hfb.append(0)
        hfn.append(avars[0][22])
    if len(avars[1]) > 0 and avars[3][5] != 1:
        hfb.append(1)
        hfn.append(avars[1][22])
    if len(avars[2]) > 0 and avars[3][5] != 2:
        hfb.append(2)
        hfn.append(avars[2][22])

    ofl = []
    ofln = []
    i = 0
    for a in avars[avars[3][5]][32]:
        if a[0] != "PARK" and not(a[0] == avars[3][0] and a[1] in hfn):
            ofl.append(a)
            ofln.append(i)
        i += 1
    
    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if bx:
            screen.blit(textbox, [0, 24])
            if scr == 0:
                if ((len(avars[0]) > 0) + (len(avars[1]) > 0) + (len(avars[2]) > 0)) > 1:
                    screen.blit((fnt.render("WITHIN HOUSE", 1, (0, 0, 100))), [8, 34])
                else:
                    screen.blit((fnt.render("WITHIN HOUSE", 1, (102, 102, 255))), [8, 34])
                if len(pfl) > 0:
                    screen.blit((fnt.render("PARK FRIENDS", 1, (0, 0, 100))), [8, 50])
                else:
                    screen.blit((fnt.render("PARK FRIENDS", 1, (102, 102, 255))), [8, 50])
                screen.blit((fnt.render("ONLINE", 1, (0, 0, 100))), [8, 66])
            elif scr == 1:
                for n in hfn:
                    screen.blit((fnt.render(n, 1, (0, 0, 100))), [8, (34 + (16 * (hfn.index(n))))])
            elif scr == 2:
                screen.blit(scrli, [232, 128])
                for n in pfl:
                    if (fsc * 6) <= pfl.index(n) <= ((fsc * 6) + 5):
                        if n[2] < 385:
                            screen.blit((fnt.render(chnamelst[(n[2] - 1)], 1, (0, 0, 100))), [8, (34 + (16 * (pfl.index(n) % 6)))])
                        else:
                            try:
                                screen.blit((fnt.render(extrchn[str(n[2])], 1, (0, 0, 100))), [8, (34 + (16 * (pfl.index(n) % 6)))])
                            except:
                                screen.blit((fnt.render("???", 1, (0, 0, 100))), [8, (34 + (16 * (pfl.index(n) % 6)))])
            elif scr == 3:
                screen.blit((fnt.render("GAME", 1, (0, 0, 100))), [8, 34])
                screen.blit((fnt.render("VISIT", 1, (0, 0, 100))), [8, 50])
                screen.blit((fnt.render("PRESENT", 1, (0, 0, 100))), [8, 66])
                screen.blit((fnt.render("LETTER", 1, (0, 0, 100))), [8, 82])
                screen.blit((fnt.render("PARK", 1, (0, 0, 100))), [8, 98])
                if marrag and (avars[avars[3][5]][32][frn][8] == 80):
                    screen.blit((fnt.render("MARRY", 1, (0, 0, 100))), [8, 114])
                else:
                    screen.blit((fnt.render("MARRY", 1, (102, 102, 255))), [8, 114])
            elif scr == 8:
                if len(ofl) > 0:
                    screen.blit((fnt.render("KNOWN", 1, (0, 0, 100))), [8, 34])
                else:
                    screen.blit((fnt.render("KNOWN", 1, (102, 102, 255))), [8, 34])
                screen.blit((fnt.render("NEW", 1, (0, 0, 100))), [8, 50])
                screen.blit((fnt.render("CREATE CODES", 1, (0, 0, 100))), [8, 66])
            elif scr == 9:
                screen.blit(scrli, [232, 128])
                for n in ofl:
                    if (fsc * 6) <= ofl.index(n) <= ((fsc * 6) + 5):
                        screen.blit((fnt.render(n[1], 1, (0, 0, 100))), [8, (34 + (16 * (ofl.index(n) % 6)))])
            elif scr == 4:
                screen.blit((fnt.render("1. RIGHT CLICK TO COPY", 1, (0, 0, 100))), [8, 34])
                screen.blit((fnt.render("YOUR CODE.", 1, (0, 0, 100))), [8, 50])
                screen.blit((fnt.render("2. COPY THE CODE YOU", 1, (0, 0, 100))), [8, 66])
                screen.blit((fnt.render("WANT TO USE.", 1, (0, 0, 100))), [8, 82])
                screen.blit((fnt.render("3. LEFT CLICK.", 1, (0, 0, 100))), [8, 98])
                screen.blit(ht, [8, 116])
                screen.blit(cons, [64, 116])
                screen.blit(ht, [216, 116])
                screen.blit(pygame.transform.flip(cons, 1, 0), [160, 116])
            elif  scr == 5:
                screen.blit((fnt.render("EATING", 1, (0, 0, 100))), [8, 34])
                screen.blit((fnt.render("BALLOON", 1, (0, 0, 100))), [8, 50])
                if avars[3][2] < 100:
                    screen.blit((fnt.render("BET", 1, (102, 102, 255))), [8, 66])
                else:
                    screen.blit((fnt.render("BET", 1, (0, 0, 100))), [8, 66])
                screen.blit((fnt.render("BALL", 1, (0, 0, 100))), [8, 82])
                screen.blit((fnt.render("ROPE", 1, (0, 0, 100))), [8, 98])
            elif scr == 12:
                screen.blit((fnt.render("GIVE", 1, (0, 0, 100))), [8, 34])
                screen.blit((fnt.render("RECEIVE", 1, (0, 0, 100))), [8, 50])
            elif scr == 10:
                if len(avars[3][4]) > 0:
                    screen.blit((fnt.render("FOOD", 1, (0, 0, 100))), [8, 34])
                else:
                    screen.blit((fnt.render("FOOD", 1, (102, 102, 255))), [8, 34])
                if len(avars[3][9]) > 0:
                    screen.blit((fnt.render("ITEM", 1, (0, 0, 100))), [8, 50])
                else:
                    screen.blit((fnt.render("ITEM", 1, (102, 102, 255))), [8, 50])
                screen.blit((fnt.render("RANDOM", 1, (0, 0, 100))), [8, 66])
            elif scr == 11:
                screen.blit(scrli, [232, 128])
                drawobj()
            elif scr == 14:
                screen.blit((fnt.render("WRITE", 1, (0, 0, 100))), [8, 34])
                screen.blit((fnt.render("RECEIVE", 1, (0, 0, 100))), [8, 50])
                if len(inbox) == 0:
                    screen.blit((fnt.render("INBOX", 1, (102, 102, 255))), [8, 66])
                else:
                    screen.blit((fnt.render("INBOX", 1, (0, 0, 100))), [8, 66])
            elif scr == 13:
                screen.blit(scrli, [232, 128])
                screen.blit(ltrbase, [0, 0])
                screen.blit(lfnt.render(("DEAR " + avars[avars[3][5]][32][frn][1] + ","), 1, (0, 0, 100)), [8, 31])
                screen.blit(lfnt.render(ltrtxt[0], 1, (0, 0, 100)), [8, 39])
                screen.blit(lfnt.render(ltrtxt[1], 1, (0, 0, 100)), [8, 47])
                screen.blit(lfnt.render(ltrtxt[2], 1, (0, 0, 100)), [8, 55])
                screen.blit(lfnt.render(ltrtxt[3], 1, (0, 0, 100)), [8, 63])
                screen.blit(lfnt.render(ltrtxt[4], 1, (0, 0, 100)), [8, 71])
                screen.blit(lfnt.render(ltrtxt[5], 1, (0, 0, 100)), [8, 79])
                screen.blit(fnt.render(avars[avars[3][5]][22], 1, (0, 0, 100)), [16, 114])
                screen.blit(asprs[avars[3][5]][shspr], [(((32 - asprs[avars[3][5]][3].get_width()) // 2) + 200), (96 + (32 - asprs[avars[3][5]][3].get_height()))])
                screen.blit(lfnt.render("GOODBYE!", 1, (0, 0, 100)), [8, 95])
            elif scr == 15:
                screen.blit((fnt.render("CLICK!!!", 1, (240, 0, 100))), [80, 50])
                screen.blit((fnt.render("POWER:", 1, (0, 0, 100))), [74, 98])
                screen.blit((fnt.render(("%02d" % power), 1, (204, 0, 100))), [148, 98])
        else:
            if scr == 4:
                screen.blit(bgi, [0, 0])
                spr, sprx, spry, flip, fsp, fsx, fsy, fflip = meet()
            elif scr == 5:
                screen.blit(bgi, [0, 0])
                if comt == 0:
                    spr, sprx, spry, flip, fsp, fsx, fsy, fflip = intro()
                elif comt == 1:
                    spr, sprx, spry, flip, fsp, fsx, fsy, fflip = visit()
                elif comt == 2:
                    spr, sprx, spry, flip, fsp, fsx, fsy, fflip = gprs()
                elif comt == 6:
                    spr, sprx, spry, flip, fsp, fsx, fsy, fflip = marrani()
            elif scr == 6:
                screen.blit(bgi, [0, 0])
                if comt == 2:
                    screen.blit(press, [144, 106])
                spr, sprx, spry, flip, fsp, fsx, fsy, fflip = bye()
            elif scr == 7:
                screen.blit(bgi, [0, 0])
                if comt == 2:
                    spr, sprx, spry, flip = opre()
            if online:
                if conmd == 0:
                    screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [sprx, spry])
                    if scr < 7:
                        screen.blit(pygame.transform.flip(fsprs[fsp], fflip, 0), [fsx, fsy])
                else:
                    a = fsprs[spr].get_height() - asprs[avars[3][5]][spr].get_height()
                    screen.blit(pygame.transform.flip(fsprs[spr], flip, 0), [(sprx - (a // 2)), (spry - a)])
                    if scr < 7:
                        screen.blit(pygame.transform.flip(asprs[avars[3][5]][fsp], fflip, 0), [(fsx - (a // 2)), (fsy + a)])
            else:
                screen.blit(pygame.transform.flip(asprs[avars[3][5]][spr], flip, 0), [sprx, spry])
                if scr < 7:
                    screen.blit(pygame.transform.flip(fsprs[fsp], fflip, 0), [fsx, fsy])
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
                #TESTING
                #if event.key == K_m and scr == 3:
                    #avars[avars[3][5]][32][frn][8] = 80
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
                        if scr == 2:
                            pygame.mixer.stop()
                            sound[2].play()
                            if fsc != ((len(pfl) - 1) // 6):
                                fsc += 1
                            else:
                                fsc = 0
                        elif scr == 9:
                            pygame.mixer.stop()
                            sound[2].play()
                            if fsc != ((len(ofl) - 1) // 6):
                                fsc += 1
                            else:
                                fsc = 0
                        elif scr == 11:
                            pygame.mixer.stop()
                            sound[2].play()
                            if oscr != objsmax:
                                oscr += 1
                            else:
                                oscr = 0
                        elif scr == 13:
                            pygame.mixer.stop()
                            sound[2].play()
                            if shspr != 18:
                                shspr += 1
                            else:
                                shspr = 3
                        clt = 0
                elif pb == 5:
                    if 24 < mp[1] < 136:
                        if scr == 2:
                            pygame.mixer.stop()
                            sound[2].play()
                            if fsc != 0:
                                fsc -= 1
                            else:
                                fsc = ((len(pfl) - 1) // 6)
                        elif scr == 9:
                            pygame.mixer.stop()
                            sound[2].play()
                            if fsc != 0:
                                fsc -= 1
                            else:
                                fsc = ((len(ofl) - 1) // 6)
                        elif scr == 11:
                            pygame.mixer.stop()
                            sound[2].play()
                            if oscr != 0:
                                oscr -= 1
                            else:
                                oscr = objsmax
                        elif scr == 13:
                            pygame.mixer.stop()
                            sound[2].play()
                            if shspr != 3:
                                shspr -= 1
                            else:
                                shspr = 18
                        clt = 0
                elif pb == 1 and bx and cclk:
                    clt = 0
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            pygame.mixer.stop()
                            sound[4].play()
                            return(avars)
                    if scr == 0:
                        if (32 < mp[1] < 48) and (8 < mp[0] < 142) and ((len(avars[0]) > 0) + (len(avars[1]) > 0) + (len(avars[2]) > 0)) > 1:
                            pygame.mixer.stop()
                            sound[3].play()
                            scr = 1
                        if (48 < mp[1] < 64) and (8 < mp[0] < 148) and len(pfl) > 0:
                            pygame.mixer.stop()
                            sound[3].play()
                            scr = 2
                            fsc = 0
                        if (64 < mp[1] < 80) and (8 < mp[0] < 78):
                            pygame.mixer.stop()
                            sound[3].play()
                            scr = 8
                    elif scr == 1:
                        if (32 < mp[1] < 48) and (8 < mp[0] < 110):
                            a = False
                            for b in avars[avars[3][5]][32]:
                                if b[0] == avars[3][0] and b[1] == hfn[0]:
                                    a = True
                                    c = avars[avars[3][5]][32]
                                    frn = c.index(b)
                                    avars[avars[3][5]][32][frn][2] = avars[hfb[0]][15]
                                    avars[avars[3][5]][32][frn][7] = avars[hfb[0]][2]
                                    marrag = ((avars[avars[3][5]][32][frn][7] > 691199) and (avars[avars[3][5]][2] > 691199) \
                                              and ((format(avars[avars[3][5]][32][frn][3], '032b')[16:28]) != (format(avars[avars[3][5]][14], '032b')[16:28])))
                            if not a:
                                bx = False
                                scr = 4
                                comt = 0
                                anifr = 83
                                c = [avars[3][0], hfn[0], avars[hfb[0]][15], avars[hfb[0]][14], avars[hfb[0]][13], avars[hfb[0]][12], avars[hfb[0]][11], avars[hfb[0]][2], 0]
                                d = [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14], avars[avars[3][5]][13], avars[avars[3][5]][12], avars[avars[3][5]][11], avars[avars[3][5]][2], 0]
                                f = avars[avars[3][5]][32]
                                f.append(c)
                                avars[avars[3][5]][32] = f
                                f = avars[hfb[0]][32]
                                f.append(d)
                                avars[hfb[0]][32] = f
                            else:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 3
                            fsprs = chsprs(avars[hfb[0]][15], avars[hfb[0]][14])
                        if (48 < mp[1] < 64) and (8 < mp[0] < 110) and len(hfn) > 1:
                            a = False
                            for b in avars[avars[3][5]][32]:
                                if b[0] == avars[3][0] and b[1] == hfn[1]:
                                    a = True
                                    c = avars[avars[3][5]][32]
                                    frn = c.index(b)
                                    avars[avars[3][5]][32][frn][2] = avars[hfb[1]][15]
                                    avars[avars[3][5]][32][frn][7] = avars[hfb[1]][2]
                                    marrag = ((avars[avars[3][5]][32][frn][7] > 691199) and (avars[avars[3][5]][2] > 691199) \
                                              and ((format(avars[avars[3][5]][32][frn][3], '032b')[16:28]) != (format(avars[avars[3][5]][14], '032b')[16:28])))
                            if not a:
                                bx = False
                                scr = 4
                                comt = 0
                                anifr = 83
                                c = [avars[3][0], hfn[1], avars[hfb[1]][15], avars[hfb[1]][14], avars[hfb[1]][13], avars[hfb[1]][12], avars[hfb[1]][11], avars[avars[3][5]][1], 0]
                                d = [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14], avars[avars[3][5]][13], avars[avars[3][5]][12], avars[avars[3][5]][11], avars[avars[3][5]][2], 0]
                                f = avars[avars[3][5]][32]
                                f.append(c)
                                avars[avars[3][5]][32] = f
                                f = avars[hfb[1]][32]
                                f.append(d)
                                avars[hfb[1]][32] = f
                            else:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 3
                            fsprs = chsprs(avars[hfb[1]][15], avars[hfb[1]][14])
                    elif scr == 2:
                        if (32 < mp[1] < 128) and (8 < mp[0] < 150) and ((fsc * 6) + ((mp[1] - 32) // 16)) < len(pfl):
                            pygame.mixer.stop()
                            sound[3].play()
                            scr = 3
                            for b in avars[avars[3][5]][32]:
                                if b[0] == "PARK" and b == pfl[(fsc * 6) + ((mp[1] - 32) // 16)]:
                                    c = avars[avars[3][5]][32]
                                    frn = c.index(b)
                                    marrag = (((avars[avars[3][5]][32][frn][7][0] + (avars[avars[3][5]][2] - avars[avars[3][5]][32][frn][7][1])) > 691199) and (avars[avars[3][5]][2] > 691199) \
                                              and ((format(avars[avars[3][5]][32][frn][3], '032b')[16:28]) != (format(avars[avars[3][5]][14], '032b')[16:28])))
                                    if avars[avars[3][5]][3] > 1:
                                        if frn < (1 + (len(avars[avars[3][5]][26]) > 0)):
                                            marrag = False
                                    e = [3600, 176400, 435600, 1382400][(b[2] > 16) + (b[2] > 48) + (b[2] > 132)]
                                    if (avars[avars[3][5]][2] - b[7][1] + b[7][0]) > e and b[2] < 379:
                                        if b[2] < 17:
                                            a = 2
                                        elif b[2] < 49:
                                            a = 3
                                        elif b[2] < 133:
                                            a = 4
                                        else:
                                            a = 6
                                        g = b[3]
                                        if g < 0:
                                            g = 4294967296 + g
                                        gn = g % 4 > 1
                                        g = format(g, '032b')
                                        l = [avars[avars[3][5]][5], avars[avars[3][5]][6], avars[avars[3][5]][7],
                                             avars[avars[3][5]][8], avars[avars[3][5]][9], avars[avars[3][5]][10]]
                                        shuffle(l)
                                        ov = [[0, a, 0, gn, 0, l[0], l[1], l[2], l[3], l[4], l[5], b[6], b[5], b[4], b[3], b[2], 0, 0, 22, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 4], [], [], [0, 0, 0, 0, 0, 0]]
                                        ov = growth.grw(ov)
                                        avars[avars[3][5]][32][frn][2] = ov[0][15]
                                        avars[avars[3][5]][32][frn][5] = ov[0][12]
                                        avars[avars[3][5]][32][frn][4] = ov[0][13]
                            fsprs = chsprs(pfl[(fsc * 6) + ((mp[1] - 32) // 16)][2], avars[avars[3][5]][32][frn][3])
                    elif scr == 3:
                        if (32 < mp[1] < 128) and (8 < mp[0] < 96):
                            if 32 < mp[1] < 48:
                                if not online:
                                    a =  randint(0, 2)
                                    if a == 2 and avars[3][2] < 100:
                                        a -= randint(1, 2)
                                    b = randint(0, 1)
                                    if a == 0:
                                        avars = eatcon.game(avars, asprs, screen, fsprs, b)
                                    elif a == 1:
                                        avars = popballoon.game(avars, asprs, screen, fsprs, b)
                                    elif a == 2:
                                        avars = moneyg.game(avars, asprs, screen, fsprs, b)
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                    if avars[avars[3][5]][32][frn][0] == avars[3][0]:
                                        upfrd()
                                    return(avars)
                                else:
                                    scr += 1
                                    pygame.mixer.stop()
                                    sound[3].play()
                            if 47 < mp[1] < 64:
                                if not online:
                                    bx = False
                                    comt = 1
                                    vst = randint(0, 1)
                                    anifr = 83
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                    if avars[avars[3][5]][32][frn][0] == avars[3][0]:
                                        upfrd()
                                else:
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    comt = 1
                                    vst = randint(0, 1)
                                    code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                      avars[avars[3][5]][2], 1, vst])
                            if 63 < mp[1] < 80:
                                if not online:
                                    bx = False
                                    comt = 2
                                    if avars[avars[3][5]][32][frn][8] < 14:
                                        pst = choice([0, 0, 1])
                                    elif avars[avars[3][5]][32][frn][8] < 41:
                                        pst = choice([0, 1, 1])
                                    elif avars[avars[3][5]][32][frn][8] < 68:
                                        pst = choice([1, 1, 2])
                                    else:
                                        pst = choice([2, 2, 1])
                                    prs = choice(prl[pst])
                                    anifr = 83
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                    if avars[avars[3][5]][32][frn][0] == avars[3][0]:
                                        upfrd()
                                else:
                                    scr = 11
                                    comt = 2
                                    pygame.mixer.stop()
                                    sound[3].play()
                            if 79 < mp[1] < 96:
                                if not online:
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                    if avars[avars[3][5]][32][frn][0] == avars[3][0]:
                                        upfrd()
                                    addmail()
                                    avars = mailico.mailbox(avars, asprs, screen, 0)
                                    return(avars)
                                else:
                                    scr = 13
                                    comt = 5
                                    pygame.mixer.stop()
                                    sound[3].play()
                            if 95 < mp[1] < 112:
                                if not online:
                                    a = randint(1, 5)
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                    if avars[avars[3][5]][32][frn][0] == avars[3][0]:
                                        upfrd()
                                    avars = park.prk(avars, asprs, screen, 1, avars[avars[3][5]][32][frn][2], a, avars[avars[3][5]][32][frn])
                                    return(avars)
                                else:
                                    pygame.mixer.stop()
                                    sound[3].play()
                                    prkty = randint(1, 5)
                                    comt = 4
                                    code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                      avars[avars[3][5]][2], 2, prkty])
                            if 111 < mp[1] < 128:
                                if marrag and (avars[avars[3][5]][32][frn][8] == 80):
                                    if not online:
                                        bx = False
                                        comt = 6
                                        anifr = 83
                                    else:
                                        pygame.mixer.stop()
                                        sound[3].play()
                                        comt = 6
                                        code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                          avars[avars[3][5]][2], 5, 0, [avars[avars[3][5]][12], avars[avars[3][5]][13]]])
                                else:
                                    scr -= 1
                            scr += 1
                    elif scr == 4:
                        try:
                            fcode = pyperclip.paste()
                            if fcode == code:
                                raise Exception("Same code!")
                            if len(fcode) == 36 and len(fcode) == len(code):
                                un, cn, ct, iv, f1, f2, fg, lt = decode(fcode, [])
                                if un == avars[3][0]:
                                    raise Exception("It's yours!")
                                for a in avars[avars[3][5]][32]:
                                    if a[0] == un and a[1] == cn:
                                        raise Exception("Same friend!")
                                c = [un, cn, ct, iv, f1, f2, fg, lt, 0]
                                f = avars[avars[3][5]][32]
                                f.append(c)
                                avars[avars[3][5]][32] = f
                                comt = 0
                                anifr = 83
                                fsprs = chsprs(ct, iv)
                                conmd = 0
                                online = True
                            else:
                                ct, lt, cnt, st, ed = decode(fcode, avars[avars[3][5]][32][frn])
                                avars[avars[3][5]][32][frn][2] = ct
                                avars[avars[3][5]][32][frn][7] = lt
                                fsprs = chsprs(ct, avars[avars[3][5]][32][frn][3])
                                if comt == 3:
                                    if cnt != 0 or st != playg or len(fcode) != 14:
                                        raise Exception("Wrong code!")
                                    b = power > ed
                                    if playg == 0:
                                        avars = eatcon.game(avars, asprs, screen, fsprs, b)
                                    elif playg == 1:
                                        avars = popballoon.game(avars, asprs, screen, fsprs, b)
                                    elif playg == 2:
                                        avars = moneyg.game(avars, asprs, screen, fsprs, b)
                                    elif playg == 3:
                                        avars = conball.game(avars, asprs, screen, fsprs, b)
                                    elif playg == 4:
                                        avars = conrope.game(avars, asprs, screen, fsprs, b)
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                    return(avars)
                                elif comt == 1:
                                    if cnt != 1 or len(fcode) != 12:
                                        raise Exception("Wrong code!")
                                    vst = (vst + st) % 2
                                    anifr = 83
                                    conmd = 0
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                elif comt == 4:
                                    if cnt != 2 or len(fcode) != 12:
                                        raise Exception("Wrong code!")
                                    prkty = ((prkty + st) % 5) + 1
                                    avars = park.prk(avars, asprs, screen, 1, avars[avars[3][5]][32][frn][2], prkty, avars[avars[3][5]][32][frn])
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                    return(avars)
                                elif comt == 2:
                                    if cnt != 3 or (conmd == 1 and (len(fcode) != 12 or st > 0)) or (conmd == 0 and (len(fcode) < 14 or st == 0)):
                                        raise Exception("Wrong code!")
                                    anifr = 83
                                    if conmd == 0:
                                        if st < 4:
                                            pst = st - 1
                                            prs = prl[pst][ed]
                                        else:
                                            prsot = len(ed) == 9
                                            if not prsot:
                                                try:
                                                    ss = pygame.image.load("Sprites/Food/" + ed[0] + ".png").convert()
                                                except:
                                                    ss = pygame.image.load("CFood/" + ed[0] + ".png").convert()
                                                s = pygame.Surface([24, 24]).convert()
                                                s.fill((0, 255, 255))
                                                s.blit(ss, [0, 0])
                                                s.set_colorkey((0, 255, 255))
                                            else:
                                                s = pygame.image.load("Sprites/Misc/item/" + ed[0] + ".png").convert()
                                            prsl[1][3] = s
                                            pst = 1
                                            prs = "ball"
                                            ballit = ed
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                elif comt == 5:
                                    if cnt != 4 or (conmd == 1 and (len(fcode) != 12 or st > 0)) or (conmd == 0 and (len(fcode) < 14 or st == 0)):
                                        raise Exception("Wrong code!")
                                    if conmd == 0:
                                        fltr = pygame.Surface([240, 160]).convert()
                                        fltr.fill((0, 255, 255))
                                        fltr.blit(ltrbase, [0, 0])
                                        fltr.blit(lfnt.render(("DEAR " + avars[avars[3][5]][22] + ","), 1, (0, 0, 100)), [8, 31])
                                        fltr.blit(lfnt.render(ed[0][0], 1, (0, 0, 100)), [8, 39])
                                        fltr.blit(lfnt.render(ed[0][1], 1, (0, 0, 100)), [8, 47])
                                        fltr.blit(lfnt.render(ed[0][2], 1, (0, 0, 100)), [8, 55])
                                        fltr.blit(lfnt.render(ed[0][3], 1, (0, 0, 100)), [8, 63])
                                        fltr.blit(lfnt.render(ed[0][4], 1, (0, 0, 100)), [8, 71])
                                        fltr.blit(lfnt.render(ed[0][5], 1, (0, 0, 100)), [8, 79])
                                        fltr.blit(fnt.render(avars[avars[3][5]][32][frn][1], 1, (0, 0, 100)), [16, 114])
                                        fltr.blit(fsprs[ed[1]], [(((32 - fsprs[3].get_width()) // 2) + 200), (96 + (32 - fsprs[3].get_height()))])
                                        fltr.blit(lfnt.render("GOODBYE!", 1, (0, 0, 100)), [8, 95])
                                        a = str(len([n for n in os.listdir("Sprites/Misc/mail/tm" + str(avars[3][5] + 1))]))
                                        pygame.image.save(fltr, "Sprites/Misc/mail/tm" + str(avars[3][5] + 1) + "/frnd_ltr_" + a + ".png")
                                        avars = mailico.mailbox(avars, asprs, screen, 0)
                                    if avars[avars[3][5]][32][frn][8] < 80:
                                        avars[avars[3][5]][32][frn][8] += 1
                                    return(avars)
                                elif comt == 6:
                                    if cnt != 5 or len(fcode) != 14:
                                        raise Exception("Wrong code!")
                                    avars[avars[3][5]][32][frn][4] = ed[0]
                                    avars[avars[3][5]][32][frn][5] = ed[1]
                                    anifr = 83
                                    conmd = 0
                            bx = False
                            bgi = pygame.image.load("Sprites/Misc/bg/onlmtrm.png").convert()
                        except:
                            pygame.mixer.stop()
                            sound[12].play()
                    elif scr == 5 and bx:
                        if (32 < mp[1] < 112) and (8 < mp[0] < 96) and ((((mp[1] - 32) // 16) != 2) or ((((mp[1] - 32) // 16) == 2) and avars[3][2] > 99)):
                            pygame.mixer.stop()
                            sound[3].play()
                            playg = (mp[1] - 32) // 16
                            comt = 3
                            if playg > 2:
                                scr = 15
                                anifr = 0
                                power = 0
                                cclk = True
                            else:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 4
                                power = randint(0, 255)
                                code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                  avars[avars[3][5]][2], 0, playg, power])
                    elif scr == 8:
                        if (32 < mp[1] < 80) and (8 < mp[0] < 232):
                            if (mp[1] - 32) // 16 == 0 and len(ofl) > 0:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 9
                                fsc = 0
                            elif (mp[1] - 32) // 16 == 1:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 4
                                if avars[avars[3][5]][0] < 9:
                                    code = encode(0, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                      avars[avars[3][5]][13], avars[avars[3][5]][12], avars[avars[3][5]][11], avars[avars[3][5]][2]])
                                else:
                                    code = encode(0, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                      avars[avars[3][5]][13], avars[avars[3][5]][12], avars[avars[3][5]][0], avars[avars[3][5]][2]])
                            elif (mp[1] - 32) // 16 == 2:
                                pygame.mixer.stop()
                                sound[9].play()
                                f = open(("ConCode/" + avars[3][0] + "_" + avars[avars[3][5]][22] + ".txt"), "w+")
                                if avars[avars[3][5]][0] < 9:
                                    code = encode(0, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                      avars[avars[3][5]][13], avars[avars[3][5]][12], avars[avars[3][5]][11], avars[avars[3][5]][2]])
                                else:
                                    code = encode(0, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                      avars[avars[3][5]][13], avars[avars[3][5]][12], avars[avars[3][5]][0], avars[avars[3][5]][2]])
                                f.write("Add code: " + code + "\n")
                                f.write("\n")
                                f.write("Games:\n")
                                for i in range(5):
                                    code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                      avars[avars[3][5]][2], 0, i, 128])
                                    f.write(["Eating", "Balloon", "Bet", "Ball", "Rope"][i] + ": " + code + "\n")
                                f.write("\n")
                                code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                  avars[avars[3][5]][2], 1, 0])
                                f.write("Visit: " + code + "\n")
                                f.write("\n")
                                code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                  avars[avars[3][5]][2], 3, 0])
                                f.write("Receive present: " + code + "\n")
                                f.write("\n")
                                code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                  avars[avars[3][5]][2], 2, 3])
                                f.write("Park: " + code + "\n")
                                if avars[avars[3][5]][2] > 691199:
                                    code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                      avars[avars[3][5]][2], 5, 0, [avars[avars[3][5]][12], avars[avars[3][5]][13]]])
                                    f.write("\n")
                                    f.write("Marry: " + code)
                                f.close()
                    elif scr == 9:
                        if (32 < mp[1] < 128) and (8 < mp[0] < 150) and ((fsc * 6) + ((mp[1] - 32) // 16)) < len(ofl):
                            pygame.mixer.stop()
                            sound[3].play()
                            scr = 3
                            frn = ofln[(fsc * 6) + ((mp[1] - 32) // 16)]
                            online = True
                            marrag = ((avars[avars[3][5]][32][frn][7] > 691199) and (avars[avars[3][5]][2] > 691199) \
                                      and ((format(avars[avars[3][5]][32][frn][3], '032b')[16:28]) != (format(avars[avars[3][5]][14], '032b')[16:28])))
                    elif scr == 10:
                        if (32 < mp[1] < 80) and (8 < mp[0] < 84):
                            kpres = (mp[1] - 32) // 16
                            if kpres == 2:
                                pygame.mixer.stop()
                                sound[3].play()
                                if avars[avars[3][5]][32][frn][8] < 14:
                                    pst = choice([0, 0, 1])
                                elif avars[avars[3][5]][32][frn][8] < 41:
                                    pst = choice([0, 1, 1])
                                elif avars[avars[3][5]][32][frn][8] < 68:
                                    pst = choice([1, 1, 2])
                                else:
                                    pst = choice([2, 2, 1])
                                prs = choice(prl[pst])
                                scr = 4
                                code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                  avars[avars[3][5]][2], 3, (pst + 1), prl[pst].index(prs)])
                            elif (kpres == 0 and len(avars[3][4]) > 0) or (kpres == 1 and len(avars[3][9]) > 0):
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 11
                                osprs = otspr(kpres)
                                oscr = 0
                                objsmax = ((len(osprs) - 1) // 24)
                    elif scr == 11:
                        if 44 < mp[1] < 116 and 14 < mp[0] < 230 and (mp[0] - (14 + (27 * ((mp[0] - 14) // 27)))) < 24:
                            o = ((mp[0] - 14) // 27) + (8 * ((mp[1] - 44) // 24)) + (oscr * 24)
                            if o < len(osprs):
                                pygame.mixer.stop()
                                sound[3].play()
                                olst = []
                                for i in range([11, 9][kpres]):
                                    if i != [4, 1][kpres]:
                                        olst.append(avars[3][(4 + (5 * kpres))][(o)][i])
                                    else:
                                        olst.append(1)
                                avars[3][(4 + (5 * kpres))][(o)][[4, 1][kpres]] -= 1
                                if avars[3][(4 + (5 * kpres))][(o)][[4, 1][kpres]] == 0:
                                    f = avars[3][(4 + (5 * kpres))]
                                    f.pop(o)
                                    avars[3][(4 + (5 * kpres))] = f
                                if not kpres:
                                    try:
                                        ss = pygame.image.load("Sprites/Food/" + olst[0] + ".png").convert()
                                    except:
                                        ss = pygame.image.load("CFood/" + olst[0] + ".png").convert()
                                    s = pygame.Surface([24, 24]).convert()
                                    s.fill((0, 255, 255))
                                    s.blit(ss, [0, 0])
                                    s.set_colorkey((0, 255, 255))
                                else:
                                    s = pygame.image.load("Sprites/Misc/item/" + olst[0] + ".png").convert()
                                prsl[1][3] = s
                                pst = 1
                                prs = "ball"
                                ballit = olst
                                scr = 4
                                code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                  avars[avars[3][5]][2], 3, 4, olst])
                    elif scr == 12:
                        if (32 < mp[1] < 64) and (8 < mp[0] < 92):
                            pygame.mixer.stop()
                            sound[3].play()
                            kpres = (mp[1] - 32) // 16
                            if kpres == 0:
                                scr = 10
                                conmd = 1
                            else:
                                scr = 4
                                conmd = 0
                                code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                  avars[avars[3][5]][2], 3, 0])
                    elif scr == 14:
                        if (32 < mp[1] < 80) and (8 < mp[0] < 92):
                            kpres = (mp[1] - 32) // 16
                            if kpres == 0:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 13
                                conmd = 1
                                shspr = 3
                                ltrtxt = ["", "", "", "", "", ""]
                                wrtln = 0
                            elif kpres == 1:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 4
                                conmd = 0
                                code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                                  avars[avars[3][5]][2], 4, 0])
                            elif len(inbox) > 0:
                                fltr = inbox[0]
                                a = str(len([n for n in os.listdir("Sprites/Misc/mail/tm" + str(avars[3][5] + 1))]))
                                pygame.image.save(fltr, "Sprites/Misc/mail/tm" + str(avars[3][5] + 1) + "/frnd_ltr_" + a + ".png")
                                avars = mailico.mailbox(avars, asprs, 0)
                                return(avars)
                    elif scr == 15 and (24 < mp[1] < 136):
                        pygame.mixer.stop()
                        sound[3].play()
                        power+= 1
                elif pb == 3 and bx:
                    if scr == 4:
                        pyperclip.copy(code)
            if event.type == pygame.KEYDOWN:
                if scr == 13:
                    if (pygame.K_a <= event.key <= pygame.K_z) and len(ltrtxt[wrtln]) < 36:
                        ltr = chr(event.key)
                        ltrtxt[wrtln] = (ltrtxt[wrtln] + str(ltr)).upper()
                    if event.key == pygame.K_SPACE and len(ltrtxt[wrtln]) < 36:
                        ltrtxt[wrtln] = ltrtxt[wrtln] + " "
                    if event.key == pygame.K_BACKSPACE:
                        if len(ltrtxt[wrtln]) > 0:
                            ltrtxt[wrtln] = ltrtxt[wrtln][:len(ltrtxt[wrtln]) - 1]
                        elif wrtln > 0:
                            wrtln -= 1
                    if event.key == pygame.K_RETURN:
                        if wrtln < 5:
                            wrtln += 1
                        else:
                            pygame.mixer.stop()
                            sound[3].play()
                            scr = 4
                            conmd = 1
                            code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                              avars[avars[3][5]][2], 4, 1, ltrtxt, shspr])
                clt = 0
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
                if bx and scr not in [4, 15, 13]:
                    clt += 1
        if chngsts:
            avars = statusup.chngsts(avars)
            chngsts = False
        if anifr < 143:
            anifr += 1
            if scr == 7 and comt == 2:
                if anifr == 108 and prs in ["poo", "flower", "cake", "cream", "ball", "rope", "letter", "fb", "chht"]:
                    return(avars)
        else:
            anifr = 0
            cclk = True
            if scr == 4 and not bx:
                scr = 5
                anifr = 84 - (12 * (comt == 6))
            elif scr == 5 and comt in [0, 1, 2] and not bx:
                scr = 6
                anifr = 84
            elif scr == 5 and comt == 6 and not bx:
                avars = marryseq.wed(avars, asprs, fsprs, avars[avars[3][5]][32][frn], screen)
                return(avars)
            elif scr == 6 and not comt in [2]:
                return(avars)
            elif scr == 6 and comt in [2]:
                scr = 7
                if comt == 2:
                    g = True
                    if online:
                        if conmd == 1:
                            g = False
                            if (avars[avars[3][5]][15] == 154) and (avars[avars[3][5]][19] > 3) and (pst == 0):
                                avars[avars[3][5]][1] = 5
                                avars = growth.grw(avars)
                            if (avars[avars[3][5]][15] == 166) and (avars[avars[3][5]][7] > 500) and (pst == 2):
                                avars[avars[3][5]][1] = 5
                                avars = growth.grw(avars)
                    if g:
                        if pst == 0:
                            if avars[avars[3][5]][17] > 0:
                                avars[avars[3][5]][17] -= 1
                        elif pst == 1:
                            if avars[avars[3][5]][17] < 6:
                                avars[avars[3][5]][17] += 1
                            if prs == "ball":
                                h = False
                                a = 0
                                for f in avars[3][(4 + (5 * prsot))]:
                                    if f[0] == ballit[0]:
                                        if f[[4, 1][prsot]] < 255:
                                            h = True
                                            break
                                    a += 1
                                if h:
                                    avars[3][(4 + (5 * prsot))][a][[4, 1][prsot]] += 1
                                else:
                                    a = avars[3][(4 + (5 * prsot))]
                                    a.append(ballit)
                                    avars[3][(4 + (5 * prsot))] = a
                            elif prs == "rope":
                                h = False
                                a = 0
                                for f in avars[3][9]:
                                    if f[0] == 'rope':
                                        if f[1] < 255:
                                            h = True
                                            break
                                    a += 1
                                if h:
                                    avars[3][9][a][1] += 1
                                else:
                                    a = avars[3][9]
                                    a.append(ropeit)
                                    avars[3][9] = a
                        else:
                            if avars[avars[3][5]][17] < 3:
                                avars[avars[3][5]][17] += 4
                            else:
                                avars[avars[3][5]][17] = 6
            elif scr == 7:
                return(avars)
            elif scr == 15:
                pygame.mixer.stop()
                sound[3].play()
                scr = 4
                code = encode(1, [avars[3][0], avars[avars[3][5]][22], avars[avars[3][5]][15], avars[avars[3][5]][14],
                                  avars[avars[3][5]][2], 0, playg, power])
        if clt > 29:
            return(avars)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

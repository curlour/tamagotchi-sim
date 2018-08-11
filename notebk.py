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
import palette
import mainscreen

def book(avars, asprs, screen):

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

    bopt = 0

    chngsts = False

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

    def cdspr(md, chd, sel):
        if md < 2:
            g = chd[sel][3]
        if md == 0:
            try:
                bs = pygame.image.load("Sprites/Characters/chara_" + str(chd[sel][4]) + "b.png")
                ss = pygame.image.load("Sprites/Characters/chara_" + str(chd[sel][4]) + "s.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, g, opal)
                ss = palette.palch(ss, g, opal)
            except:
                bs = pygame.image.load("Sprites/NPC/Nazotchi.png")
                ss = pygame.image.load("Sprites/NPC/Nazo.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, g, opal)
                ss = palette.palch(ss, g, opal)
            s = (bs.get_width() // 4)
            gspr = pygame.Surface([s, s]).convert()
            gspr.fill((0, 255, 255))
            gspr.blit(bs, [0, 0])
            gspr.set_colorkey((0, 255, 255))
            gspr.convert()
            gico = pygame.Surface([16, 16])
            gico.fill((0, 255, 255))
            gico.blit(ss, [0, 0])
            gico.set_colorkey((0, 255, 255))
            gico.convert()
            pstages = []
            for n in chd[sel][6]:
                try:
                    ss = pygame.image.load("Sprites/Characters/chara_" + str(n) + "s.png")
                    opal = []
                    for i in range(32):
                        opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                    ss = palette.palch(ss, g, opal)
                except:
                    ss = pygame.image.load("Sprites/NPC/Nazo.png")
                    opal = []
                    for i in range(32):
                        opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                    ss = palette.palch(ss, g, opal)
                st = pygame.Surface([16, 16])
                st.fill((0, 255, 255))
                st.blit(ss, [0, 0])
                st.set_colorkey((0, 255, 255))
                st.convert()
                pstages.append(st)
            return(gspr, gico, pstages)
        elif md == 1:
            try:
                bs = pygame.image.load("Sprites/Characters/chara_" + str(chd[sel][2]) + "b.png")
                ss = pygame.image.load("Sprites/Characters/chara_" + str(chd[sel][2]) + "s.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, g, opal)
                ss = palette.palch(ss, g, opal)
            except:
                bs = pygame.image.load("Sprites/NPC/Nazotchi.png")
                ss = pygame.image.load("Sprites/NPC/Nazo.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, g, opal)
                ss = palette.palch(ss, g, opal)
            s = (bs.get_width() // 4)
            fspr = pygame.Surface([s, s]).convert()
            fspr.fill((0, 255, 255))
            if avars[avars[3][5]][32][frsel][8] < 14:
                fspr.blit(bs, [-(s * 3), 0])
            elif avars[avars[3][5]][32][frsel][8] < 41:
                fspr.blit(bs, [0, 0])
            elif avars[avars[3][5]][32][frsel][8] < 68:
                fspr.blit(bs, [-(s * 2), 0])
            else:
                fspr.blit(bs, [-(s * 3), -(s * 1)])
            fspr.set_colorkey((0, 255, 255))
            fspr.convert()
            fbar = pygame.Surface([(160 - (2 * chd[sel][8])), 16]).convert()
            fbar.fill((102, 102, 102))
            fun = fnt.render(chd[sel][0], 1, (0, 0, 100))
            fcn = fnt.render(chd[sel][1], 1, (0, 0, 100))
            return(fspr, fbar, fun, fcn)
        elif md == 2:
            try:
                bs = pygame.image.load("Sprites/Characters/chara_" + str(chd[1]) + "b.png")
                ss = pygame.image.load("Sprites/Characters/chara_" + str(chd[1]) + "s.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, chd[0], opal)
                ss = palette.palch(ss, chd[0], opal)
            except:
                bs = pygame.image.load("Sprites/NPC/Nazotchi.png")
                ss = pygame.image.load("Sprites/NPC/Nazo.png")
                opal = []
                for i in range(32):
                    opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                bs = palette.palch(bs, chd[0], opal)
                ss = palette.palch(ss, chd[0], opal)
            psp = pygame.Surface([32, 32]).convert()
            psp.fill((0, 255, 255))
            psp.blit(bs, [-96, -32])
            psp.set_colorkey((0, 255, 255))
            psp.convert()
            psp = pygame.transform.flip(psp, 1, 0)
            pst = []
            for n in (chd[3] + [chd[1]]):
                try:
                    ss = pygame.image.load("Sprites/Characters/chara_" + str(n) + "s.png")
                    opal = []
                    for i in range(32):
                        opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                    ss = palette.palch(ss, chd[0], opal)
                except:
                    ss = pygame.image.load("Sprites/NPC/Nazo.png")
                    opal = []
                    for i in range(32):
                        opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                    ss = palette.palch(ss, chd[0], opal)
                st = pygame.Surface([16, 16])
                st.fill((0, 255, 255))
                st.blit(ss, [-16, 0])
                st.set_colorkey((0, 255, 255))
                st.convert()
                pst.append(st)
            if len(sel) > 0:
                try:
                    bs = pygame.image.load("Sprites/Characters/chara_" + str(sel[1]) + "b.png")
                    ss = pygame.image.load("Sprites/Characters/chara_" + str(sel[1]) + "s.png")
                    opal = []
                    for i in range(32):
                        opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                    bs = palette.palch(bs, sel[0], opal)
                    ss = palette.palch(ss, sel[0], opal)
                except:
                    bs = pygame.image.load("Sprites/NPC/Nazotchi.png")
                    ss = pygame.image.load("Sprites/NPC/Nazo.png")
                    opal = []
                    for i in range(32):
                        opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                    bs = palette.palch(bs, sel[0], opal)
                    ss = palette.palch(ss, sel[0], opal)
                pss = pygame.Surface([32, 32]).convert()
                pss.fill((0, 255, 255))
                pss.blit(bs, [-96, -32])
                pss.set_colorkey((0, 255, 255))
                pss.convert()
            else:
                pss = None
            pn = fnt.render(chd[2], 1, (0, 0, 100))
            return(psp, pss, pn, pst)
        elif md == 3:
            spls = []
            if len(chd[(sel * 6):]) > 5:
                a = 6
            else:
                a = len(chd[(sel * 6):])
            for j in range(a):
                l = []
                for n in (chd[j + (sel * 6)][2] + [chd[j + (sel * 6)][1]]):
                    try:
                        ss = pygame.image.load("Sprites/Characters/chara_" + str(n) + "s.png")
                        opal = []
                        for i in range(32):
                            opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                        ss = palette.palch(ss, chd[j + (sel * 6)][0], opal)
                    except:
                        ss = pygame.image.load("Sprites/NPC/Nazo.png")
                        opal = []
                        for i in range(32):
                            opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
                        ss = palette.palch(ss, chd[j + (sel * 6)][0], opal)
                    st = pygame.Surface([16, 16])
                    st.fill((0, 255, 255))
                    st.blit(ss, [-16, 0])
                    st.set_colorkey((0, 255, 255))
                    st.convert()
                    l.append(st)
                spls.append(l)
            return(spls)
        elif md == 4:
            spls = []
            #print(chd)
            for i in range((sel * 24), ((sel + 1) * 24)):
                st = pygame.Surface([16, 16])
                st.fill((0, 255, 255))
                if format(chd, '0384b')[i] == '1':
                    ss = pygame.image.load("Sprites/Characters/chara_" + str(i + 1) + "s.png")
                    st.blit(ss, [-16, 0])
                else:
                    st.blit((lfnt.render("?", 1, (0, 0, 100))), [6, 5])
                st.set_colorkey((0, 255, 255))
                st.convert()
                spls.append(st)
            return(spls)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 8, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    male = pygame.image.load("Sprites/Misc/menu/male.png").convert()
    female = pygame.image.load("Sprites/Misc/menu/female.png").convert()

    mame = pygame.image.load("Sprites/Misc/menu/mas.png").convert()
    meme = pygame.image.load("Sprites/Misc/menu/mes.png").convert()
    kuchi = pygame.image.load("Sprites/Misc/menu/kus.png").convert()
    nofs = pygame.image.load("Sprites/Misc/menu/nos.png").convert()
    symlst = [nofs, mame, meme, kuchi]

    frnds = pygame.image.load("Sprites/Misc/bg/frndscr.png").convert()

    grave = pygame.image.load("Sprites/Misc/menu/grave.png").convert()

    ghost = pygame.image.load("Sprites/Misc/sick/ghost.png").convert()

    heart = pygame.image.load("Sprites/Misc/emo/heart.png").convert()

    arrow = pygame.image.load("Sprites/Misc/txtbox/arrow1.png").convert()

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

    clock = pygame.time.Clock()

    anifr = 0

    sound = sounds.imprtsnd(avars)

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
        screen.blit(textbox, [0, 24])
        if bopt == 0:
            if len(avars[avars[3][5]][32]) > 0:
                screen.blit((fnt.render("FRIENDS", 1, (0, 0, 100))), [8, 34])
            else:
                screen.blit((fnt.render("FRIENDS", 1, (102, 102, 255))), [8, 34])
            if avars[avars[3][5]][3] > 1:
                screen.blit((fnt.render("FAMILY", 1, (0, 0, 100))), [8, 50])
            else:
                screen.blit((fnt.render("FAMILY", 1, (102, 102, 255))), [8, 50])
            if len(avars[3][10]) > 0:
                screen.blit((fnt.render("GRAVEYARD", 1, (0, 0, 100))), [8, 66])
            else:
                screen.blit((fnt.render("GRAVEYARD", 1, (102, 102, 255))), [8, 66])
            screen.blit((fnt.render("TAMADEX", 1, (0, 0, 100))), [8, 82])
        elif bopt == 1:
            screen.blit(scrli, [232, 128])
            if avars[3][10][grvsel][4] < 385:
                screen.blit((fnt.render(chnamelst[(avars[3][10][grvsel][4] - 1)], 1, (0, 0, 100))), [8, 34])
            else:
                try:
                    screen.blit((fnt.render(extrchn[str(avars[3][10][grvsel][4])], 1, (0, 0, 100))), [8, 34])
                except:
                    screen.blit((fnt.render("???", 1, (0, 0, 100))), [8, 34])
            if avars[3][10][grvsel][3] % 2 == 0:
                screen.blit(male, [216, 32])
            else:
                screen.blit(female, [216, 32])
            screen.blit((fnt.render(avars[3][10][grvsel][5], 1, (0, 0, 100))), [128, 54])
            screen.blit((fnt.render((str(avars[3][10][grvsel][2]) + "G"), 1, (0, 0, 100))), [184, 72])
            screen.blit((fnt.render((str(avars[3][10][grvsel][1] // 86400) + "  YEARS"), 1, (0, 0, 100))), [120, 90])
            screen.blit(ghost, [12, 68])
            screen.blit(grave, [47, 52])
            screen.blit(gspr, [(57 + ((32 - gspr.get_width()) // 2)), (64 + ((32 - gspr.get_width()) // 2))])
            screen.blit(gico, [(24 + (32 * len(pstages))), 108])
            z = 0
            while z < len(pstages):
                screen.blit(pstages[z], [(24 + (32 * z)), 108])
                screen.blit(arrow, [(44 + (32 * z)), 112])
                z += 1
        elif bopt == 2:
            screen.blit(scrli, [232, 128])
            screen.blit(frnds, [8, 32])
            screen.blit(fspr, [(16 + ((32 - fspr.get_width()) // 2)), (40 + ((32 - fspr.get_width()) // 2))])
            if avars[avars[3][5]][32][frsel][3] % 2 == 0:
                screen.blit(male, [16, 78])
            else:
                screen.blit(female, [16, 78])
            screen.blit(fbar, [(200 - (160 - (2 * avars[avars[3][5]][32][frsel][8]))), 94])
            screen.blit(fun, [54, 38])
            if avars[avars[3][5]][32][frsel][2] < 385:
                screen.blit((fnt.render(chnamelst[(avars[avars[3][5]][32][frsel][2] - 1)], 1, (0, 0, 100))), [54, 54])
            else:
                try:
                    screen.blit((fnt.render(extrchn[str(avars[avars[3][5]][32][frsel][2])], 1, (0, 0, 100))), [54, 54])
                except:
                    screen.blit((fnt.render("???", 1, (0, 0, 100))), [54, 54])
            screen.blit(fcn, [54, 70])
        elif bopt == 3:
            screen.blit((fnt.render("PARENTS", 1, (0, 0, 100))), [8, 34])
            if avars[avars[3][5]][3] > 2:
                screen.blit((fnt.render("GRANDPARENTS", 1, (0, 0, 100))), [8, 50])
            else:
                screen.blit((fnt.render("GRANDPARENTS", 1, (102, 102, 255))), [8, 50])
            screen.blit((fnt.render("FAMILY TREE", 1, (0, 0, 100))), [8, 66])
        elif bopt == 4 or bopt == 5:
            if avars[avars[3][5]][25 + (2 * (bopt == 5))][1] < 385:
                screen.blit((fnt.render(chnamelst[(avars[avars[3][5]][25 + (2 * (bopt == 5))][1] - 1)], 1, (0, 0, 100))), [8, 34])
            else:
                try:
                    screen.blit((fnt.render(extrchn[str(avars[avars[3][5]][25 + (2 * (bopt == 5))][1])], 1, (0, 0, 100))), [8, 34])
                except:
                    screen.blit((fnt.render("???", 1, (0, 0, 100))), [8, 34])
            screen.blit((fnt.render(avars[avars[3][5]][25 + (2 * (bopt == 5))][2], 1, (0, 0, 100))), [8, 50])
            if avars[avars[3][5]][25 + (2 * (bopt == 5))][0] % 2 == 0:
                screen.blit(male, [216, 40])
            else:
                screen.blit(female, [216, 40])
            screen.blit(symlst[['no', 'ma', 'me', 'ku'].index(avars[avars[3][5]][25 + (2 * (bopt == 5))][4])], [8, 72])
            screen.blit(symlst[['no', 'ma', 'me', 'ku'].index(avars[avars[3][5]][25 + (2 * (bopt == 5))][5])], [24, 88])
            screen.blit(psp, [80, 72])
            if len(avars[avars[3][5]][26 + (2 * (bopt == 5))]) > 0:
                screen.blit(heart, [112, 64])
                screen.blit(pss, [128, 72])
                screen.blit(symlst[['no', 'ma', 'me', 'ku'].index(avars[avars[3][5]][26 + (2 * (bopt == 5))][2])], [200, 72])
                screen.blit(symlst[['no', 'ma', 'me', 'ku'].index(avars[avars[3][5]][26 + (2 * (bopt == 5))][3])], [216, 88])
            for i in range(len(pst)):
                screen.blit(pst[i], [(24 + (32 * i)), 108])
                if i < (len(pst) - 1):
                    screen.blit(arrow, [(44 + (32 * i)), 112])
        elif bopt == 6:
            screen.blit(scrli, [232, 128])
            for j in range(len(spls)):
                for i in range(len(spls[j])):
                    screen.blit(spls[j][i], [(24 + (32 * i)), (32 + (16 * j))])
                    if i < (len(spls[j]) - 1):
                        screen.blit(arrow, [(44 + (32 * i)), (36 + (16 * j))])
        elif bopt == 7:
            screen.blit(scrli, [232, 128])
            for i in range(24):
                screen.blit((lfnt.render('%03d' % ((dexs * 24) + i + 1), 1, (0, 0, 100))), [(18 + (27 * (i % 8))), (60 + (24 * (i // 8)))])
                screen.blit(spls[i], [(18 + (27 * (i % 8))), (44 + (24 * (i // 8)))])
        elif bopt == 8:
            screen.blit(dchas[0], [8, 32])
            screen.blit((lfnt.render(('%03d' % cen) + " / " + ["BABY", "CHILD", "TEEN", "ADULT", "SENIOR"][(cen > 16) + (cen > 48) + (cen > 132) + (cen > 378)], 1, (0, 0, 100))), \
                        [48, 37])
            if cen < 385:
                screen.blit((fnt.render(chnamelst[cen - 1], 1, (0, 0, 100))), [48, 46])
            else:
                try:
                    screen.blit((fnt.render(extrchn[str(cen)], 1, (0, 0, 100))), [48, 46])
                except:
                    screen.blit((fnt.render("???", 1, (0, 0, 100))), [48, 46])
            for i in range(7):
                screen.blit(dchas[i + 1], [(8 + (32 * i)), 80])
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
                #if event.key == K_d and bopt == 2:
                    #f = avars[avars[3][5]][32]
                    #f.pop(frsel)
                    #avars[avars[3][5]][32] = f
                    #bopt = 0
            if event.type == KEYUP:
                if event.key in [303, 304]:
                    spclk = False
            if event.type == MOUSEBUTTONDOWN:
                mp = event.pos
                d = (screen.get_size()[0] // 240)
                mp = ((mp[0] // d), (mp[1] // d))
                pb = event.button  + (spclk * (1 + (event.button > 2)))
                if pb in [2, 4]:
                    clt = 0
                    if bopt == 1:
                        pygame.mixer.stop()
                        sound[2].play()
                        if grvsel != (len(avars[3][10]) - 1):
                            grvsel += 1
                        else:
                            grvsel = 0
                        gspr, gico, pstages = cdspr(0, avars[3][10], grvsel)
                    elif bopt == 2:
                        pygame.mixer.stop()
                        sound[2].play()
                        if frsel != (len(avars[avars[3][5]][32]) - 1):
                            frsel += 1
                        else:
                            frsel = 0
                        fspr, fbar, fun, fcn = cdspr(1, avars[avars[3][5]][32], frsel)
                    elif bopt == 6:
                        pygame.mixer.stop()
                        sound[2].play()
                        if gensel != ((len(avars[avars[3][5]][29]) - 1) // 6):
                            gensel += 1
                        else:
                            gensel = 0
                        spls = cdspr(3, avars[avars[3][5]][29], gensel)
                    elif bopt == 7:
                        pygame.mixer.stop()
                        sound[2].play()
                        if dexs != 15:
                            dexs += 1
                        else:
                            dexs = 0
                        spls = cdspr(4, avars[3][23], dexs)
                elif pb == 5:
                    clt = 0
                    if bopt == 1:
                        pygame.mixer.stop()
                        sound[2].play()
                        if grvsel != 0:
                            grvsel -= 1
                        else:
                            grvsel = (len(avars[3][10]) - 1)
                        gspr, gico, pstages = cdspr(0, avars[3][10], grvsel)
                    elif bopt == 2:
                        pygame.mixer.stop()
                        sound[2].play()
                        if frsel != 0:
                            frsel -= 1
                        else:
                            frsel = (len(avars[avars[3][5]][32]) - 1)
                        fspr, fbar, fun, fcn = cdspr(1, avars[avars[3][5]][32], frsel)
                    elif bopt == 6:
                        pygame.mixer.stop()
                        sound[2].play()
                        if gensel != 0:
                            gensel -= 1
                        else:
                            gensel = ((len(avars[avars[3][5]][29]) - 1) // 6)
                        spls = cdspr(3, avars[avars[3][5]][29], gensel)
                    elif bopt == 7:
                        pygame.mixer.stop()
                        sound[2].play()
                        if dexs != 0:
                            dexs -= 1
                        else:
                            dexs = 15
                        spls = cdspr(4, avars[3][23], dexs)
                elif pb == 1:
                    clt = 0
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            sound[4].play()
                            return(avars)
                    if bopt == 0 and 8 < mp[0] < 232:
                        if 64 < mp[1] < 80 and len(avars[3][10]) > 0:
                            pygame.mixer.stop()
                            sound[3].play()
                            bopt = 1
                            grvsel = 0
                            gspr, gico, pstages = cdspr(0, avars[3][10], 0)
                        if 32 < mp[1] < 48 and len(avars[avars[3][5]][32]) > 0:
                            pygame.mixer.stop()
                            sound[3].play()
                            bopt = 2
                            frsel = 0
                            fspr, fbar, fun, fcn = cdspr(1, avars[avars[3][5]][32], 0)
                        if 48 < mp[1] < 64 and avars[avars[3][5]][3] > 1:
                            pygame.mixer.stop()
                            sound[3].play()
                            bopt = 3
                        if 80 < mp[1] < 96:
                            pygame.mixer.stop()
                            sound[3].play()
                            bopt = 7
                            dexs = 0
                            spls = cdspr(4, avars[3][23], dexs)
                    elif bopt == 3 and 8 < mp[0] < 232:
                        if 32 < mp[1] < 48:
                            pygame.mixer.stop()
                            sound[3].play()
                            bopt = 4
                            psp, pss, pn, pst = cdspr(2, avars[avars[3][5]][25], avars[avars[3][5]][26])
                        if 48 < mp[1] < 64 and avars[avars[3][5]][3] > 2:
                            pygame.mixer.stop()
                            sound[3].play()
                            bopt = 5
                            psp, pss, pn, pst = cdspr(2, avars[avars[3][5]][27], avars[avars[3][5]][28])
                        if 64 < mp[1] < 80:
                            pygame.mixer.stop()
                            sound[3].play()
                            bopt = 6
                            gensel = 0
                            spls = cdspr(3, avars[avars[3][5]][29], 0)
                    elif bopt == 7 and (14 < mp[0] < 226) and (((mp[0] - 14) % 27) < 24) and (44 < mp[1] < 140):
                        cen = ((mp[0] - 14) // 27) + (((mp[1] - 44) // 24) * 8) + (dexs * 24) + 1
                        if format(avars[3][23], '0384b')[cen - 1] == '1':
                            pygame.mixer.stop()
                            sound[3].play()
                            bopt = 8
                            dchas = []
                            l = [int('00060000', 16), int('F0060000', 16), int('0F060000', 16), int('00F60000', 16), \
                                 int('0FF60000', 16), int('F0F60000', 16), int('FF060000', 16), int('FFF60000', 16)]
                            for i in range(8):
                                bs = pygame.image.load("Sprites/Characters/chara_" + str(cen) + "b.png")
                                ss = pygame.image.load("Sprites/Characters/chara_" + str(cen) + "s.png")
                                opal = []
                                for p in range(32):
                                    opal.append(ss.get_at(((16 + (8 * (p % 2))), (16 + (p // 2)))))
                                bs = palette.palch(bs, l[i], opal)
                                x = (bs.get_width() // 4)
                                j = pygame.Surface([x, x])
                                j.fill((0, 255, 255))
                                j.blit(bs, [0, 0])
                                k = pygame.Surface([32, 32])
                                k.fill((0, 255, 255))
                                k.blit(j, [((32 - x) // 2), ((32 - x) // 2)])
                                k.set_colorkey((0, 255, 255))
                                k.convert()
                                dchas.append(k)
                    elif bopt == 8 and (8 < mp[0] < 40) and (32 < mp[1] < 64):
                        pygame.mixer.stop()
                        sound[4].play()
                        bopt = 7
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
        if anifr < 23:
            anifr += 1
        else:
            anifr = 0
        if chngsts:
            avars = statusup.chngsts(avars)
            chngsts = False
        if clt > 29:
            return(avars)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()

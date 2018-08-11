import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import shelve
import borders
import sounds
import varsup
import statusup
import palette
import mainscreen

def status(avars, asprs, screen):

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

    shft = False

    clt = 0

    spclk = False

    stsopt = 0

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
    
    def icoanim():
        if ((anifr / 12) - (anifr // 12)) < 0.5:
            ico = 1
        else:
            ico = 2
        ix = (176+ (22 * avars[3][5])) + ((16 - asprs[avars[3][5]][ico].get_width()) // 2)
        iy = 4 + ((16 - asprs[avars[3][5]][ico].get_height()) // 2)
        return(ico, ix, iy)

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 0, 0)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()
    
    fhng = pygame.image.load("Sprites/Misc/menu/hngf.png").convert()
    ehng = pygame.image.load("Sprites/Misc/menu/hnge.png").convert()
    fhpy = pygame.image.load("Sprites/Misc/menu/hpyf.png").convert()
    ehpy = pygame.image.load("Sprites/Misc/menu/hpye.png").convert()
    inti = pygame.image.load("Sprites/Misc/menu/inti.png").convert()
    styi = pygame.image.load("Sprites/Misc/menu/styi.png").convert()
    kndi = pygame.image.load("Sprites/Misc/menu/kndi.png").convert()
    humi = pygame.image.load("Sprites/Misc/menu/humi.png").convert()
    gori = pygame.image.load("Sprites/Misc/menu/gori.png").convert()
    pasi = pygame.image.load("Sprites/Misc/menu/pasi.png").convert()

    male = pygame.image.load("Sprites/Misc/menu/male.png").convert()
    female = pygame.image.load("Sprites/Misc/menu/female.png").convert()
    grpf = pygame.image.load("Sprites/Misc/menu/" + avars[avars[3][5]][12] + "s.png").convert()
    grpm = pygame.image.load("Sprites/Misc/menu/" + avars[avars[3][5]][13] + "s.png").convert()
    if avars[avars[3][5]][11] in ["ma", "me", "ku", "no"]:
        grp = pygame.image.load("Sprites/Misc/menu/" + avars[avars[3][5]][11] + "b.png").convert()
    else:
        grp = pygame.image.load("Sprites/Misc/menu/spb.png").convert()
    weis = pygame.image.load("Sprites/Misc/menu/weight.png").convert()

    weil = pygame.Surface((16, 16)).convert()
    weil.fill((255, 255, 255, 255))
    s = pygame.image.load("Sprites/Misc/menu/weil.png").convert()
    w = avars[avars[3][5]][18]
    a = [4, 9, 19, 29][(avars[avars[3][5]][1] > 1) + (avars[avars[3][5]][1] > 2) + (avars[avars[3][5]][1] > 3)]
    b = [24, 39, 59, 74][(avars[avars[3][5]][1] > 1) + (avars[avars[3][5]][1] > 2) + (avars[avars[3][5]][1] > 3)]
    c = [44, 59, 79, 89][(avars[avars[3][5]][1] > 1) + (avars[avars[3][5]][1] > 2) + (avars[avars[3][5]][1] > 3)]
    weil.blit(s, [-(16 * ((w > a) + (w > b) + (w > c))), 0])

    carel = pygame.Surface((16, 16)).convert()
    carel.fill((255, 255, 255, 255))
    s = pygame.image.load("Sprites/Misc/menu/care.png").convert()
    c = avars[avars[3][5]][19]
    carel.blit(s, [-(16 * c), 0])

    poot = pygame.image.load("Sprites/Misc/menu/poo.png").convert()

    pstages = []

    if avars[avars[3][5]][1] > 1:
        g = avars[avars[3][5]][14]
        for n in avars[avars[3][5]][24]:
            ss = pygame.image.load("Sprites/Characters/chara_" + str(n) + "s.png")
            opal = []
            for i in range(32):
                opal.append(ss.get_at(((16 + (8 * (i % 2))), (16 + (i // 2)))))
            ss = palette.palch(ss, g, opal)
            s = pygame.Surface([16, 16])
            s.fill((0, 255, 255))
            s.blit(ss, [0, 0])
            s.set_colorkey((0, 255, 255))
            s.convert()
            pstages.append(s)

    arrow = pygame.image.load("Sprites/Misc/txtbox/arrow1.png").convert()

    money = pygame.image.load("Sprites/Misc/menu/gotchipt.png").convert()

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

    hungt = lfnt.render("STOMACH", 1, (0, 0, 100))
    happt = lfnt.render("MOOD", 1, (0, 0, 100))

    intlb = lfnt.render("LOGIC", 1, (0, 128, 255))
    stylb = lfnt.render("ARTISTRY", 1, (255, 128, 51))
    kndlb = lfnt.render("KINDNESS", 1, (102, 255, 51))
    humlb = lfnt.render("HUMOUR", 1, (153, 128, 0))
    gorlb = lfnt.render("BEAUTY", 1, (0, 153, 128))
    paslb = lfnt.render("PASSION", 1, (204, 0, 153))

    inttx = fnt.render(("%03d" % avars[avars[3][5]][5]), 1, (0, 128, 255))
    stytx = fnt.render(("%03d" % avars[avars[3][5]][6]), 1, (255, 128, 51))
    kndtx = fnt.render(("%03d" % avars[avars[3][5]][7]), 1, (102, 255, 51))
    humtx = fnt.render(("%03d" % avars[avars[3][5]][8]), 1, (153, 128, 0))
    gortx = fnt.render(("%03d" % avars[avars[3][5]][9]), 1, (0, 153, 128))
    pastx = fnt.render(("%03d" % avars[avars[3][5]][10]), 1, (204, 0, 153))

    intftx = fnt.render("999", 1, (0, 128, 255))
    styftx = fnt.render("999", 1, (255, 128, 51))
    kndftx = fnt.render("999", 1, (102, 255, 51))
    humftx = fnt.render("999", 1, (153, 128, 0))
    gorftx = fnt.render("999", 1, (0, 153, 128))
    pasftx = fnt.render("999", 1, (204, 0, 153))
    
    intbox = pygame.Surface([72, 16]).convert()
    intbox.fill((0, 64, 128))
    if avars[avars[3][5]][5] < 1000:
        intbox.fill((255, 255, 255), (1, 1, 70, 14))
        intbox.fill((0, 128, 255), (1, 1, ((70 * avars[avars[3][5]][5]) // 1000), 14))
    else:
        intbox.fill((0, 128, 255), (1, 1, 70, 14))
    stybox = pygame.Surface([72, 16]).convert()
    stybox.fill((128, 64, 25))
    if avars[avars[3][5]][6] < 1000:
        stybox.fill((255, 255, 255), (1, 1, 70, 14))
        stybox.fill((255, 128, 51), (1, 1, ((70 * avars[avars[3][5]][6]) // 1000), 14))
    else:
        stybox.fill((255, 128, 51), (1, 1, 70, 14))
    kndbox = pygame.Surface([72, 16]).convert()
    kndbox.fill((51, 128, 25))
    if avars[avars[3][5]][7] < 1000:
        kndbox.fill((255, 255, 255), (1, 1, 70, 14))
        kndbox.fill((102, 255, 51), (1, 1, ((70 * avars[avars[3][5]][7]) // 1000), 14))
    else:
        kndbox.fill((102, 255, 51), (1, 1, 70, 14))
    humbox = pygame.Surface([72, 16]).convert()
    humbox.fill((76, 64, 0))
    if avars[avars[3][5]][8] < 1000:
        humbox.fill((255, 255, 255), (1, 1, 70, 14))
        humbox.fill((153, 128, 0), (1, 1, ((70 * avars[avars[3][5]][8]) // 1000), 14))
    else:
        humbox.fill((153, 128, 0), (1, 1, 70, 14))
    gorbox = pygame.Surface([72, 16]).convert()
    gorbox.fill((0, 76, 64))
    if avars[avars[3][5]][9] < 1000:
        gorbox.fill((255, 255, 255), (1, 1, 70, 14))
        gorbox.fill((0, 153, 128), (1, 1, ((70 * avars[avars[3][5]][9]) // 1000), 14))
    else:
        gorbox.fill((0, 153, 128), (1, 1, 70, 14))
    pasbox = pygame.Surface([72, 16]).convert()
    pasbox.fill((102, 0, 76))
    if avars[avars[3][5]][10] < 1000:
        pasbox.fill((255, 255, 255), (1, 1, 70, 14))
        pasbox.fill((204, 0, 153), (1, 1, ((70 * avars[avars[3][5]][10]) // 1000), 14))
    else:
        pasbox.fill((204, 0, 153), (1, 1, 70, 14))

    sound = sounds.imprtsnd(avars)

    clock = pygame.time.Clock()

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
        ico, ix, iy = icoanim()
        screen.blit(textbox, [0, 24])
        screen.blit(scrli, [232, 128])
        if stsopt == 0:
            screen.blit(hungt, [8, 31])
            for i in range(4):
                if avars[avars[3][5]][16] > i:
                    screen.blit(fhng, [(16 + (24 * i)), 40])
                else:
                    screen.blit(ehng, [(16 + (24 * i)), 40])
            screen.blit(happt, [128, 31])
            for i in range(4):
                if avars[avars[3][5]][17] > i:
                    screen.blit(fhpy, [(136 + (24 * i)), 40])
                else:
                    screen.blit(ehpy, [(136 + (24 * i)), 40])
            screen.blit(intlb, [8, 55])
            screen.blit(inti, [16, 64])
            screen.blit(stylb, [8, 79])
            screen.blit(styi, [16, 88])
            screen.blit(kndlb, [8, 103])
            screen.blit(kndi, [16, 112])
            screen.blit(humlb, [120, 55])
            screen.blit(humi, [128, 64])
            screen.blit(gorlb, [120, 79])
            screen.blit(gori, [128, 88])
            screen.blit(paslb, [120, 103])
            screen.blit(pasi, [128, 112])
            if not shft:
                screen.blit(intbox, [40, 64])
                screen.blit(stybox, [40, 88])
                screen.blit(kndbox, [40, 112])
                screen.blit(humbox, [152, 64])
                screen.blit(gorbox, [152, 88])
                screen.blit(pasbox, [152, 112])
            else:
                if avars[avars[3][5]][5] < 1000:
                    screen.blit(inttx, [40, 66])
                else:
                    screen.blit(intftx, [40, 66])
                if avars[avars[3][5]][6] < 1000:
                    screen.blit(stytx, [40, 90])
                else:
                    screen.blit(styftx, [40, 90])
                if avars[avars[3][5]][7] < 1000:
                    screen.blit(kndtx, [40, 114])
                else:
                    screen.blit(kndftx, [40, 114])
                if avars[avars[3][5]][8] < 1000:
                    screen.blit(humtx, [152, 66])
                else:
                    screen.blit(humftx, [152, 66])
                if avars[avars[3][5]][9] < 1000:
                    screen.blit(gortx, [152, 90])
                else:
                    screen.blit(gorftx, [152, 90])
                if avars[avars[3][5]][10] < 1000:
                    screen.blit(pastx, [152, 114])
                else:
                    screen.blit(pasftx, [152, 114])
        elif stsopt == 1:
            if avars[avars[3][5]][15] < 385:
                screen.blit((fnt.render(chnamelst[(avars[avars[3][5]][15] - 1)], 1, (0, 0, 100))), [8, 34])
            else:
                try:
                    screen.blit((fnt.render(extrchn[str(avars[avars[3][5]][15])], 1, (0, 0, 100))), [8, 34])
                except:
                    screen.blit((fnt.render("???", 1, (0, 0, 100))), [8, 34])
            #print('%08x' % avars[avars[3][5]][14])
            if avars[avars[3][5]][14] % 2 == 0:
                screen.blit(male, [216, 32])
            else:
                screen.blit(female, [216, 32])
            screen.blit(grpf, [8, 56])
            screen.blit(grpm, [104, 56])
            screen.blit(grp, [40, 56])
            screen.blit((fnt.render((str(avars[avars[3][5]][3]) + "G"), 1, (0, 0, 100))), [184, 58])
            screen.blit((fnt.render((str((avars[avars[3][5]][2]) // 86400) + "  YEARS"), 1, (0, 0, 100))), [8, 82])
            if avars[avars[3][5]][33] > 3:
                screen.blit(poot, [120, 80])
            screen.blit(carel, [136, 80])
            screen.blit(weil, [152, 80])
            screen.blit(weis, [168, 80])
            screen.blit((fnt.render((str(avars[avars[3][5]][18] ) + "g"), 1, (0, 0, 100))), [184, 82])
            screen.blit(asprs[avars[3][5]][ico], [(24 + (32 * len(pstages))), 104])
            z = 0
            while z < len(pstages):
                screen.blit(pstages[z], [(24 + (32 * z)), 104])
                screen.blit(arrow, [(44 + (32 * z)), 108])
                z += 1
        elif stsopt == 2:
            screen.blit((fnt.render("USERNAME:", 1, (0, 0, 100))), [8, 34])
            screen.blit((fnt.render(avars[3][0], 1, (0, 0, 100))), [40, 50])
            screen.blit((fnt.render("BIRTHDAY:", 1, (0, 0, 100))), [8, 66])
            screen.blit((fnt.render(avars[3][1][:2], 1, (0, 0, 100))), [43, 82])
            screen.blit((fnt.render("M", 1, (0, 0, 100))), [66, 82])
            screen.blit((fnt.render(avars[3][1][2:], 1, (0, 0, 100))), [83, 82])
            screen.blit((fnt.render("D", 1, (0, 0, 100))), [106, 82])
            screen.blit((fnt.render("MONEY:", 1, (0, 0, 100))), [8, 98])
            screen.blit((fnt.render(str(avars[3][2]), 1, (0, 0, 100))), [(92 - (10 * (len(str(avars[3][2]))))), 114])
            screen.blit(money, [96, 112])
        for event in pygame.event.get():
            if event.type == QUIT:
                varsup.updtvrs(avars)
                kr = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                #print(event.key)
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
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if stsopt != 2:
                            stsopt += 1
                        else:
                            stsopt = 0
                        clt = 0
                elif pb == 5:
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if stsopt != 0:
                            stsopt -= 1
                        else:
                            stsopt = 2
                        clt = 0
                elif pb == 1:
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            sound[4].play()
                            return(avars)
                    clt = 0
                elif pb == 3:
                    if 24 < mp[1] < 136:
                        shft = not shft
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

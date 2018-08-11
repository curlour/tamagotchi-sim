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
import weather
import dirty
import mainscreen

def mailbox(avars, asprs, screen, md):

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

    global nflip
    nflip = False

    chngsts = False

    scr = 0

    clt = 0

    msel = 0

    swt = False

    inf = False

    tyod = 1

    swthr = ["skyd", "skyaf", "skyn"]
    cwthr = ["skydc", "skydc", "skync"]
    wthrbk = [swthr, cwthr, cwthr]

    pgbk = ["pgbk", "pgbks", "pgbka", "pgbkw"]

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
        a.blit(house, [0, 0])
        if w != 0:
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
        if tm == 2:
            a.blit(nwin, [204, 80])
        a.set_colorkey(c)
        bg.blit(a, [0, 0])
        return(bg)

    def mailani():
        nflip = False
        if anifr < 24 or anifr > 119:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                nzs = 5
            else:
                nzs = 3
            if anifr < 24:
                nflip = True
            if anifr < 6 or anifr > 137:
                nzx = -24
            elif anifr < 12 or 131 < anifr < 138:
                nzx = 0
            elif anifr < 18 or 125 < anifr < 132:
                nzx = 24
            else:
                nzx = 48
        elif anifr < 36 or 107 < anifr < 120:
            nzs = 2
            nzx = 48
        elif anifr < 84:
            if ((anifr / 12) - (anifr // 12)) < 0.5:
                nzs = 0
            else:
                nzs = 1
            nzx = 48
        elif anifr < 108:
            if anifr < 90 or anifr > 101:
                nzs = 3
            else:
                nzs = 4
            nflip = True
            nzx = 48
        return nzs, nzx, nflip

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 5, 0)

    nsprs = []
    s = pygame.image.load("Sprites/NPC/Nazotchi.png").convert()
    for i in range(6):
        a = pygame.Surface([32, 32]).convert()
        a.fill((0, 255, 255))
        a.blit(s, [-([0, 32, 64, 0, 32, 64][i]), -([0, 0, 0, 64, 64, 64][i])])
        a.set_colorkey((0, 255, 255))
        nsprs.append(a)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    house = pygame.image.load("Sprites/Misc/bg/house.png").convert()
    nwin = pygame.image.load("Sprites/Misc/bg/housewn.png").convert()

    mailbx = pygame.image.load("Sprites/Misc/obj/mailbx1.png").convert()
    letter = pygame.image.load("Sprites/Misc/obj/letter.png").convert()

    g = pygame.Surface([32, 32]).convert()
    g.fill((0, 255, 255))
    g.blit(pygame.image.load("Sprites/NPC/Guide.png").convert(), [0, 0])
    g.set_colorkey((0, 255, 255))

    b = pygame.Surface([32, 32]).convert()
    b.fill((0, 255, 255))
    b.blit(pygame.image.load("Sprites/NPC/Burglar.png").convert(), [0, 0])
    b.set_colorkey((0, 255, 255))

    s = pygame.Surface([32, 32]).convert()
    s.fill((0, 255, 255))
    s.blit(pygame.image.load("Sprites/NPC/Santa.png").convert(), [0, 0])
    s.set_colorkey((0, 255, 255))

    k = pygame.Surface([32, 32]).convert()
    k.fill((0, 255, 255))
    k.blit(pygame.image.load("Sprites/NPC/King.png").convert(), [0, 0])
    k.set_colorkey((0, 255, 255))

    nwsprs = [g, b, k, s]

    nwsprn = [1, 1, 2, 0, 0]

    gtnw = pygame.image.load("Sprites/Misc/bg/gotchinews.png").convert()
    tmlt = pygame.image.load("Sprites/Misc/bg/tamaletter.png").convert()

    if 0 < avars[avars[3][5]][31] < 4:
        worki = pygame.image.load("Sprites/Misc/mail/" + ["kinderen", "schoolen", "joben"][avars[avars[3][5]][31] - 1] + ".png").convert()
    elif 3 < avars[avars[3][5]][31] < 40:
        worki = pygame.image.load("Sprites/Misc/mail/job_" + str(avars[avars[3][5]][31] - 3) + ".png").convert()
    else:
        worki = pygame.image.load("Sprites/Misc/mail/retire.png").convert()

    ltrbox = pygame.image.load("Sprites/Misc/txtbox/box3.png").convert()

    inbox = []
    
    for file in os.listdir("Sprites/Misc/mail/tm" + str(avars[3][5] + 1)):
        if file.endswith(".png"):
            if pygame.image.load("Sprites/Misc/mail/tm" + str(avars[3][5] + 1) + "/" + file).get_rect().size == (240, 160):
                inbox.append(pygame.image.load("Sprites/Misc/mail/tm" + str(avars[3][5] + 1) + "/" + file).convert())

    inbox.reverse()

    rain = pygame.image.load("Sprites/Misc/bg/rain.png").convert()
    snow = pygame.image.load("Sprites/Misc/bg/snow.png").convert()

    raing = pygame.image.load("Sprites/Misc/bg/rpgb.png").convert()
    snowg = pygame.image.load("Sprites/Misc/bg/spgb.png").convert()

    s, tm , w = weather.chktime(avars)

    obgi = outbg()

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

    if avars[3][11] > -1:
        newtx = fnt.render("NEWS", 1, (0, 0, 100))
    else:
        newtx = fnt.render("NEWS", 1, (102, 102, 255))
    pertx = fnt.render("PERSONAL", 1, (0, 0, 100))
    if avars[avars[3][5]][31] == 0:
        wrktx = fnt.render("WORK", 1, (102, 102, 255))
    else:
        wrktx = fnt.render("WORK", 1, (0, 0, 100))
    if len(inbox) == 0:
        frntx = fnt.render("FRIENDS", 1, (102, 102, 255))
    else:
        frntx = fnt.render("FRIENDS", 1, (0, 0, 100))

    newstx = [["TO ALL INHABITANTS OF TAMAGOTCHI  PLANET:",
               "THE GOTCHI  BANK HAS BEEN ROBBED. THE",
               "BULGLAR HAS NOT BEEN FOUND YET. THE VICTIMS,",
               "THOSE WHOSE MONEY WAS TAKEN, WILL BE",
               "INFORMED BY MAIL.",
               "",
               "PLEASE CHECK YOUR MAIL TONIGHT."],
              ["TO ALL CITIZENS OF TAMAGOTCHI  TOWN:",
               "A BULGLAR HAS BEEN SEEN WANDERING",
               "AROUND TAMAGOTCHI  TOWN. PLEASE MAKE SURE",
               "YOUR HOUSE IS WELL PROTECTED TO PREVENT",
               "ANY ROBBERY.",
               "",
               "PLEASE BE CAREFUL."],
              ["NEWS FROM GOTCHI  KING'S CASTLE:",
               "THE  KING HAS LEFT HIS CASTLE AND IS NOW",
               "VISITING SOME OF OUR HOMES.",
               "IF YOU ARE  LUCKY ENOUGH, HE  MIGHT GIVE  YOU",
               "A PRESENT!",
               "",
               "HOW EXCITING!"],
              ["EVERYTHING IS GOING FINE ON OUR TOWN.",
               "WE HOPE  YOU ALL HAVE A GOOD DAY",
               "",
               "AS USUAL, A LETTER WILL BE  SENT TO EVERY OF",
               "OUR CITIZENS THIS AFTERNOON.",
               "",
               "PLEASE  STAY TUNED FOR MORE  NEWS TOMORROW!"],
              []]

    if (time.strftime("%m") + time.strftime("%d")) == avars[3][1]:
        newstx.append(["IT SEEMS LIKE SOMEONE IS HAVING A",
                     "BIRTHDAY TODAY...",
                     "HAPPY BIRTHDAY, " + avars[3][0] + "!",
                     "",
                     "WE HOPE YOU HAVE A GREAT DAY!",
                     "",
                     "PLEASE, ACCEPT THIS CAKE!"])
    if 2 < int(time.strftime("%m")) < 6:
        if int(time.strftime("%m")) == 3 and int(time.strftime("%d")) < 11:
            newstx[4] = ["THE  WINTER FREEZE IS LEAVING AT LAST.",
                         "IT IS NOW THE BEGINNING OF A NEW SEASON",
                         "HERE, IN TAMAGOTCHI  TOWN.",
                         "",
                         "WE WANT TO WISH ALL THE FAMILIES WITH",
                         "GIRLS A HEALTHY GROWTH.",
                         "DO NOT FORGET THE ORNAMENTAL DOLLS!"]
        elif int(time.strftime("%m")) == 4 and int(time.strftime("%d")) < 11:
            newstx[4] = ["THE FLOWERS ARE  BLOOMING, DYEING OUR TOWN",
                         "WITH THE  SOFT COLOURS OF SPRING.",
                         "CHERRY BLOSSOMS CAN BE  SEEN ALL AROUND.",
                         "",
                         "WE WANT TO WISH ALL OUR CITIZENS A HAPPY AND",
                         "EVENTFUL SEASON.",
                         "ENJOY THE VIEWS AS LONG AS YOU CAN!"]
            newstx.append(["WE HOPE YOU ARE ENJOYING THIS BEAUTIFUL",
                         "SEASON, WITH  ALL OUR FLOWERS AT FULL BLOOM.",
                         "",
                         "WE HAVE SENT YOU A GIFT.",
                         "PLEASE ACCEPT IT!",
                         "",
                         "WE WILL SEND YOU ANOTHER LETTER SOON."])
        elif int(time.strftime("%m")) == 5 and int(time.strftime("%d")) < 11:
            newstx[4] = ["THE FLOWERS ARE SLOWLY DISAPPEARING AT",
                         "THE INMINENT ARRIVAL OF SUMMER, ALL OVER",
                         "OUR TOWN, TAMAGOTCHI  TOWN.",
                         "",
                         "WE WANT TO WISH ALL THE FAMILIES WITH",
                         "BOYS A HEALTHY GROWTH.",
                         "DO NOT FORGET THE CARP STREAMERS!"]
        else:
            newstx[4] = ["TODAY IS JUST ANOTHER PEACEFUL AND NICE",
                         "SPRING DAY...",
                         "",
                         "FLOWERS ARE EVERYWHERE TO BE SEEN AND BIRDS",
                         "ARE SINGING THEIR MOST CHEERFUL MELODIES.",
                         "",
                         "THOSE WITH ALLERGIES SHOULD BE CAREFUL."]
    elif 5 < int(time.strftime("%m")) < 9:
        if int(time.strftime("%m")) == 7 and int(time.strftime("%d")) < 11:
            newstx[4] = ["THE SUN SHINES BRIGHT ON TAMAGOTCHI  TOWN.",
                         "THIS SEASON WILL BRING US SEVERAL CLEAR,",
                         "STAR FILLED NIGHTS!",
                         "THE PERFECT WEATHER FOR THE STAR  FESTIVAL.",
                         "",
                         "MAKE SURE TO MAKE A WISH UPON A STAR",
                         "TONIGHT, FOR THEY MAY GRANT IT TO YOU!"]
            newstx.append(["WE HOPE YOU ARE ENJOYING SUMMER, IN SPITE  OF",
                         "THE  HEAT!",
                         "",
                         "BE SURE TO MAKE YOUR WISH, SO IT CAN BE",
                         "GRANTED TO YOU!",
                         "",
                         "WE HOPE YOU LIKE  THIS  GIFT!"])
        elif int(time.strftime("%m")) == 8 and 10 < int(time.strftime("%d")) < 21:
            newstx[4] = ["THIS SUMMER IS BRINGING US MANY CLEAR  DAYS,",
                         "A PERFECT WEATHER FOR FIREWORKS!",
                         "",
                         "BE PREPARED TO SEE THE NIGHT SKY FILLED WITH",
                         "COLOURFUL BLASTS!",
                         "",
                         "HAVE A NICE SUMMER BREAK!"]
        else:
            newstx[4] = ["THE  SUMMER HEAT IS EVAPORATING ALL OUR",
                         "WORRIES AND THE  WIND IS BLOWING ALL OUR",
                         "TROUBLES AWAY.",
                         "",
                         "THIS IS THE IDEAL SEASON FOR RELAXING.",
                         "",
                         "TRY NOT TO GET SUN BURNED!"]
    elif 8 < int(time.strftime("%m")) < 12:
        if (int(time.strftime("%m")) == 10 and int(time.strftime("%d")) > 25) or (int(time.strftime("%m")) == 11 and int(time.strftime("%d")) < 5):
            newstx[4] = ["RAIN FALLS ON THE  GRAVEYARD TO REMIND US OF",
                         "THE INEXORABLE  PASSAGE OF TIME  AND OF ALL",
                         "OUR LOVED ONES WHO HAVE LEFT US.",
                         "",
                         "LET US CELEBRTE THIS HOLIDAY IN THEIR HONOUR",
                         "AND REPLACE THE GRIEF WITH JOY!",
                         "OR JUST EAT CANDY IF YOU WANT."]
            newstx.append(["WE  HOPE YOU ARE  ENJOYING THIS FRIGHTENING",
                         "YET DELICIOUS  HOLIDAY!",
                         "",
                         "WE PREPARED A SPOOKY SWEET TREAT JUST",
                         "FOR YOU!",
                         "",
                         "WE HOPE YOU ENJOY IT!"])
        else:
            newstx[4] = ["THE RAIN IS FALLING.",
                         "THE  TREES ARE  COLOURED  BRIGHT RED.",
                         "HOW ENSORCELLING.",
                         "",
                         "WE  HOPE YOU ALL ENJOY THIS BEAUTIFUL SEASON",
                         "AS MUCH AS WE DO!",
                         "TRY NOT TO CATCH A COLD, THOUGH."]
    else:
        if int(time.strftime("%m")) == 12 and int(time.strftime("%d")) > 19:
            newstx[4] = ["WHAT ARE THOSE BELLS JINGLING?",
                         "IT SEEMS LIKE  THE  HOLIDAYS  ARE  FINALLY HERE!",
                         "",
                         "IT IS TIME TO SET ALL THE  DECORATIONS  UP AND",
                         "WAIT FOR THE  ARRIVAL OF  SANTACLAUTCHI!",
                         "",
                         "MERRY CHRISTMAS, TAMAGOTCHI TOWN!"]
            nwsprn[4] = 3
            newstx.append(["WE HOPE YOU ARE ENJOYING YOUR HOLIDAYS!",
                         "",
                         "PLEASE  ACCEPT THESE  PRESENT!",
                         "IT WILL HELP YOU MAKE THE MOST OUT OF YOUR",
                         "WINTER HOLIDAYS!",
                         "",
                         "MERRY CHRISTMAS!"])
        elif int(time.strftime("%m")) == 1 and int(time.strftime("%d")) < 11:
            newstx[4] = ["HAPPY NEW YEAR  " + time.strftime("%Y") + "!",
                         "",
                         "IT IS FINALLY THE DAWN OF A NEW YEAR.",
                         "",
                         "WE HOPE ALL YOUR RESOLUTIONS  HAVE  BECOME  A",
                         "REALITY BY THE TIME THIS YEAR ENDS!",
                         "TRY TO MAKE THE BEST OUT OF THIS NEW YEAR!"]
            newstx.append(["GREETINGS!",
                         "WE HOPE  " + time.strftime("%Y") + " HAD A GREAT START FOR YOU!",
                         "",
                         "WE WOULD LIKE TO GIVE  YOU THIS  PRESENT AND",
                         "WISH YOU AN EVENTFUL YEAR.",
                         "",
                         "HAPPY NEW YEAR!"])
        else:
            newstx[4] = ["OUR TOWN IS COVERED WITH PURE  WHITE SNOW.",
                         "WE  WANT TO GO OUTSIDE TO SEE  IT, BUT THE",
                         "WARMTH OF OUR HOMES  SEEMS  TO BE  MORE",
                         "INVITING THAN IT EVER WAS...",
                         "",
                         "WE HOPE  YOU ALL ENJOY YOURSELVES DURING",
                         "THIS FREEZING SEASON!"]
            
    if avars[avars[3][5]][31] == 0:
        newstx.append(["GOOD EVENING!",
                     "WE ARE CONTACTING YOU TO REMIND YOU THAT",
                     avars[avars[3][5]][22] + " IS STILL UNEMPLOYED.",
                     "",
                     "WE HOPE YOU CAN FIND A JOB SOON!",
                     "",
                     "BYE!"])
    elif avars[avars[3][5]][31] == 1:
        newstx.append(["LETTER FROM TAMAGOTCHI  PRESCHOOL!",
                     "",
                     avars[avars[3][5]][22] + "'S CLASS WON A COMPETITION!",
                     "",
                     "THEY ALL GOT A PRIZE!",
                     "",
                     "WELL DONE!"])
        newstx.append(["LETTER FROM TAMAGOTCHI  PRESCHOOL...",
                     "",
                     avars[avars[3][5]][22] + "'S CLASS WAS CHOSEN TO PAY FOR THE",
                     "NEW TOYS FOR OUR STUDENTS.",
                     "EACH ONE HAS TO PAY 200G.",
                     "",
                     "SORRY FOR THE  INCONVENIENCE..."])
    elif avars[avars[3][5]][31] == 2:
        newstx.append(["LETTER FROM TAMAGOTCHI  SCHOOL!",
                     "",
                     avars[avars[3][5]][22] + "'S CLASS WON A COMPETITION!",
                     "",
                     "THEY ALL GOT A PRIZE!",
                     "",
                     "WELL DONE!"])
        newstx.append(["LETTER FROM TAMAGOTCHI  SCHOOL...",
                     "",
                     avars[avars[3][5]][22] + "'S CLASS WAS CHOSEN TO PAY FOR THE",
                     "NEW SCHOOL MATERIAL FOR OUR STUDENTS.",
                     "EACH ONE HAS TO PAY 300G.",
                     "",
                     "SORRY FOR THE  INCONVENIENCE..."])
    else:
        newstx.append(["LETTER FROM GOTCHI CASTLE!",
                     "",
                     avars[avars[3][5]][22] + " HAS BEEN WORKING HARD!",
                     "",
                     "YOU DESERVE A BONUS!",
                     "",
                     "WELL DONE!"])
        newstx.append(["LETTER FROM GOTCHI CASTLE...",
                     "",
                     avars[avars[3][5]][22] + "'S WORKPLACE  NEEDS  FUNDING IN",
                     "ORDER TO IMPROVE THE FACILITIES.",
                     "EACH ONE HAS TO PAY 500G.",
                     "",
                     "SORRY FOR THE  INCONVENIENCE..."])

    if avars[3][11] == 0 or avars[3][11] == 1:
        newstx.append(["LETTER FROM GOTCHI BANK...",
                     "",
                     "YOU HAVE  BEEN ROBBED.",
                     "THE BURGLAR PRESUMED TO BE  THE  CULPRIT IS",
                     "KNOWN TO STEAL QUANTITIES UP TO 500G.",
                     "",
                     "WE ARE VERY SORRY..."])
    elif avars[3][11] == 2:
        newstx.append(["LETTER FROM GOTCHI BANK!",
                     "",
                     "THE GOTCHI KING HAS COME HERE AND GAVE AWAY",
                     "MONEY TO SEVERAL CITIZENS!",
                     "YOU RECEIVED 1000G!",
                     "",
                     "YOU ARE SO LUCKY!"])

    mailsp = pygame.image.load("Sprites/Misc/obj/letter.png").convert()

    if md == 0 and ((int(avars[3][6][:2]) < 16 and avars[3][11] < 0) or (int(avars[3][6][:2]) > 15 and avars[3][11] < 5)) and avars[avars[3][5]][1] > 1:
        tyod = 0
        if int(avars[3][6][:2]) < 16:
            avars[3][11] = randint(0, 4)
        else:
            if (time.strftime("%m") + time.strftime("%d")) == avars[3][1]:
                avars[3][11] = 5
            else:
                avars[3][11] = randint(5, (len(newstx) - 1))
            if newstx[avars[3][11]][0] == "IT SEEMS LIKE SOMEONE IS HAVING A":
                h = False
                a = 0
                for f in avars[3][4]:
                    if f[0] == 'BDCake':
                        h = True
                        break
                    a += 1
                if h:
                    avars[3][4][a][4] += 1
                else:
                    a = avars[3][4]
                    a.append(['BDCake', 4, 4, 4, 1, 2, 2, 2, 2, 2, 2])
                    avars[3][4] = a
                s = pygame.image.load("Sprites/Food/BDCake.png").convert()
                mailsp = pygame.Surface([24, 24]).convert()
                mailsp.fill((0, 255, 255))
                mailsp.blit(s, [0, 0])
                mailsp.set_colorkey((0, 255, 255))
                avars[avars[3][5]][17] = 6
            elif newstx[avars[3][11]][0] in ["WE HOPE YOU ARE ENJOYING THIS BEAUTIFUL",
                                             "WE HOPE YOU ARE ENJOYING SUMMER, IN SPITE  OF",
                                             "WE  HOPE YOU ARE  ENJOYING THIS FRIGHTENING",
                                             "WE HOPE YOU ARE ENJOYING YOUR HOLIDAYS!",
                                             "GREETINGS!"]:
                if newstx[avars[3][11]][0] == "WE HOPE YOU ARE ENJOYING THIS BEAUTIFUL":
                    h = False
                    a = 0
                    for f in avars[3][4]:
                        if f[0] == 'Sakuramochi':
                            h = True
                            break
                        a += 1
                    if h:
                        avars[3][4][a][4] += 3
                    else:
                        a = avars[3][4]
                        a.append(['Sakuramochi', 3, 3, 2, 3, 0, 6, 0, 0, 6, 0])
                        avars[3][4] = a
                elif newstx[avars[3][11]][0] == "WE HOPE YOU ARE ENJOYING SUMMER, IN SPITE  OF":
                    h = False
                    a = 0
                    for f in avars[3][4]:
                        if f[0] == 'Beans':
                            h = True
                            break
                        a += 1
                    if h:
                        avars[3][4][a][4] += 3
                    else:
                        a = avars[3][4]
                        a.append(['Beans', 3, 3, 1, 3, 0, 0, 6, 0, 0, 6])
                        avars[3][4] = a
                elif newstx[avars[3][11]][0] == "WE  HOPE YOU ARE  ENJOYING THIS FRIGHTENING":
                    h = False
                    a = 0
                    for f in avars[3][4]:
                        if f[0] == 'PumPie':
                            h = True
                            break
                        a += 1
                    if h:
                        avars[3][4][a][4] += 3
                    else:
                        a = avars[3][4]
                        a.append(['PumPie', 3, 3, 3, 3, 6, 0, 0, 6, 0, 0])
                        avars[3][4] = a
                elif newstx[avars[3][11]][0] == "WE HOPE YOU ARE ENJOYING YOUR HOLIDAYS!":
                    h = False
                    a = 0
                    for f in avars[3][4]:
                        if f[0] == 'XMasCake':
                            h = True
                            break
                        a += 1
                    if h:
                        avars[3][4][a][4] += 3
                    else:
                        a = avars[3][4]
                        a.append(['XMasCake', 4, 4, 3, 3, 2, 2, 2, 2, 2, 2])
                        avars[3][4] = a
                elif newstx[avars[3][11]][0] == "GREETINGS!":
                    h = False
                    a = 0
                    for f in avars[3][4]:
                        if f[0] == 'Zouni':
                            h = True
                            break
                        a += 1
                    if h:
                        avars[3][4][a][4] += 3
                    else:
                        a = avars[3][4]
                        a.append(['Zouni', 2, 2, 2, 3, 1, 1, 1, 1, 1, 1])
                        avars[3][4] = a
                mailsp = pygame.image.load("Sprites/Misc/obj/present.png").convert()
                if avars[avars[3][5]][17] < 6:
                    avars[avars[3][5]][17] += 1
            elif newstx[avars[3][11]][0] == "GOOD EVENING!":
                if avars[avars[3][5]][17] > 0:
                    avars[avars[3][5]][17] -= 1
            elif newstx[avars[3][11]][0] in ["LETTER FROM TAMAGOTCHI  PRESCHOOL!",
                                             "LETTER FROM TAMAGOTCHI  SCHOOL!",
                                             "LETTER FROM GOTCHI CASTLE!"]:
                if avars[3][2] < 99499:
                    avars[3][2] += 500
                else:
                    avars[3][2] = 99999
                if avars[avars[3][5]][17] < 5:
                    avars[avars[3][5]][17] += 2
                else:
                    avars[avars[3][5]][17] = 6
            elif newstx[avars[3][11]][0] in ["LETTER FROM TAMAGOTCHI  PRESCHOOL...",
                                             "LETTER FROM TAMAGOTCHI  SCHOOL...",
                                             "LETTER FROM GOTCHI CASTLE..."]:
                if avars[avars[3][5]][31] == 2:
                    a = 200
                elif avars[avars[3][5]][31] == 3:
                    a = 300
                else:
                    a = 500
                if avars[3][2] > a:
                    avars[3][2] -= a
                else:
                    avars[3][2] = 0
                if avars[avars[3][5]][17] > 2:
                    avars[avars[3][5]][17] -= 2
                else:
                    avars[avars[3][5]][17] = 0
            elif newstx[avars[3][11]][0] == "LETTER FROM GOTCHI BANK...":
                mailsp = pygame.image.load("Sprites/Misc/obj/money.png").convert()
                if avars[3][2] > 500:
                    avars[3][2] -= 500
                else:
                    avars[3][2] = 0
                if avars[avars[3][5]][17] > 2:
                    avars[avars[3][5]][17] -= 2
                else:
                    avars[avars[3][5]][17] = 0
            elif newstx[avars[3][11]][0] == "LETTER FROM GOTCHI BANK!":
                mailsp = pygame.image.load("Sprites/Misc/obj/money.png").convert()
                if avars[3][2] < 98999:
                    avars[3][2] += 1000
                else:
                    avars[3][2] = 99999
                if avars[avars[3][5]][17] < 3:
                    avars[avars[3][5]][17] += 3
                else:
                    avars[avars[3][5]][17] = 6
        n = pygame.Surface([240, 160]).convert()
        n.fill((0, 255, 255))
        if avars[3][11] < 5:
            n.blit(gtnw, [40, 32])
            n.blit(nwsprs[nwsprn[avars[3][11]]], [8, 32])
        else:
            n.blit(tmlt, [8, 32])
            n.blit(lfnt.render(avars[3][0], 1, (0, 0, 100)), [68, 53])
            n.blit(mailsp, [196, 36])
        n.blit(lfnt.render(newstx[avars[3][11]][0], 1, (0, 0, 100)), [8, 71])
        n.blit(lfnt.render(newstx[avars[3][11]][1], 1, (0, 0, 100)), [8, 79])
        n.blit(lfnt.render(newstx[avars[3][11]][2], 1, (0, 0, 100)), [8, 87])
        n.blit(lfnt.render(newstx[avars[3][11]][3], 1, (0, 0, 100)), [8, 95])
        n.blit(lfnt.render(newstx[avars[3][11]][4], 1, (0, 0, 100)), [8, 103])
        n.blit(lfnt.render(newstx[avars[3][11]][5], 1, (0, 0, 100)), [8, 111])
        n.blit(lfnt.render(newstx[avars[3][11]][6], 1, (0, 0, 100)), [8, 119])
        pygame.image.save(n, "Sprites/Misc/mail/news.png")
        
    if avars[3][11] > -1:
        nwsimg = pygame.image.load("Sprites/Misc/mail/news.png").convert()
        nwsimg.set_colorkey((0, 255, 255))

    sound = sounds.imprtsnd(avars)

    clock = pygame.time.Clock()

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if md == 0:
            screen.blit(obgi, [0, 0])
            if w == 2:
                if ((anifr / 12) - (anifr // 12)) < 0.5:
                    y = 0
                else:
                    if s < 3:
                        y = 16
                    else:
                        y = 8
                if s < 3:
                    screen.blit(rain, [0, y])
                else:
                    screen.blit(snow, [0, y])
            screen.blit(mailbx, [106, 94])
            nzs, nzx, nflip = mailani()
            screen.blit(pygame.transform.flip(nsprs[nzs], nflip, 0), [nzx, 98])
            if 89 < anifr < 102:
                screen.blit(letter, [82, 100])
            if anifr == 0 or anifr == 12 or anifr == 90 or anifr == 120 or anifr == 132:
                sound[6].play()
            elif anifr == 24 or anifr == 108:
                sound[9].play()
        elif md == 1:
            if scr < 2:
                screen.blit(textbox, [0, 24])
            if scr == 0:
                screen.blit(newtx, [8, 34])
                screen.blit(pertx, [8, 50])
            elif scr == 1:
                screen.blit(wrktx, [8, 34])
                screen.blit(frntx, [8, 50])
            elif scr == 2:
                screen.blit(ltrbox, [0, 0])
                screen.blit(nwsimg, [0, 0])
            elif scr == 3:
                screen.blit(worki, [0, 0])
            elif scr == 4:
                screen.blit(inbox[msel], [0, 0])
                screen.blit(scrli, [232, 128])
            elif scr == 5:
                screen.blit(outbox[msel], [0, 0])
                screen.blit(scrli, [232, 128])
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
                if (pb in [2, 4]) and scr > 3:
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if msel != msmax:
                            msel += 1
                        else:
                            msel = 0
                        clt = 0
                elif pb == 5 and scr > 3:
                    if 24 < mp[1] < 136:
                        sound[2].play()
                        if msel != 0:
                            msel -= 1
                        else:
                            msel = msmax
                        clt = 0
                elif pb == 1:
                    clt = 0
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            sound[4].play()
                            return(avars)
                    if md == 1:
                        if 32 < mp[1] < 48 and 8 < mp[0] < 110:
                            if scr == 0 and avars[3][11] > -1:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 2
                            elif scr == 1 and avars[avars[3][5]][31] > 0:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 3
                        elif 48 < mp[1] < 64 and 8 < mp[0] < 110:
                            if scr == 0:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 1
                            elif scr == 1 and len(inbox) > 0:
                                pygame.mixer.stop()
                                sound[3].play()
                                scr = 4
                                msel = 0
                                msmax = len(inbox) - 1
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
            if avars[avars[3][5]][20] or not avars[avars[3][5]][21]:
                return(avars)
            chngsts = False
        if anifr < 143:
            anifr += 1
        else:
            anifr = 0
            if md == 0:
                if tyod == 0:
                    md = 1
                    scr = 2
                elif len(inbox) > 0:
                    md = 1
                    scr = 4
                else:
                    return(avars)
        if clt > 29 and md == 1 and scr < 2:
            return(avars)
        r = pygame.Surface([240, 160]).convert()
        r.blit(screen, [0, 0])
        r = pygame.transform.scale(r, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(r, [0, 0])
        clock.tick(16)
        pygame.display.update()

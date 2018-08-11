import pygame, sys
import os
from pygame.locals import *
import shelve
import inisel
import eggsel
import mainscreen

kr = True
            
pygame.init()
screen = pygame.display.set_mode((240, 160))
pygame.display.set_caption('Tamagotchi PC')

fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

clock = pygame.time.Clock()

while kr:
    if os.path.isfile('save_db.dat'):
        try:
            d = shelve.open('save_db')
            if not (('egg2' in d) or ('egg3' in d)) and d['egg1'] == None:
                d.close()
                eggsel.crdani(screen)
            else:
                d.close()
                mainscreen.mnscr()
        except (EOFError, KeyError):
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
    else:
        inisel.init()

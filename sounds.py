import pygame, sys
import os
from pygame.locals import *

def imprtsnd(avars):
    abeep = pygame.mixer.Sound("Sound/attention.ogg")
    hbeep = pygame.mixer.Sound("Sound/happy.ogg")
    abbeep = pygame.mixer.Sound("Sound/ab.ogg")
    bbbeep = pygame.mixer.Sound("Sound/bb.ogg")
    cbbeep = pygame.mixer.Sound("Sound/cb.ogg")
    poobeep = pygame.mixer.Sound("Sound/poo.ogg")
    stpbeep = pygame.mixer.Sound("Sound/step.ogg")
    htchbeep = pygame.mixer.Sound("Sound/ecrack.ogg")
    brnbeep = pygame.mixer.Sound("Sound/born.ogg")
    meetbeep = pygame.mixer.Sound("Sound/meet.ogg")
    rdybeep = pygame.mixer.Sound("Sound/ready.ogg")
    gobeep = pygame.mixer.Sound("Sound/go.ogg")
    erbeep = pygame.mixer.Sound("Sound/error.ogg")
    gmbeep = pygame.mixer.Sound("Sound/gmon.ogg")
    sadbeep = pygame.mixer.Sound("Sound/sad.ogg")
    cngbeep = pygame.mixer.Sound("Sound/cong.ogg")
    evobeep = pygame.mixer.Sound("Sound/evo.ogg")
    dthbeep = pygame.mixer.Sound("Sound/death.ogg")
    trmpbeep = pygame.mixer.Sound("Sound/trumpet.ogg")
    cn = pygame.mixer.Sound("Sound/cn.ogg")
    dn = pygame.mixer.Sound("Sound/dn.ogg")
    en = pygame.mixer.Sound("Sound/en.ogg")
    fn = pygame.mixer.Sound("Sound/fn.ogg")

    abeep.set_volume(float(avars[3][8]))
    hbeep.set_volume(float(avars[3][8]))
    abbeep.set_volume(float(avars[3][8]))
    bbbeep.set_volume(float(avars[3][8]))
    cbbeep.set_volume(float(avars[3][8]))
    poobeep.set_volume(float(avars[3][8]))
    stpbeep.set_volume(float(avars[3][8]))
    htchbeep.set_volume(float(avars[3][8]))
    brnbeep.set_volume(float(avars[3][8]))
    meetbeep.set_volume(float(avars[3][8]))
    rdybeep.set_volume(float(avars[3][8]))
    gobeep.set_volume(float(avars[3][8]))
    erbeep.set_volume(float(avars[3][8]))
    gmbeep.set_volume(float(avars[3][8]))
    sadbeep.set_volume(float(avars[3][8]))
    cngbeep.set_volume(float(avars[3][8]))
    evobeep.set_volume(float(avars[3][8]))
    dthbeep.set_volume(float(avars[3][8]))
    trmpbeep.set_volume(float(avars[3][8]))
    cn.set_volume(float(avars[3][8]))
    dn.set_volume(float(avars[3][8]))
    en.set_volume(float(avars[3][8]))
    fn.set_volume(float(avars[3][8]))

    sounds = [abeep, hbeep, abbeep, bbbeep, cbbeep, poobeep, stpbeep, htchbeep, brnbeep, meetbeep, rdybeep, gobeep, erbeep, gmbeep, sadbeep, cngbeep,
              evobeep, dthbeep, trmpbeep, cn, dn, en, fn]

    return(sounds)
    

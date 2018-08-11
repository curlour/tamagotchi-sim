import pygame, sys
import os
from pygame.locals import *

def dirt(spr):
    a = pygame.Surface([spr.get_width(), spr.get_height()]).convert()
    a.fill((128, 0, 0))
    a.blit(spr, [0, 0])
    b = pygame.Surface([spr.get_width(), spr.get_height()]).convert()
    b.fill((128, 0, 0))
    b.set_alpha(128)
    a.blit(b, [0, 0])
    a.set_colorkey((128, 0, 0))
    return (a)

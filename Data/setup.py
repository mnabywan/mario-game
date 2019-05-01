import os
from . import tools
import pygame
from . import constants

pygame.init()
SCREEN = pygame.display.set_mode(constants.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()
GFX = tools.load_all_gfx(os.path.join("graphics"))

import pygame
import os

class Control(object):
    """Class to control project, contains game loop"""
    '''
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock= pygame.time.Clock()
        self.caption = caption
        self.fps = 60
        self.current_time = 0.0
        self.keys = pygame.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None

'''

    def load_all_gfx(directory, colorkey=(255, 0, 255), accept=('.png', 'jpg', 'bmp')):
        graphics = {}
        for pic in os.listdir(directory):
            name, ext = os.path.splitext(pic)
            if ext.lower() in accept:
                img = pg.image.load(os.path.join(directory, pic))
                if img.get_alpha():
                    img = img.convert_alpha()
                else:
                    img = img.convert()
                    img.set_colorkey(colorkey)
                graphics[name] = img
        return graphics


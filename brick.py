import pygame
class Brick(object):


    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.is_visible = True


    def draw(self):
        rect =  pygame.Rect(self.x,self.y, self.width, self.height)
        pygame.draw.rect(self.game.level.screen, (0,0,0),rect)

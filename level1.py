import pygame
from mario import Mario
import constants as c
from collider import *


class Level1:
    def __init__(self, game, width, heigth):
        self.game = game
        self.setup_mario()
        self.init_background(self.mario, width, heigth)



    def init_background(self, mario, width, heigth):
        self.screen_height = heigth
        self.screen_width = width
        self.bg_pos = [0, 0]
        self.level_width = c.LEVEL_WIDTH
        self.level_heigth = c.LEVEL_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg = pygame.image.load('/home/mateusz/Documents/MarioGame/assets/level_1.png')
        self.bg = pygame.transform.scale(self.bg, (self.level_width, self.level_heigth))
        self.setup_background_elements()

    def draw_background(self):
        self.delta_x = -self.bg_pos[0]
        if self.mario.vel[0] and self.mario.inthemiddle and self.mario.coordinate_x < self.level_width - self.screen_width * 0.5:
            self.bg_pos[0] = -self.mario.coordinate_x + self.screen_width * 0.5
        self.delta_x += self.bg_pos[0]
        self.update_background_elements()
        self.screen.blit(self.bg, self.bg_pos)
        self.bg_elem_group.draw(self.screen)
        #self.screen.blit(self.bg, self.bg_pos)


    def read_map(self):
        f = open('/home/mateusz/Documents/MarioGame/assets/map.txt')
        self.map = f.readlines()
        for i in range(0, c.HEIGHT_ELEMENTS, 1):
            self.map[i] = self.map[i].split()


    def setup_background_elements(self):
        self.read_map()
        self.bg_elem_group = pygame.sprite.Group()
        for i in range(0, c.HEIGHT_ELEMENTS, 1):
            for j in range(0, c.WIDTH_ELEMENTS, 1):
                if self.map[i][j] != "0":
                    element = Collider(c.MULTIPLICATION*j, c.MULTIPLICATION*i, c.MULTIPLICATION, c.MULTIPLICATION)
                    self.bg_elem_group.add(element)

    def setup_mario(self):
        self.mario = Mario


    def check_mario_collisions_x(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        if bg_elem:
            if self.mario.rect.x < bg_elem.rect.left:
                self.mario.rect.right = bg_elem.rect.left
                #self.mario.can_move_right = False

            elif self.mario.rect.x < bg_elem.rect.right:
                self.mario.rect.left = bg_elem.rect.right
                #self.mario.can_move_left = False

            #self.mario.vel = 0
            #self.mario.coordinate_x -= self.mario.vel[0]


    def check_mario_collisions_y(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        if bg_elem:

            if self.mario.rect.y < bg_elem.rect.bottom:
                self.mario.rect.top = bg_elem.rect.bottom

            elif self.mario.rect.y > bg_elem.rect.top:
                self.mario.rect.bottom = bg_elem.rect.top

    def update_background_elements(self):
        for element in self.bg_elem_group:
            element.rect.x += self.delta_x

        #self.check_mario_collisions_y()
        #self.check_mario_collisions_x()


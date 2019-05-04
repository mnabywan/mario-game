from Data import constants as c
from Data.collider import *
from Data.mario import Mario
import os
from . import setup



class Level1:
    def __init__(self, game, width, heigth):
        self.game = game
        self.mario = Mario(self.game)
        self.mario.rect.x = 20
        self.mario.rect.bottom = c.GROUND_HEIGHT

        self.init_background(self.mario, width, heigth)

    def move_mario(self):
        return self.mario.handle_state()

    def draw_mario(self):
        return self.mario.draw()

    def init_background(self, mario, width, heigth):
        self.screen_height = heigth
        self.screen_width = width
        self.bg_pos = [0, 0]
        self.level_width = c.LEVEL_WIDTH
        self.level_heigth = c.LEVEL_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg = setup.GFX['level1']
        self.bg = pygame.transform.scale(self.bg, (self.level_width, self.level_heigth))
        self.setup_background_elements()


    def draw_background(self):
        self.delta_x = -self.bg_pos[0]
        if self.mario.vel[0] and self.mario.in_the_middle and self.mario.coordinate_x < self.level_width - self.screen_width * 0.5:
            self.bg_pos[0] = -self.mario.coordinate_x + self.screen_width * 0.5
        self.delta_x += self.bg_pos[0]
        self.update_background_elements()
        self.screen.blit(self.bg, self.bg_pos)
        self.bg_elem_group.draw(self.screen)
        #self.screen.blit(self.bg, self.bg_pos)

    def read_map(self):
        f = open('./assets/map.txt')
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

    def check_mario_collisions_x(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        if bg_elem:
            if self.mario.rect.x < bg_elem.rect.x:
                self.mario.rect.right = bg_elem.rect.left
            else:
                self.mario.rect.left = bg_elem.rect.right

            self.mario.vel[0] = 0


    def check_mario_collisions_y(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        if bg_elem:

            if bg_elem.rect.bottom > self.mario.rect.bottom:
                self.mario.vel[1] = 0
                self.mario.rect.bottom = bg_elem.rect.top
                self.mario.state = c.WALK

            elif self.mario.rect.top > bg_elem.rect.top:
                self.mario.rect.top = bg_elem.rect.bottom
                self.mario.state = c.FALL
                #self.mario.rect.bottom = bg_elem.rect.top

    def update_background_elements(self):
        for element in self.bg_elem_group:
            element.rect.x += self.delta_x

        self.check_mario_collisions_y()
        self.check_mario_collisions_x()


from Data import constants as c
from Data.collider import *
from Data.mario import Mario
from Data.brick import Brick
from Data.enemy import Enemy
import os
from . import setup

#na nastepnych zajeciach prezentacje mamy mieć że w miarę dziala albo ukryte niedorobki
#za nastepne 2 tygodnie oddawanie do prowadzacego
#12 min na pokazanie

class Level1:
    def __init__(self, game, width, heigth):
        self.game = game
        self.mario = Mario(self.game)
        self.init_background(width, heigth)

    def move_mario(self):
        return self.mario.handle_state()

    def move_enemy(self):
        for enemy in self.enemy_group:
            enemy.move()

    def draw_mario(self):
        return self.mario.draw()

    def draw_enemy(self):
        return self.enemy_group.draw(self.screen)

    def init_background(self, width, heigth):
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
        self.bricks_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        #self.screegn.blit(self.bg, self.bg_pos)

    def read_map(self):
        f = open('./assets/map.txt')
        self.map = f.readlines()
        for i in range(0, c.HEIGHT_ELEMENTS, 1):
            self.map[i] = self.map[i].split()

    def setup_background_elements(self):
        self.read_map()
        self.bg_elem_group = pygame.sprite.Group()
        self.bricks_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        for i in range(0, c.HEIGHT_ELEMENTS, 1):
            for j in range(0, c.WIDTH_ELEMENTS, 1):
                if self.map[i][j] == "1" or self.map[i][j] == "2" or self.map[i][j] == "3":
                    element = Collider(c.MULTIPLICATION*j, c.MULTIPLICATION*i, c.MULTIPLICATION, c.MULTIPLICATION)
                    self.bg_elem_group.add(element)

                elif self.map[i][j] == "4":
                    brick = Brick(c.MULTIPLICATION*j, c.MULTIPLICATION*i)
                    self.bricks_group.add(brick)

                elif self.map[i][j] == "5":
                    enemy = Enemy(c.MULTIPLICATION*j, c.MULTIPLICATION*i, c.RIGHT)
                    self.enemy_group.add(enemy)


        #enemy1 = Enemy(200, c.GROUND_HEIGHT, c.LEFT)
        #enemy2 = Enemy(300, c.GROUND_HEIGHT, c.RIGHT)
        #enemy3 = Enemy(1200, c.GROUND_HEIGHT, c.RIGHT)

        #self.enemy_group.add(enemy1, enemy2)

    def check_mario_collisions_x(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        brick = pygame.sprite.spritecollideany(self.mario, self.bricks_group)
        enemy = pygame.sprite.spritecollideany(self.mario, self.enemy_group)
        if bg_elem:
            self.mario_collisions_x(bg_elem)

        elif brick:
            self.mario_collisions_x(brick)

        elif enemy:
            self.mario_collisions_enemy_x(enemy)

        self.mario_falling()

    def mario_collisions_enemy_x(self, enemy):
        if self.mario.rect.x < enemy.rect.x or self.mario.rect.x+self.mario.rect.width < enemy.rect.x + enemy.rect.width:
            if not self.mario.is_big:
                self.mario.dead = True
            else:
                self.mario.is_big = False
                self.mario.rect.y -= 10
                self.mario.state = c.FALL

            print("Enemy killed mario")




    def mario_collisions_x(self, elements):
        if self.mario.rect.x < elements.rect.x:
            self.mario.rect.right = elements.rect.left
        else:
            self.mario.rect.left = elements.rect.right

        self.mario.vel[0] = 0



    def check_mario_collisions_y(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        brick = pygame.sprite.spritecollideany(self.mario, self.bricks_group)
        enemy = pygame.sprite.spritecollideany(self.mario, self.enemy_group)

        if bg_elem:
            self.mario_collisions_y(bg_elem)

        elif brick:
            self.mario_collisions_y(brick)

        elif enemy:
            self.mario_enemy_collisions_y(enemy)

    def mario_collisions_y(self, element):
        if element.rect.bottom > self.mario.rect.bottom  :
            self.mario.vel[1] = 0
            self.mario.rect.bottom = element.rect.top
            self.mario.state = c.WALK # zmien na fall!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        elif self.mario.rect.top > element.rect.top:
            self.mario.rect.top = element.rect.bottom
            element.rect.y += 400
            #self.mario.is_big = True
            self.mario.state = c.FALL
            print( "aaaaaaaa")

    def mario_enemy_collisions_y(self, enemy):
        if enemy.rect.bottom > self.mario.rect.bottom:
            self.mario.vel[1] = 0
            self.mario.rect.bottom = enemy.rect.top
            enemy.die()
            self.mario.rect.y -= 50
            self.mario.state = c.JUMP

        elif self.mario.rect.top > enemy.rect.top:
            self.mario.rect.top = enemy.rect.bottom
            self.mario.state = c.FALL


    def check_enemy_x_collisions(self, enemy):
        bg_elem = pygame.sprite.spritecollideany(enemy, self.bg_elem_group)
        #enemy_collider = pygame.sprite.spritecollideany(enemy, self.enemy_group)
        if bg_elem:
            if enemy.direction == c.RIGHT:
                enemy.rect.right = bg_elem.rect.left
                enemy.direction = c.LEFT
                enemy.vel[0] = -2
                #print("HALO")
            elif enemy.direction == c.LEFT:
                enemy.rect.left = bg_elem.rect.right
                enemy.direction = c.RIGHT
                enemy.vel[0] = 2
                #print("HALO2")

    def update_background_elements(self):
        for element in self.bg_elem_group:
            element.rect.x += self.delta_x

        for brick in self.bricks_group:
            brick.rect.x += self.delta_x

        for enemy in self.enemy_group:
            self.check_enemy_x_collisions(enemy)
            enemy.rect.x += self.delta_x



        self.check_mario_collisions_y()
        self.check_mario_collisions_x()


    def check_mario_for_falling(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        brick = pygame.sprite.spritecollideany(self.mario, self.bricks_group)
        enemy = pygame.sprite.spritecollideany(self.mario, self.enemy_group)

        if bg_elem is None and brick is None and enemy is None:
            self.mario.state = c.FALL


    def mario_falling(self):
        self.mario.rect.y += 1
        test_collide_group = pygame.sprite.Group(self.bg_elem_group,
                                                 self.bricks_group, self.enemy_group)


        if pygame.sprite.spritecollideany(self.mario, test_collide_group) is None:
            if self.mario.state != c.JUMP:
                self.mario.state = c.FALL


        self.mario.rect.y -= 1



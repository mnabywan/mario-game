from Data import constants as c
from Data.collider import *
from Data.mario import Mario
from Data.brick import Brick
from Data.enemy import Enemy
from Data.box import Box
from Data.game_info import GameInfo
import os
from . import setup

#na nastepnych zajeciach prezentacje mamy mieć że w miarę dziala albo ukryte niedorobki
#za nastepne 2 tygodnie oddawanie do prowadzacego
#12 min na pokazanie

class Level1:
    def __init__(self, game, width, heigth):
        self.game = game
        self.mario = Mario(self.game)
        self.game_info = GameInfo(self.game)
        self.init_background(width, heigth)

    def move_mario(self):
        return self.mario.handle_state()

    def move_enemy(self):
        for enemy in self.enemy_group:
            if not enemy.dead:
                enemy.move()
            else:
                enemy.die()


    def move_powrup(self):
        for powerup in self.powerup_group:
            powerup.move()

    def draw_mario(self):
        return self.mario.draw()

    def draw_enemy(self):
        return self.enemy_group.draw(self.screen)

    def draw_game_info(self):
        return self.game_info.print_game_info()

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
        self.box_group.draw(self.screen)
        self.powerup_group.draw(self.screen)
        self.coin_group.draw(self.screen)

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
        self.box_group = pygame.sprite.Group()
        self.powerup_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()


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

                elif self.map[i][j] == "6":
                    box = Box(c.MULTIPLICATION*j, c.MULTIPLICATION*i, c.MUSHROOM, self.powerup_group, True)
                    self.box_group.add(box)

                elif self.map[i][j] == "7":
                    box = Box(c.MULTIPLICATION*j, c.MULTIPLICATION*i, c.COIN, self.coin_group, True)
                    self.box_group.add(box)
                elif self.map[i][j] == "8":
                    box = Box(c.MULTIPLICATION * j, c.MULTIPLICATION * i, c.MUSHROOM, self.powerup_group, False)
                    self.box_group.add(box)
                elif self.map[i][j] == "9":
                    brick = Brick(c.MULTIPLICATION*j, c.MULTIPLICATION*i)
                    self.bricks_group.add(brick)

        #enemy1 = Enemy(200, c.GROUND_HEIGHT, c.LEFT)
        #enemy2 = Enemy(300, c.GROUND_HEIGHT, c.RIGHT)
        #enemy3 = Enemy(1200, c.GROUND_HEIGHT, c.RIGHT)

        #self.enemy_group.add(enemy1, enemy2)



    def check_mario_collisions_x(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        brick = pygame.sprite.spritecollideany(self.mario, self.bricks_group)
        enemy = pygame.sprite.spritecollideany(self.mario, self.enemy_group)
        box = pygame.sprite.spritecollideany(self.mario, self.box_group)
        powerup = pygame.sprite.spritecollideany(self.mario, self.powerup_group)
        coin = pygame.sprite.spritecollideany(self.mario, self.coin_group)

        if bg_elem:
            self.mario_collisions_x(bg_elem)

        elif brick:
            self.mario_collisions_x(brick)
            self.mario.can_jump = False

        elif enemy:
            self.mario_collisions_enemy_x(enemy)

        elif box:
            pass     #TODO

        elif powerup:
            self.mario_collisions_powerup_x(powerup)

        elif not bg_elem and not box and not brick and not powerup and not enemy:
            self.mario.can_jump = True


        self.mario_falling()

    def mario_collisions_enemy_x(self, enemy):
        if self.mario.rect.x < enemy.rect.x or self.mario.rect.x+self.mario.rect.width < enemy.rect.x + enemy.rect.width:
            if not self.mario.is_big:
                self.mario.lives -= 1
            else:
                self.mario.big_to_small(enemy.rect.x , enemy.rect.bottom)
                self.mario.rect.y -= 30
                self.mario.state = c.FALL

            print("Enemy killed mario")


    def mario_collisions_powerup_x(self, powerup):
        if self.mario.rect.x < powerup.rect.x or self.mario.rect.x + self.mario.rect.width < powerup.rect.x + powerup.rect.width:
            if not self.mario.is_big:
                self.mario.small_to_big(powerup.rect.x, powerup.rect.bottom)
                self.check_mario_collisions_y()
                self.check_mario_collisions_x()
                powerup.kill()




    def mario_collisions_x(self, elements):
        if self.mario.rect.x < elements.rect.x:
            self.mario.rect.right = elements.rect.left
        else:
            self.mario.rect.left = elements.rect.right

        self.mario.vel[0] = 0
        self.mario.vel[1] = 0 #proba



    def check_mario_collisions_y(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        brick = pygame.sprite.spritecollideany(self.mario, self.bricks_group)
        enemy = pygame.sprite.spritecollideany(self.mario, self.enemy_group)
        box = pygame.sprite.spritecollideany(self.mario, self.box_group)

        brick, box = self.prevent_collision_conflict(brick, box)

        if bg_elem:
            self.mario_bg_collisions_y(bg_elem)

        elif brick:
            self.mario_brick_collisions_y(brick)

        elif enemy:
            self.mario_enemy_collisions_y(enemy)

        elif box:
            self.mario_box_collisions_y(box)

    def mario_bg_collisions_y(self, element):
        if element.rect.bottom > self.mario.rect.bottom:
            self.mario.vel[1] = 0
            self.mario.rect.bottom = element.rect.top
            self.mario.state = c.WALK

        elif self.mario.rect.top > element.rect.top:
            self.mario.rect.top = element.rect.bottom
            #self.mario.is_big = True
            self.mario.state = c.FALL




    def mario_brick_collisions_y(self, brick):
        if brick.rect.bottom > self.mario.rect.bottom:
            self.mario.vel[1] = 0
            self.mario.rect.bottom = brick.rect.top
            self.mario.state = c.WALK

        elif self.mario.rect.top > brick.rect.top:
            self.mario.rect.top = brick.rect.bottom
            if self.mario.is_big:
                brick.kill()
            else:
                print("ala")

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

    def mario_box_collisions_y(self, box):
        if box.rect.bottom > self.mario.rect.bottom:
            self.mario.vel[1] = 0
            self.mario.rect.bottom = box.rect.top
            self.mario.state = c.WALK

        elif self.mario.rect.top > box.rect.top:
            self.mario.rect.top = box.rect.bottom
            if not box.is_bumped and box.content == c.MUSHROOM:
                print("was not bumped")
                box.bump()
            elif not box.is_bumped and box.content == c.COIN:
                box.bump()
            else:
                print("was bumped")


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



    def check_enemy_y_collisions(self, enemy):
        bg_elem = pygame.sprite.spritecollideany(enemy, self.bg_elem_group)
        box = pygame.sprite.spritecollideany(enemy, self.box_group)
        brick = pygame.sprite.spritecollideany(enemy, self.bricks_group)



        if bg_elem:
            self.enemy_collisions_y(enemy, bg_elem)
            #print("kol")

        elif box:
            self.enemy_collisions_y(enemy, box)
            #print("kol_box")


        elif brick:
            self.enemy_collisions_y(enemy, brick)
            #print("kol_brick")


        elif not bg_elem and not box and not brick:
            print("NIE MA kolizji")
            #powerup.rect.x += 2
            #powerup.rect.y += 2

    def enemy_collisions_y(self, enemy ,element):
        if element.rect.bottom > enemy.rect.bottom:
            enemy.vel[1] = 0
            enemy.rect.bottom = element.rect.top

        elif enemy.rect.top > element.rect.top:
            enemy.rect.top = element.rect.bottom
            #self.mario.is_big = True

    def update_background_elements(self):
        for element in self.bg_elem_group:
            element.rect.x += self.delta_x

        for brick in self.bricks_group:
            brick.rect.x += self.delta_x

        for enemy in self.enemy_group:
            self.check_enemy_x_collisions(enemy)
            enemy.rect.y += 2
            self.check_enemy_y_collisions(enemy) #TODO
            enemy.rect.x += self.delta_x

        for box in self.box_group:
            box.rect.x += self.delta_x

        for coin in self.coin_group:
            coin.rect.x += self.delta_x
            coin.update()

        for powerup in self.powerup_group:
            self.check_mushroom_x_collisions(powerup)
            powerup.rect.y += 2
            self.check_mushroom_y_collisions(powerup)
            powerup.rect.y -= powerup.vel[1]
            powerup.rect.x += self.delta_x

        self.check_mario_collisions_y()
        self.check_mario_collisions_x()

    def check_mario_for_falling(self):
        bg_elem = pygame.sprite.spritecollideany(self.mario, self.bg_elem_group)
        brick = pygame.sprite.spritecollideany(self.mario, self.bricks_group)
        enemy = pygame.sprite.spritecollideany(self.mario, self.enemy_group)
        box = pygame.sprite.spritecollideany(self.mario, self.box_group)

        if bg_elem is None and brick is None and enemy is None and box is None:
            self.mario.state = c.FALL

    def mario_falling(self):
        self.mario.rect.y += 1
        test_collide_group = pygame.sprite.Group(self.bg_elem_group, self.bricks_group, self.enemy_group, self.box_group)

        if pygame.sprite.spritecollideany(self.mario, test_collide_group) is None:
            if self.mario.state != c.JUMP:
                self.mario.gravity = c.GRAVITY
                self.mario.vel[1] = self.mario.max_y_vel
                self.mario.state = c.FALL

        self.mario.rect.y -= 1

    def check_mushroom_x_collisions(self, powerup):
        bg_elem = pygame.sprite.spritecollideany(powerup, self.bg_elem_group)
        box = pygame.sprite.spritecollideany(powerup, self.box_group)
        brick = pygame.sprite.spritecollideany(powerup, self.bricks_group)

        if bg_elem:
            self.mushroom_collisions_x(powerup, bg_elem)

        elif box:
            self.mushroom_collisions_x(powerup, box)

        elif brick:
            self.mushroom_collisions_x(powerup, brick)

    def mushroom_collisions_x(self,powerup, element):

            if powerup.direction == c.RIGHT:
                powerup.rect.right = element.rect.left
                powerup.direction = c.LEFT
                powerup.vel[0] = -2

            elif powerup.direction == c.LEFT:
                powerup.rect.left = element.rect.right
                powerup.direction = c.RIGHT
                powerup.vel[0] = 2

    def check_mushroom_y_collisions(self, powerup):
        bg_elem = pygame.sprite.spritecollideany(powerup, self.bg_elem_group)
        box = pygame.sprite.spritecollideany(powerup, self.box_group)
        brick = pygame.sprite.spritecollideany(powerup, self.bricks_group)

        if bg_elem:
            self.mushroom_collisions_y(powerup, bg_elem)
            #print("kol")

        elif box:
            self.mushroom_collisions_y(powerup, box)
            #print("kol_box")

        elif brick:
            self.mushroom_collisions_y(powerup, brick)
            #print("kol_brick")

        elif not bg_elem and not box and not brick:
            print("NIE MA kolizji")
            #powerup.rect.x += 2
            #powerup.rect.y += 2

    def mushroom_collisions_y(self, powerup ,element):
        if element.rect.bottom > powerup.rect.bottom:
            powerup.vel[1] = 0
            powerup.rect.bottom = element.rect.top

        elif powerup.rect.top > element.rect.top:
            powerup.rect.top = element.rect.bottom
            #self.mario.is_big = True



    def prevent_collision_conflict(self, obstacle1, obstacle2):
        """Allows collisions only for the item closest to marios centerx"""
        if obstacle1 and obstacle2:
            obstacle1_distance = self.mario.rect.centerx - obstacle1.rect.centerx
            if obstacle1_distance < 0:
                obstacle1_distance *= -1
            obstacle2_distance = self.mario.rect.centerx - obstacle2.rect.centerx
            if obstacle2_distance < 0:
                obstacle2_distance *= -1

            if obstacle1_distance < obstacle2_distance:
                obstacle2 = False
            else:
                obstacle1 = False

        return obstacle1, obstacle2
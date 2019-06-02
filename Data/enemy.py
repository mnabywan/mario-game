import pygame
from . import constants as c
from . import setup

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        self.sprite_sheet = setup.GFX['enemies1']

        #self.x_acc = 0.15

        pygame.sprite.Sprite.__init__(self)

        self.images = []
        self.load_images_from_sheet()
        self.frame_index = 0
        self.direction = direction
        self.wait_before_death = 20
        self.dead = False
        self.falling = False

        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.initial_vel()
        self.rect.x = x
        self.rect.y = y
        self.r = 0


        self.mask = pygame.mask.from_surface(self.image)
        #self.state = c.WALK

    def initial_vel(self):
        if self.direction == c.LEFT:
            self.vel = [-2,0]
        else:
            self.vel = [2,0]

    def load_images_from_sheet(self):
        self.images.append(self.get_image(0, 4, 16, 16))
        self.images.append(self.get_image(30, 4, 16, 16))
        self.images.append(self.get_image(61, 0, 16, 16))
        self.images.append(pygame.transform.flip(self.images[1], False, True)) #w lewo


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pygame.Surface([width, height])
        rect = image.get_rect()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pygame.transform.scale(image,
                                   (int(rect.width)*2,
                                    int(rect.height)*2))
        return image

    def move(self):
        if not self.dead:
            if self.direction == c.LEFT:
                self.vel = [-2,0]
            else:
                self.vel = [2,0]

            self.rect.x += self.vel[0]
            ##self.rect.y += 2
            if not self.falling:
                self.r += self.vel[0]
            if self.r <= -120:
                self.direction = c.RIGHT
            if self.r >= 120:
                self.direction = c.LEFT

        if self.dead:
            self.kill()

    def die(self):
        self.dead = True
        self.frame_index = 2
        self.vel = [0, 0]
        self.image = self.images[self.frame_index]
        self.wait_before_death -= 1
        if self.wait_before_death == 0:
            self.kill()


    def draw(self):
        self.enemy_group.draw(self.game.level.screen)


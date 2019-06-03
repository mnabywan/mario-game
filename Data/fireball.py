import pygame
from . import constants as c
from . import setup

class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, group, direction):
        self.sprite_sheet = setup.GFX['objects']

        pygame.sprite.Sprite.__init__(self)

        self.images = []
        self.load_images_from_sheet()
        self.frame_index = 0
        self.direction = direction

        self.dead = False
        self.go_down = True

        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.initial_vel()
        self.rect.x = x
        self.rect.y = y

        self.mask = pygame.mask.from_surface(self.image)
        self.group = group
        #self.state = c.WALK

    def initial_vel(self):
        if self.direction == c.LEFT:
            self.vel = [-4,3]
        else:
            self.vel = [4,3]

    def load_images_from_sheet(self):
        self.images.append(self.get_image(96, 144, 8, 8))


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
            if self.direction == c.RIGHT and self.go_down:
                self.vel = [15, 13]
            elif self.direction == c.RIGHT and not self.go_down:
                self.vel = [15, -13]

            elif self.direction == c.LEFT and self.go_down:
                self.vel = [-15, 13]
            elif self.direction == c.LEFT and not self.go_down:
                self.vel = [-15, -13]

            self.rect.x += self.vel[0]
            self.rect.y += self.vel[1]

        if self.dead:
            self.kill()


    def draw(self):
        self.group.draw(self.game.level.screen)


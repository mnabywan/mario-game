import pygame
from . import setup
from . import constants as c
from . import powerup
from . import coin

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y,  content, group):
        self.sprite_sheet = setup.GFX['tiles']
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.load_images_from_sheet()

        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rest_height = y
        self.gravity = 1.2

        self.is_bumped = False
        self.vel = [0,0]

        self.mask = pygame.mask.from_surface(self.image)

        self.content = content
        self.group = group

    def load_images_from_sheet(self):
        """Create frame list"""
        self.images.append(
            self.get_image(384, 0, 16, 16))
        self.images.append(
            self.get_image(400, 0, 16, 16))
        self.images.append(
            self.get_image(416, 0, 16, 16))
        self.images.append(
            self.get_image(432, 0, 16, 16))




    def get_image(self, x, y, width, height):
        """Extract image from sprite sheet"""
        image = pygame.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        image = pygame.transform.scale(image,
                                   (int(rect.width*2),
                                    int(rect.height*2)))
        return image

    def bump(self):
        self.is_bumped = True
        if self.content == c.MUSHROOM:
            self.group.add(powerup.Mushroom(self.rect.x, self.rect.y - c.MULTIPLICATION ))

        if self.content == c.COIN:
            self.group.add(coin.Coin(self.rect.x, self.rect.y - c.MULTIPLICATION))

        self.frame_index = 3
        self.image = self.images[self.frame_index]


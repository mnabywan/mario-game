import pygame
from . import setup
from . import constants as c

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.sprite_sheet = setup.GFX['objects']
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.load_images_from_sheet()

        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x + 5
        self.rect.y = y
        self.start_y = y
        self.mask = pygame.mask.from_surface(self.image)



    def load_images_from_sheet(self):
        self.images.append(self.get_image(52, 113, 8, 14))
        self.images.append(self.get_image(4, 113, 8, 14))
        self.images.append(self.get_image(20, 113, 8, 14))
        self.images.append(self.get_image(36, 113, 8, 14))



    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pygame.Surface([width, height])
        rect = image.get_rect()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pygame.transform.scale(image,
                                   (int(rect.width*2),
                                    int(rect.height*2)))
        return image

    def update(self):
        self.rect.y -= 1
        self.image = self.images[self.frame_index]
        self.mask = pygame.mask.from_surface(self.image)
        if (self.start_y - self.rect.y) % 10 == 0:
            self.frame_index += 1
        if self.frame_index == 4:
            self.kill()


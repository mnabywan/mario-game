import pygame
from . import constants as c
from . import setup

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.sprite_sheet = setup.GFX['enemies1']
        self.game = game
        #self.x_acc = 0.15

        pygame.sprite.Sprite.__init__(self)

        self.images = []
        self.load_images_from_sheet()
        self.frame_index = 1


        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y

        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self)

        self.mask = pygame.mask.from_surface(self.image)
        self.state = c.WALK



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
        self.vel = [2,2]
        self.move_right = True

        '''
        if self.rect.x == 800 and self.move_right == True:
            self.move_right = False
            self.rect.x -= self.vel[0]
        elif self.rect.x < 20 and self.move_right == False:
            self.move_right == True
            self.rect.x += self.vel[0]
        elif self.move_right :
            self.rect.x += self.vel[0]
            print("W prawo")
        elif self.move_right == False :
            self.rect.x -= self.vel[0]
            print("W lewo")
        '''

    def draw(self):
        self.enemy_group.draw(self.game.level.screen)
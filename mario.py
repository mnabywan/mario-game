import pygame
from pygame.math import Vector2


class Mario(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.width = 32
        self.height = 64
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = game.screen_height - self.height - 50
        self.mario_group = pygame.sprite.Group()
        self.mario_group.add(self)
        self.setup_movement()
        self.y = game.screen_height - self.height - 50

    def setup_movement(self):
        self.coordinate_x = self.rect.x
        self.coordinate_y = self.rect.y  # zawsze, wiec jest niepotrzebna
        self.speed = 10
        self.vel = [0, 0]
        self.isJump = False
        self.jumpCount = 10
        self.inthemiddle = False

    def move(self):
        pressed = pygame.key.get_pressed()
        self.vel = [0, 0]

        if pressed[pygame.K_RIGHT] and self.coordinate_x < self.game.level.level_width - self.width - self.vel[0]:

            self.vel[0] = self.speed
            self.coordinate_x += self.vel[0]
            self.inthemiddle = True
            if self.coordinate_x >= self.game.level.level_width - self.game.screen_width * 0.5 or self.rect.x < self.game.screen_width * 0.5 - \
                    self.vel[0]:
                self.rect.x += self.vel[0]
                self.inthemiddle = False
        if pressed[pygame.K_LEFT] and self.rect.x > self.vel[0]:
            self.vel = [-self.speed, 0]
            self.inthemiddle = False
            self.rect.x += self.vel[0]
            self.coordinate_x += self.vel[0]

        if not (self.isJump):

            # if pressed[pygame.K_UP] and self.y > self.vel:
            #    self.y -= self.vel
            #    #self.add_force(Vector2(0,-self.speed))

            if pressed[pygame.K_DOWN] and self.y < self.game.screen_height - self.height - self.vel[1]:
                self.vel[1] += self.speed
                self.y += self.vel[1]
            #     self.add_force(Vector2(0,self.speed))

            if pressed[pygame.K_UP]:
                self.isJump = True

        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1

            else:
                self.isJump = False
                self.jumpCount = 10
        # self.y += 5
        print(self.coordinate_x)
        print(self.rect.y)

    def draw(self):
        # self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # pygame.draw.rect(self.game.level.screen, (255, 0, 0), self.rect)
        self.rect.y = self.y
        self.mario_group.draw(self.game.level.screen)

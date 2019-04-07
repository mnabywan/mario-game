import pygame


class Mario(object):

    def __init__(self, game):
        self.game = game

        self.ground_level = 95
        size = self.game.screen.get_size()



        self.width = 30
        self.height = 50
        self.x = 0
        self.y = game.screen_height - self.height - self.ground_level
        self.speed = 1.0
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.onGround = True



    def draw(self):
        rect =  pygame.Rect(self.x,self.y, self.width, self.height)
        pygame.draw.rect(self.game.screen, (255,0,0),rect)


    def move(self):
        pressed = pygame.key.get_pressed()


        if pressed[pygame.K_RIGHT] and self.x < self.game.screen_width - self.width - self.vel:
            self.x += self.vel

        if pressed[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel

        if not(self.isJump):

            if pressed[pygame.K_x]:
                self.isJump = True

        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -=1

            else:
                self.isJump = False
                self.jumpCount = 10



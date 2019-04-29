import pygame
from Data import setup, constants as c


class Mario(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['mario_bros']

        self.game = game

        #self.setup_timers() #TO DO
        #self.setup_states() #TO DO
        self.setup_movement()  #TO DO
        #self.setup_counters()  #TO DO
        self.load_images_from_sheet()


        self.state = c.WALK
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


        self.key_timer = 0

        #self.width = c.MARIO_WIDTH
        #self.height = c.MARIO_HEIGHT
        #self.image = pygame.Surface((self.width, self.height))
        #self.image.fill(c.RED)
        #self.rect = self.image.get_rect()
        #self.rect.x = 0
        #self.rect.y = game.screen_height - self.height - 50
        #self.mario_group = pygame.sprite.Group()
        #self.mario_group.add(self)
        #self.setup_movement()
        #self.y = game.screen_height - self.height - 50

    def setup_movement(self):
        self.coordinate_x = self.rect.x
        self.coordinate_y = self.rect.y  # zawsze, wiec jest niepotrzebna
        self.speed = 5
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

            #if pressed[pygame.K_DOWN] and self.y < self.game.screen_height - self.height - self.vel[1]:
            #    self.vel[1] += self.speed
            #    self.y += self.vel[1]
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

    def load_images_from_sheet(self):
        """To extract images from sheet and add them to properly lists"""
        self.right_small_frames = []
        self.left_small_frames = []

        self.right_big_frames = []
        self.left_big_frames = []

        self.right_fire_frames = []
        self.left_fire_frames = []

        self.right_small_frames.append(
            self.get_image(178, 32, 12, 16))  # Right [0]
        self.right_small_frames.append(
            self.get_image(80,  32, 15, 16))  # Right walking 1 [1]
        self.right_small_frames.append(
            self.get_image(96,  32, 16, 16))  # Right walking 2 [2]
        self.right_small_frames.append(
            self.get_image(112,  32, 16, 16))  # Right walking 3 [3]
        self.right_small_frames.append(
            self.get_image(144, 32, 16, 16))  # Right jump [4]
        self.right_small_frames.append(
            self.get_image(130, 32, 14, 16))  # Right skid [5]
        self.right_small_frames.append(
            self.get_image(160, 32, 15, 16))  # Death frame [6]
        self.right_small_frames.append(
            self.get_image(320, 8, 16, 24))  # Transition small to big [7]
        self.right_small_frames.append(
            self.get_image(241, 33, 16, 16))  # Transition big to small [8]
        self.right_small_frames.append(
            self.get_image(194, 32, 12, 16))  # Frame 1 of flag pole Slide [9]
        self.right_small_frames.append(
            self.get_image(210, 33, 12, 16))  # Frame 2 of flag pole slide [10]


        self.right_big_frames.append(
            self.get_image(176, 0, 16, 32))  # Right standing [0]
        self.right_big_frames.append(
            self.get_image(81, 0, 16, 32))  # Right walking 1 [1]
        self.right_big_frames.append(
            self.get_image(97, 0, 15, 32))  # Right walking 2 [2]
        self.right_big_frames.append(
            self.get_image(113, 0, 15, 32))  # Right walking 3 [3]
        self.right_big_frames.append(
            self.get_image(144, 0, 16, 32))  # Right jump [4]
        self.right_big_frames.append(
            self.get_image(128, 0, 16, 32))  # Right skid [5]
        self.right_big_frames.append(
            self.get_image(336, 0, 16, 32))  # Right throwing [6]
        self.right_big_frames.append(
            self.get_image(160, 10, 16, 22))  # Right crouching [7]
        self.right_big_frames.append(
            self.get_image(272, 2, 16, 29))  # Transition big to small [8]
        self.right_big_frames.append(
            self.get_image(193, 2, 16, 30))  # Frame 1 of flag pole slide [9]
        self.right_big_frames.append(
            self.get_image(209, 2, 16, 29))  # Frame 2 of flag pole slide [10]

    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pygame.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pygame.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image



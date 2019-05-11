import pygame
from Data import setup, constants as c


class Mario(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['mario_bros']
        self.game = game
        self.x_acc = 0.15

        self.setup_timers()
        self.setup_states()
        self.setup_counters()
        self.setup_movement()
        self.load_images_from_sheet()

        self.state = c.STAND
        self.image = self.right_small_frames[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.coordinate_x = self.rect.x
        self.coordinate_y = self.rect.y  # zawsze, wiec jest niepotrzebna

        self.key_timer = 0

        self.rect.x = 0
        self.rect.bottom = c.GROUND_HEIGHT
        print(self.rect.width)

        self.mario_group = pygame.sprite.Group()
        self.mario_group.add(self)


        self.y = game.screen_height - c.GROUND_HEIGHT

    def standing(self):
        pressed = pygame.key.get_pressed()
        self.frame_index = 0
        self.vel = [0, 0]

        if pressed[pygame.K_RIGHT]:
            self.facing_right = True
            self.state = c.WALK
        elif pressed[pygame.K_LEFT]:
            self.facing_right = False
            self.state = c.WALK
        elif pressed[pygame.K_UP]:
            self.state = c.JUMP
            self.vel[1] = c.JUMP_VEL
        else:
            self.state = c.STAND

        # self.image = self.right_big_frames[self.frame_index]

    def walking(self):
        self.vel[1] = c.JUMP_VEL
        if self.frame_index < 3:
            self.frame_index = 0
        else:
            self.frame_index = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and self.coordinate_x < self.game.level.level_width - self.rect.width - self.vel[0]:

            self.vel[0] = self.speed
            self.coordinate_x += self.vel[0]
            self.in_the_middle = True
            if self.coordinate_x >= self.game.level.level_width - self.game.screen_width * 0.5 or self.rect.x < self.game.screen_width * 0.5 - \
                    self.vel[0]:
                self.rect.x += self.vel[0]
                self.in_the_middle = False
        if pressed[pygame.K_LEFT] and self.rect.x > self.vel[0]:
            self.vel[0] = -self.speed
            self.in_the_middle = False
            self.facing_right = False
            self.rect.x += self.vel[0]
            self.coordinate_x += self.vel[0]

        if (pressed[pygame.K_UP]):
            self.state = c.JUMP

        elif (not pressed[pygame.K_UP]) or (not pressed[pygame.K_LEFT]) or (not pressed[pygame.K_RIGHT]):
            self.state = c.STAND

        # if (self.is_big):
        #    self.image = self.right_big_frames[self.frame_index]
        # else:
        #    self.image = self.right_big_frames[self.frame_index]

    def jumping(self):
        pressed = pygame.key.get_pressed()
        self.frame_index = 4
        self.gravity = c.JUMP_GRAVITY
        self.vel[1] += self.gravity

        self.state = c.FALL
        if self.vel[1] >= 0 and self.vel[1] < self.max_y_vel:
            self.gravity = c.GRAVITY  # bylo same gravity #ok
            self.state = c.FALL
            self.state = c.FALL

        if pressed[pygame.K_RIGHT] and self.coordinate_x < self.game.level.level_width - self.rect.width - self.vel[
            0]:  # zmina z self.width na self.rect.widt

            self.vel[0] = self.speed
            # self.vel[0] += self.x_acc
            self.coordinate_x += self.vel[0]
            self.in_the_middle = True
            if self.coordinate_x >= self.game.level.level_width - self.game.screen_width * 0.5 or self.rect.x < self.game.screen_width * 0.5 - \
                    self.vel[0]:
                self.rect.x += self.vel[0]
                self.in_the_middle = False
        if pressed[pygame.K_LEFT] and self.rect.x > self.vel[0]:
            self.vel[0] = -self.speed
            # self.vel[0] -= self.x_acc
            self.in_the_middle = False
            self.rect.x += self.vel[0]
            self.coordinate_x += self.vel[0]

        if pressed[pygame.K_UP]:
            # self.gravity = c.GRAVITY
            self.state = c.JUMP

        #       self.image = self.right_big_frames[self.frame_index]
        # self.rect.x += self.vel[0]
        # self.rect.x += self.vel[0]
        # self.coordinate_x += self.vel[0]
        self.rect.y += self.vel[1]

    def falling(self):
        self.check_for_death_jump()
        pressed = pygame.key.get_pressed()
        self.vel[1] += self.gravity

        if self.vel[0] > 0 and self.coordinate_x < self.game.level.level_width - self.rect.width - self.vel[
            0]:  # zmiana z self.width na self.rect.width

            self.vel[0] = self.speed
            self.coordinate_x += self.vel[0]
            self.in_the_middle = True
            if self.coordinate_x >= self.game.level.level_width - self.game.screen_width * 0.5 or self.rect.x < self.game.screen_width * 0.5 - \
                    self.vel[0]:
                self.rect.x += self.vel[0]
                self.in_the_middle = False
        elif self.vel[0] < 0 and self.rect.x > self.speed:
            self.vel[0] = -self.speed
            self.in_the_middle = False
            self.rect.x += self.vel[0]
            self.coordinate_x += self.vel[0]

        if self.vel[1] < c.MAX_Y_VEL:
            self.vel[1] += self.gravity

        if pressed[pygame.K_LEFT]:
            self.vel[0] -= self.speed
        #
        elif pressed[pygame.K_RIGHT]:
            self.vel[0] += self.speed

        # self.rect.x += self.vel[0]
        # self.coordinate_x += self.vel[0]
        self.rect.y += self.vel[1]

        # if pressed[pygame.K_LEFT]:
        #   self.vel[0] -= self.speed

        # elif pressed[pygame.K_RIGHT]:
        #   self.vel[0] += self.speed

    def check_for_death_jump(self):
        if self.rect.y >= self.game.screen_height - self.rect.height - 10:
            self.rect.y = self.game.screen_height - self.rect.height - 10
            print("Death fall")
            self.frame_index = 0
            self.dead = True

    def draw(self):
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
            self.get_image(80, 32, 15, 16))  # Right walking 1 [1]
        self.right_small_frames.append(
            self.get_image(96, 32, 16, 16))  # Right walking 2 [2]
        self.right_small_frames.append(
            self.get_image(112, 32, 16, 16))  # Right walking 3 [3]
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

        for frame in self.right_small_frames:
            new_frame = pygame.transform.flip(frame, True, False)
            self.left_small_frames.append(new_frame)


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

        for frame in self.right_big_frames:
            new_frame = pygame.transform.flip(frame, True, False)
            self.left_big_frames.append(new_frame)


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pygame.Surface([width, height])
        rect = image.get_rect()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pygame.transform.scale(image,
                                       (int(rect.width * c.MARIO_SIZE_MULTIPLIER),
                                        int(rect.height * c.MARIO_SIZE_MULTIPLIER)))
        return image

    def setup_movement(self):
        self.vel = [0, 0]
        self.speed = 5
        self.gravity = c.GRAVITY
        self.max_y_vel = c.MAX_Y_VEL

    def setup_counters(self):
        self.frame_index = 0  # informs which frame we show on screen

    def setup_timers(self):
        self.walking_timer = 0

    def setup_states(self):
        'sets up states to affect to mario behaviour'
        self.facing_right = True
        self.is_big = False
        self.in_the_middle = False
        self.allow_jump = True
        self.dead = False
        self.fire = False

    def handle_state(self):
        """Determines Mario's behavior based on his state"""
        if self.state == c.STAND:
            self.standing()
        elif self.state == c.WALK:
            self.walking()
        elif self.state == c.JUMP:
            self.jumping()
        elif self.state == c.FALL:
            self.falling()
        self.actualise_image()


    def actualise_image(self):
        if not self.is_big:
            if self.facing_right:
                self.image = self.right_small_frames[self.frame_index]

            else:
                self.image = self.left_small_frames[self.frame_index]

        else:
            if self.facing_right:
                self.image = self.right_big_frames[self.frame_index]

            else:
                self.image = self.left_big_frames[self.frame_index]

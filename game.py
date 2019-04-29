import pygame, sys
import constants as c
from mario import Mario
from brick import Brick
from level1 import Level1
from collider import Map



class Game(object):

    def redraw(self):
        self.level.screen.fill(c.BLACK)
        self.draw()
        pygame.display.flip()

    def __init__(self):
        # Config tps
        self.tps_max = c.TPS_MAX

        # init
        pygame.init()
        self.screen_height = c.SCREEN_HEIGHT
        self.screen_width = c.SCREEN_WIDTH

        self.mario = Mario(self)
        self.level = Level1(self, self.screen_width, self.screen_height)

        #self.bg = pygame.image.load('/home/mateusz/PycharmProjects/Mario/graphics/bg.jpg')
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        #self.brick1 = Brick(self, 120, 140)

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # Drawing
            self.redraw()

    def tick(self):
        self.mario.move()

    def draw(self):
        self.level.draw_background()
        self.mario.draw()



if __name__ == "__main__":
    Game()

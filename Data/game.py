from Data.level1 import Level1
from Data import constants as c
import pygame,sys,os
import Data.tools

class Game(object):
    def redraw(self):
        self.level.screen.fill(c.BLACK)
        self.draw()
        pygame.display.flip()

    def __init__(self):
        # Config tps
        self.tps_max = c.TPS_MAX
        self.GFX = Data.tools.load_all_gfx(os.path.join("graphics"))
        # init
        pygame.init()
        self.screen_height = c.SCREEN_HEIGHT
        self.screen_width = c.SCREEN_WIDTH

        self.level = Level1(self, self.screen_width, self.screen_height)

        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0


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


from Data.level1 import Level1
from Data import constants as c
import pygame, sys, os
import Data.tools


#najwazniejsze dodać zabijanie przeciwnikow + kolizje z otoczeniem

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
        self.screen = pygame.display.get_surface()
        self.level = Level1(self, self.screen_width, self.screen_height)

        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        while self.level.mario.alive():
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

        if not self.level.mario.alive():
            input("Want to play one more time? Enter - yes, Escape - no")

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_KP_ENTER]:
            print("Pressed")

        elif pressed[pygame.K_ESCAPE]:
            sys.exit(0)


    def tick(self):
        #self.level.mario.move()
        self.level.move_mario()
        self.level.move_enemy()
        #if(self.level.mario.state == c.STAND):
        #    print("stand")
        #elif(self.level.mario.state == c.WALK):
        #    print("walk")
        #elif(self.level.mario.state == c.JUMP):
        #    print("jump")
        #elif(self.level.mario.state == c.FALL):
        #    print("fall")

    def draw(self):
        self.level.draw_background()
        self.level.draw_mario()

    def load_all_gfx(directory, colorkey=(255, 0, 255), accept=('.png', 'jpg', 'bmp')):
        graphics = {}
        for pic in os.listdir(directory):
            name, ext = os.path.splitext(pic)
            if ext.lower() in accept:
                img = pygame.image.load(os.path.join(directory, pic))
                if img.get_alpha():
                    img = img.convert_alpha()
                else:
                    img = img.convert()
                    img.set_colorkey(colorkey)
                graphics[name] = img
        return graphics



if __name__ == "__main__":
    Game()


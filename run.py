import pygame, sys
from mario import Mario


class Game(object):

    def redraw(self):
        self.screen.blit(self.bg, (0,0))
        #self.screen.fill((0, 0, 0))
        self.draw()
        pygame.display.flip()


    def __init__(self):
        # cONFIG
        self.tps_max = 70.0

        #init
        pygame.init()
        self.screen_height = 601
        self.screen_width = 1641
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg = pygame.image.load('/home/mateusz/PycharmProjects/Mario/graphics/bg.jpg')
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.mario = Mario(self)



        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key ==  pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            #Drawing
            self.redraw()


    def tick(self):
        self.mario.move()

    def draw(self):
        self.mario.draw()
        


if __name__ == "__main__":
    Game()

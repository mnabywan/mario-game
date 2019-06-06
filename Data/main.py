

# from . import setup,tools
# from states import main_menu,load_screen,level1
# from . import constants as c

from Data.game import Game
from Data import constants as c
import pygame, sys


game_state = c.START

def main():
    """Add states to control here."""
    #game_state = c.START
    game = Game()
    while 1:
        handle_game_states()
    #game.update()


class Main(object):
    def __init__(self):
        self.game_state = c.START
        self.game = 0

        while 1:
            handle_game_states(self)
            handle_pressed_key(self)


def handle_game_states(self):
    if self.game_state == c.START:
        if self.game == 0:
            self.game = Game() #TODO recreating a game??
            self.game.update()
        # font = pygame.font.SysFont(None, 45)
        # text = font.render("PRESS SPACE TO START ", True, c.WHITE)
        # self.game.screen.blit(text, (110, 110))
        print("START")

    elif self.game_state == c.PLAYING:
        self.game.game_state = c.PLAYING
        self.game.update()
        if not self.game.level.mario.alive() or self.game.level.game_info.time <= 1:
            self.game_state = c.GAMEOVER
        print("PLAYING")
        if self.game.level.mario_in_castle:
            self.game_state = c.WIN
    elif self.game_state == c.PAUSE:
        self.game.game_state = c.PAUSE
        # font = pygame.font.SysFont(None, 45)
        # text = font.render("PRESS SPACE TO CONTINUE ", True, c.WHITE)
        # self.game.screen.blit(text, (0, 0))
        print(self.game.level.game_info.time)
        print(self.game.counter)
        print("PAUSE")

    elif self.game_state == c.GAMEOVER:
        if self.game.game_state != c.GAMEOVER:
            self.game.game_state = c.GAMEOVER
            self.game.update()
            one_update_flag = False
    elif self.game_state == c.WIN:
        if self.game.game_state != c.WIN:
            self.game.game_state = c.WIN
            self.game.update()


# def handle_pressed_key(self):
#     pressed = pygame.key.get_pressed()
#     if pressed[pygame.K_SPACE]:
#         print("pressed!!!")
#         if self.game_state == c.PAUSE:
#             self.game_state = c.PLAYING
#
#         elif self.game_state == c.PLAYING:
#             self.game_state = c.PAUSE
#
#         elif self.game_state == c.GAMEOVER:
#             self.game_state = c.START
#
#         elif self.game_state == c.START:
#             self.game_state = c.PLAYING
#
#     elif pressed[pygame.K_ESCAPE]:
#         sys.exit(0)

def handle_pressed_key(self):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.game_state == c.PAUSE:
                    self.game_state = c.PLAYING

                elif self.game_state == c.PLAYING:
                    self.game.game_state = c.PAUSE
                    self.game.update(False)
                    self.game_state = c.PAUSE

                elif self.game_state == c.GAMEOVER:
                    self.game = 0
                    self.game_state = c.START

                elif self.game_state == c.WIN:
                    self.game = 0
                    self.game_state = c.START

                elif self.game_state == c.START:
                    self.game_state = c.PLAYING

            elif event.key == pygame.K_ESCAPE:
                sys.exit(0)


if __name__ == "__main__":
    Main()

    #run_it.setup_states(state_dict, c.MAIN_MENU)
   # control.main()
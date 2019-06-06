from Data.game import Game
from Data import constants as c
import pygame, sys


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
            self.game = Game()
            self.game.update()
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
        print(self.game.level.game_info.time)
        print(self.game.counter)
        print("PAUSE")

    elif self.game_state == c.GAMEOVER:
        if self.game.game_state != c.GAMEOVER:
            self.game.game_state = c.GAMEOVER
            self.game.update()
    elif self.game_state == c.WIN:
        if self.game.game_state != c.WIN:
            self.game.game_state = c.WIN
            self.game.update()

def handle_pressed_key(self):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.game_state == c.PAUSE:
                    self.game_state = c.PLAYING

                elif self.game_state == c.PLAYING:
                    self.game.game_state = c.PAUSE
                    self.game.update()
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


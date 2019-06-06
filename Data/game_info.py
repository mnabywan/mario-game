import pygame
from . import setup
from . import constants as c
from os import path

class GameInfo (pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.coins = 0
        self.score = 0

        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, c.BEST_SCORE_FILE), "r") as f:
            try:
                self.best_score = int(f.read())
            except:
                self.best_score = 0
        self.time = 200

    def print_coins(self):
        font = pygame.font.SysFont(None, 45)
        text = font.render("COINS " + str(self.coins), True, c.WHITE)
        self.game.screen.blit(text, (0, 0))

    def print_time(self):
        font = pygame.font.SysFont(None, 45)
        text = font.render("TIME "+ str(self.time), True, c.WHITE)
        self.game.screen.blit(text, (200, 0))

    def print_score(self):
        font = pygame.font.SysFont(None, 45)
        text = font.render("SCORE "+ str(self.score), True, c.WHITE)
        self.game.screen.blit(text, (400, 0))

    def print_best_score(self):
        font = pygame.font.SysFont(None, 45)
        text = font.render("BEST SCORE "+ str(self.best_score), True, c.WHITE)
        self.game.screen.blit(text, (400, 0))


    def print_start_msg(self):
        font = pygame.font.SysFont(None, 45)
        text = font.render("PRESS SPACE TO START ", True, c.WHITE)
        self.game.screen.blit(text, (300, 200))

    def print_pause_msg(self):
        font = pygame.font.SysFont(None, 45)
        text = font.render("PRESS SPACE TO CONTINUE THE GAME ", True, c.WHITE)
        self.game.screen.blit(text, (200, 200))

    def print_gameover_msg(self):
        font1 = pygame.font.SysFont(None, 45)
        font2 = pygame.font.SysFont(None, 65)
        font3 = pygame.font.SysFont(None, 30)
        text1 = font1.render("PRESS SPACE TO START A NEW GAME", True, c.WHITE)
        text2 = font2.render("GAME OVER", True, c.WHITE)
        text3 = font3.render("YOUR SCORE:  " + str(self.score), True, c.WHITE)
        text4 = font3.render("BEST SCORE:  " + str(self.best_score), True, c.WHITE)
        self.game.screen.blit(text1, (210, 200))
        self.game.screen.blit(text2, (365, 150))
        self.game.screen.blit(text3, (410, 250))
        self.game.screen.blit(text4, (410, 280))

    def print_win_msg(self):
        font1 = pygame.font.SysFont(None, 45)
        font2 = pygame.font.SysFont(None, 65)
        font3 = pygame.font.SysFont(None, 30)
        text1 = font1.render("PRESS SPACE TO START A NEW GAME", True, c.WHITE)
        text2 = font2.render("YOU WON!", True, c.WHITE)

        if (self.best_score < self.score):
            with open(path.join(self.dir, c.BEST_SCORE_FILE), "w") as f:
                f.write(str(self.score))

        text3 = font3.render("YOUR SCORE:  " + str(self.score), True, c.WHITE)
        text4 = font3.render("BEST SCORE:  " + str(self.best_score), True, c.WHITE)
        self.game.screen.blit(text1, (210, 200))
        self.game.screen.blit(text2, (365, 150))
        self.game.screen.blit(text3, (410, 250))
        self.game.screen.blit(text4, (410, 280))

    def print_game_info(self):
        self.print_coins()
        self.print_score()
        self.print_time()
        if self.game.game_state == c.START:
            self.print_start_msg()
        elif self.game.game_state == c.PAUSE:
            self.print_pause_msg()
        elif self.game.game_state == c.GAMEOVER:
            self.print_gameover_msg()
        elif self.game.game_state == c.WIN:
            self.score += self.time * 10
            self.print_win_msg()

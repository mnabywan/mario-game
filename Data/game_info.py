import pygame
from . import setup
from . import constants as c

class GameInfo (pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.coins = 0
        self.score = 0
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

    def print_game_info(self):
        self.print_coins()
        self.print_score()
        self.print_time()
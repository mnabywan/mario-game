
#screen dimensions
SCREEN_HEIGHT = 464
SCREEN_WIDTH = 1000
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)
GROUND_HEIGHT = SCREEN_HEIGHT - 50  #???

#colours (red, green,  blue)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#tps
TPS_MAX = 70.0

#level size
LEVEL_WIDTH = 6784
LEVEL_HEIGHT = SCREEN_HEIGHT
WIDTH_ELEMENTS = 212
HEIGHT_ELEMENTS = 14
MULTIPLICATION = 32

#mario size
MARIO_SIZE_MULTIPLIER = 2
#MARIO_HEIGHT = 64
#MARIO_WIDTH = 32

#mario states
STAND = 'stand'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'

#mario forces
WALK_ACCEL = .15
RUN_ACCEL = 20

#GRAVITY = 1.01
GRAVITY = 0.1
JUMP_GRAVITY = .31
JUMP_VEL = -10
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800
MAX_WALK_SPEED = 6

#brick
BRICK_SIZE_MULTIPLIER = 2.69

#directions
LEFT = 'left'
RIGHT = 'right'

#inside coin box
COIN = 'coin'
MUSHROOM = 'mushroom'

#game states
START = 'start'
PLAYING = 'playing'
PAUSE = 'pause'
GAMEOVER = 'gameover'
WIN = 'win'

BEST_SCORE_FILE = "score.txt"
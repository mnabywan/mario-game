
#screen dimensions
SCREEN_HEIGHT = 464
SCREEN_WIDTH = 1000
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)
GROUND_HEIGHT = SCREEN_HEIGHT - 50  #???

#colours (red, green,  blue)
BLACK = (0,0,0)
RED = (255,0,0)

#tps
TPS_MAX = 70.0

#level size
LEVEL_WIDTH = 6784
LEVEL_HEIGHT = SCREEN_HEIGHT
WIDTH_ELEMENTS = 212
HEIGHT_ELEMENTS = 14
MULTIPLICATION = 32



#mario size
MARIO_SIZE_MULTIPLIER = 2.5
#MARIO_HEIGHT = 64
#MARIO_WIDTH = 32

#mario states
STAND = 'stand'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SHOOT = 'shoot'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
#FLAGPOLE = 'flag pole'
#WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL = 'end of level'

#mario forces
WALK_ACCEL = .15
RUN_ACCEL = 20
SMALL_TURNAROUND = .35

GRAVITY = 1.01
JUMP_GRAVITY = .31
JUMP_VEL = -10
FAST_JUMP_VEL = -12.5
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800
MAX_WALK_SPEED = 6


#enemy state
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

### ENGINE ###
UPDATE_PERIOD_MS = 2
DRAW_PERIOD_MS = 15

### WINDOW ###
WINDOW_SIZE = (640, 480)

### GRAPHICS ###
SPRITE_PATH = "sprite/"
SPACESHIP_SPRITE_NAME = "spaceship.png"
ALIEN_SPRITE_NAMES = [
    ["alien1_frame1.png", "alien1_frame2.png"],
    ["alien2_frame1.png", "alien2_frame2.png"],
    ["alien3_frame1.png", "alien3_frame2.png"]
]
ALIEN_EXPLOSION_SPRITE_NAME = "alien_explosion.png"
MISSILE_EXPLOSION_SPRITE_NAME = "missile_explosion.png"
LASER_EXPLOSION_SPRITE_NAME = "laser_explosion.png"
BARRICADE_SPRITE_NAME = "barricade.png"

### SOUND ###
SOUND_PATH = "sound/"
ALIEN_DESTROYED_SOUND = "alien_destroyed.wav"
ALIEN_MOVE_SOUND = "fastinvader.wav"
SPACESHIP_SHOOT_SOUND = "shoot.wav"

### ENTITIES ###
WORLD_DIM = (640, 480)

SPACESHIP_STARTING_POSITION = (WORLD_DIM[0] // 2, WORLD_DIM[1] * 9 // 10)
SPACESHIP_SPEED_PIXEL_PER_SECOND = 100

ALIEN_FORMATION = [[1] * 11, [2] * 11, [2] * 11, [3] * 11, [3] * 11]
ALIEN_FORMATION_WIDTH = 360
ALIEN_MOVE_SEQUENCE = [(1, 0), (0, 1), (-1, 0), (-1, 0), (0, 1), (1, 0)]
ALIEN_SPEED_PIXEL_PER_SECOND = 3
ALIEN_MOVE_SEQUENCE_PERIOD_SECOND = 25 / ALIEN_SPEED_PIXEL_PER_SECOND
ALIEN_FIRING_PERIOD_MS = 1000
ALIEN_SPRITE_SHIFT_DELAY_MS = 500

EXPLOSION_DURATION_MS = 250

MISSILE_RECT_DIM = (2, 6)
MISSILE_RECT_COLOR = (0, 255, 0)
MISSILE_SPEED_PIXEL_PER_SECOND = 500

LASER_RECT_DIM = (2, 6)
LASER_RECT_COLOR = (255, 255, 0)
LASER_SPEED_PIXEL_PER_SECOND = 100

BARRICADE_POSITIONS = [
    ( (WORLD_DIM[0]//14) + (WORLD_DIM[0]//7  *1), WORLD_DIM[1] * 7 // 10),
    ((WORLD_DIM[0]//14) + (WORLD_DIM[0]//7  *3), WORLD_DIM[1] * 7 // 10),
    ((WORLD_DIM[0]//14) + (WORLD_DIM[0]//7  *5), WORLD_DIM[1] * 7 // 10)
]
BARRICADE_EXPLOSION_RADIUS = 4
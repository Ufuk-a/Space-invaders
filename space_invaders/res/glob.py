WIDTH, HEIGHT = 600, 600
FULLSCREEN = False
PIXEL_WIDTH, PIXEL_HEIGHT = 30, 30

TITLE = "EMPTY PYGAME"
DRAW_GRID = 1
FPS = 60


class colors:
    red = (255, 0, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    lime = (0, 255, 0)
    turq = (64, 224, 208)
    orange = (255, 69, 0)
    white = (255, 255, 255)
    green = (34, 139, 34)


class states:
    empty = 0
    wall = 1


(WIDTH, HEIGHT) = (WIDTH + 1, HEIGHT + 1) if DRAW_GRID else (WIDTH, HEIGHT)
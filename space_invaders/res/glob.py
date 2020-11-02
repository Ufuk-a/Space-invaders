import pygame  # 3. parti importları burada yapabilirsin
pygame.init()

WIDTH, HEIGHT = 600, 600
FULLSCREEN = False
PIXEL_WIDTH, PIXEL_HEIGHT = 30, 30

TITLE = "Space Invaders"
FPS = 60
FONT = pygame.font.SysFont("space_invaders\\res\\pixelated.ttf", 30)

class colors:
    red = (255, 0, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    lime = (0, 255, 0)
    turq = (64, 224, 208)
    orange = (255, 69, 0)
    white = (255, 255, 255)
    green = (34, 139, 34)



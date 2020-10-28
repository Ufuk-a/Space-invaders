from emptypygame.res.glob import *
import pygame


def main():
    pygame.display.init()
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    screen_size = (WIDTH, HEIGHT)
    screen_args = (screen_size, pygame.FULLSCREEN) if FULLSCREEN else (screen_size, )
    screen = pygame.display.set_mode(*screen_args)

    while True:
        if not runTime(screen, clock):
            break

    pygame.quit()


def runTime(screen, clock):
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            

        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()

    pygame.display.update()
    return True


if __name__ == "__main__":
    main()

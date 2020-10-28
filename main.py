from space_invaders.lib.player import Player
from space_invaders.res.glob import *


def main():
    pygame.display.init()
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # fullscreen meselesini neden yok ettin ki
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    # screen.fill((0, 0, 0))
    screen.fill(colors.black)

    # oluşumları döngü içine koyarsan sürekli olarak baştan oluşturur
    human_ship = Player(screen, x=0, health=100, ammo=100, is_enemy=False)
    # sonra hareket edemezsin 

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        # render ve update tarzı şeyleri eventlerle uğraştıktan sonra koy (burası)
        human_ship.render()
        
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

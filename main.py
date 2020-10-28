import pygame


def main():
    pygame.display.init()
    pygame.display.set_caption("Space-Invaders")
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((500, 500))
    screen.fill((0, 0, 0))

    while True:
        if not runTime(screen, clock):
            break


    pygame.quit()

class player:
    
    def __init__(self, x, health, ammo, is_enemy):
        self.x = x
        self.health = health
        self.ammo = ammo
        self.is_enemy = is_enemy
    
    def render(x):
        y = 100
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10))    

def runTime(screen, clock):
    clock.tick(60)
    human_ship = player(0, 100, 100, False)
    human_ship.render()

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

from space_invaders.lib.classes import *
from space_invaders.res.glob import *


def main():
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    
    ships = pygame.sprite.Group()
    player = HumanShip(300)
    ships.add(player)
    screen.fill(colors.black)
    
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False 

        ships.update()
        ships.draw(screen)
        pygame.display.update()
        
    
    pygame.quit() 

if __name__ == "__main__":
    main()

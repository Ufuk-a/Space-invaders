from space_invaders.lib.classes import *
from space_invaders.res.glob import *


def main():
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False 

         
        screen.fill(colors.black)   
        ships.update()
        bullets.update()
        ships.draw(screen)
        bullets.draw(screen)
        pygame.display.update()
        
    
    pygame.quit() 

if __name__ == "__main__":
    main()
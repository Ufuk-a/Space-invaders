from space_invaders.res.glob import *
from space_invaders.lib.human_ship import * #bunu yapmanın 1 satırlık yolu olduğna 100% eminim ama bilmiyorum
from space_invaders.lib.enemy_ship import *
from space_invaders.lib.bullet import *



def main():
    
    # updatelerin parametreleri farklı olduğu için sprite gruplarını bölmem gerekiyor kafayı yicem
    player_ship = pygame.sprite.Group()
    enemy_ship = pygame.sprite.Group() 
    bullets = pygame.sprite.Group() 
    player = HumanShip(10000)
    enemy = EnemyShip(100)
    player_ship.add(player)
    enemy_ship.add(enemy)   
    
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
        player_ship.update(player_ship, Bullet, bullets, screen)
        enemy_ship.update(player, bullets, Bullet)     
        bullets.update(bullets, player, enemy)
        player_ship.draw(screen)
        enemy_ship.draw(screen)
        bullets.draw(screen)
        pygame.display.update()
        

if __name__ == "__main__":
    main()
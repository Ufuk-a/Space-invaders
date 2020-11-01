from space_invaders.lib.human_ship import HumanShip
from space_invaders.res.glob import *
pygame.init()

player_image = pygame.image.load("space_invaders\\res\\human_ship.png")

class EnemyShip(pygame.sprite.Sprite):
    
    def __init__(self, hp):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.transform.flip(player_image, False, True)
        self.rect = self.image.get_rect()
        self.x = 300
        self.rect.center = (self.x + 32, 100)                
        self.hp = hp

    def update(self, player, bullets, Bullet, enemy_ship):
        
        #Enemy movement
        speed = 1.5
        if player.rect.x < self.rect.x:
            self.x -= speed
            self.rect.x = self.x
        elif player.rect.x > self.rect.x:
            self.x += speed    
            self.rect.x = self.x
        
        #shoot logic
        if self.x + 32 > player.rect.x and self.x + 32 < player.rect.x + 64:
            shoot = Bullet(self.x + 32, 120, "down")
            bullets.add(shoot) 
        
        #Boundary  
        if self.rect.left < 0:
            self.rect.left = 0
            self.x = 0
        elif self.rect.right > 600:
            self.rect.right = 600       
            self.x = 536
            
        #health logic 
        if self.hp == 0:
            enemy_ship.remove(self)    
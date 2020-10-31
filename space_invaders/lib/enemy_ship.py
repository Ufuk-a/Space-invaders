from space_invaders.lib.bullet import *
from space_invaders.res.glob import *
pygame.init()

player_image = pygame.image.load("space_invaders\\res\\human_ship.png")

class EnemyShip(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.transform.flip(player_image, False, True)
        self.rect = self.image.get_rect()
        self.x = 300
        self.rect.center = (self.x + 32, 100)                

    def update(self, player, bullets):
        
        speed = 1.5
        if player.rect.x < self.rect.x:
            self.x -= speed
            self.rect.x = self.x
        elif player.rect.x > self.rect.x:
            self.x += speed    
            self.rect.x = self.x
        else:
            shoot = Bullet(self.x + 32, 120, "down")
            bullets.add(shoot)
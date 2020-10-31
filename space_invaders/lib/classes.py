from pygame.display import update
from space_invaders.res.glob import *
pygame.init()

ships = pygame.sprite.Group()
player_image = pygame.image.load("space_invaders\\res\\human_ship.png")

class HumanShip(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = player_image
        self.rect = self.image.get_rect()
        self.x = 300
        self.rect.center = (self.x, 500)
        
    def update(self):
        key = pygame.key.get_pressed()
        dist = 2
        if key[pygame.K_LEFT]:
            self.rect.x -= dist
        elif key[pygame.K_RIGHT]:
            self.rect.x += dist    
            
    def get_x(self):
        return self.rect.x
                
player = HumanShip()
            
class EnemyShip(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.transform.flip(player_image, False, True)
        self.rect = self.image.get_rect()
        self.x = 300
        self.rect.center = (self.x, 100)                

    def update(self):
        
        speed = 1.5 
        if player.rect.x > self.rect.x:
            self.rect.x += speed
        elif player.rect.x < self.rect.x:
            self.rect.x -= speed    
        else:
            pass
            
enemy = EnemyShip()

ships.add(player, enemy)    

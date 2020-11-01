from space_invaders.res.glob import *
pygame.init()

player_image = pygame.image.load("space_invaders\\res\\human_ship.png")

class HumanShip(pygame.sprite.Sprite):
    
    def __init__(self, hp):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = player_image
        self.rect = self.image.get_rect()
        self.x = 300
        self.rect.center = (self.x + 32, 500)
        self.hp = hp    
    
    def update(self, player_ship, Bullet, bullets):
        
        #Movement
        key = pygame.key.get_pressed()
        speed = 3
        if key[pygame.K_LEFT]:
            self.x -= speed
            self.rect.x = self.x
        elif key[pygame.K_RIGHT]:
            self.x += speed    
            self.rect.x = self.x
        
        
        #Boundary
        if self.rect.left < 0:
            self.rect.left = 0
            self.x = 0
        elif self.rect.right > 600:
            self.rect.right = 600       
            self.x = 536
            
        #health logic 
        if self.hp == 0:
            player_ship.remove(self)
            
        #shoot
        if key[pygame.K_SPACE]:    
            shoot = Bullet(self.x + 32, 468, "up")
            bullets.add(shoot)     
                
            
            
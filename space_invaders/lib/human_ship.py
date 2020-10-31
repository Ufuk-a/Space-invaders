from space_invaders.res.glob import *
pygame.init()

player_image = pygame.image.load("space_invaders\\res\\human_ship.png")

class HumanShip(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = player_image
        self.rect = self.image.get_rect()
        self.x = 300
        self.rect.center = (self.x + 32, 500)
        
    def update(self):
        key = pygame.key.get_pressed()
        speed = 3
        if key[pygame.K_LEFT]:
            self.x -= speed
            self.rect.x = self.x
        elif key[pygame.K_RIGHT]:
            self.x += speed    
            self.rect.x = self.x
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.x = 0
        elif self.rect.right > 600:
            self.rect.right = 600       
            self.x = 536

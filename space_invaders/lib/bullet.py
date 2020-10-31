from space_invaders.res.glob import *
pygame.init()

bullet_image = pygame.image.load("space_invaders\\res\\bullet.png")
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, 0)
        self.direction = direction
        self.x = x
        self.y = y
    
    def update(self, bullets):
        
        speed = 10
        if self.y > 0 and self.y < 600:
            if self.direction == "up":
                self.y -= speed
                self.rect.y = self.y
                
            if self.direction == "down":
                self.y += speed    
                self.rect.y = self.y
                
        else:
            bullets.remove(self)        

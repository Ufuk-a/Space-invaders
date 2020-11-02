from space_invaders.res.glob import *

bullet_image = pygame.image.load("space_invaders\\res\\images\\bullet.png")
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, 0)
        self.direction = direction
        self.x = x
        self.y = y
    
    def update(self, bullets, player, enemy):
        
        #Bullet movement
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
            
        #Collision logic    
        if self.direction == "down":
            if self.y < player.rect.y + 64 and self.y > player.rect.y:
                if self.x > player.rect.x and self.x < player.rect.x + 64:
                    player.hp -= 5
                    bullets.remove(self)
        if self.direction == "up":
            if self.y < enemy.rect.y + 64 and self.y > enemy.rect.y:
                if self.x > enemy.rect.x and self.x < enemy.rect.x + 64:
                    enemy.hp -=5 
                    bullets.remove(self)
                        
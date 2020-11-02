from space_invaders.lib.bullet import Bullet
from space_invaders.res.glob import *

player_image = pygame.image.load("space_invaders\\res\\images\\human_ship.png")

class HumanShip(pygame.sprite.Sprite):
    
    def __init__(self, hp):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = player_image
        self.rect = self.image.get_rect()
        self.x = 300
        self.rect.center = (self.x + 32, 500)
        self.hp = hp    
        self.score = 0
    
    def update(self, bullets, screen):
        key = pygame.key.get_pressed()
    
        #health logic
        if self.hp < 0:
            self.hp = 0
        
        if self.hp == 0:
            end_score = FONT.render(f"You died! Your score was: {self.score}", False, colors.white)
            screen.blit(end_score,(200,300)) 
            if key[pygame.K_SPACE]:
                pygame.display.quit()    
        
        
        #Movement
        speed = 3
        if self.hp != 0:
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
            
 
        #shoot
        if key[pygame.K_SPACE]:    
            shoot = Bullet(self.x + 32, 468, "up")
            bullets.add(shoot)     
                
                
        #score
        score_text = FONT.render(f"Score: {self.score}", False, colors.white)
        screen.blit(score_text,(0,0))
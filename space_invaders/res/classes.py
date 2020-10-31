from space_invaders.res.glob import *
pygame.init()
#bunun ağır günah olduğnu hissediyorum ama baska türlü nasıl burda image loadlamam gerekiyor

player_image = pygame.image.load("space_invaders\\res\\human_ship.png")

class HumanShip(pygame.sprite.Sprite):
    
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = player_image
        self.rect = self.image.get_rect()
        self.x = x
        self.rect.center = (x, 500)
        
        

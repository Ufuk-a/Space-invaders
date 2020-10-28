from space_invaders.res.glob import *  # her dosyanın başında bulunsun bu

# classlarda PascalCase
# class player:


class Player:
    def __init__(self, screen, x, health, ammo, is_enemy):
        self.is_enemy = is_enemy  # kesinlikle kullanma
        self.health = health
        self.screen = screen
        self.ammo = ammo
        self.x = x

    #             çalışmama sebebi screenin global olmamasıydı bunu zaten biliyorsun,
    #         screene erişmek için ya screen kullandığın fonksiyonlara (render)
    #     parametre olarak onu alırsın (render(self, screen, ...)) ya da direkt
    #   player içine özellikmiş gibi alırsın ve tüm fonksiyonlardan baştan vermekle uğraşmazsın
    # her foksiyona ayrı vermenin daha avantajlı olduğu zamanlar da oluyor

    # def render(x): # self koymamışsın
    def render(self, x):
        y = 100
        # pygame.draw.rect(self.screen, (255, 255, 255), (x, y, 10, 10))
        pygame.draw.rect(self.screen, colors.white, (x, y, 10, 10))

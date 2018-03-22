from plane_sprites import*

class Bullet(GameSpirte):
    """子弹类"""

    bullet_images = []
    def __init__(self,bullet_id = 0):

        super().__init__(image_name= "images/bullet/b1.png",speed = [0,-12])
        self.load_images()
        self.image = Bullet.bullet_images[bullet_id]
        self.rect = self.image.get_rect()
        if bullet_id == 0:
            self.bullet_power = 20


    def update(self):
        super().update()
        if self.rect.bottom < 0 :
            self.kill()


    def __del__(self):
        print("子弹被删除")

    def load_images(self):
        Bullet.bullet_images.extend([ \
            pygame.image.load("images/bullet/b1.png").convert_alpha(), \
            pygame.image.load("images/bullet/b2.png").convert_alpha(), \
            pygame.image.load("images/bullet/s1.png").convert_alpha(), \
            ])

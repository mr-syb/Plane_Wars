from plane_sprites import*

class Bullet(GameSpirte):
    """子弹类"""

    bullet_id = 0
    def __init__(self):#def __init__(self,position):

        super().__init__(image_name= "images/images/bullet/b1.png",speed = [0,-12])
        #self.rect.center = position

    def update(self):
        super().update()
        if self.rect.bottom < 0 :
            self.kill()


    def __del__(self):
        print("子弹被删除")

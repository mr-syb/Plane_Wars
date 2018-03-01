from plane_sprites import*
from plane_bullet import*
from plane_music import*


class Hero(GameSpirte):
    """英雄精灵"""

    # 英雄序列
    __hero_id = 0
    #所有的英雄图片
    __hero_images = []

    #初始化英雄精灵,image_name = "images/images/me/m1_1.png"
    def __init__(self):
    # 加载英雄图像
        self.load_images()
    #设置英雄image属性
        self.image = Hero.__hero_images[Hero.__hero_id]
    #设置英雄mask属性，用于碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
    # 设置英雄初始位置
        #self.rect = (SIZE[0] - self.rect.width) // 2,SIZE[1] - self.rect.height
        self.rect = self.image.get_rect()
        self.rect.center = SIZE[0] // 2, SIZE[1] + 60
    # 设置英雄速度
        self.speed = [0,0]
    # 设置子弹精灵组
        self.bullet_group = pygame.sprite.Group()



    def update(self):
        self.rect.left += int(self.speed[0])
        self.rect.top += int(self.speed[1])



        #检测是否出界
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > height:
            self.rect.bottom = height
        elif self.rect.right > width:
            self.rect.right = width

    #自定义屏幕绘制函数
    def draw(self,screen):
        screen.blit(self.image, self.rect)

    #加载所有英雄图片
    def load_images(self):
        Hero.__hero_images.extend([ \
            pygame.image.load("images/images/me/m1_1.png").convert_alpha(), \
            pygame.image.load("images/images/me/m1_2.png").convert_alpha(), \
            pygame.image.load("images/images/me/m2_1.png").convert_alpha(), \
            pygame.image.load("images/images/me/m2_2.png").convert_alpha(), \
            pygame.image.load("images/images/me/m3_1.png").convert_alpha(), \
            pygame.image.load("images/images/me/m3_2.png").convert_alpha(), \
            pygame.image.load("images/images/me/m4_1.png").convert_alpha(), \
            pygame.image.load("images/images/me/m4_2.png").convert_alpha(), \
            pygame.image.load("images/images/me/m5_1.png").convert_alpha(), \
            pygame.image.load("images/images/me/m5_2.png").convert_alpha(), \
            pygame.image.load("images/images/me/m6_1.png").convert_alpha(), \
            pygame.image.load("images/images/me/m6_2.png").convert_alpha(), \
            ])
    #发射子弹
    def fire(self):
        print("发射子弹")

        bullet_sound.play()
        for i in (0,1):

            #创建子弹精灵
            bullet = Bullet()
            if Hero.__hero_id == 2:
                bullet.rect.bottom = self.rect.top - i * 70
                bullet.rect.centerx = self.rect.centerx


            #设置精灵的位置
            bullet.rect.bottom = self.rect.top - i*70
            bullet.rect.centerx = self.rect.centerx

            #将子弹添加到子弹精灵组
            self.bullet_group.add(bullet)

    #摧毁英雄
    def __del__(self):
        print("摧毁英雄")



    #设置英雄序列
    @classmethod
    def set_hero_id(cls,num):
        Hero.__hero_id = num

    #英雄序列加一
    @classmethod
    def add_hero_id(cls):
        Hero.__hero_id += 1




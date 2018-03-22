from plane_sprites import*
from plane_bullet import*
from plane_music import*


class Hero(GameSpirte):
    """英雄精灵"""

    # 英雄序列
    __hero_id = 0
    #所有的英雄图片
    __hero_images = []
    #飞机护盾
    __shield_images = []
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
    # 飞机护盾
        self.shield_num = 100
        self.shield = Shield(self.rect.centerx,self.rect.top)
        #self.shield_group = pygame.sprite.Group()


    def update(self):
        #英雄更新
        self.rect.left += int(self.speed[0])
        self.rect.top += int(self.speed[1])
        #护盾更新
        self.shield.update(self.rect.centerx,self.rect.centery)
        if self.shield_num > 33 and self.shield_num < 66:
            self.shield.image = self.shield.new_images[1]
        if self.shield_num < 33 and self.shield_num > 0:
            self.shield.image = self.shield.new_images[0]
        if self.shield_num < 0:
            self.shield.kill()
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
            pygame.image.load("images/me/m1_1.png").convert_alpha(), \
            pygame.image.load("images/me/m1_2.png").convert_alpha(), \
            pygame.image.load("images/me/m2_1.png").convert_alpha(), \
            pygame.image.load("images/me/m2_2.png").convert_alpha(), \
            pygame.image.load("images/me/m3_1.png").convert_alpha(), \
            pygame.image.load("images/me/m3_2.png").convert_alpha(), \
            pygame.image.load("images/me/m4_1.png").convert_alpha(), \
            pygame.image.load("images/me/m4_2.png").convert_alpha(), \
            pygame.image.load("images/me/m5_1.png").convert_alpha(), \
            pygame.image.load("images/me/m5_2.png").convert_alpha(), \
            pygame.image.load("images/me/m6_1.png").convert_alpha(), \
            pygame.image.load("images/me/m6_2.png").convert_alpha(), \
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

    #获取英雄ID
    @classmethod
    def get_hero_id(cls):
        return Hero.__hero_id

    #英雄序列加一
    @classmethod
    def add_hero_id(cls):
        Hero.__hero_id += 1


class Shield(GameSpirte):
    """护盾类"""

    def __init__(self,x,y):
        super().__init__(image_name= "images/me/shield3.png",speed = [0,0])
        self.shield_images = []
        self.load_images()
        #变换后的护盾图片
        self.new_images = []
        self.rotate_image()
        self.image = self.new_images[2]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = x,y

    def update(self,x,y):
        self.rect.centerx = x
        self.rect.centery = y - 50
        #super().update()
        #self.rect.y += self.speed[1]
        #self.rect.x += self.speed[0]


    def load_images(self):
        self.shield_images.extend([ \
            pygame.image.load("images/me/shield1.png").convert_alpha(), \
            pygame.image.load("images/me/shield2.png").convert_alpha(), \
            pygame.image.load("images/me/shield3.png").convert_alpha(), \
            ])

    def rotate_image(self):
        rates = [1.18,1.07,0.94,1.28,1.61]
        if Hero.get_hero_id() == 0 or Hero.get_hero_id() == 1:
            rate = 1
            #self.new_images = self.shield_images
        elif Hero.get_hero_id() == 2 or Hero.get_hero_id() == 3:
            rate = rates[0]
        elif Hero.get_hero_id() == 4 or Hero.get_hero_id() == 5:
            rate = rates[1]
        elif Hero.get_hero_id() == 6 or Hero.get_hero_id() == 7:
            rate = rates[2]
        elif Hero.get_hero_id() == 8 or Hero.get_hero_id() == 9:
            rate = rates[3]
        elif Hero.get_hero_id() == 10 or Hero.get_hero_id() == 11:
            rate = rates[4]

        for s in self.shield_images:
            #变换护盾图片大小
            temp = pygame.transform.smoothscale(s, (int(self.rect.width*rate+1) , int(self.rect.height*rate+1)) )
            self.new_images.append(temp)

    #自定义屏幕绘制函数
    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def __del__(self):
        print("护盾删除-------------------------------")

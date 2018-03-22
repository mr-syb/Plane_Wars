from plane_sprites import*
from random import randint

class Enemy(GameSpirte):
    """敌方精灵"""

    def __init__(self,image_name = "images/enemies/e1_1.png",speed = [0,2] ):

        #1.调用父类初始函数
        super().__init__(image_name,speed)
        e_id = randint(0, 19)
        self.e_images = []
        #爆炸精灵动画字典，————有两个列表与子弹碰撞时使用大的，与护盾碰撞时使用小的
        self.explosion_anim = {}
        self.explosion_anim['lg'] = []
        self.explosion_anim['sm'] = []

        #2.加载敌机图片
        self.load_images()
        scale_num  = randint(1, 3)
        self.image = pygame.transform.scale(self.e_images[e_id],\
                    (self.rect.width //scale_num,self.rect.height//scale_num))
        self.rect = self.image.get_rect()
        #2.设置敌机大小
        self.enemy_size = max(self.rect.width // 2,self.rect.height // 2)
        #3.随机化敌机出场位置
        self.rect.left = randint(0,width - self.rect.width)
        self.rect.top = randint(-5 * height, 0)
        # 随机化敌机速度
        self.speed = [0,104//self.enemy_size]
        #设置敌机血量
        self.energy =  self.enemy_size
        # 敌机实时血量
        self.real_time_energy = self.energy
        #设置mask属性用于碰撞检测
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        #调用父类update函数
        super().update()
        if self.rect.top > height:
            self.kill()
            print("已删除。。。")

    def load_images(self):
        self.e_images = []
        self.e_images.extend([ \
            pygame.image.load("images/enemies/e1_1.png").convert_alpha(), \
            pygame.image.load("images/enemies/e1_2.png").convert_alpha(), \
            pygame.image.load("images/enemies/e1_3.png").convert_alpha(), \
            pygame.image.load("images/enemies/e1_4.png").convert_alpha(), \
            pygame.image.load("images/enemies/e1_5.png").convert_alpha(), \
            pygame.image.load("images/enemies/e2_1.png").convert_alpha(), \
            pygame.image.load("images/enemies/e2_2.png").convert_alpha(), \
            pygame.image.load("images/enemies/e2_3.png").convert_alpha(), \
            pygame.image.load("images/enemies/e2_4.png").convert_alpha(), \
            pygame.image.load("images/enemies/e2_5.png").convert_alpha(), \
            pygame.image.load("images/enemies/e3_1.png").convert_alpha(), \
            pygame.image.load("images/enemies/e3_2.png").convert_alpha(), \
            pygame.image.load("images/enemies/e3_3.png").convert_alpha(), \
            pygame.image.load("images/enemies/e3_4.png").convert_alpha(), \
            pygame.image.load("images/enemies/e3_5.png").convert_alpha(), \
            pygame.image.load("images/enemies/e4_1.png").convert_alpha(), \
            pygame.image.load("images/enemies/e4_2.png").convert_alpha(), \
            pygame.image.load("images/enemies/e4_3.png").convert_alpha(), \
            pygame.image.load("images/enemies/e4_4.png").convert_alpha(), \
            pygame.image.load("images/enemies/e4_5.png").convert_alpha(), \
            ])






    def add_enemies(self,plane_enemys_group, enemys_group, num):
        for i in range(num):
            e1 = Enemy()
            plane_enemys_group.add(e1)
            enemys_group.add(e1)

    """def add_mid_enemies(mid__enemys_group, enemys_group, num):
        for i in range(num):
            e1 = enemy("images/enemy2.png")
            mid__enemys_group.add(e1)
            enemys_group.add(e1)

    def add_big_enemies(big__enemys_group, enemys_group, num):
        for i in range(num):
            e1 = enemy("images/enemy3_n1.png")
            big__enemys_group.add(e1)
            enemys_group.add(e1)"""


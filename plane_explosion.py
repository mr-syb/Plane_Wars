from plane_sprites import*

class Explosion(GameSpirte):
    def __init__(self, center, size):
        #调用父类初始化函数
        super().__init__("images/explode/ex0.png")
        # 爆炸精灵动画字典，————有两个列表与子弹碰撞时使用大的，与护盾碰撞时使用小的
        self.explosion_anim = {}
        self.explosion_anim['lg'] = []
        self.explosion_anim['sm'] = []

        self.load_image()

        self.size = size
        self.image = self.explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def load_image(self):
        explode = []
        explode.extend([ \
            pygame.image.load("images/explode/ex1.png").convert_alpha(), \
            pygame.image.load("images/explode/ex1.png").convert_alpha(), \
            pygame.image.load("images/explode/ex2.png").convert_alpha(), \
            pygame.image.load("images/explode/ex3.png").convert_alpha(), \
            pygame.image.load("images/explode/ex4.png").convert_alpha(), \
            pygame.image.load("images/explode/ex5.png").convert_alpha(), \
            pygame.image.load("images/explode/ex6.png").convert_alpha(), \
            pygame.image.load("images/explode/ex7.png").convert_alpha(), \
            pygame.image.load("images/explode/ex8.png").convert_alpha(), \
            ])

        """explode.extend([ \
            pygame.image.load("images/explode/e_01.png").convert_alpha(), \
            pygame.image.load("images/explode/e_02.png").convert_alpha(), \
            pygame.image.load("images/explode/e_03.png").convert_alpha(), \
            pygame.image.load("images/explode/e_04.png").convert_alpha(), \
            pygame.image.load("images/explode/e_05.png").convert_alpha(), \
            pygame.image.load("images/explode/e_06.png").convert_alpha(), \
            pygame.image.load("images/explode/e_07.png").convert_alpha(), \
            pygame.image.load("images/explode/e_08.png").convert_alpha(), \
            pygame.image.load("images/explode/e_09.png").convert_alpha(), \
            pygame.image.load("images/explode/e_10.png").convert_alpha(), \
            pygame.image.load("images/explode/e_11.png").convert_alpha(), \
            pygame.image.load("images/explode/e_12.png").convert_alpha(), \
            pygame.image.load("images/explode/e_13.png").convert_alpha(), \
            pygame.image.load("images/explode/e_14.png").convert_alpha(), \
            pygame.image.load("images/explode/e_15.png").convert_alpha(), \
            pygame.image.load("images/explode/e_16.png").convert_alpha(), \
            ])
        """




        for i in range(9):
            img = explode[i]
            img.set_colorkey(BLACK)
            img_lg = pygame.transform.scale(img, (75, 75))
            self.explosion_anim['lg'].append(img_lg)
            img_sm = pygame.transform.scale(img, (32, 32))
            self.explosion_anim['sm'].append(img_sm)
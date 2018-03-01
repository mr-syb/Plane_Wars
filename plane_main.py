from plane_sprites import *
from plane_music import *
import time
import plane_hero as hero
import plane_enemy as enemy
import plane_background as bg
import plane_bullet as bullet
import plane_explosion as explosion

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化。。。")
        #1.开始菜单
        self.__start_menu()
        #2.创建游戏窗口
        self.screen = pygame.display.set_mode(SIZE,pygame.FULLSCREEN)
        self.caption_icon = pygame.image.load("images/caption_icon.png").convert_alpha()
        pygame.display.set_caption("飞机大战")
        pygame.display.set_icon(self.caption_icon)#设置标题图片

        #3.创建游戏时钟
        self.clock = pygame.time.Clock()

        #4.调用私有方法，创建精灵和精灵组
        self.__creat_sprits()

        #5.设置当前帧，用于播放精灵动画
        self.current_frame = 0

        #6.设置定时器事件___英雄发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT,200)






    """
    定义并实现私有方法，
    """
    #开始菜单
    def __start_menu(self):
        self.start_screen = pygame.display.set_mode(SIZE,pygame.FULLSCREEN)
        start_bg = pygame.image.load("images/images/background/start_bg.png").convert_alpha()
        button1 = pygame.image.load("images/images/button/button1.png").convert_alpha()
        button2 = pygame.image.load("images/images/button/button2.png").convert_alpha()
        button3 = pygame.image.load("images/images/button/button3.png").convert_alpha()
        button4 = pygame.image.load("images/images/button/button4.png").convert_alpha()
        button5 = pygame.image.load("images/images/button/button5.png").convert_alpha()
        button6 = pygame.image.load("images/images/button/button6.png").convert_alpha()
        button7 = pygame.image.load("images/images/button/button7.png").convert_alpha()
        button8 = pygame.image.load("images/images/button/button8.png").convert_alpha()
        help_txt = pygame.image.load("images/images/background/help.png").convert_alpha()
        #约定展示按钮的初始形态
        show_button1 = button1
        show_button2 = button3
        show_button3 = button5
        show_button4 = button7
        #获取按钮的rect
        button1_rect = button1.get_rect()
        button3_rect = button3.get_rect()
        button5_rect = button5.get_rect()
        button7_rect = button7.get_rect()
        button1_rect.center = (1100,350)
        button3_rect.center = (1100,420)
        button5_rect.center = (1100,490)
        button7_rect.center = (1100,560)


        while True:
            # 用于展示帮助信息
            show_help = True
            #绘制初始界面背景及按钮初始形态
            self.start_screen.blit(start_bg,(0,0))
            self.start_screen.blit(show_button1, button1_rect)
            self.start_screen.blit(show_button2, button3_rect)
            self.start_screen.blit(show_button3, button5_rect)
            self.start_screen.blit(show_button4, button7_rect)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.__game_over()

                #绘制和检测 开始游戏，选择战机，帮助，退出游戏按钮
                if event.type == pygame.MOUSEMOTION:
                    if button1_rect.collidepoint(event.pos):
                        show_button1 = button1
                    else:
                        show_button1 = button2
                    if button3_rect.collidepoint(event.pos):
                        show_button2 = button3
                    else:
                        show_button2 = button4
                    if button5_rect.collidepoint(event.pos):
                        show_button3 = button5
                    else:
                        show_button3 = button6
                    if button7_rect.collidepoint(event.pos):
                        show_button4 = button7
                    else:
                        show_button4 = button8
                #按钮响应
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and button1_rect.collidepoint(event.pos):
                        button_sound.play()
                        time.sleep(1)
                        return 0
                    if event.button == 1 and button3_rect.collidepoint(event.pos):
                        button_sound.play()
                        self.select_hero()
                    if event.button == 1 and button5_rect.collidepoint(event.pos):
                        button_sound.play()
                        while show_help:
                            self.start_screen.blit(help_txt, (200,100))
                            pygame.display.update()
                            #再次点击鼠标停止显示帮助信息
                            for keydown in pygame.event.get():
                                if keydown.type == pygame.MOUSEBUTTONDOWN:
                                    show = False
                    if event.button == 1 and button7_rect.collidepoint(event.pos):
                        button_sound.play()
                        time.sleep(1)
                        self.__game_over()

            pygame.display.update()

    #选择战机
    def select_hero(self):
        start_bg = pygame.image.load("images/images/background/select_bg.png").convert_alpha()
        plane_1 = pygame.image.load("images/images/me/m1_1.png").convert_alpha()
        plane_2 = pygame.image.load("images/images/me/m2_1.png").convert_alpha()
        plane_3 = pygame.image.load("images/images/me/m3_1.png").convert_alpha()
        plane_4 = pygame.image.load("images/images/me/m4_1.png").convert_alpha()
        plane_5 = pygame.image.load("images/images/me/m5_1.png").convert_alpha()
        plane_6 = pygame.image.load("images/images/me/m6_1.png").convert_alpha()

        start_bg_rect = start_bg.get_rect()
        plane_1_rect = plane_1.get_rect()
        plane_2_rect = plane_2.get_rect()
        plane_3_rect = plane_3.get_rect()
        plane_4_rect = plane_4.get_rect()
        plane_5_rect = plane_5.get_rect()
        plane_6_rect = plane_6.get_rect()

        start_bg_rect.x,start_bg_rect.y = (200,100)
        plane_1_rect.x,plane_1_rect.y = (250,200)
        plane_2_rect.x, plane_2_rect.y = (420, 200)
        plane_3_rect.x, plane_3_rect.y = (600, 200)
        plane_4_rect.x, plane_4_rect.y = (250, 400)
        plane_5_rect.x, plane_5_rect.y = (420, 400)
        plane_6_rect.x, plane_6_rect.y = (600, 400)

        show_slect = True
        while show_slect:
            show_rect1 = show_rect2 = show_rect3 = show_rect4 = show_rect5 = show_rect6 = True
            self.start_screen.blit(start_bg, start_bg_rect)
            self.start_screen.blit(plane_1, plane_1_rect)
            self.start_screen.blit(plane_2, plane_2_rect)
            self.start_screen.blit(plane_3, plane_3_rect)
            self.start_screen.blit(plane_4, plane_4_rect)
            self.start_screen.blit(plane_5, plane_5_rect)
            self.start_screen.blit(plane_6, plane_6_rect)



            for event in pygame.event.get():
                # 再次点击鼠标停止显示帮助信息

                """if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and plane_1_rect.collidepoint(event.pos):
                        button_sound.play()
                        time.sleep(1)
                    if event.button == 1 and plane_2_rect.collidepoint(event.pos):
                        button_sound.play()
                        time.sleep(1)
                    if event.button == 1 and plane_3_rect.collidepoint(event.pos):
                        button_sound.play()
                        time.sleep(1)
                    if event.button == 1 and plane_4_rect.collidepoint(event.pos):
                        button_sound.play()
                        time.sleep(1)
                    if event.button == 1 and plane_5_rect.collidepoint(event.pos):
                        button_sound.play()
                        time.sleep(1)
                    if event.button == 1 and plane_6_rect.collidepoint(event.pos):
                        button_sound.play()
                        time.sleep(1)"""


                if event.type == pygame.MOUSEMOTION:
                    if plane_1_rect.collidepoint(event.pos):
                        while show_rect1:
                            pygame.draw.rect(self.start_screen, RED, plane_1_rect, 2)
                            pygame.display.update()
                            for mouse_move in pygame.event.get():
                                if mouse_move.type == pygame.MOUSEBUTTONDOWN:
                                    if mouse_move.button == 1:
                                        button_sound.play()
                                        hero.Hero.set_hero_id(0)
                                        show_slect = False

                                if mouse_move.type == pygame.MOUSEMOTION:
                                    if not plane_1_rect.collidepoint(mouse_move.pos):
                                        show_rect1 = False


                    if plane_2_rect.collidepoint(event.pos):
                        while show_rect2:
                            pygame.draw.rect(self.start_screen, RED, plane_2_rect, 2)
                            pygame.display.update()
                            for mouse_move in pygame.event.get():
                                if mouse_move.type == pygame.MOUSEBUTTONDOWN:
                                    if mouse_move.button == 1:
                                        button_sound.play()
                                        hero.Hero.set_hero_id(2)
                                        show_slect = False

                                if mouse_move.type == pygame.MOUSEMOTION:
                                    if not plane_2_rect.collidepoint(mouse_move.pos):
                                        show_rect2 = False

                    if plane_3_rect.collidepoint(event.pos):
                        while show_rect3:
                            pygame.draw.rect(self.start_screen, RED, plane_3_rect, 2)
                            pygame.display.update()
                            for mouse_move in pygame.event.get():
                                if mouse_move.type == pygame.MOUSEBUTTONDOWN:
                                    if mouse_move.button == 1:
                                        button_sound.play()
                                        hero.Hero.set_hero_id(4)
                                        show_slect = False

                                if mouse_move.type == pygame.MOUSEMOTION:
                                    if not plane_3_rect.collidepoint(mouse_move.pos):
                                        show_rect3 = False

                    if plane_4_rect.collidepoint(event.pos):
                        while show_rect4:
                            pygame.draw.rect(self.start_screen, RED, plane_4_rect, 2)
                            pygame.display.update()
                            for mouse_move in pygame.event.get():
                                if mouse_move.type == pygame.MOUSEBUTTONDOWN:
                                    if mouse_move.button == 1:
                                        button_sound.play()
                                        hero.Hero.set_hero_id(6)
                                        show_slect = False

                                if mouse_move.type == pygame.MOUSEMOTION:
                                    if not plane_4_rect.collidepoint(mouse_move.pos):
                                        show_rect4 = False

                    if plane_5_rect.collidepoint(event.pos):
                        while show_rect5:
                            pygame.draw.rect(self.start_screen, RED, plane_5_rect, 2)
                            pygame.display.update()
                            for mouse_move in pygame.event.get():
                                if mouse_move.type == pygame.MOUSEBUTTONDOWN:
                                    if mouse_move.button == 1:
                                        button_sound.play()
                                        hero.Hero.set_hero_id(8)
                                        show_slect = False

                                if mouse_move.type == pygame.MOUSEMOTION:
                                    if not plane_5_rect.collidepoint(mouse_move.pos):
                                        show_rect5 = False

                    if plane_6_rect.collidepoint(event.pos):
                        while show_rect6:
                            pygame.draw.rect(self.start_screen, RED, plane_6_rect, 2)
                            pygame.display.update()
                            for mouse_move in pygame.event.get():
                                if mouse_move.type == pygame.MOUSEBUTTONDOWN:
                                    if mouse_move.button == 1:
                                        button_sound.play()
                                        hero.Hero.set_hero_id(10)
                                        show_slect = False

                                if mouse_move.type == pygame.MOUSEMOTION:
                                    if not plane_6_rect.collidepoint(mouse_move.pos):
                                        show_rect6 = False





            pygame.display.update()



            #创建精灵和精灵组

    #创建精灵和精灵组
    def __creat_sprits(self):

        #创建背景精灵和精灵组
        bg1 = bg.Background()
        bg2 = bg.Background(is_alt=True)
        #bgcold = bg.Background_Cold()
        #bgstar1 = bg.Background("images/BackgroundStars.png")
        #bgstar2 = bg.Background("images/BackgroundStars.png",True)
        #self.back_group = pygame.sprite.Group(bgstar1,bgstar2,bgcold)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建英雄精灵---通过动画精灵播放
        self.hero1 = hero.Hero()
        hero.Hero.add_hero_id()
        hero2 = hero.Hero()
        self.hero_frames = [self.hero1,hero2]
        self.show_hero = hero.Hero()


        #创建子弹精灵
        """self.bullet_group = pygame.sprite.Group()
        bullet_num = 10
        position = self.show_hero.rect.midtop
        for i in range(bullet_num):
            b1 = bullet.Bullet(position)
            self.bullet_group.add(b1)
        """
        #创建敌机精灵
        self.enemy_group = pygame.sprite.Group()
        self.plane_enemy_group = pygame.sprite.Group()
        enemy.Enemy.add_enemies(self,self.plane_enemy_group,self.enemy_group,150)

        """self.mid_enemy_group = pygame.sprite.Group()
        enemy.Enemy.add_mid_enemies(self.mid_enemy_group, self.enemy_group, 4)

        self.big_enemy_group = pygame.sprite.Group()
        enemy.Enemy.add_big_enemies(self.big_enemy_group, self.enemy_group, 4)
        """
        #创建爆炸精灵
        self.expl_group = pygame.sprite.Group()


    #游戏开始
    def start_game(self):
        print("游戏开始。。。")
            #1.播放背景音乐
        pygame.mixer.music.play(-1)
        while running :
            #2.设置刷新帧率
            self.clock.tick(FPS)
            #3，事件监听
            self.__event_handler()
            #4.碰撞检测
            self.__check_collide()
            #5.更新绘制精灵组
            if pygame.display.get_active():  #最小化感知,最小化时暂停游戏
                pygame.mixer.music.unpause() #取消背景音乐暂停
                self.__update_sprites()
            else:
                PlaneGame.pause_game(self)
            # 播放精灵动画
            self.__animate()
            #6.更新/显示
            # 7.绘制游戏中相关信息
            self.draw_text()

            pygame.display.update()
            self.screen.fill(BLACK)


    #暂停游戏
    def pause_game(self):
        pygame.mixer.music.pause()
        #global  running
       # while running:
         #   pass
    #事件监听函数
    def __event_handler(self):
        for event in pygame.event.get():

            #判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over(self)
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    PlaneGame.__game_over(self)

            #处理定时器事件____英雄发射子弹事件
            elif event.type == HERO_FIRE_EVENT:
                self.show_hero.fire()


            #处理按键响应，使用键盘提供的方法获取键盘按键---返回一个元组，用过索引判断是否持续处理键盘时间
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_ESCAPE]:
                self.__game_over()

            self.show_hero.speed = [0,0]
            if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]:
                self.show_hero.speed[0] = 10
                print("向右移动。。。")
            if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]:
                self.show_hero.speed[0] = -10
                print("向左移动。。。")
            if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
                self.show_hero.speed[1] = 10
                print("向下移动。。。")
            if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
                self.show_hero.speed[1] = -10
                print("向上移动。。。")
            if self.show_hero.speed[0] and self.show_hero.speed[1]:
                self.show_hero.speed[0] /= 1.414
                self.show_hero.speed[1] /= 1.414

    #碰撞检测
    def __check_collide(self):

        global  score
        #子弹摧毁敌机
        hits = pygame.sprite.groupcollide(self.enemy_group,self.show_hero.bullet_group,False,True)
        for hit in hits:
            score += 150 - hit.enemy_size
            if hit.energy < 36:
                hit.real_time_energy = 0
            else:
                hit.real_time_energy -= 20
            if hit.real_time_energy <= 0:
            #random.choice(expl_sounds).play()
                enemy2_down_sound.play()
                expl = explosion.Explosion(hit.rect.center, 'lg')
                self.expl_group.add(expl)
                hit.kill()
        #敌机撞毁英雄__发挥发生碰撞的敌机列表
        enemies = pygame.sprite.spritecollide(self.show_hero,self.enemy_group,True,pygame.sprite.collide_mask)
        for hit in enemies:
            #player.shield -= hit.radius * 2
            expl2 = explosion.Explosion(hit.rect.center, 'sm')
            self.expl_group.add(expl2)
            """if player.shield <= 0:
                running = False
            """
        #如果被摧毁的敌机列表有内容，摧毁英雄
        #if len(enemies):
            #time.sleep(3)
            #self.show_hero.kill()

    #更新和绘制精灵，精灵组
    def __update_sprites(self):

        global last_update
        now = pygame.time.get_ticks()

        #背景精灵
        self.back_group.update()
        self.back_group.draw(self.screen)

        #英雄精灵

        self.show_hero.update()
        self.show_hero.draw(self.screen)

        #子弹精灵
        self.show_hero.bullet_group.update()
        self.show_hero.bullet_group.draw(self.screen)

        #敌机精灵
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        #爆炸精灵
        self.expl_group.update()
        self.expl_group.draw(self.screen)

    #播放精灵动画
    def __animate(self):

        global last_update
        now = pygame.time.get_ticks()

        if now - last_update > 50:
            last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.hero_frames)
            self.show_hero.image = self.hero_frames[self.current_frame].image
            self.show_hero.mask = self.hero1.mask
            #self.show_hero.rect = self.hero_frames[self.current_frame].rect

    #绘制游戏时相关信息
    def draw_text(self):

        #绘制分数
        score_font = pygame.font.Font("font/font.ttf", 36)
        score_text = score_font.render("Score : %s" % str(score), True, WHITE)
        self.screen.blit(score_text, (10, 5))

        #绘制血条
        for each in self.enemy_group:

            if each.enemy_size > 36:
                pygame.draw.line(self.screen, BLACK, \
                                 (each.rect.left, each.rect.top - 5), \
                                 (each.rect.right, each.rect.top - 5), \
                                 2)
                # 当生命大于20%显示绿色，否则显示红色
                energy_remain = each.real_time_energy / each.energy
                if energy_remain > 0.3:
                    energy_color = GREEN
                else:
                    energy_color = RED
                pygame.draw.line(self.screen, energy_color, \
                                 (each.rect.left, each.rect.top - 5), \
                                 (each.rect.left + each.rect.width * energy_remain, \
                                  each.rect.top - 5), 2)
    #游戏结束，定义为静态方法
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()




if __name__ == "__main__":

    try:
        #创建游戏对象
        game = PlaneGame()
        #启动游戏
        game.start_game()
    #异常处理
    except SystemExit:
        pass
    except:
        #输出错误信息
        traceback.print_exc()
        #退出程序
        pygame.quit()
        #等待用户输入，防止窗体一闪而过
        #input()


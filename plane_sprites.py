import pygame
import sys
import traceback

#初始化pygame模块，获取当前设备的分辨率
pygame.init()
vInfo = pygame.display.Info()#获取当前屏幕分辨率返回值中vInfo.current_w, vInfo.current_h分别表示当前窗口的宽和高

#屏幕大小的常量
SIZE = width, height = vInfo.current_w, vInfo.current_h #width, height = 1366, 768
#设置刷新帧率
FPS = 60
#设置游戏运行状态变量
running = True
#用于延时
last_update = 0
#用于标记是否转换图片
switch_image = True
#颜色
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
#英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT
#获得分数
score = 0


class GameSpirte(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self,image_name,speed = [0,1]):

        #调用父类的初始化方法
        super().__init__()

        #定义对象的属性
        self.image = pygame.image.load(image_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = speed

        # 加载图片数据
        #self.load_images(image_name)

    def update(self):

        #在屏幕的垂直方向上移动
        self.rect.y += self.speed[1]


    """
    def load_images(self,image_name = []):
        self.images = []
        for len in len(image_name):
            self.images.append(pygame.image.load(image_name[len]).convert_alpha())
    """


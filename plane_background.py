from plane_sprites import*


class Background(GameSpirte):
    """移动游戏背景精灵"""

    def __init__(self,image_name = "images/background/background.png",  is_alt = False):
        """alt用来表示是否是第二个背景精灵，如果是，则将其绘制在屏幕上方，实现两张背景图片一起滚动"""

        #1.调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__(image_name)
        if is_alt:
            self.rect.top = -self.rect.height

    def update(self):
        #1.调用父类的方法实现
        super().update()

        #2。判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.top >= height:
            self.rect.top = -self.rect.height
    #def load_images(self):
        #self.backgroundstar =


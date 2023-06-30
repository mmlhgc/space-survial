# 好好学习，天天向上
# 学习菜狗：Amao
# 开发时间：2023/6/30 13:39
import pygame


class Ship():
    def __init__(self, screen):
        '''初始化飞船并将其设置为其初始位置'''
        self.screen = screen

        # 加载飞船并获得其外接矩形
        new_image = pygame.image.load('img/player.png')
        self.image = pygame.transform.scale(new_image, (50, 38))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船防在屏幕中央位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

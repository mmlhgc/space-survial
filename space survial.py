# 好好学习，天天向上
# 学习菜狗：Amao
# 开发时间：2023/6/30 9:46

import pygame
from settings import Settings
from ship import Ship

def run_game():
    # 初始化一个游戏并创建屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('space-survial')
    clock = pygame.time.Clock()
    running = True

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while running:
        clock.tick(10)
        # 监视鼠标键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    run_game()

import pygame
import sys

class Pumpkin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 스프라이트 이미지
        images_name = [f'images/walking/walk{n}.png' for n in range(1, 11)]
        self.images = [pygame.image.load(name).convert_alpha() for name in images_name]

        """다른방법 
        self.images = [pygame.image.load(f'images/walking/walk{n}.png')
                                         .convert_alpha() for n in range(1, 11)]
        """
        # 스프라이트 위치, 크기
        # self.rect = pygame.Rect(250, 150, 150, 198)
        # 자주 쓰이는 방법
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect().move(250, 150)


    def update(self):
        # 조건이 True일 때의 실행 내용 if 조건 False일 때 실행 내용
        self.index = self.index + 1 if self.index + 1 < len(self.images) else 0
        self.image = self.images[self.index]
        """
        tmp = self.index + 1
        if tmp == len(self.images):
            self.index = 0
        else:
            self.index = tmp
        """
        # 앞으로 나아가게 하는 코드 (화면에 지나면 안보임)
        # dx = 5
        # self.rect.x += dx

        self.rect.x = self.rect.x + 5
        if self.rect.x >= 640:
            self.rect.x = 0


class AnimPumpkin:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(pygame.Color('pink'))
        self.pumpkin = Pumpkin()
        self.pumpkin_grp = pygame.sprite.Group(self.pumpkin)
        self.clock = pygame.time.Clock()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.pumpkin_grp.clear(self.screen, self.background)
        self.pumpkin_grp.update()
        self.pumpkin_grp.draw(self.screen)
        pygame.display.flip()

    def do_anim(self):
        fps = 50
        # frame per second
        keep_going = True
        while keep_going:
            self.clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_going = False

            self.render()

        sys.exit(0)


if __name__ == '__main__':
    anim = AnimPumpkin()
    anim.do_anim()

import random
import sys
import pygame

SCREEN = pygame.display.set_mode((640, 480))

class Mole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/mole/mole.gif').convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        rand_x = random.randint(0, SCREEN.get_width())
        rand_y = random.randint(0, SCREEN.get_height())
        self.rect.center = (rand_x, rand_y)

        # 두더지가 화면 밖으로 벗어나지 않도록 설정 하려면?
        # => rand_x 와 rand_y를 조정

class RandomMole:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('두더지 잡기')

        # self.background = pygame.Surface(SCREEN.get_size())
        # self.background.fill(pygame.Color('black'))
        # SCREEN.blit(self.background, (0, 0))

        # 두더지 만들기
        self.mole = Mole()
        self.mole_group = pygame.sprite.Group(self.mole)

        self.clock = pygame.time.Clock()

    def render(self):
        # self.mole_group.clear(SCREEN, self.background)
        self.mole_group.update()
        # self.mole.update() 자동호출
        # 전역변수 스크린 사용
        SCREEN.fill('black')
        self.mole_group.draw(SCREEN)
        pygame.display.flip()

    def gen_mole(self):
        fps = 10
        keep_going = True
        while keep_going:
            self.clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 두더지의 스프라이트가 겹치는 점 클릭한 점이 있다면
                    if self.mole.rect.collidepoint(pygame.mouse.get_pos()):
                        # move 함수 호출한다
                        self.mole.move()
            self.render()

        sys.exit(0)

if __name__ == '__main__':
    mole = RandomMole()
    mole.gen_mole()
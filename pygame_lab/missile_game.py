import sys
import pygame
import random

SCREEN = pygame.display.set_mode((640, 480))

class Missile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/missile/missile.png').convert_alpha()
        self.rect = self.image.get_rect()
        x, y = SCREEN.get_size()
        self.rect.center = (random.randint(0, x), y)
        # 델타 y 값 지정
        self.dy = random.randint(5, 15)

    def update(self):
        self.rect.centery = self.rect.centery - self.dy

        if self.rect.top < 0:
            self.image = pygame.image.load('images/missile/bang.png').convert_alpha()
            self.rect.top = 0


class FireMissile:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Fire Missile_미사일 발사 게임")
        self.background = pygame.Surface(SCREEN.get_size())
        self.background.fill(pygame.Color('black'))
        SCREEN.blit(self.background, (0, 0))

        self.missile_group = pygame.sprite.Group()
        for n in range(3):
            self.missile_group.add(Missile())

        self.clock = pygame.time.Clock()

    def render(self):
        self.missile_group.clear(SCREEN, self.background)
        #화면 지우고 업데이트 > 일반적인 방법
        self.missile_group.update()
        self.missile_group.draw(SCREEN)

        pygame.display.flip()

    def fire(self):
        fps = 100
        # 3개 미사일 추가
        # for num in range(3):
        #    self.missile_group.add(Missile())
        keep_going = True

        while keep_going:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_going = False
                    # pygame.quit()
                    # break
            for missile in self.missile_group.sprites():
                if missile.rect.top == 0:
                    self.missile_group.remove(missile)
                    self.missile_group.add(Missile())

            self.render()

        sys.exit(0)


if __name__ == '__main__':
    game = FireMissile()
    game.fire()
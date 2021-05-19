import pygame
import sys

class PacmanGame:
    def __init__(self):
        pygame.init() #pygame의 init()실행
        self.screen = pygame.display.set_mode((640, 480)) #screen 속성
        pygame.display.set_caption('Image Surface Processing') # 윈도우 캡션

        imgs = ['blinky.png','clyde.png','cobra.png','inky.png','pinky.png']
        imgs = ['images/pacman/'+file for file in imgs]
        self.chars = [pygame.image.load(img).convert() for img in imgs]

        # 배경 속성
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background_img = pygame.image.load('images/pacman/pacman_intro.png').convert()

        self.clock = pygame.time.Clock()

    def render(self, pos):
        self.screen.blit(self.background, (0, 0))
        self.background.blit(self.background_img, (0, 0))
        for name in self.chars:
            x, y = pos
            pos = ((x+80)%600, y)
            self.screen.blit(name, pos)

        pygame.display.flip()

    def game_loop(self):
        keep_going = True
        pos = (x, y) = (0, 200)

        while keep_going:
            self.clock.tick(5) #frame rate 갱신 3-1

            for event in pygame.event.get(): #이벤트 획득
                if event.type == pygame.QUIT:
                    keep_going = False

            self.render(pos)

            x, y = pos
            pos = (x+10, y)

        sys.exit(0)


if __name__ == '__main__':
    pacman = PacmanGame()
    pacman.game_loop()
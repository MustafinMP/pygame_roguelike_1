import pygame, sys, os
from buttons import *
from field import *
from menu import *

FPS = 60
STEP = 64
size = width, height = 1200, 720
pygame.init()
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
lst = []


def load_image(name, colorkey=None):
    fullname = os.path.join('data/sprites', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class GameManager:
    '''Главный класс всей игры.'''

    def __init__(self):
        self.game_stack = [GameField()]

    def draw(self):
        self.game_stack[-1].draw(screen)


class Ball:
    def __init__(self, pos):
        self.pos = list(pos)
        self.vect_x = 3
        self.vect_y = 3
        print(pos)

    def draw(self):
        if self.pos[0] <= 20 or self.pos[0] >= width - 20:
            self.vect_x *= -1
        if self.pos[1] <= 20 or self.pos[1] >= height - 20:
            self.vect_y *= -1
        self.pos[0] += self.vect_x
        self.pos[1] += self.vect_y
        pygame.draw.circle(screen, (250, 0, 0), self.pos, 20)


def terminate():
    pygame.quit()
    sys.exit()


def draw(pos):
    if pos is not None:
        ball = Ball(pos)
        lst.append(ball)
    for i in lst:
        i.draw()


if __name__ == '__main__':
    manager = GameManager()
    running = True
    while running:
        screen.fill((0, 0, 0))
        pos = None
        for event in pygame.event.get():
            size = width, height = pygame.display.get_window_size()
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.circle(screen,
                                   (0, 0, 255), event.pos, 20)
                pos = event.pos
        #     game_stack[-1].update(event)  # обработка событий
        # game_stack[-1].update_()  # движение и прочие события
        draw(pos)
        manager.draw()
        pygame.display.flip()
        clock.tick(FPS)

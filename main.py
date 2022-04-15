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

    def active_update(self, event):
        pass

    def passive_update(self, size):
        self.game_stack[-1].passive_update(size)


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    manager = GameManager()
    running = True
    while running:
        screen.fill((0, 0, 0))
        pos = None
        size = width, height = pygame.display.get_window_size()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            manager.active_update(event)
        manager.passive_update(size)
        manager.draw()
        pygame.display.flip()
        clock.tick(FPS)

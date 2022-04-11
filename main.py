import pygame, sys, os

FPS = 60
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
lst = []


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


class AbstractButton(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, args):
        if self.rect.collidepoint(args[0].pos):
            # match args[0].type:
                pass

    def is_pressed(self):
        pass


class AbstractActionButton(pygame.sprite.Sprite):
    def __init__(self, x, y, pressed_image, not_pressed_image, *group):
        super().__init__(*group)
        self.images = {True: load_image(pressed_image),
                       False: load_image(not_pressed_image)
        }
        self.pressed = False
        self.image = self.images[self.pressed]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, args):
        if self.rect.collidepoint(args[0].pos):
            match args[0].type:
                case pygame.MOUSEBUTTONDOWN:
                    self.pressed = False
                    self.image = self.images[self.pressed]
                case pygame.MOUSEBUTTONUP:
                    self.pressed = False
                    self.image = self.images[self.pressed]

    def is_pressed(self):
        return self.pressed


class Ball:
    def __init__(self, pos):
        self.pos = list(pos)
        self.vect_x = 3
        self.vect_y = 3
        print(pos)

    def draw(self):
        if self.pos[0] <= 20 or self.pos[0] >= 780:
            self.vect_x *= -1
        if self.pos[1] <= 20 or self.pos[1] >= 580:
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
    running = True
    while running:
        screen.fill((0, 0, 0))
        pos = None
        for event in pygame.event.get():
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

        pygame.display.flip()
        clock.tick(FPS)
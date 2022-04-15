import pygame
import main


class AbstractButton(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.image = main.load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, args):
        pass

    def is_pressed(self):
        pass


class AbstractActionButton(pygame.sprite.Sprite):
    def __init__(self, x, y, pressed_image, not_pressed_image, *group):
        super().__init__(*group)
        self.images = {True: main.load_image(pressed_image),
                       False: main.load_image(not_pressed_image)
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

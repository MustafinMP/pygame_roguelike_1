import pygame
import main
import player
import json

Group = pygame.sprite.Group
Sprite = pygame.sprite.Sprite


class GameField:
    '''
    Игровое поле.

    Отвечает непосредственно за игровой процесс (декорации, игроки, кнопки).
    '''

    def __init__(self):
        self.player_group = Group()
        self.enemies_group = Group()
        self.walls_group = Group()
        self.floor_group = Group()
        self.doors_group = Group()

        file = open('data/levels/level_1.json')
        level_data = json.load(file)

        self.player_coords = level_data['start_coords']
        self.player = player.Player(list(map(lambda i: i * main.STEP, self.player_coords)),
                                    self.player_group)

        variance = self.player.get_variance()
        for floor_group in level_data['floor'].keys():
            for coords in level_data['floor'][floor_group]:
                Floor(coords[0] * main.STEP, coords[1] * main.STEP, floor_group + '.png', variance,  self.floor_group)

        for wall_group in level_data['walls'].keys():
            for coords in level_data['walls'][wall_group]:
                Wall(coords[0] * main.STEP, coords[1] * main.STEP, wall_group + '.png', variance, self.walls_group)

    def draw(self, screen):
        self.floor_group.draw(screen)
        self.walls_group.draw(screen)
        self.player_group.draw(screen)
        self.enemies_group.draw(screen)

    def active_update(self, event):
        match event.type:

            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        self.player.update_vector('y', - main.SPEED)
                    case pygame.K_DOWN:
                        self.player.update_vector('y', main.SPEED)
                    case pygame.K_RIGHT:
                        self.player.update_vector('x', main.SPEED)
                    case pygame.K_LEFT:
                        self.player.update_vector('x', - main.SPEED)
                    case pygame.K_LSHIFT:
                        self.player.game_position['x'] += main.SPEED

            case pygame.KEYUP:
                match event.key:
                    case pygame.K_UP:
                        self.player.stop_vector('y')
                    case pygame.K_DOWN:
                        self.player.stop_vector('y')
                    case pygame.K_RIGHT:
                        self.player.stop_vector('x')
                    case pygame.K_LEFT:
                        self.player.stop_vector('x')

    def passive_update(self, size):
        self.player.passive_update(size, self.walls_group, self.doors_group)
        variance = self.player.get_variance()
        for sprite in self.floor_group.sprites():
            sprite.passive_update(variance)
        for sprite in self.walls_group.sprites():
            sprite.passive_update(variance)


class Floor(Sprite):
    def __init__(self, x, y, image, variance, *group):
        super().__init__(*group)
        self.image = main.load_image(image)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.rect.x, self.rect.y = x - variance[0], y - variance[1]

    def passive_update(self, offset):
        self.rect.x = self.position[0] - offset[0]
        self.rect.y = self.position[1] - offset[1]


class Wall(Sprite):
    def __init__(self, x, y, image, variance, *group):
        super().__init__(*group)
        self.image = main.load_image(image)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.rect.x, self.rect.y = x - variance[0], y - variance[1]

    def passive_update(self, offset):
        self.rect.x = self.position[0] - offset[0]
        self.rect.y = self.position[1] - offset[1]


class Door(Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.images = {False: main.load_image('closed_door.png'),
                       True: main.load_image('opened_door.png')}
        self.image = self.images[False]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_opened = False

    def ping_the_door(self):
        self.is_opened = not self.is_opened
        self.image = self.images[self.is_opened]

from pygame.sprite import Sprite, Group
import main
import player
import json


class GameField:
    '''Игровое поле. Отвечает непосредственно за игровой процесс (декорации, игроки, кнопки).'''

    def __init__(self):
        self.player_group = Group()
        self.enemies_group = Group()
        self.walls_group = Group()
        self.floor_group = Group()

        file = open('data/levels/level_1.json')
        level_data = json.load(file)

        self.player_coords = level_data['start_coords']
        self.player = player.Player(self.player_coords, self.player_group)

        for floor_group in level_data['floor'].keys():
            for coords in level_data['floor'][floor_group]:
                Floor(coords[0] * main.STEP, coords[1] * main.STEP, floor_group + '.png', self.floor_group)

    def draw(self, screen):
        self.player_group.draw(screen)
        self.enemies_group.draw(screen)
        self.walls_group.draw(screen)
        self.floor_group.draw(screen)

    def passive_update(self, size):
        self.player.passive_update(size)


class Floor(Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.image = main.load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.image = main.load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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

from pygame.sprite import Sprite, Group
import main


class Player(Sprite):
    def __init__(self, position, *group):
        super().__init__(*group)
        self.image = main.load_image('knight_f_idle_anim_f0.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = [main.width // 2 - self.rect.width // 2,
                                    main.height // 2 - self.rect.height // 2]
        self.game_position = position

    def passive_update(self, size):
        x, y = size
        self.rect.x, self.rect.y = [x // 2 - self.rect.width // 2,
                                    y // 2 - self.rect.height // 2]


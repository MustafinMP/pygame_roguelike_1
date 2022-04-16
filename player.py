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
        self.vector_x = 0
        self.vector_y = 0

    def passive_update(self, size):
        x, y = size
        self.rect.x, self.rect.y = [x // 2 - self.rect.width // 2,
                                    y // 2 - self.rect.height // 2]
        self.game_position[0] += self.vector_x
        self.game_position[1] += self.vector_y

    def get_variance(self):
        return [self.game_position[0] - self.rect.x,
                self.game_position[1] - self.rect.y - self.rect.height + main.STEP]

    def update_vector(self, key, speed):
        match key:
            case 'x':
                if self.vector_x == 0 or speed == self.vector_x:
                    self.vector_x = speed
            case 'y':
                if self.vector_y == 0 or speed == self.vector_y:
                    self.vector_y = speed

    def stop_vector(self, key):
        match key:
            case 'x':
                self.vector_x = 0
            case 'y':
                self.vector_y = 0


class HpDisplay:
    pass  # TODO: сделать класс для отображения ХП в виде сердечек

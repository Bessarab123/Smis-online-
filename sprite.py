"""ТУт должны быть спрайты различных объектов таких как игрок объекты архитектуры и тп"""
import pygame
import os
from const import SIZE, WHITE


def load_image(name, k=1):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    image = pygame.transform.scale(image, (SIZE * k, SIZE * k))
    image.set_colorkey(WHITE)
    return image


class Sprites(pygame.sprite.Sprite):
    def __init__(self, x, y, *group: pygame.sprite.Group):
        super().__init__(group)
        self.rect.x += x
        self.rect.y += y
        self.mask = self.image.get_masks()


class Player(Sprites):
    image_left = load_image('player1face — копия.bmp')
    image_right = pygame.transform.flip(image_left, True, False)
    image_0 = load_image("player1face.bmp")

    def __init__(self, x, y, name, *group):
        self.name = name
        self.image = Player.image_left
        self.rect = self.image.get_rect()
        self.state = 0
        self.v = 2
        super().__init__(x, y, group)

    def change_state(self, state):
        """state ==
        1 - left
        2 - right
        0 - Who I'm?"""
        if state == 1:
            if not (self.image is self.image_left):
                self.image = self.image_left
        elif state == 2:
            if not (self.image is self.image_right):
                self.image = self.image_right
        elif state == 0:
            if not (self.image is self.image_0):
                self.image = self.image_0


class Fountain(Sprites):
    image = load_image("fountain.bmp", 3)

    def __init__(self, x, y, *group):
        self.rect = self.image.get_rect()
        super().__init__(x, y, group)


class Grass(Sprites):
    image = load_image("grass.bmp", 2)

    def __init__(self, x, y, *group):
        self.rect = self.image.get_rect()
        super().__init__(x, y, group)

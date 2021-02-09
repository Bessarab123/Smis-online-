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


class Player(Sprites):
    image_left = load_image('Lol.bmp')
    image_right = pygame.transform.flip(image_left, True, False)

    def __init__(self, x, y, name, *group):
        self.name = name
        self.image = Player.image_left
        self.rect = self.image.get_rect()
        self.status = 0
        self.v = 4
        super().__init__(x, y, group)

    def change_status(self, text):
        if text == "L":
            if not (self.image is self.image_left):
                self.image = self.image_left
        elif text == "R":
            if not (self.image is self.image_right):
                self.image = self.image_right


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

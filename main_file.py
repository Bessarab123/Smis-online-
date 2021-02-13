import pygame

screen = pygame.display.set_mode((1, 1))  # Нужно создать окно чуть раньше
from const import *
from sprite import *


def main_circle():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((2 ** 9, 2 ** 9))
    all_sprite = pygame.sprite.Group()
    lis = []
    lis.append(Player(0, 0, 'kos', all_sprite))
    players = [lis[-1]]
    lis.append(Fountain(100, 100, all_sprite))
    im = load_image('grass.bmp', 2)
    top, left = -10, 0
    x, y = 0, 0
    while True:
        screen.fill(BLACK)
        if left > -256: left -= 256  # Я НЕ ПОНИМАЮ ПОЧЕМУ ОНО РАБОТАЕТ
        if left < -256: left += 256
        if top > -256: top -= 256  # Я ОПЯТЬ НЕ ПОНИМАЮ ПОЧЕМУ ОНО РАБОТАЕТ
        if top < -256: top += 256
        for i in range(5):
            for j in range(5):
                screen.blit(im, (left + 256 * i, top + 256 * j))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return
            elif event.type == 1025:
                pass
            elif event.type == 1026:
                pass
            elif event.type == 1024:
                x1, y1 = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[1]:
                    for obj in all_sprite:
                        dx = x - x1
                        dy = y - y1
                        obj.rect.x -= dx
                        obj.rect.y -= dy
                        left -= dx / 2  # TODO понять почему надо делить на два
                        top -= dy / 2

                x, y = x1, y1
        if pygame.key.get_pressed()[pygame.K_UP]:
            players[0].rect.y -= players[0].v
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            players[0].rect.y += players[0].v
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            players[0].rect.x -= players[0].v
            players[0].change_state(1)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            players[0].rect.x += players[0].v
            players[0].change_state(2)
        if not (pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN]):
            players[0].change_state(0)

        all_sprite.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    main_circle()
    exit()

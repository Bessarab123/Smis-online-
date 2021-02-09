import pygame
screen = pygame.display.set_mode((500, 500))
from const import *
from sprite import *


def main_circle():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    all_sprite = pygame.sprite.Group()
    lis = []
    lis.append(Grass(0, 0, all_sprite))
    lis.append(Player(0, 0, 'kos', all_sprite))
    players = []
    players.append(lis[-1])
    lis.append(Fountain(100, 100, all_sprite))

    x, y = 0, 0
    while True:
        screen.fill(WHITE)
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
                        obj.rect.x -= x - x1
                        obj.rect.y -= y - y1
                x, y = x1, y1
        if pygame.key.get_pressed()[pygame.K_UP]:
            players[0].rect.y -= 2
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            players[0].rect.y += 2
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            players[0].rect.x -= 2
            players[0].change_status('L')
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            players[0].rect.x += 2
            players[0].change_status('R')



        all_sprite.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    main_circle()
    exit()

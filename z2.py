import sys
import os
import pygame
from Samples.geocoder import get_coordinates
from Samples.mapapi_PG import show_map

if __name__ == '__main__':
    toponym_to_find = " ".join(sys.argv[1:])

    if toponym_to_find:
        ranning = True
        zoom = 10
        lat, lon = get_coordinates(toponym_to_find)

        map_file = 'map.png'
        # Инициализируем pygame
        pygame.init()
        screen = pygame.display.set_mode((600, 450))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_PAGEUP:
                        if zoom < 23:
                            zoom += 1
                    elif event.key == pygame.K_PAGEDOWN:
                        if zoom > 0:
                            zoom -= 1
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 4 and zoom < 23:
                        zoom += 1
                    elif event.button == 5 and zoom > 0:
                        zoom -= 1
            ll_spn = f'll={lat},{lon}&z={zoom}'
            point_param = f'pt={lat},{lon}'
            show_map(ll_spn, 'map', point_param)
            screen.blit(pygame.image.load(map_file), (0, 0))
            pygame.display.flip()
        pygame.quit()

        # Удаляем за собой файл с изображением.
        os.remove(map_file)

    else:
        print('Нет данных')

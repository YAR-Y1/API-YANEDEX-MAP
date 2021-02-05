import sys
import os
import math
import pygame
from Samples.geocoder import get_coordinates
from Samples.mapapi_PG import show_map

LON_STEP = 0.01
LAT_STEP = 0.025

if __name__ == '__main__':
    toponym_to_find = [i for i in input('Что вы хотите найти?').split()]
    if toponym_to_find:
        ranning = True
        zoom = 10
        lat_M, lon_M = get_coordinates(toponym_to_find)
        lat, lon = lat_M, lon_M
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
                    elif event.key == pygame.K_PAGEUP:
                        if zoom < 23:
                            zoom += 1
                    elif event.key == pygame.K_PAGEDOWN:
                        if zoom > 0:
                            zoom -= 1
                    elif event.key == pygame.K_UP:
                        lon += LON_STEP * 2 ** (15 - zoom)
                    elif event.key == pygame.K_DOWN:
                        lon -= LON_STEP * 2 ** (15 - zoom)
                    elif event.key == pygame.K_RIGHT:
                        lat += LAT_STEP * 2 ** (15 - zoom)
                    elif event.key == pygame.K_LEFT:
                        lat -= LAT_STEP * 2 ** (15 - zoom)
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 4 and zoom < 23:
                        zoom += 1
                    elif event.button == 5 and zoom > 0:
                        zoom -= 1
                if lon > 85:
                    lon = 85
                if lon < -85:
                    lon = -85
                if lat > 180:
                    lat = 180
                if lat < -180:
                    lat = -180
                print(lat)
                print(lon)
                print()
            ll_spn = f'll={lat},{lon}&z={zoom}'
            point_param = f'pt={lat_M},{lon_M}'
            show_map(ll_spn, 'map', point_param)
            screen.blit(pygame.image.load(map_file), (0, 0))
            pygame.display.flip()
        pygame.quit()

        # Удаляем за собой файл с изображением.
        os.remove(map_file)

    else:
        print('Нет данных')

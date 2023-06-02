import pygame, time, math, random, os, sys
clock = pygame.time.Clock()
from pygame.locals import *
from images import *

pygame.init() 
pygame.display.set_caption("Magic Mushroom")

height = 640
length = 1120
FPS = 60

WINDOW_SIZE = (length,height)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((length/2, height/2))

TILE_SIZE = grass_image.get_width()

def mapper(datei):
    game_map = []
    game_map_t = []
    with open(datei, "r") as file:
        for line in file:
            for char in line:
                game_map_t.append(char)
            game_map.append(game_map_t)
            game_map_t = []
    return game_map 

def blitter(map):
    tile_rects = []
    y = 0
    for row in map:
        x = 0
        for tile in row:
            # Blöcke: ----------------------------------------------------------
            if tile == '1':
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '3':
                display.blit(stone_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '4':
                #display.blit(shroom_pink_image, (x * TILE_SIZE, y * TILE_SIZE))
                pass
            if tile == '5':
                #display.blit(shroom_pink_image, (x * TILE_SIZE, y * TILE_SIZE))
                pass

            # Obstacles: -------------------------------------------------------
            if tile == '6':
                display.blit(shroom_green_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '7':
                display.blit(shroom_red_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '8':
                display.blit(shroom_glow_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '9':
                display.blit(shroom_pink_image, (x * TILE_SIZE, y * TILE_SIZE))

            if tile == '1' or tile == "2" or tile == "3" or tile == "4" or tile == "5":
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    return tile_rects

game_map = mapper("levels/level_1.txt")

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

moving_right = False
moving_left = False

player_y_momentum = 0
air_timer = 0

player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100,100,100,50)

while True: # game loop
    display.fill((146,244,255))

    tile_rects = blitter(mapper("levels/level_1.txt"))

    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum > 3:
        player_y_momentum = 3

    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom']:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1

    display.blit(player_image_real, (player_rect.x, player_rect.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 

        if event.type == KEYDOWN:
            if event.key == K_d: #rechts
                moving_right = True
                player_image_real = player_image

            if event.key == K_a: #links
                moving_left = True
                player_image_real = player_image_r

            if event.key == K_SPACE:
                if air_timer < 6:
                    player_y_momentum = -5
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(FPS)
import pygame, time, math, random, os, sys
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init() 
pygame.display.set_caption("Magic Mushroom")

height = 640
length = 1120

WINDOW_SIZE = (length,height)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((length/2, height/2))

GReeeN = (0, 255, 0)
schwarz = (0, 0 , 0)
white = (255, 255, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
lightblue = (173, 216, 230)

player_image = pygame.image.load('images/wiz.png').convert()
player_image = pygame.transform.scale(player_image, (20, 20))
player_image.set_colorkey((0, 0, 0))

grass_image = pygame.image.load('world/grass.png')
TILE_SIZE = grass_image.get_width()

dirt_image = pygame.image.load('world/dirt.png')

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
            if tile == '1':
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    return tile_rects

game_map = mapper("overworld.txt")

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

    tile_rects = blitter(mapper("overworld.txt"))

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

    display.blit(player_image, (player_rect.x, player_rect.y))

    for event in pygame.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if air_timer < 6:
                    player_y_momentum = -5
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps

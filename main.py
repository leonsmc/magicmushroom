import pygame, time, math, random, class_ as c, function_ as f

pygame.init()
pygame.display.set_caption("Magic Mushroom")

height = 640
length = 800

block_c_height = height/16
block_c_length = length/16

GReeeN = (0, 255, 0)
schwarz = (0, 0 , 0)
white = (255, 255, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
lightblue = (173, 216, 230)

player_image = pygame.image.load('images/wiz.png')
player_image = pygame.transform.scale(player_image, (40, 40))
player_image.set_colorkey((0, 0, 0))

game_map = [
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','3','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2','2','2','2'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','3','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','3','0','0','0','0'],
    ['2','2','0','0','0','3','0','0','0','0','0','3','0','0','0','0','0','2','2','2','2','2','2','2','2'],
    ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

grass_image = pygame.image.load('world/grass.png')
grass_image = pygame.transform.scale(grass_image, (32, 32))


TILE_SIZE = grass_image.get_width()

dirt_image = pygame.image.load('world/dirt.png')
dirt_image = pygame.transform.scale(dirt_image, (32, 32))

shroom_p_image = pygame.image.load('world/shroom_pink.png')
shroom_p_image = pygame.transform.scale(shroom_p_image, (32, 32))

FPS = 60
running = True

WINDOW_SIZE = (length, height) # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

clock = pygame.time.Clock()

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(lightblue)
    pressed = pygame.key.get_pressed()

    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                screen.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                screen.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == "3":
                screen.blit(shroom_p_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    screen.blit(player_image, (100, 100))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
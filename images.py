import pygame

pygame.init() 

player_image = pygame.image.load('world/wiz_r.png')
player_image = pygame.transform.scale(player_image, (20, 20))
player_image.set_colorkey((0, 0, 0))

player_image_r = pygame.image.load('world/wiz_l.png')
player_image_r = pygame.transform.scale(player_image_r, (20, 20))
player_image_r.set_colorkey((0, 0, 0))

player_image_real = player_image

player_image = pygame.transform.scale(player_image, (20, 20))
player_image.set_colorkey((0, 0, 0))

grass_image = pygame.image.load('world/grass.png')

dirt_image = pygame.image.load('world/dirt.png')

pink_image = pygame.image.load('world/shroom_pink.png')
pink_image.set_colorkey((0, 0, 0)) 

GReeeN = (0, 255, 0)
schwarz = (0, 0 , 0)
white = (255, 255, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
lightblue = (173, 216, 230)

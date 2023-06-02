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
stone_image = pygame.image.load("world/stone.png")

shroom_pink_image = pygame.image.load('world/shroom_pink.png')
shroom_pink_image.set_colorkey((0, 0, 0)) 
shroom_glow_image = pygame.image.load("world/shroom_glow.png")
shroom_glow_image.set_colorkey((51,51,51))
shroom_red_image = pygame.image.load('world/shroom_red.png')
shroom_red_image.set_colorkey((0, 0, 0))  
shroom_green_image = pygame.image.load('world/shroom_green.png')
shroom_green_image.set_colorkey((0, 0, 0))

GReeeN = (0, 255, 0)
schwarz = (0, 0 , 0)
white = (255, 255, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
lightblue = (173, 216, 230)

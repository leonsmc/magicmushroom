import pygame

pygame.init() 

player_image = pygame.image.load('world/wiz_r.png')
player_image = pygame.transform.scale(player_image, (16, 16))
player_image.set_colorkey((0, 0, 0))

player_image_r = pygame.image.load('world/wiz_l.png')
player_image_r = pygame.transform.scale(player_image_r, (16, 16))
player_image_r.set_colorkey((0, 0, 0))

player_image_real = player_image

player_image = pygame.transform.scale(player_image, (16, 16))
player_image.set_colorkey((0, 0, 0))

grass_image = pygame.image.load('world/grass.png')
dirt_image = pygame.image.load('world/dirt.png')
stone_image = pygame.image.load("world/stone.png")
stone_dark_image = pygame.image.load("world/stone_dark.png")

shroom_pink_image = pygame.image.load('world/shroom_pink.png')
shroom_pink_image = pygame.transform.scale(shroom_pink_image, (32, 32))
shroom_pink_image.set_colorkey((0, 0, 0)) 
shroom_glow_image = pygame.image.load("world/shroom_glow.png")
shroom_glow_image = pygame.transform.scale(shroom_glow_image, (32, 32))
shroom_glow_image.set_colorkey((51,51,51))
shroom_red_image = pygame.image.load('world/shroom_red.png')
shroom_red_image = pygame.transform.scale(shroom_red_image, (32, 32))
shroom_red_image.set_colorkey((0, 0, 0))  
shroom_green_image = pygame.image.load('world/shroom_green.png')
shroom_green_image = pygame.transform.scale(shroom_green_image, (32, 32))
shroom_green_image.set_colorkey((0, 0, 0))

game_over_image = pygame.image.load('world/black.png')


GReeeN = (0, 255, 0)
schwarz = (0, 0 , 0)
white = (255, 255, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)
lightblue = (173, 216, 230)

font = pygame.font.Font('freesansbold.ttf', 32)

level_1_location = [(64 ,96), (156*2, 144*2), (288*2, 208*2), (250*2, 288*2), (40*2, 208*2), (16*2, 144*2), (208*2, 32*2)]
level_2_location = [(80*2, 16*2), (240*2, 128*2), (214*2, 16*2), (48*2, 80*2), (110*2, 272*2), (280*2, 272*2), (186*2, 192*2)]
level_3_location = [(80*2, 16*2), (214*2, 16*2), (288*2, 80*2), (208*2, 128*2), (272*2, 16*2), (240*2, 256*2), (62*2, 208*2),(114*2, 240*2), (30*2, 128*2), (114*2, 192*2)]
level_4_location = [(80*2, 16*2), (214*2, 144*2), (118*2, 112*2), (48*2, 16*2), (32*2, 224*2), (46*2, 288*2), (266*2, 240*2), (256*2, 160*2)]

var = 1
shroom_location = (32, 640-64)

running = True
x = True
uwu = True
lawnmower = True
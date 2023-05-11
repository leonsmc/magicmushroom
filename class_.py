import pygame, time, math, random

plane_i = pygame.image.load("images/plane.png")
plane_i = pygame.transform.scale(plane_i, (60, 60))
plane_r = plane_i.get_rect()

class Plane:
    def __init__(self, x, y, height, width, color):
        self.x = x - width / 2
        self.y = y - height / 2
        self.height = height
        self.width = width
        self.color = color
        self.rect = pygame.Rect(x, y, height, width)
        self.surface = pygame.Surface((height, width)) # 1
        self.surface.blit(plane_i, (0, 0))
        self.angle = 0
        self.speed = 0 # 2

    def draw(self, screen): # 3
        self.rect.topleft = (int(self.x), int(self.y))
        rotated = pygame.transform.rotate(self.surface, self.angle)
        surface_rect = self.surface.get_rect(topleft = self.rect.topleft)
        new_rect = rotated.get_rect(center = surface_rect.center)
        screen.blit(rotated, new_rect.topleft)
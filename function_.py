import pygame, time, math, random

def move_car_wasd(class_, pressed_key):
    class_.speed *= 0.9 # 5
    if pressed_key[pygame.K_w]: class_.speed += 0.5 # 6
    if pressed_key[pygame.K_s]: class_.speed -= 0.5 # 6
    if pressed_key[pygame.K_a]: class_.angle += class_.speed / 2 # 7
    if pressed_key[pygame.K_d]: class_.angle -= class_.speed / 2 # 7
    class_.x -= class_.speed * math.sin(math.radians(class_.angle)) # 8
    class_.y -= class_.speed * math.cos(math.radians(-class_.angle)) # 8

def check_collision(player_rect, obstacle_rect, radius): 
    player_center = (player_rect.centerx, player_rect.centery)
    obstacle_center = (obstacle_rect.centerx, obstacle_rect.centery)

    distance = math.sqrt((player_center[0] - obstacle_center[0]) ** 2 + (player_center[1] - obstacle_center[1]) ** 2)

    if distance <= radius:
        return True
    else:
        return False
    
def wasd_move(rect, speed):
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_d]:
        rect.move_ip(speed, 0)
    if pressed_key[pygame.K_w]:
        rect.move_ip(0, -speed)
    if pressed_key[pygame.K_a]:
        rect.move_ip(-speed, 0)
    if pressed_key[pygame.K_s]:
        rect.move_ip(0, speed)
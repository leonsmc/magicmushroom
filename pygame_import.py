import pygame, math, random

def wasd_move_ud(rect, speed): # moves rect only up and down
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        rect.move_ip(0, -speed)
    if pressed_key[pygame.K_s]:
        rect.move_ip(0, speed)

def wasd_move_lr(rect, speed): # moves rect only left and right
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_a]:
        rect.move_ip(-speed, 0)
    if pressed_key[pygame.K_d]:
        rect.move_ip(speed, 0)

def arrow_move(rect, speed): # moves rect with the arrowkeys and given speed
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_RIGHT]:
        rect.move_ip(speed, 0)
    if pressed_key[pygame.K_UP]:
        rect.move_ip(0, -speed)
    if pressed_key[pygame.K_LEFT]:
        rect.move_ip(-speed, 0)
    if pressed_key[pygame.K_DOWN]:
        rect.move_ip(0, speed)

def wasd_move(rect, speed): # moves rect with the arrowkeys and given speed
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_d]:
        rect.move_ip(speed, 0)
    if pressed_key[pygame.K_w]:
        rect.move_ip(0, -speed)
    if pressed_key[pygame.K_a]:
        rect.move_ip(-speed, 0)
    if pressed_key[pygame.K_s]:
        rect.move_ip(0, speed)

def random_movement(rect, speed, c, ct): # Moves enemy in random directions for ... secs
    if ct == 40:
        c = random.randint(1, 8)
        ct = 0
        
    if c == 1:
        rect.move_ip(speed, 0)
    if c == 2:
        rect.move_ip(0, -speed)
    if c == 3:
        rect.move_ip(-speed, 0)
    if c == 4:
        rect.move_ip(0, speed)
    if c == 5:
        rect.move_ip(speed, speed)
    if c == 6:
        rect.move_ip(-speed, speed)
    if c == 7:
        rect.move_ip(speed, -speed)
    if c == 8:
        rect.move_ip(-speed, -speed)
    
    ct += 1
    return c, ct

def check_collision(player_rect, obstacle_rect, radius): #Checks if rect1 collides with rect2 in given radius
    # Calculate the center point of each rectangle
    player_center = (player_rect.centerx, player_rect.centery)
    obstacle_center = (obstacle_rect.centerx, obstacle_rect.centery)

    # Calculate the distance between the center points
    distance = math.sqrt((player_center[0] - obstacle_center[0]) ** 2 + (player_center[1] - obstacle_center[1]) ** 2)

    # Check if the distance is less than the given radius
    if distance <= radius:
        return True
    else:
        return False

def move_enemy_follow(enemy_image, enemy_rect, player_rect, speed): # Makes enemy_rect follow player_rect with given speed
    if player_rect.x < enemy_rect.x:
        enemy_rect.move_ip(-speed, 0)
    if player_rect.x > enemy_rect.x:
        enemy_rect.move_ip(speed, 0)
    if player_rect.y < enemy_rect.y:
        enemy_rect.move_ip(0, -speed)
    if player_rect.y > enemy_rect.y:
        enemy_rect.move_ip(0, speed)

def move_enemy_line(enemy_image, enemy_rect, player_rect, speed): # Makes enemy_rect follow player_rect if he passes him he continues in a straight line
    enemy_rect.move_ip(-speed, 0)
    if enemy_rect.x >  player_rect.x:
        if player_rect.y < enemy_rect.y:
            enemy_rect.move_ip(0, -speed)
        if player_rect.y > enemy_rect.y:
            enemy_rect.move_ip(0, speed)

def move_enemy_random(enemy_rect, length, heigth, speed): # Moves rect from right to left and spawns it new on the right with random heigth
     enemy_rect.move_ip(-speed, 0)
     if enemy_rect.x == 0:
        enemy_rect.x = length
        enemy_rect.y = random.randint(0, heigth)
     
def move_enemy_ud(enemy_rect, speed): # Moves the rect downwards with given speed
    enemy_rect.move_ip(0, speed)

def move_enemy_lr(enemy_rect, speed): # Moves the rect from left to right with given speed
    enemy_rect.move_ip(speed, 0)
 
def move_enemy_rl(enemy_rect, speed): # Moves the rect from roght to left with given speed
    enemy_rect.move_ip(-speed, 0)
 
def borders(rect, height, length): # Pops the rect off the borders of the window. also returns a True value
    if rect.y > 10:
        wasd_move(rect, 3)
    if rect.y < 0:
        rect.move_ip(0, 10)

    if rect.y  < height-10:
        wasd_move(rect, 3)
    if rect.y > height - 40:
        rect.move_ip(0, -10)
    
    if rect.x > 10:
        wasd_move(rect, 3)
    if rect.x < 0:
        rect.move_ip(10, 0)

    if rect.x  < length-10:
        wasd_move(rect, 3)
    if rect.x > length - 40:
        rect.move_ip(-10, 0)
    return True

def border_tp(rect, length, height): # If rect leaves the screen it appears on the opposite side again. also returns a True value
    # If rect leaves the right edge, wrap to the left edge
    if rect.right < 0:
        rect.left = length

    # If rect leaves the left edge, wrap to the right edge
    if rect.left > length:
        rect.right = 0

    # If rect leaves the bottom edge, wrap to the top edge
    if rect.bottom < 0:
        rect.top = height

    # If rect leaves the top edge, wrap to the bottom edge
    if rect.top > height:
        rect.bottom = 0
    return True

def rot_center(image, angle): # Rotates the given image once on its own center for "angle" degree

    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def move_car_class_wasd(class_, pressed_key):
    class_.speed *= 0.9 # 5
    if pressed_key[pygame.K_w]: class_.speed += 0.5 # 6
    if pressed_key[pygame.K_s]: class_.speed -= 0.5 # 6
    if pressed_key[pygame.K_a]: class_.angle += class_.speed / 2 # 7
    if pressed_key[pygame.K_d]: class_.angle -= class_.speed / 2 # 7
    class_.x -= class_.speed * math.sin(math.radians(class_.angle)) # 8
    class_.y -= class_.speed * math.cos(math.radians(-class_.angle)) # 8

def move_car_class_arrow(class_, pressed_key):
    class_.speed *= 0.9 # 5
    if pressed_key[pygame.K_UP]: class_.speed += 0.5 # 6
    if pressed_key[pygame.K_DOWN]: class_.speed -= 0.5 # 6
    if pressed_key[pygame.K_LEFT]: class_.angle += class_.speed / 2 # 7
    if pressed_key[pygame.K_RIGHT]: class_.angle -= class_.speed / 2 # 7
    class_.x -= class_.speed * math.sin(math.radians(class_.angle)) # 8
    class_.y -= class_.speed * math.cos(math.radians(-class_.angle)) # 8

def draw_borders(coords, color, thickness):
    """
    Draw borders between coordinates in a list using Pygame's draw.line function
    """
    screen = pygame.display.get_surface()
    for i in range(len(coords)-1):
        pygame.draw.line(screen, color, coords[i], coords[i+1], thickness)
import random

def random_movement_border(rect, speed, c, ct, coords):
    if ct == 40:
        c = random.randint(1, 8)
        ct = 0
        
    # Calculate the next position of the enemy based on the movement direction
    next_pos = rect.move(0, 0)
    if c == 1:
        next_pos.move_ip(speed, 0)
    elif c == 2:
        next_pos.move_ip(0, -speed)
    elif c == 3:
        next_pos.move_ip(-speed, 0)
    elif c == 4:
        next_pos.move_ip(0, speed)
    elif c == 5:
        next_pos.move_ip(speed, speed)
    elif c == 6:
        next_pos.move_ip(-speed, speed)
    elif c == 7:
        next_pos.move_ip(speed, -speed)
    elif c == 8:
        next_pos.move_ip(-speed, -speed)
    
    # Check if the next position of the enemy is within the boundary defined by the coords list
    if is_within_boundary(next_pos, coords):
        rect.move_ip(next_pos.x - rect.x, next_pos.y - rect.y)
    
    ct += 1
    return c, ct

def is_within_boundary(rect, coords):
    # Check if the rectangle defined by rect is within the boundary defined by the coords list
    for i in range(len(coords)):
        p1 = coords[i]
        p2 = coords[(i + 1) % len(coords)]
        if not is_within_line(rect, p1, p2):
            return False
    return True

def is_within_line(rect, p1, p2):
    # Check if the rectangle defined by rect is within the line defined by p1 and p2
    if p1[0] == p2[0]:
        # Vertical line
        if p1[0] < rect.left or p1[0] > rect.right:
            return False
        if p1[1] < p2[1]:
            return rect.top >= p1[1] and rect.bottom <= p2[1]
        else:
            return rect.top >= p2[1] and rect.bottom <= p1[1]
    else:
        # Horizontal line
        if p1[1] < rect.top or p1[1] > rect.bottom:
            return False
        if p1[0] < p2[0]:
            return rect.left >= p1[0] and rect.right <= p2[0]
        else:
            return rect.left >= p2[0] and rect.right <= p1[0]

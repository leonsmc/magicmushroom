import pygame, time, math, random, sys
clock = pygame.time.Clock()
from pygame.locals import *
from images import *



pygame.init() 
pygame.display.set_caption("Magic Mushroom")

height = 640
length = 640
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

def check_collision(player_rect, location, radius):
    # Calculate the distance between the player's center and the location
    player_center = player_rect.center
    distance = math.sqrt((player_center[0]*2 - location[0])**2 + (player_center[1]*2 - location[1])**2)
    
    # Check if the distance is less than or equal to the radius
    if distance <= radius:
        return True
    else:
        return False
    
def collision(player_rect, obstacle_rect):
    if player_rect.colliderect(obstacle_rect):
        return True
    return False
    

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
                display.blit(stone_dark_image, (x * TILE_SIZE, y * TILE_SIZE))
                pass
            if tile == '5':
                #
                pass


            if tile == '1' or tile == "2" or tile == "3" or tile == "4" or tile == "5":
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    return tile_rects

level1_map = mapper("levels/level_1.txt")

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
timer = 7*60
level = 1
zeit_gesamt = 0
minuten = 0
punkte = 0



player_rect = pygame.Rect(32, 32, player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100,100,100,50)

while True: # game loop
    if zeit_gesamt == 60*60:
        zeit_gesamt -= 60*60
        minuten += 1
    zeit_anzeige = font.render(f"Punkte: {punkte} / Zeit: {round(timer/60)}", True, "white")
    zeit_anzeige_rect = zeit_anzeige.get_rect()
    zeit_ges_anzeige = font.render(f"Zeit: {minuten}min {round(zeit_gesamt/60)}s", True, "white")
    punkte_ges_anzeige = font.render(f"{punkte} Punkte", True, "white")

    timer -= 1
    if level <= 4:
        zeit_gesamt += 1
    if timer <= 0 and level <= 4:
        level += 1
        timer = 7*60

    if level == 1:
        display.fill("black")
        tile_rects = blitter(mapper("levels/level_1.txt"))
        if kopf == 0:
            player_rect.center=(40, 16*2)
            kopf += 1

    elif level == 2:
        display.fill(lightblue)
        tile_rects = blitter(mapper("levels/level_2.txt"))
        if kopf == 1:
            player_rect.center=(40, 16*2)
            kopf += 1

    elif level == 3:
        display.fill(lightblue)
        tile_rects = blitter(mapper("levels/level_3.txt"))
        if kopf == 2:
            player_rect.center=(40, 16*2)
            kopf += 1
    elif level == 4:
        display.fill("black")
        tile_rects = blitter(mapper("levels/level_4.txt"))
        if kopf == 3:
            player_rect.center=(40, 16*2)
            kopf += 1
    elif level > 4:
        if kopf == 4:
            player_rect.center=(40, 16*2)
            kopf = 0
        display.fill("black")
        tile_rects = blitter(mapper("levels/level_end.txt"))
        display.blit(restart_image, restart_rect)
        display.blit(exit_image, exit_rect)
        
        if collision(player_rect, exit_rect):
            sys.exit()
        if collision(player_rect, restart_rect):
            level = 1
            zeit_gesamt = 0
            minuten = 0
            timer = 0
            punkte = 0

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
            sys.exit()

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
    if level <= 4:
        screen.blit(zeit_anzeige, zeit_anzeige_rect)
    else:
        screen.blit(game_over_image, (0, 0))
        screen.blit(surf, (0, 0))
        screen.blit(zeit_ges_anzeige, (320-100, 220))
        screen.blit(punkte_ges_anzeige, (320-70, 270))
        neuer_highscore = punkte

        # Pfad zur Textdatei
        dateipfad = "highscore.txt"

        # Highscore aus der Datei lesen
        with open(dateipfad, "r") as datei:
            alter_highscore = int(datei.read())

        # Überprüfen, ob der neue Highscore größer ist
        if neuer_highscore > alter_highscore:
            # Den neuen Highscore in die Datei schreiben
            with open(dateipfad, "w") as datei:
                datei.write(str(neuer_highscore))
        with open(dateipfad, "r") as datei:
            highscore = int(datei.read())

        highscore_anzeige = font.render(f"Highscore: {highscore}", True, "white")
        screen.blit(highscore_anzeige, (320-100, 170))

    if level == 1:
        if check_collision(player_rect, shroom_location, 32) == True:
            shroom_location = level_1_location[random.randint(0,6)]
            timer += 140
            punkte += 100
        screen.blit(shroom_pink_image, shroom_location)
    
    if level == 2:
        if x == True:
            shroom_location = (80*2, 16*2)
            x = False
        if var == 1:
            screen.blit(shroom_red_image, shroom_location)
            if check_collision(player_rect, shroom_location, 32) == True:
                shroom_location = level_2_location[random.randint(0,6)]
                timer += 90
                punkte += 120
                var = random.randint(1,2)
        if var == 2:
            screen.blit(shroom_green_image, shroom_location)
            if check_collision(player_rect, shroom_location, 32) == True:
                shroom_location = level_2_location[random.randint(0,6)]
                timer += 180
                punkte += 50
                var = random.randint(1,2)

    if level == 3:
        if uwu == True:
            shroom_location = (80*2, 16*2)
            uwu = False
        if var == 1:
            screen.blit(shroom_red_image, shroom_location)
            if check_collision(player_rect, shroom_location, 32) == True:
                shroom_location = level_3_location[random.randint(0, len(level_3_location)-1)]
                timer += 60
                punkte += 120
                var = random.randint(1,3)
        if var == 2:
            screen.blit(shroom_pink_image, shroom_location)
            if check_collision(player_rect, shroom_location, 32) == True:
                shroom_location = level_3_location[random.randint(0, len(level_3_location)-1)]
                timer += 180 
                punkte += 100
                var = random.randint(1,3)
        if var == 3:
            screen.blit(shroom_green_image, shroom_location)
            if check_collision(player_rect, shroom_location, 32) == True:
                shroom_location = level_3_location[random.randint(0, len(level_3_location)-1)]
                timer += 100
                punkte += 50
                var = random.randint(1,3)

    if level == 4:
        if lawnmower == True:
            shroom_location = (80*2, 16*2)
            lawnmower = False
        if var == 1:
            screen.blit(shroom_glow_image, shroom_location)
            if check_collision(player_rect, shroom_location, 32) == True:
                shroom_location = level_4_location[random.randint(0, 7)]
                timer += 140
                punkte += 180
                var = random.randint(3,4)
        if var == 2:
            screen.blit(shroom_red_image, shroom_location)
            if check_collision(player_rect, shroom_location, 32) == True:
                shroom_location = level_4_location[random.randint(0, 7)]
                timer += 180
                punkte += 120
                var = random.randint(2,4)
        if var == 3:
            screen.blit(shroom_green_image, shroom_location)
            if check_collision(player_rect, shroom_location, 32) == True:
                shroom_location = level_4_location[random.randint(0, 7)]
                timer += 100
                punkte += 50
                var = random.randint(1,2)
        if var == 4:
            screen.blit(shroom_pink_image, shroom_location)
            if check_collision(player_rect, shroom_location, 32) == True:
                shroom_location = level_4_location[random.randint(0, 7)]
                timer += 200
                punkte += 100
                var = random.randint(1,3)

    if level > 4:
        while running == True:
            player_rect.center = (320/2, 280)
            running = False

        
        #screen.blit(shroom_pink_image, shroom_location)
    
    pygame.display.update()
    clock.tick(FPS)
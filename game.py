import pygame as pg
import os
import sys
from random import randint
from pygame.math import Vector2
from constants import *
from pixelleap_models.player import Player
from pixelleap_models.enemy import Enemy
from pixelleap_models.goal import Goal
from pixelleap_models.spike import Spike
from pixelleap_models.platforms import Platform
from pixelleap_models.movingPlatform import MovingPlatform
from pixelleap_models.coin import Coin

# functions
# -----------------------------------------------------------------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_player_rect(player: Player) -> pg.Rect:
    return pg.Rect(
        int(player.p.x - player.w // 2),
        int(player.p.y - player.h // 2),
        player.w,
        player.h
    )

def get_platform_rect(platform: Platform) -> pg.Rect:
    return pg.Rect(platform.x, platform.y, platform.w, platform.h)

def get_moving_platform_rect(movingPlatform: MovingPlatform) -> pg.Rect:
    return pg.Rect(movingPlatform.x, movingPlatform.y, movingPlatform.w, movingPlatform.h)

def get_coin_rect(coin: Coin) -> pg.Rect:
    return pg.Rect(coin.x - coin.r, coin.y - coin.r, coin.r * 2, coin.r * 2)

def get_goal_rect(goal: Goal) -> pg.Rect:
    return pg.Rect(goal.x, goal.y, goal.w, goal.h) 

def get_spike_rect(spike: Spike) -> pg.Rect:
    return pg.Rect(spike.x, spike.y, spike.w, spike.h)

def get_enemy_rect(enemy: Enemy) -> pg.Rect:
    return pg.Rect(int(enemy.x), int(enemy.y), enemy.w, enemy.h)

def draw_player(screen, player: Player):
    rect = get_player_rect(player)
    pg.draw.rect(screen, (41, 128, 185), rect)
    head_h = rect.height // 3
    head_rect = pg.Rect(rect.x, rect.y, rect.width, head_h)
    pg.draw.rect(screen, (52, 73, 94), head_rect)
    visor_y = rect.y + 6
    visor_w = rect.width - 8
    pg.draw.rect(screen, (241, 196, 15), (rect.x + 4, visor_y, visor_w, 4))
    pg.draw.rect(screen, (231, 76, 60), (rect.x + 2, rect.y + head_h, rect.width - 4, 3))
    pg.draw.rect(screen, (30, 30, 30), (rect.x, rect.bottom - 6, rect.width, 6))

def draw_background(screen):
    screen.fill((20, 24, 45))
  
    pg.draw.rect(screen, (241, 196, 15), (650, 50, 60, 60))
    pg.draw.rect(screen, (20, 24, 45), (665, 50, 45, 45)) 
    
    stars = [(100, 80), (250, 40), (400, 120), (550, 60), (750, 150), (50, 200), (320, 180)]
    for sx, sy in stars:
        pg.draw.rect(screen, (255, 255, 255), (sx, sy, 4, 4))
        
    castle_color = (30, 35, 60)
    pg.draw.rect(screen, castle_color, (100, 300, 80, 300)) 
    pg.draw.rect(screen, castle_color, (300, 250, 100, 350)) 
    pg.draw.rect(screen, castle_color, (600, 280, 90, 320)) 
    
    pg.draw.rect(screen, (25, 30, 50), (0, 400, 800, 200))
    
    for i in range(100, 180, 20): pg.draw.rect(screen, castle_color, (i, 280, 10, 20))
    for i in range(300, 400, 25): pg.draw.rect(screen, castle_color, (i, 230, 15, 20))
    for i in range(600, 690, 20): pg.draw.rect(screen, castle_color, (i, 260, 10, 20))

def draw_platform(screen, platform: Platform):
    rect = get_platform_rect(platform)
    pg.draw.rect(screen, PLATFORM_COLOR, rect)

def draw_goal(screen, goal: Goal):
    rect = get_goal_rect(goal)
    
    pg.draw.rect(screen, (139, 69, 19), rect)
    
    lid_rect = pg.Rect(rect.x, rect.y, rect.width, rect.height // 2)
    pg.draw.rect(screen, (101, 67, 33), lid_rect)
    
    gold = (255, 215, 0)
    pg.draw.rect(screen, gold, (rect.x, rect.y, rect.width, 4)) 
    pg.draw.rect(screen, gold, (rect.x, rect.bottom - 4, rect.width, 4)) 
    pg.draw.rect(screen, gold, (rect.x, rect.y, 4, rect.height)) 
    pg.draw.rect(screen, gold, (rect.right - 4, rect.y, 4, rect.height)) 
    
    mid_y = rect.y + rect.height // 2
    pg.draw.rect(screen, gold, (rect.x, mid_y - 2, rect.width, 4))
    
    lock_size = 10
    lock_x = rect.x + (rect.width - lock_size) // 2
    lock_y = mid_y - (lock_size // 2)
    pg.draw.rect(screen, (192, 192, 192), (lock_x, lock_y, lock_size, lock_size)) 
    pg.draw.rect(screen, (0, 0, 0), (lock_x + 3, lock_y + 3, 4, 5)) 

def draw_moving_platform(screen, movingPlatform: MovingPlatform):
    rect = get_moving_platform_rect(movingPlatform)
    pg.draw.rect(screen, MOVING_PLATFORM_COLOR, rect)

def draw_coin(screen, coin: Coin):
    if not coin.collected:
        # outer edge
        pg.draw.circle(screen, COIN_COLOR, (coin.x, coin.y), coin.r)
        # inner circle
        pg.draw.circle(screen, COIN_COLOR_2ND, (coin.x, coin.y), coin.r - 3)
        # Shining Glow
        pg.draw.circle(screen, COIN_COLOR_3RD, (coin.x - 2, coin.y - 2), coin.r // 3)

def draw_spike(screen, spike: Spike):
    num_spikes = spike.w // 15
    if num_spikes < 1:
        num_spikes = 1
    spike_width = spike.w / num_spikes
    for i in range(num_spikes):
        x_left = spike.x + i * spike_width
        x_right = spike.x + (i + 1) * spike_width
        x_mid = x_left + spike_width / 2
        spike_points = [
            (x_left, spike.y + spike.h),   # Bottom left angle
            (x_right, spike.y + spike.h),  # Bottom right angle
            (x_mid, spike.y)               # Peak of spike
        ]
        pg.draw.polygon(screen, SPIKE_COLOR, spike_points)
        # spike_points for draw triangle

def draw_enemy(screen, enemy: Enemy):
    rect = get_enemy_rect(enemy)
    # Enemy body
    pg.draw.rect(screen, enemy.color, rect)
    # Eyes
    eye_y = int(enemy.y + enemy.h * 0.3)
    eye_size = max(3, enemy.w // 6)
    left_eye_x = int(enemy.x + enemy.w * 0.25)
    right_eye_x = int(enemy.x + enemy.w * 0.75 - eye_size)
    pg.draw.rect(screen, WHITE_COLOR, (left_eye_x, eye_y, eye_size, eye_size))
    pg.draw.rect(screen, WHITE_COLOR, (right_eye_x, eye_y, eye_size, eye_size))

def draw_platforms(screen):
    global platforms
    for platform in platforms:
        draw_platform(screen, platform)

def draw_moving_platforms(screen):
    global moving_platforms
    for moving_platform in moving_platforms:
        draw_moving_platform(screen, moving_platform)

def draw_coins(screen):
    global coins
    for coin in coins:
        draw_coin(screen, coin)

def draw_spikes(screen):
    global spikes
    for spike in spikes:
        draw_spike(screen, spike)

def draw_enemies(screen):
    global enemies
    for enemy in enemies:
        draw_enemy(screen, enemy)

def game_win_screen():
    global points, game_lose, game_win, controls_active
    font_win = pg.font.SysFont("Segoe UI", 48)
    font_text = pg.font.SysFont("Nirmala UI", 36)
    text = font_win.render("--- GAME WINNER! ---", True, GREEN_COLOR)
    text_points = font_text.render(f"POINTS COLLECTED : {points}", True, WHITE_COLOR)
    text_enter =  font_text.render("Press ENTER to play again", True, WHITE_COLOR)
    screen.fill(BG_COLOR)
    screen.blit(text, (SCREEN_W // 2 - text.get_width() // 2, 50))
    screen.blit(text_points, (SCREEN_W // 2 - text_points.get_width() // 2, SCREEN_H // 2))
    screen.blit(text_enter, (SCREEN_W // 2 - text_enter.get_width() // 2, SCREEN_H // 1.3))
     # Check for Enter to restart
    keys = pg.key.get_pressed()
    if keys[pg.K_RETURN]:
        reset_level()
        game_win = False
        game_lose = False
        player.lives = 3
        controls_active = True
        win_sound.stop()

def game_lose_screen():
    global points, game_win, game_lose, controls_active
    font_lose = pg.font.SysFont("Segoe UI", 48)
    font_text = pg.font.SysFont("Nirmala UI", 36)
    text = font_lose.render("--- GAME LOSER! ---", True, RED_COLOR)
    text_points = font_text.render(f"POINTS COLLECTED : {points}", True, WHITE_COLOR)
    text_enter =  font_text.render("Press ENTER to play again", True, WHITE_COLOR)
    screen.fill(BG_COLOR)
    screen.blit(text, (SCREEN_W // 2 - text.get_width() // 2, 50))
    screen.blit(text_points, (SCREEN_W // 2 - text_points.get_width() // 2, SCREEN_H // 2))
    screen.blit(text_enter, (SCREEN_W // 2 - text_enter.get_width() // 2, SCREEN_H // 1.3))
     # Check for Enter to restart
    keys = pg.key.get_pressed()
    if keys[pg.K_RETURN]:
        reset_level()
        game_win = False
        game_lose = False
        player.lives = 3
        controls_active = True
        lose_sound.stop()

def controls_screen():
    rect = pg.Rect(0, 0, 400, 400)
    rect.center = (SCREEN_W // 2, SCREEN_H // 2)
    # box for show/hide controls
    pg.draw.rect(screen, BG_COLOR, rect)
    # border
    pg.draw.rect(screen, WHITE_COLOR, rect, 2)
    # text
    controls = [
    ("WASD / ARROWS", "Move"),
    ("SPACE", "Jump"),
    ("W / UP ARROW", "Jump"),
    ("C", "Controls"),
    ("ESC", "Quit"),
    ("R", "Reset")
    ]
    y = rect.y + 100
    for left, right in controls:
        left_text = font.render(left, True, (255, 255, 255))
        right_text = font.render(right, True, (255, 255, 255))
        # crtanje u dve kolone
        screen.blit(left_text, (rect.x + 20, y))
        screen.blit(right_text, (rect.right - right_text.get_width() - 20, y))
        y += 35
    
def text_points():
    global font
    text_points = font.render(f"Points: {points}", True, WHITE_COLOR)
    screen.blit(text_points, (10, 10))

def text_deaths():
    global font
    text_lives = font.render(f"Lives left: {player.lives}", True, WHITE_COLOR)
    screen.blit(text_lives, (SCREEN_W // 1.27, 10))

def collision_player_coin():
    global points
# Check collision beetween player and coin
    player_rect = get_player_rect(player)
    for coin in coins:
        if not coin.collected and player_rect.colliderect(get_coin_rect(coin)):
            coin.collected = True
            coin_sound.play()
            points += coin.value

def collision_player_spikes():
    global deaths
    player_rect = get_player_rect(player)
    for spike in spikes:
        if player_rect.colliderect(get_spike_rect(spike)):
            player.lives -= 1
            hit_sound.play()
            reset_player(player)
            return
        
def collision_player_enemy():
    player_rect = get_player_rect(player)
    for enemy in enemies:
        if player_rect.colliderect(get_enemy_rect(enemy)):
            player.lives -= 1
            hit_sound.play()
            reset_player(player)
            return

def check_win():
    global game_win, controls_active
    if not game_win and get_player_rect(player).colliderect(get_goal_rect(goal)):
        game_win = True 
        controls_active = False
        win_sound.play()
        
def check_lose():
    global game_lose, controls_active
    if not game_lose and player.lives == 0:
        game_lose = True
        controls_active = False
        lose_sound.play()

def update_player(player: Player, platforms, moving_platforms):
    keys = pg.key.get_pressed()
    player.v.x = 0
    # movement keys
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        player.v.x = -PLAYER_SPEED
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        player.v.x = PLAYER_SPEED
    # Jump if player is on ground and not jumped, if someone press space or w or up arrow and if player on ground do jump
    if player.is_jumping == False:
        if keys[pg.K_SPACE] or keys[pg.K_w] or keys[pg.K_UP] and player.on_base:
            player.v.y = JUMP_SPEED
            player.on_base = False
            player.is_jumping = True
            jump_sound.play()
    # add gravity to player
    player.v.y += GRAVITY

    # All platforms checking for collision
    all_platform_rects = []
    for platform in platforms:
        all_platform_rects.append(get_platform_rect(platform))
    for moving_platform in moving_platforms:
        all_platform_rects.append(get_moving_platform_rect(moving_platform))

    # movement for player
    # move x 
    player.p.x += player.v.x
    rect = get_player_rect(player)

    # Check collision with platform x coordinate
    for platform in platforms:
        platform_rect = get_platform_rect(platform)
        if rect.colliderect(platform_rect):
            if player.v.x > 0:
                rect.right = platform_rect.left
            elif player.v.x < 0:
                rect.left = platform_rect.right
            player.p.x = rect.centerx

    # move y
    player.p.y += player.v.y
    rect = get_player_rect(player)
    player.on_base = False
    platform_below = None

    for platform_rect in all_platform_rects:
        if rect.colliderect(platform_rect):
            if player.v.y > 0:
                rect.bottom = platform_rect.top
                player.p.y = rect.centery
                player.v.y = 0
                player.on_base = True
                player.is_jumping = False
                platform_below = platform_rect
            elif player.v.y < 0:
                rect.top = platform_rect.bottom
                player.p.y = rect.centery
                player.v.y = 0
                player.is_jumping = True

    if player.on_base and platform_below:
        for moving_p in moving_platforms:
            moving_p_rect = get_moving_platform_rect(moving_p)
            if moving_p_rect == platform_below:
                player.p.x += moving_p.vx
                player.p.y += moving_p.vy
                break

    for platform in platforms:
        platform_rect = get_platform_rect(platform)
        if rect.colliderect(platform_rect):
            if player.v.x > 0: # fall
                rect.bottom = platform_rect.top
                player.p.y = rect.centery
                player.v.y = 0
                player.on_base = True
                player.is_jumping = False
            elif player.v.x < 0: # jump 
                rect.top = platform_rect.bottom
                player.p.y = rect.centery
                player.v.y = 0
                player.is_jumping = True

    # make screen borders for player (left/right)
    if rect.right > SCREEN_W:
        rect.right = SCREEN_W
        player.p.x = rect.centerx
    if rect.left < 0:
        rect.left = 0
        player.p.x = rect.centerx
    # check if player is below ground
    if rect.bottom > SCREEN_H:
        rect.bottom = SCREEN_H
        player.p.y = rect.centery
        player.v.y = 0
        # !IMPORTANT - set player to be on base when player touch bottom screen and set is_jumping to False
        player.on_base = True
        player.is_jumping = False
    
def update_moving_platform(movingPlatform: MovingPlatform):
    # Platform movement
    movingPlatform.x += movingPlatform.vx
    movingPlatform.y += movingPlatform.vy
    # Horizontal borders
    if movingPlatform.x <= movingPlatform.min_x:
        movingPlatform.x = movingPlatform.min_x
        movingPlatform.vx *= -1 # movingPlatform.vx = -movingPlatform.vx
    elif movingPlatform.x >= movingPlatform.max_x:
        movingPlatform.x = movingPlatform.max_x
        movingPlatform.vx *= -1 # movingPlatform.vx = -movingPlatform.vx
    # Vertical borders
    if movingPlatform.y <= movingPlatform.min_y:
        movingPlatform.y = movingPlatform.min_y
        movingPlatform.vy *= -1 # movingPlatform.vy = -movingPlatform.vy
    elif movingPlatform.y >= movingPlatform.max_y:
        movingPlatform.y = movingPlatform.max_y
        movingPlatform.vy *= -1 # movingPlatform.vy = -movingPlatform.vy

def update_enemy(enemy: Enemy):
    enemy.x += enemy.vx
    # Border reflection
    if enemy.x <= enemy.min_x:
        enemy.x = enemy.min_x
        enemy.vx *= -1 # enemy.vx = -enemy.vx
    elif enemy.x + enemy.w >= enemy.max_x:
        enemy.x = enemy.max_x - enemy.w
        enemy.vx *= -1 # enemy.vx = -enemy.vx

def update():
    # Update moving platoforms
    for moving_platform in moving_platforms:
        update_moving_platform(moving_platform)
    for enemy in enemies:
        update_enemy(enemy)
    update_player(player, platforms, moving_platforms)
    collision_player_spikes()
    collision_player_enemy()
    collision_player_coin()
    check_win()
    check_lose()

def draw():
    global game_win, game_lose
    draw_background(screen)
    # calling function for draw player on the screen
    draw_player(screen, player)
    # calling function for draw every platform from list
    draw_platforms(screen)
    # calling function for draw every moving platform from list
    draw_moving_platforms(screen)
    # calling function for draw every coin from list
    draw_coins(screen)
    # calling function for draw every spike from list
    draw_spikes(screen)
    # calling function for draw every enemy from list
    draw_enemies(screen)
    # calling function for draw goal from list
    draw_goal(screen, goal)
    # calling function for draw text for points
    text_points()
    text_deaths()
    if game_win:
        game_win_screen()
        player.p = Vector2(PLAYER_START_X, PLAYER_START_Y)
    if game_lose:
        game_lose_screen()
        player.p = Vector2(PLAYER_START_X, PLAYER_START_Y)

def reset_player(player: Player):
    player.p = Vector2(PLAYER_START_X, PLAYER_START_Y)
    player.v = Vector2(0, 0)
    player.on_base = False
 
def reset_level():
    global points, game_win 
    points = 0
    game_win = False
    reset_player(player)
    for enemy in enemies:
        enemy.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    for coin in coins:
        coin.collected = False
        coin.x = randint(PLAYER_START_X, SCREEN_W)
        coin.y = randint(240, 520)
#----------------------------------------------------------------------------------------
# Screen and clock
pg.init()
screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
clock = pg.time.Clock()

# Font
font = pg.font.SysFont(None, 36, bold=False, italic=False)

# Sounds
pg.mixer.init()

coin_sound = pg.mixer.Sound(resource_path("sfx/super-mario-coin-sound.mp3"))
coin_sound.set_volume(0.3)

jump_sound = pg.mixer.Sound(resource_path("sfx/maro-jump-sound-effect_1.mp3"))
jump_sound.set_volume(0.06)

win_sound = pg.mixer.Sound(resource_path("sfx/win-level-complete-mario.mp3"))
win_sound.set_volume(0.1)

lose_sound = pg.mixer.Sound(resource_path("sfx/five-nights-at-freddys-full-scream-sound_2.mp3"))
lose_sound.set_volume(0.1)

hit_sound = pg.mixer.Sound(resource_path("sfx/hit1.mp3"))
hit_sound.set_volume(0.1)

control_sound = pg.mixer.Sound(resource_path("sfx/the-rock-meme-sound-effect.mp3"))
control_sound.set_volume(0.1)

# Instance of player
player = Player(
    p = Vector2(PLAYER_START_X, PLAYER_START_Y),
    v = Vector2(0, 0),
    w = 30,
    h = 40,
    on_base = False,
    is_jumping = False,
    lives = 3
)
# List of platforms
platforms = [
    Platform(0, SCREEN_H - 40, SCREEN_W, 40), # ground
    Platform(150, 450, 150, 20),
    Platform(400, 350, 150, 20),
    Platform(550, 250, 150, 20)
]
# List of moving platforms
moving_platforms = [
    MovingPlatform(
        x=200, y=350, w=120, h=20,
        vx=2, vy=0,
        min_x=150, max_x=400,
        min_y=350, max_y=350
    ),
    MovingPlatform(
        x=500, y=400, w=100, h=20,
        vx=0, vy=1.5,
        min_x=500, max_x=500,
        min_y=300, max_y=500
    )
]
# List of coins
coins = [
    Coin(x=200, y=420, r=10, value=10),    # On platform
    Coin(x=580, y=240, r=10, value=10),    # On upper platform
    Coin(x=350, y=520, r=10, value=10),    # On ground
    Coin(x=650, y=520, r=10, value=10),    # On ground
    Coin(x=300, y=320, r=15, value=25)     # Bigger, more valuable coin
]
# List of spikes
spikes = [
    Spike(350, SCREEN_H - 55, 60, 15),   # On ground
    Spike(500, SCREEN_H - 55, 45, 15),   # On ground
    Spike(150, 435, 60, 15),           # On platform
]
# List of enemies
enemies = [
    # Enemy on ground
    Enemy(
        x=600, y=SCREEN_H - 70,
        w=30, h=30,
        vx=2,
        min_x=570, max_x=770, 
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
    ),
    # Enemy on platform
    Enemy(
        x=630, y=225,
        w=25, h=25,
        vx=1.5,
        min_x=550, max_x=700,
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
    ),
]
# Goal
goal = Goal( 700, 200, 40, 40 )

jumped = False
game_win = False
game_lose = False
points = 0
controls_clicked = False
controls_active = True
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_r:
                reset_level()
            if event.key == pg.K_c:
                controls_clicked = not controls_clicked
                if controls_active:
                    control_sound.play()   
    update()
    draw()
    if controls_clicked and controls_active:
        controls_screen()      
    pg.display.flip()
    clock.tick(FPS)
    pg.display.set_caption(f"Pixel Leap - Platformer game  |   fps: {round(clock.get_fps(), 2)}   |   Controls - c")
pg.quit()
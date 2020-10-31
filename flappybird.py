import pygame, sys, random, platform


separation_bar = r'\\' if platform.system() == 'Windows' else '/'
b = separation_bar

def draw_bg():
    screen.blit(bg_surface, (bg_x_position, 0))
    screen.blit(bg_surface, (bg_x_position + 378, 0))


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 600))
    screen.blit(floor_surface, (floor_x_pos + 378, 600))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 200))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 672:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 600:
        return False

    return True


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 2, 1)
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(180, 30))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(180, 30))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(180, 60))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pygame.init()
screen = pygame.display.set_mode((378, 672))
clock = pygame.time.Clock()

#game_font = pygame.font.Font('04B_19.ttf', 40) - issue
font = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font, 40)

# Game Variables
gravity = 1
bird_movement = 0
game_active = True
score = 0
high_score = 0

bg_surface = pygame.image.load(f'assets{b}background-night.png').convert()
bg_surface = pygame.transform.scale(bg_surface, [378, 672])
bg_x_position = 0

floor_surface = pygame.image.load(f'assets{b}base.png').convert()
#floor_surface = pygame.transform.scale2x(floor_surface)
floor_surface = pygame.transform.scale(floor_surface, [378, pygame.Surface.get_height(floor_surface)])
floor_x_pos = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load(f'assets{b}bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load(f'assets{b}bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load(f'assets{b}bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 336))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
# bird_surface = pygame.transform.scale2x(bird_surface)
# bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load(f'assets{b}pipe-green.png')
#pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 2000)
pipe_height = [380, 410, 440, 470] # Sequência: Maior altura > menor altura

game_over_surface = pygame.transform.scale2x(pygame.image.load(f'assets{b}message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(189, 336))

flap_sound = pygame.mixer.Sound(f'sound{b}sfx_wing.wav')
death_sound = pygame.mixer.Sound(f'sound{b}sfx_hit.wav')
score_sound = pygame.mixer.Sound(f'sound{b}sfx_point.wav')
score_sound_countdown = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and game_active:
                bird_movement = 0
                bird_movement -= 15
                flap_sound.play()
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 336)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            print(pipe_list)

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

    #screen.blit(bg_surface, (0, 0))

    bg_x_position -= 4
    draw_bg()
    if bg_x_position <= -378:
        bg_x_position = 0

    if game_active:
        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        score += 0.01
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -378:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(40)

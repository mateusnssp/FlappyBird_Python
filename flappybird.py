import pygame, sys, random

def draw_bg():
    screen.blit(bg_surface, (bg_x_position, 0))
    screen.blit(bg_surface, (bg_x_position + 378, 0))

def draw_floor():
    screen.blit(floor_surface, (floor_x_position, 600))
    screen.blit(floor_surface, (floor_x_position + 378, 600))

def create_pipe():
    random_pipe_position = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_position))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_position - 200))
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
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 600:
        return False

    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, bird_movement * 2, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return  new_bird, new_bird_rect

pygame.init()


# <Game variables>

SCREEN_WIDTH = 378
SCREEN_HEIGHT = 672


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

gravity = 1
bird_movement = 0
game_active = True
score = 0
high_score = 0

bg_surface = pygame.image.load('./assets/background-night.png').convert()
bg_surface = pygame.transform.scale(bg_surface, [SCREEN_WIDTH, SCREEN_HEIGHT])
#bg_surface = pygame.transform.scale2x(bg_surface)
bg_x_position = 0

floor_surface = pygame.image.load('./assets/base.png').convert()
#floor_surface = pygame.transform.scale2x(floor_surface)
floor_surface = pygame.transform.scale(floor_surface, [378, pygame.Surface.get_height(floor_surface)])
floor_x_position = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load('./assets/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('./assets/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('./assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 336))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# bird_surface = pygame.image.load('./assets/redbird-midflap.png').convert_alpha()
# bird_surface = pygame.transform.scale(bird_surface, (pygame.Surface.get_width(bird_surface) * 1, pygame.Surface.get_height(bird_surface) * 1))
# bird_surface = pygame.transform.scale2x(bird_surface)
# bird_rect = bird_surface.get_rect(center=(100, 336))

pipe_surface = pygame.image.load('./assets/pipe-green.png').convert()

pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 2000)
pipe_height =  [380, 410, 440, 470]  # Sequência: Maior altura > menor altura





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_active and event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                bird_movement = 0
                bird_movement -= 15
        if game_active == False and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            game_active = True
            pipe_list.clear()
            bird_rect.center = (100, 336)
            bird_movement = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            print(pipe_list)

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0



            bird_surface, bird_rect = bird_animation()




    bg_x_position -= 4
    draw_bg()
    if bg_x_position <= -378:
        bg_x_position = 0

    if game_active == True:

        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)


    # Floor
    floor_x_position -= 1
    draw_floor()
    if floor_x_position <= -378:
        floor_x_position = 0




    pygame.display.update()

    clock.tick(40)


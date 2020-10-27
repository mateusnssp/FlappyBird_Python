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

pygame.init()


# <Game variables>

SCREEN_WIDTH = 378
SCREEN_HEIGHT = 672


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

gravity = 1
bird_movement = 0

bg_surface = pygame.image.load('./assets/background-night.png').convert()
bg_surface = pygame.transform.scale(bg_surface, [SCREEN_WIDTH, SCREEN_HEIGHT])
#bg_surface = pygame.transform.scale2x(bg_surface)
bg_x_position = 0

floor_surface = pygame.image.load('./assets/base.png').convert()
#floor_surface = pygame.transform.scale2x(floor_surface)
floor_surface = pygame.transform.scale(floor_surface, [378, pygame.Surface.get_height(floor_surface)])
floor_x_position = 0

bird_surface = pygame.image.load('./assets/redbird-midflap.png').convert()
bird_surface = pygame.transform.scale(bird_surface, (pygame.Surface.get_width(bird_surface) * 1, pygame.Surface.get_height(bird_surface) * 1))
bird_rect = bird_surface.get_rect(center=(100, 336))

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
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                bird_movement = 0
                bird_movement -= 16
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            print(pipe_list)





    bg_x_position -= 4
    draw_bg()
    if bg_x_position <= -378:
        bg_x_position = 0



    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

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


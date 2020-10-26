import pygame, sys

def draw_bg():
    screen.blit(bg_surface, (bg_x_position, 0))
    screen.blit(bg_surface, (bg_x_position + 378, 0))

def draw_floor():
    screen.blit(floor_surface, (floor_x_position, 630))
    screen.blit(floor_surface, (floor_x_position + 378, 630))

def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (200, 357))
    return  new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        # screen.blit(pipe_surface, (200, 357))  # Base --> altura mímimo 357
        screen.blit(pipe_surface, pipe)

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
floor_surface = pygame.transform.scale(floor_surface, [378, 200])
floor_x_position = 0

bird_surface = pygame.image.load('./assets/redbird-midflap.png').convert()
bird_surface = pygame.transform.scale(bird_surface, (pygame.Surface.get_width(bird_surface) * 1, pygame.Surface.get_height(bird_surface) * 1))
bird_rect = bird_surface.get_rect(center=(100, 336))

pipe_surface = pygame.image.load('./assets/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)





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
            pipe_list.append(create_pipe())
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


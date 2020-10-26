import pygame, sys

def draw_bg():
    screen.blit(bg_surface, (bg_x_position, 0))
    screen.blit(bg_surface, (bg_x_position + 378, 0))

def draw_floor():
    screen.blit(floor_surface, (floor_x_position, 630))
    screen.blit(floor_surface, (floor_x_position + 378, 630))



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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 16





    bg_x_position -= 4
    draw_bg()
    if bg_x_position <= -378:
        bg_x_position = 0

    floor_x_position -= 1
    draw_floor()
    if floor_x_position <= -378:
        floor_x_position = 0

    bird_movement += gravity
    bird_rect.centery += bird_movement





    screen.blit(bird_surface, bird_rect)



    pygame.display.update()

    clock.tick(40)


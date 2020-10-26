import pygame, sys

def draw_bg():
    screen.blit(bg_surface, (bg_x_position, 0))
    screen.blit(bg_surface, (bg_x_position + 378, 0))

def draw_floor():
    screen.blit(floor_surface, (floor_x_position, 630))
    screen.blit(floor_surface, (floor_x_position + 378, 630))



pygame.init()


# <Game variables>
screen = pygame.display.set_mode((378, 672))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('./assets/background-night.png').convert()
bg_surface = pygame.transform.scale(bg_surface, [378, 672]) #378
#bg_surface = pygame.transform.scale2x(bg_surface)
bg_x_position = 0

floor_surface = pygame.image.load('./assets/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface, [378, 200])
floor_x_position = 0

bird = pygame.image.load('./assets/redbird-midflap.png').convert()
bird = pygame.transform.scale2x(bird)
bird_x_position = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(bg_surface, (0, 0))

    bg_x_position -= 1
    draw_bg()
    if bg_x_position <= -378:
        bg_x_position = 0

    floor_x_position -= 1
    draw_floor()
    if floor_x_position <= -378:
        floor_x_position = 0

    screen.blit(bird, (43, 187))





    pygame.display.update()

    clock.tick(120)


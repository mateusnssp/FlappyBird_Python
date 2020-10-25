import pygame, sys

def draw_floor():
    screen.blit(flor_surface, (flor_x_position, 600))
    screen.blit(flor_surface, (flor_x_position + 378, 600))

pygame.init()
screen = pygame.display.set_mode((378, 672))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

flor_surface = pygame.image.load('./assets/base.png').convert()
flor_surface = pygame.transform.scale2x(flor_surface)
flor_x_position = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(bg_surface, (0, 0))
    flor_x_position -= 1
    draw_floor()
    if flor_x_position <= -378:
        flor_x_position = 0




    pygame.display.update()
    clock.tick(120)



import pygame

pygame.init()

game_x = 800
game_y = 600


gameDisplay = pygame.display.set_mode((game_x, game_y))  # TODO change to relative sizing
pygame.display.set_caption('GladiatorRPG')
clock = pygame.time.Clock()

exit_game = False

while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


    pygame.display.update()
    clock.tick(60)

pygame.quit()


import pygame
from GladiatorRPG.Visualizer.scene import *  # Combat

pygame.init()
myfont = pygame.font.SysFont("monospace", 15)


game_x = 800
game_y = 600

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
button_clicked_color = (50, 50, 50)


gameDisplay = pygame.display.set_mode((game_x, game_y))  # TODO change to relative sizing
pygame.display.set_caption('GladiatorRPG')
clock = pygame.time.Clock()


gameDisplay.fill(white)


button_handler1 = ButtonHandler(gameDisplay)
#  button_handler.add_button(game_x * .15, game_y * .8, game_x * .2, game_y * .9, "asdf", blue)
button1 = Button(5, game_y * 0.8, 100, game_y * 0.85, "New Game", blue)
button2 = Button(100, game_y * 0.8, 171, game_y * 0.85, "Begin Combat", green)

button_handler1.add_button(button1)
button_handler1.add_button(button2)

imageTest = Graphic('Defualt_Image.png', 50, 50)

graphic_handler1 = GraphicHandler(gameDisplay)
graphic_handler1.add_graphic(imageTest)


# build a scene
scene_handler = SceneHandler(gameDisplay)


# scene1 = Scene(button_handler1, graphic_handler1)
combat = Combat(gameDisplay)

scene_handler.add_scene(combat)
scene_handler.current_scene = combat

scene_handler.draw_scene()

exit_game = False

while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos

                # check button area (for now confined to bottom 20% of screen
                if True:  # mouse_y > game_y * 0.8;  # TODO: efficiency spot
                    for button in combat.scene.button_handler.button_list:
                        if button.within(mouse_x, mouse_y):
                            button.action()

    scene_handler.draw_scene()

    pygame.display.update()
    clock.tick(60)

pygame.quit()


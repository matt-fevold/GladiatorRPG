import pygame

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


class Scene:
    # for generic scene creation.
    def __init__(self):
        # Add UI element handlers here as I need them
        self.ButtonManager = ButtonHandler()
        self.GraphicManager = GraphicHandler()

    def draw_scene(self):
        pass


class Combat(Scene):
    def __init__(self):
        super().__init__()


class Handler:
    def __init__(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError


class Graphic:
    def __init__(self, image_name, image_x, image_y):

        self.image_x = image_x  # the x/y location on the screen passed
        self.image_y = image_y
        self.image = pygame.image.load('Assets/' + image_name)

        # self.draw_graphic()

    def draw_graphic(self, screen):
        screen.blit(self.image, [self.image_x, self.image_y])


class GraphicHandler(Handler):
    """handle a group of graphics
    """
    def __init__(self, screen):
        self.graphic_list = []
        self.screen = screen

    def add_graphic(self, image):
        self.graphic_list.append(image)

    def draw_graphics(self):
        [g.draw_graphic(self.screen) for g in self.graphic_list]

    def draw(self):
        self.draw_graphics()


class Button:
    # all a button is is a rectangle, some text, and an action on left click

    def __init__(self, screen, x_1, y_1, x_2, y_2, text, color):
        self.name = text
        self.color = color
        self.screen = screen

        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2

        # self.draw_button()

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, (self.x_1, self.y_1,
                                              self.x_2, self.y_2))

        self.draw_text()

    def draw_text(self):
        label = myfont.render(self.name, 1, black)
        center_x = (self.x_2 - self.x_1) / 2 + self.x_1
        center_y = (self.y_2 - self.y_1) / 2 + self.y_1

        gameDisplay.blit(label, (center_x, center_y))

    # TODO make clicking better, seems only clicks work on left side.
    def within(self, mouse_click_x, mouse_click_y):
        if self.x_1 <= mouse_click_x <= self.x_2:
            if self.y_1 < mouse_click_y <= self.y_2:

                return True

    def action(self):
        self.color = button_clicked_color
        self.draw_button(gameDisplay)
        print(self.name, " is pressed")


class ButtonHandler(Handler):
    # place all buttons here,
    def __init__(self, screen):
        self.button_list = []
        self.screen = screen

    def add_button(self, butt):
        # self.button_list.append(Button(x_1, y_1, x_2, y_2, text, button_color))  # can't believe i wrote this line
                                                                            # keeping until new method works
        self.button_list.append(butt)

    def draw_buttons(self):
        # draw all the buttons
        [b.draw_button(self.screen) for b in self.button_list]

    def draw(self):
        self.draw_buttons()


gameDisplay.fill(white)
button_handler = ButtonHandler(gameDisplay)
#  button_handler.add_button(game_x * .15, game_y * .8, game_x * .2, game_y * .9, "asdf", blue)
button1 = Button(gameDisplay, 5, game_y * 0.8, 100, game_y * 0.85, "New Game", blue)
button2 = Button(gameDisplay, 100, game_y * 0.8, 171, game_y * 0.85, "Begin Combat", green)

button_handler.add_button(button1)
button_handler.add_button(button2)
# imageTest = pygame.image.load('Assets/Defualt_Image.png')

imageTest = Graphic('Defualt_Image.png', 50, 50)

button_handler.draw_buttons()

graphic_handler = GraphicHandler(gameDisplay)
graphic_handler.add_graphic(imageTest)
graphic_handler.draw_graphics()

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
                    for button in button_handler.button_list:
                        if button.within(mouse_x, mouse_y):
                            button.action()

    # gameDisplay.blit(imageTest, [50, 50])
    #imageTest.draw_graphic(gameDisplay)


    pygame.display.update()
    clock.tick(60)

pygame.quit()


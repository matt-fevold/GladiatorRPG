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


class Button:
    def __init__(self, x_1, y_1, x_2, y_2, text, color):
        self.name = text
        #pygame.draw.rect(gameDisplay, color, (x_1, y_1,  x_2, y_2))
        # print(text)
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2
        self.color = color

        self.draw_button()

    def draw_button(self):
        pygame.draw.rect(gameDisplay, self.color, (self.x_1, self.y_1,
                                                   self.x_2, self.y_2))

        self.draw_text()

    def draw_text(self):
        label = myfont.render(self.name, 1, black)
        center_x = (self.x_2 - self.x_1) / 2 + self.x_1
        center_y = (self.y_2 - self.y_1) / 2 + self.y_1

        gameDisplay.blit(label, (center_x, center_y))

    def within(self, mouse_click_x, mouse_click_y):
        if self.x_1 <= mouse_click_x <= self.x_2:
            if self.y_1 < mouse_click_y <= self.y_2:

                return True

    def action(self):
        self.color = button_clicked_color
        self.draw_button()
        print(self.name, " is pressed")


class ButtonHandler:
    # place all buttons here,
    def __init__(self):
        self.button_list = []

    def add_button(self, x_1, y_1, x_2, y_2, text, button_color):
        self.button_list.append(Button(x_1, y_1, x_2, y_2, text, button_color))


gameDisplay.fill(white)
button_handler = ButtonHandler()
#  button_handler.add_button(game_x * .15, game_y * .8, game_x * .2, game_y * .9, "asdf", blue)
button_handler.add_button(5, game_y * 0.8, 50, game_y * 0.85, "New Game", blue)
button_handler.add_button(51, game_y * 0.8, 101, game_y * 0.85, "Begin Combat", green)


exit_game = False


while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos

                # check button area (for now confined to bottom 20% of screen
                if True: #mouse_y > game_y * 0.8: #TODO: efficiency spot
                    for button in button_handler.button_list:
                        if button.within(mouse_x, mouse_y):
                            button.action()

    pygame.display.update()
    clock.tick(60)

pygame.quit()


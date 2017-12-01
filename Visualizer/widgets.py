import pygame


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
button_clicked_color = (50, 50, 50)


class Graphic:
    def __init__(self, image_name, image_x, image_y):

        self.image_x = image_x  # the x/y location on the screen passed
        self.image_y = image_y
        self.image = pygame.image.load('Visualizer/Assets/' + image_name)

        # self.draw_graphic()

    def draw_graphic(self, screen):
        screen.blit(self.image, [self.image_x, self.image_y])


class Button:
    # all a button is is a rectangle, some text, and an action on left click

    def __init__(self, x_1, y_1, x_2, y_2, text, color):
        self.name = text
        self.color = color

        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2

        self.myfont = pygame.font.SysFont("monospace", 15)

        # self.draw_button()

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, (self.x_1, self.y_1,
                                              self.x_2, self.y_2))

        self.draw_text(screen)

    def draw_text(self, screen):
        label = self.myfont.render(self.name, 1, black)
        center_x = (self.x_2 - self.x_1) / 2 + self.x_1
        center_y = (self.y_2 - self.y_1) / 2 + self.y_1

        screen.blit(label, (center_x, center_y))

    # TODO make clicking better, seems only clicks work on left side.
    def within(self, mouse_click_x, mouse_click_y):
        if self.x_1 <= mouse_click_x <= self.x_2:
            if self.y_1 < mouse_click_y <= self.y_2:

                return True

    def action(self):
        self.color = button_clicked_color
        # self.draw_button(screen)
        print(self.name, " is pressed")


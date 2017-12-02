# from GladiatorRPG.Visualizer.scene import Combat


class Handler:
    def __init__(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError


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


class SceneHandler(Handler):
    def __init__(self, screen):
        self.scene_list = []
        self.screen = screen
        self.current_scene = None  # Combat()

    def draw(self):
        self.current_scene.draw_scene()

    def draw_scene(self):
        self.draw()

    def add_scene(self, scene):
        self.scene_list.append(scene)


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
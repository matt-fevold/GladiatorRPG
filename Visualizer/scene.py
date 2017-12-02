from GladiatorRPG.Visualizer.handlers import SceneHandler, Handler, GraphicHandler,  ButtonHandler
from GladiatorRPG.Visualizer.widgets import  Button, Graphic
from GladiatorRPG.Visualizer.colors import Color

color = Color()  # TODO find a better way to do color


class Scene:
    # for generic scene creation.
    def __init__(self, buttonhandler, graphichandler):  # TODO find better way to do this, going to be lazy for now.
        # Add UI element handlers here as I need them
        self.button_handler = buttonhandler
        self.graphic_handler = graphichandler

    def draw_scene(self):
        self.button_handler.draw_buttons()
        self.graphic_handler.draw_graphics()

    def draw(self):
        self.draw_scene()  # TODO probably not needed


class Combat:
    def __init__(self, screen):
        self.screen = screen
        button_handler = ButtonHandler(screen)
        graphic_handler = GraphicHandler(screen)

        self.scene = Scene(button_handler, graphic_handler)

        attack_button = Button(100, 100, 100, 50, "ATTACK", color.blue)  # TODO find better way to do color, ugly af
        run_button = Button(200, 100, 100, 50, "RUN", color.green)

        self.scene.button_handler.add_button(run_button)
        self.scene.button_handler.add_button(attack_button)

        # self.draw_scene()

    def draw_scene(self):
        self.scene.draw()

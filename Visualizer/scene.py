from GladiatorRPG.Visualizer.handlers import SceneHandler, Handler, GraphicHandler,  ButtonHandler
from GladiatorRPG.Visualizer.widgets import  Button, Graphic


class Scene:
    # for generic scene creation.
    def __init__(self, buttonhandler, graphichandler):
        # Add UI element handlers here as I need them
        self.button_handler = buttonhandler
        self.graphic_handler = graphichandler

    def draw_scene(self):
        self.button_handler.draw_buttons()
        self.graphic_handler.draw_graphics()

    def draw(self):
        self.draw_scene()  # TODO probably not needed


class Combat(Scene):
    def __init__(self):
        pass
        #super().__init__(None, None)

import pygame as pg

from timer import Timer
from sceneobject import SceneObject as Obj
from shapes import *
from movement import *


class Scene:
    WIN_SIZE = (1920, 1080)
    W = WIN_SIZE[0]
    H = WIN_SIZE[1]
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    film_sound_path = "../resources/film_sound.mp3"

    def __init_objects__(self):
        self.objects = []

        self.objects += [Obj(RandomRect(self.WIN_SIZE), RandomWanderingMovement(self.WIN_SIZE)) for _ in range(3)]
        self.objects += [Obj(RandomCircle(self.WIN_SIZE), RandomWanderingMovement(self.WIN_SIZE)) for _ in range(3)]
        self.objects += [Obj(RandomRect(self.WIN_SIZE), LinearMovement(self.WIN_SIZE)) for _ in range(3)]
        self.objects += [Obj(RandomCircle(self.WIN_SIZE), LinearMovement(self.WIN_SIZE)) for _ in range(3)]

    def __init_sound__(self):
        pg.init()
        pg.mixer.music.load(self.film_sound_path)
        pg.mixer.music.play(-1)

    def __init__(self):
        self.__init_objects__()
        self.__init_sound__()
        self.timer = Timer()

    def run(self):
        clear_color = [0, 0, 0]

        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            self.screen.fill(clear_color)

            self.timer.update()
            [shape.update(self.timer.delta_time) for shape in self.objects]
            [shape.render(self.screen) for shape in self.objects]
            pg.display.update()

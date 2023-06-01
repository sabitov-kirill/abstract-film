import pygame as pg
import color
import random

class Rect:
    def __init__(self, col, size):
        self.color = col
        self.size = size

    def render(self, screen, position):
        pg.draw.rect(
            screen, self.color,
            pg.Rect(position[0], position[1], self.size[0], self.size[1])
        )


class Circle:
    def __init__(self, col, radius):
        self.color = col
        self.radius = radius

    def render(self, screen, position):
        pg.draw.circle(screen, self.color, position, self.radius)


class RandomRect(Rect):
    def __init__(self, screen_size):
        super().__init__(
            color.rand_color(),
            [random.randint(0, screen_size[0]), random.randint(0, screen_size[1])],
        )


class RandomCircle(Circle):
    def __init__(self, screen_size):
        super().__init__(
            color.rand_color(),
            random.randint(0, screen_size[0] // 6)
        )
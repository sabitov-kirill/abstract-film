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

"""
class RandomMoveRect(RandomRect):
    MAX_SPEED = 5000

    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.screen_size = screen_size
        self.speed = random.randint(0, self.MAX_SPEED)

    def update(self, delta_time):
        self.pos = [(pi + random.randint(-self.speed, self.speed) * delta_time) % mi
                    for pi, mi in zip(self.pos, self.screen_size)]


class MoveStraightRandomRect(RandomRect):
    MAX_SPEED = 350

    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.screen_size = screen_size
        self.speed = [random.randint(-self.MAX_SPEED, self.MAX_SPEED), random.randint(0, self.MAX_SPEED)]

    def update(self, delta_time):
        self.pos = [(pi + si * delta_time) % mi for pi, si, mi in zip(self.pos, self.speed, self.screen_size)]


class MoveStraightRandomCircle(RandomCircle):
    MAX_SPEED = 350

    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.screen_size = screen_size
        self.speed = [random.randint(-self.MAX_SPEED, self.MAX_SPEED), random.randint(0, self.MAX_SPEED)]

    def update(self, delta_time):
        self.centre = [(pi + si * delta_time) % mi for pi, si, mi in zip(self.centre, self.speed, self.screen_size)]


class RandomMoveCircle(RandomCircle):
    MAX_SPEED = 5000

    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.screen_size = screen_size
        self.speed = random.randint(0, self.MAX_SPEED)

    def update(self, delta_time):
        self.centre = [(pi + random.randint(-self.speed, self.speed) * delta_time) % mi
                       for pi, mi in zip(self.centre, self.screen_size)]
"""
import pygame as pg


class Timer:
    def __init__(self):
        self.ticks_last_frame = pg.time.get_ticks()
        self.delta_time = 0

    def update(self):
        t = pg.time.get_ticks()
        self.delta_time = (t - self.ticks_last_frame) / 1000.0
        self.ticks_last_frame = t
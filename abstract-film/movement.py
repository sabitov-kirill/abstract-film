import random


class Movement:
    def __init__(self, start_position):
        self.position = start_position

    def update(self, delta_time):
        pass


class RandomWanderingMovement(Movement):
    MIN_SPEED = 1
    MAX_SPEED = 5000

    def __init__(self, movement_bounds):
        super().__init__([random.randint(0, bound) for bound in movement_bounds])
        self.speed_range = random.randint(self.MIN_SPEED, self.MAX_SPEED)
        self.movement_bounds = movement_bounds

    def update(self, delta_time):
        self.position = [(position + random.randint(-self.speed_range, self.speed_range) * delta_time) % bound
                         for position, bound in zip(self.position, self.movement_bounds)]


class LinearMovement(Movement):
    MAX_SPEED = 350
    MIN_SPEED = -MAX_SPEED

    def __init__(self, movement_bounds):
        super().__init__([random.randint(0, bound) for bound in movement_bounds])
        self.speed = [random.randint(self.MIN_SPEED, self.MAX_SPEED) for _ in range(len(movement_bounds))]
        self.movement_bounds = movement_bounds

    def update(self, delta_time):
        self.position = [(position + speed * delta_time) % bound
                         for position, speed, bound in zip(self.position, self.speed, self.movement_bounds)]
        
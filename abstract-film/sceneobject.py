class SceneObject:
    def __init__(self, shape, movement):
        self.shape = shape
        self.movement = movement

    def update(self, delta_time):
        self.movement.update(delta_time)

    def render(self, screen):
        self.shape.render(screen, self.movement.position)

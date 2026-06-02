import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        asteroid_right_vector = self.velocity.rotate(angle)
        asteroid_left_vector = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_right = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_left = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_right.velocity = asteroid_right_vector * 1.2
        asteroid_left.velocity = asteroid_left_vector * 1.2

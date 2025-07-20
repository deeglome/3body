"""
Python module for physics
"""
import math
from pygame.math import Vector2
G = 6.67E-11

class Body:
    def __init__(self, pos: Vector2, mass: float, vel: Vector2, acc: Vector2):
        self.pos = pos
        self.mass = mass
        self.vel = vel
        self.acc = acc

    def g_force(self, other):
        force = G * self.mass * other.mass / (self.distance_to(other))**2 * (self.pos - other.pos).normalize()
        self.acc = force / self.mass * force.normalize()
        other.acc = -force / other.mass * force.normalize()

    def update(self, dt):
        self.pos.x += self.vel.x * dt + 0.5 * self.acc.x * dt**2
        self.pos.y += self.vel.y * dt + 0.5 * self.acc.y * dt**2

        self.vel.x += self.acc.x * dt
        self.vel.y += self.acc.y * dt

if __name__ == "__main__":
    pass

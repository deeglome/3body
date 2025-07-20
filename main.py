"""
Main module to run pygame
"""
import pygame
from phy import *
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("3body")
clock = pygame.time.Clock()
running = True
ORIGIN = pygame.Vector2(640, 360)

def draw(body):
    pygame.draw.circle(screen, "#ccc7d1", ORIGIN + body.pos, 10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    screen.fill("#000033")

    bd = Body(pygame.Vector2(), 1E24, pygame.Vector2(), pygame.Vector2())
    draw(bd)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

import pygame
import random

pygame.init()

# stałe ekranu
WIDTH = 800
HEIGHT = 600
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Topnienie śniegu")
clock = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
DARK_BLUE = (20, 30, 50)
ICE_BLUE = (200, 230, 255)
SNOW_DRIFT_COLOR = (220, 235, 255)

class Snowflake:
    def __init__(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = -10
        self.radius = random.randint(8, 16)
        self.speed = random.uniform(1.5, 3.5 - self.radius / 8)
        self.active = True
        self.melting = False
        self.melt_timer = 0

    def update(self):
        if self.melting:
            self.melt_timer += 1
            self.radius -= 0.5

            if self.radius <= 0:
                self.active = False
            return

        self.y += self.speed

        # check collision
        # column_index = int(self.x // 10)
        # if 0 <= self.y <= len(drifts):


    def is_clicked(self, position):
        pass

# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     pygame.display.flip()
#
# pygame.quit()
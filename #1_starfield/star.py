import numpy as np
import pygame


class Star:
    def __init__(self):
        width, height = pygame.display.get_window_size()
        self.screen = pygame.display.get_surface()
        self.width = width
        self.height = height
        self.x = np.random.uniform(0, width)
        self.y = np.random.uniform(0, height)
        self.pz = self.z = np.random.uniform(0, width)
        self.r = self.get_radius()

    def translate_position(self, scalar, origin_x=0.0, origin_y=0.0):
        sx = Star.get_scaled_coordinate(scalar, self.x, origin_x)
        sy = Star.get_scaled_coordinate(scalar, self.y, origin_y)
        return sx, sy

    @staticmethod
    def get_scaled_coordinate(scalar, coordinate, origin):
        new_coordinate = coordinate - origin
        new_coordinate = origin * (1 + new_coordinate / scalar)
        return new_coordinate

    def update(self, reduction):
        self.z -= reduction
        if self.z < 1:
            self.reset_star()
        self.r = self.get_radius()

    def reset_star(self):
        self.z = self.width
        self.x = np.random.uniform(0, self.width)
        self.y = np.random.uniform(0, self.height)
        self.pz = self.z

    def show(self):
        sx, sy = self.get_star_position()
        px, py = self.get_previous_star_position()
        self.draw_star(sx, sy)
        # self.draw_tail(sx, sy, px, py)

    def draw_star(self, sx, sy):
        pygame.draw.ellipse(self.screen, (255, 255, 255), (sx, sy, self.r, self.r))

    def draw_tail(self, sx, sy, px, py):
        pygame.draw.line(self.screen, (255, 255, 255), (px, py), (sx, sy))

    def get_radius(self):
        return 16 * (1 - self.z / self.width)

    def get_star_position(self):
        return self.translate_position(self.z, self.width / 2, self.height / 2)

    def get_previous_star_position(self):
        return self.translate_position(self.pz, self.width / 2, self.height / 2)

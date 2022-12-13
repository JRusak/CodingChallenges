import numpy as np
import pygame
from math import *


class Box:
    def __init__(self, center_position, base_position=None, size=50, angles=(0, 0, 0), color=(0, 0, 0)):
        self.center_position = center_position
        self.base_position = base_position
        self.size = size // 2
        self.x_angle, self.y_angle, self.z_angle = angles
        self.rotation_x = self.rotation_y = self.rotation_z = 0
        self.set_rotation()
        self.color = color
        self.points = self.get_points()
        self.projection_matrix = np.array([
            [1, 0, 0],
            [0, 1, 0]
        ])

    def get_points(self):
        points = []
        for x in (-1, 1):
            for y in (-1, 1):
                for z in (-1, 1):
                    point = [x, y, z]
                    if self.base_position:
                        point[0] += self.base_position[0]
                        point[1] += self.base_position[1]
                        point[2] += self.base_position[2]
                    points.append(np.array(point))

        return points

    def connect_points(self, screen, i, j, points):
        pygame.draw.line(
            screen, self.color, (points[i][0], points[i][1]), (points[j][0], points[j][1]))

    def set_rotation(self):
        self.rotation_z = np.array([
            [cos(self.z_angle), -sin(self.z_angle), 0],
            [sin(self.z_angle), cos(self.z_angle), 0],
            [0, 0, 1],
        ])

        self.rotation_y = np.array([
            [cos(self.y_angle), 0, sin(self.y_angle)],
            [0, 1, 0],
            [-sin(self.y_angle), 0, cos(self.y_angle)],
        ])

        self.rotation_x = np.array([
            [1, 0, 0],
            [0, cos(self.x_angle), -sin(self.x_angle)],
            [0, sin(self.x_angle), cos(self.x_angle)],
        ])

    def draw_connections(self, screen, projected_points):
        for i in range(7):
            if not i & 1:
                self.connect_points(screen, i, i + 1, projected_points)
            if i < 4:
                self.connect_points(screen, i, i + 4, projected_points)
            if i in (0, 1) or i in (4, 5):
                self.connect_points(screen, i, i + 2, projected_points)

    def rotate_point(self, point):
        rotated2d = np.dot(self.rotation_x, point.reshape((3, 1)))
        rotated2d = np.dot(self.rotation_y, rotated2d)
        rotated2d = np.dot(self.rotation_z, rotated2d)
        return rotated2d

    def project_points(self):
        projected_points = []

        for point in self.points:
            rotated2d = self.rotate_point(point)
            projected2d = np.dot(self.projection_matrix, rotated2d)

            x = int(projected2d[0][0] * self.size) + self.center_position[0]
            y = int(projected2d[1][0] * self.size) + self.center_position[1]

            projected_points.append([x, y])

        return projected_points

    @staticmethod
    def draw_projected_points(screen, projected_points):
        for point in projected_points:
            pygame.draw.circle(screen, (255, 0, 0), (point[0], point[1]), 5)

    def show(self, screen, draw_points=True):
        self.set_rotation()
        projected_points = self.project_points()
        if draw_points:
            Box.draw_projected_points(screen, projected_points)
        self.draw_connections(screen, projected_points)

    def get_position(self):
        return self.center_position

    def get_angles(self):
        return self.x_angle, self.y_angle, self.z_angle

    def rotate_x(self, a):
        self.x_angle += a

    def rotate_y(self, a):
        self.y_angle += a

    def rotate_z(self, a):
        self.z_angle += a

    def translate_center(self, new_center):
        self.center_position = new_center

    def translate_x(self, x):
        self.center_position[0] += x

    def translate_y(self, y):
        self.center_position[1] += y

    def translate_z(self, z):
        self.center_position[2] += z

    def translate(self, x, y, z):
        self.translate_x(x)
        self.translate_y(y)
        self.translate_x(z)

    def scale(self, scale):
        self.size *= scale

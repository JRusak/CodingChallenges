import pygame
from Tools.box import Box


class Sponge(Box):
    def __init__(self, x, y, z, r, base_position=pygame.math.Vector3(0, 0, 0)):
        self.pos = pygame.math.Vector3(x, y, z)
        super().__init__(self.pos, base_position=base_position, size=r)
        self.r = r

    def generate(self):
        boxes = []

        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    new_r = self.r / 3
                    new_x = self.pos.x + x * new_r
                    new_y = self.pos.y + y * new_r
                    new_z = self.pos.z + z * new_r

                    s = Sponge(new_x, new_y, new_z, new_r, pygame.math.Vector3(x, y, z))

                    o_x, o_y, o_z = self.center_position
                    new_center = [o_x + new_x, o_y + new_y, o_z + new_z]
                    s.translate_center(new_center)

                    boxes.append(s)

        return boxes

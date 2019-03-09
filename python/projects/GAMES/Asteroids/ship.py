import math
import random

import pyxel

from bullet import Bullet
from utils import check_bounds, rotate_around_origin, Point

import constants
import sound


class Ship:
    radius = constants.SHIP_RADIUS

    def __init__(self, x, y, colour):
        self.starting_x = x
        self.starting_y = y
        self.starting_colour = colour
        self.reset()
        self.accelerating = False
        self.shooting = False

    def reset(self):
        self.x = self.starting_x
        self.y = self.starting_y
        self.colour = self.starting_colour
        self.direction = 0
        self.momentum_x = 0
        self.momentum_y = 0

        self.points = []
        for point in constants.SHIP_POINTS:
            self.points.append(Point(*point))

    def rotate(self, direction):
        if direction == "l":
            multipler = 1
        elif direction == "r":
            multipler = -1
        else:
            raise ValueError("Direction must be the 'l'eft or 'r'ight")

        rotation_angle = constants.ROTATION * multipler

        for point in self.points:
            point.rotate_point(rotation_angle)

        self.direction += rotation_angle

    def accelerate(self):

        self.accelerating = True

        acc_x, acc_y = rotate_around_origin(
            (0, -constants.ACCELERATION), self.direction
        )
        self.momentum_x += acc_x
        self.momentum_y += acc_y

        acceleration = math.hypot(self.momentum_x, self.momentum_y)
        if acceleration > constants.MAX_ACCELERATION:
            scale = constants.MAX_ACCELERATION / acceleration
            self.momentum_x *= scale
            self.momentum_y *= scale
            assert (
                round(math.hypot(self.momentum_x, self.momentum_y), 0)
                == constants.MAX_ACCELERATION
            )

    def shoot(self):
        vel_x, vel_y = rotate_around_origin(
            (0, -constants.BULLET_VELOCITY), self.direction
        )
        ship_tip = self.points[0]
        Bullet(
            self.points[0].x + self.x,
            self.points[0].y + self.y,
            vel_x,
            vel_y,
            constants.BULLET_COLOUR,
        )

    def yes_shoot(self):
        if not self.shooting:
            sound.start_shoot()
            self.shooting = True

    def no_shoot(self):
        if self.shooting:
            sound.stop_shoot()
            self.shooting = False

    def destroy(self):
        pass

    def update_position(self):
        self.x += self.momentum_x
        self.y += self.momentum_y
        self.momentum_x *= constants.DRAG
        self.momentum_y *= constants.DRAG

        self.x = check_bounds(self.x, pyxel.width, constants.BUFFER)
        self.y = check_bounds(self.y, pyxel.height, constants.BUFFER)

    def display(self):

        for point1, point2 in zip(self.points, self.points[1:] + [self.points[0]]):
            pyxel.line(
                x1=point1.x + self.x,
                y1=point1.y + self.y,
                x2=point2.x + self.x,
                y2=point2.y + self.y,
                col=self.colour,
            )

        if self.accelerating:
            self.display_acceleration()

    def display_acceleration(self):
        x1, y1 = rotate_around_origin(
            (0, constants.SHIP_ACCELERATION_POINTS[0]), self.direction
        )
        x2, y2 = rotate_around_origin(
            (0, constants.SHIP_ACCELERATION_POINTS[1]), self.direction
        )
        pyxel.line(
            x1=x1 + self.x,
            y1=y1 + self.y,
            x2=x2 + self.x,
            y2=y2 + self.y,
            col=constants.SHIP_ACCELERATION_COLOUR,
        )


class ShipBreakup:
    def __init__(self, ship):
        self.segments = []

        def random_velocity():
            direction = random.random() * math.pi * 2
            velocity = rotate_around_origin(
                (0, -constants.SHIP_DRIFT_VELOCITY), direction
            )
            return velocity

        for point1, point2 in zip(ship.points, ship.points[1:] + [ship.points[0]]):
            rvel_x, rvel_y = random_velocity()
            line_velocity = (rvel_x + ship.momentum_x, rvel_y + ship.momentum_y)
            spin = constants.SHIP_BREAKUP_ROTATION * random.choice((-1, 1))

            line = Line.line_from_two_points(
                point1.x + ship.x,
                point1.y + ship.y,
                point2.x + ship.x,
                point2.y + ship.y,
                velocity=line_velocity,
                spin=spin,
                colour=ship.colour,
            )
            self.segments.append(line)

    def update(self):
        for segment in self.segments:
            segment.update()

    def display(self):
        for segment in self.segments:
            segment.display()


class Line:

    def __init__(self, x, y, length, direction, velocity, spin, colour):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
        self.vel_x, self.vel_y = velocity
        self.spin = spin
        self.colour = colour

        self.points = []
        for end in (1, -1):
            self.points.append(Point(0, end * self.length / 2))

        self.rotate(direction)

    @classmethod
    def line_from_two_points(cls, x1, y1, x2, y2, velocity, spin, colour):
        x = sum((x1, x2)) / 2
        y = sum((y1, y2)) / 2
        length = math.hypot(x1 - x2, y1 - y2)
        direction = -math.atan2(y1 - y2, x1 - x2) - math.pi / 2
        return cls(x, y, length, direction, velocity, spin, colour)

    def rotate(self, radians):
        for point in self.points:
            point.rotate_point(radians)

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

        self.vel_x *= constants.SHIP_BREAKUP_DRAG
        self.vel_y *= constants.SHIP_BREAKUP_DRAG

        self.x = check_bounds(self.x, pyxel.width, constants.BUFFER)
        self.y = check_bounds(self.y, pyxel.height, constants.BUFFER)

        self.rotate(self.spin)

    def display(self):
        point1, point2 = self.points
        pyxel.line(
            x1=point1.x + self.x,
            y1=point1.y + self.y,
            x2=point2.x + self.x,
            y2=point2.y + self.y,
            col=self.colour,
        )

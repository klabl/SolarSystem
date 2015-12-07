from abc import *
from math import*
from src.tmp.Drawable import Drawable

from pyglet.gl.gl import *
from pyglet.gl.glu import *
__author__ = 'pwngu'


class Orb:
    # What does metaclass mean? Super class?
    __metaclass__ = ABCMeta

    def __init__(self, name, radius, surface, year_scale=1, day_scale=1, rotation_cw=True):

        self.pos_x, self.pos_y, self.pos_z = 0, 0, 0
        self.cur_rotation_angle_year = 0
        self.cur_rotation_angle = 0

        self.system_center = None
        self.system = []

        self.name = name
        self.radius = radius
        self.surface = surface
        self.year_scale = year_scale
        self.day_scale = day_scale
        self.rotation_cw = rotation_cw

    def add_orb(self, orb):

        if isinstance(orb, Orb):
            self.system.append(orb)
        else:
            raise Exception

    def set_system_center(self, orb):

        if isinstance(orb, Orb):
            self.system_center = orb
        else:
            raise Exception

    def update(self, time):

        self.cur_rotation_angle += self.day_scale
        self.cur_rotation_angle_year += self.year_scale

        for orb in self.system:
            orb.update(time)

    def draw(self):
        # TODO alle Parameter auf attribute beziehen z.B. bei rotate
        # Reihenfolge: Erst wird transliert DANN rotiert
        # das was ganz unten steht wird als erstes ausgefuehrt

        # yearscale
        glRotatef(self.cur_rotation_angle_year, 0, 1, 0)
        glTranslatef(self.pos_x, self.pos_y, self.pos_z)

        # dayscale
        glRotatef(self.cur_rotation_angle, 0, 1, 0)
        gluSphere(self.surface, self.radius, 20, 12)

        for orb in self.system:
            orb.draw()


class Planet(Orb):

    def __init__(self, name, radius, surface, year_scale=1, day_scale=1, rotation_cw_=True):
        super(Planet, self).__init__(name, radius, surface, year_scale, day_scale, rotation_cw_)


class Star(Orb):

    def __init__(self, name, radius, year_scale=1, day_scale=1, rotation_cw=True, light_strength=1):
        super(Star, self).__init__(name, radius, year_scale, day_scale, rotation_cw)
        self.__light_strength = light_strength


class Surface(object):

    def __init__(self, size, pattern, circle):
        self.size = size
        self.pattern = pattern
        self.circle = circle

from abc import *

__author__ = 'klaus'


class Orb:
    __metaclass__ = ABCMeta

    def __init__(self, name, radius, surface, year_scale=1, day_scale=1, rotation_cw=True):
        self.__system_center = None
        self.__system = []
        self.__name = name
        self.__radius = radius
        self.__surface = surface
        self.__year_scale = year_scale
        self.__day_scale = day_scale
        self.__rotation_cw = rotation_cw

    def add_orb(self, orb):

        if isinstance(orb, Orb):
            self.__system.append(orb)
        else:
            raise Exception

    def get_system(self):

        return self.__system

    def set_system_center(self, orb):

        if isinstance(orb, Orb):
            self.__system_center = orb
        else:
            raise Exception


class Planet(Orb):
    __metaclass__ = Orb


class Star(Orb):
    __metaclass__ = Orb

    def __init__(self, name, radius, year_scale=1, day_scale=1, rotation_cw=True, light_strength=1):
        super(Star, self).__init__(name, radius, year_scale, day_scale, rotation_cw)
        self.__light_strength = light_strength


class Surface(object):

    def __init__(self, size, pattern, circle):
        self.__size = size
        self.__pattern = pattern
        self.__circle = circle

from abc import *

__author__ = 'Klaus'


class Orb:
    __metaclass__ = ABCMeta

    def __init__(self, name, radius, model, year_scale=1, day_scale=1, rotation_cw=True, system_center=None,):

        self.system_center = system_center
        self.set_system_center(system_center)

        self.system = []

        self.name = name
        self.radius = radius
        self.model = model
        self.year_scale = year_scale
        self.day_scale = day_scale
        self.rotation_cw = rotation_cw

        self.model = model
        self.orbit_root = None


    def add_orb(self, orb):

        if isinstance(orb, Orb):
            self.system.append(orb)
        else:
            raise Exception

    def show_tex(self, show=True):
        if show:
            self.model.model.setTexture(self.model.texture, 1)
        else:
            self.model.model.clearTexture()

    def set_system_center(self, orb):

        if orb is None:
            self.system_center = None
            self.orbit_root = render.attachNewNode('orbit_root_' + self.name)
            self.model.model.reparentTo(self.orbit_root)

        elif isinstance(orb, Orb):
            self.system_center = orb
            self.orbit_root = orb.orbit_root.attachNewNode('orbit_root_' + self.name)
            self.model.model.reparentTo(self.orbit_root)

        else:
            raise Exception

    def change_speed(self, factor, orb_name=None):

        if orb_name is None:

            self.day_scale *= factor
            self.year_scale *= factor

            for orb in self.system:
                orb.day_scale *= factor
                orb.year_scale *= factor
            return

        if self.name == orb_name:
            self.day_scale *= factor
            self.year_scale *= factor
        else:
            for orb in self.system:
                if orb.name == orb_name:
                    orb.day_scale *= factor
                    orb.year_scale *= factor
                    break

    def stop(self, orb_name=None):



class Planet(Orb):

    def __init__(self, name, radius, model, year_scale=1, day_scale=1, rotation_cw_=True):
        super(Planet, self).__init__(name, radius, model, year_scale, day_scale, rotation_cw_)


class Star(Orb):

    def __init__(self, name, radius, year_scale=1, day_scale=1, rotation_cw=True, light_strength=1):
        super(Star, self).__init__(name, radius, year_scale, day_scale, rotation_cw)
        self.__light_strength = light_strength


class OrbModel(object):

    def __init__(self, texture, size_scale=1, model="../models/planet_sphere"):
        self.model = loader.loadTexture(model)
        self.texture = loader.loadTexture(texture)
        self.model.setTexture(self.texture, 1)
        self.model.setScale(size_scale)

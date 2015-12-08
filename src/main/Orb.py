from abc import *

__author__ = 'Klaus'


class Orb:
    __metaclass__ = ABCMeta

    def __init__(self, name, orbit_radius, model, year_scale, day_scale, rotation_cw=True, system_center=None):

        print ("init " + name)

        self.system = []

        self.name = name
        self.orbit_radius = orbit_radius
        self.model = model
        self.year_scale = year_scale
        self.day_scale = day_scale
        self.rotation_cw = rotation_cw
        self.orbit_root = None

        self.system_center = system_center
        self.set_system_center(system_center)

        self.model = model

    def add_orb(self, orb):

        if isinstance(orb, Orb):
            self.system.append(orb)
        else:
            raise Exception

    def show_tex(self, show=True, orb_name=None):
        if orb_name is None or orb_name == self.name:
            if show:
                self.model.model.setTexture(self.model.texture)
            else:
                self.model.model.clearTexture()

        for orb in self.system:
            orb.show_tex(show, orb_name)

    def move(self, move=True, orb_name=None):
        if orb_name is None or orb_name == self.name:
            if move:
                # TODO: resume moving self
                pass
            else:
                # TODO: stop moving self
                pass

        for orb in self.system:
            orb.move(move, orb_name)

    def set_system_center(self, orb):

        if orb is None:
            self.system_center = None
            self.orbit_root = render.attachNewNode('orbit_root_' + self.name)
            self.model.model.reparentTo(self.orbit_root)
            self.model.model.setPos(self.orbit_radius, 0, 0)
            print "set pos to " + str(self.orbit_radius)

        elif isinstance(orb, Orb):
            self.system_center = orb
            self.orbit_root = orb.orbit_root.attachNewNode('orbit_root_' + self.name)
            self.model.model.reparentTo(self.orbit_root)
            self.model.model.setPos(orb.model.size + orb.orbit_radius + self.orbit_radius - self.model.size, 0, 0)
            print "set pos to " + str(orb.model.size + orb.orbit_radius + self.orbit_radius - self.model.size)

            orb.add_orb(self)

        else:
            raise Exception

    def change_speed(self, factor, orb_name=None):

        if orb_name is None or orb_name == self.name:
            # TODO: multiply current speed with factor
            pass

        for orb in self.system:
            orb.change_speed(factor, orb_name)

    def __repr__(self):
        return self.name + (str(self.system) if len(self.system) != 0 else "")


class Planet(Orb):
    def __init__(self, name, orbit_radius, model, year_scale=1, day_scale=1, rotation_cw=True, system_center=None):
        super(Planet, self).__init__(name, orbit_radius, model, year_scale, day_scale, rotation_cw, system_center)


class Star(Orb):
    def __init__(self, name, orbit_radius, model, year_scale=1, day_scale=1, rotation_cw=True, system_center=None,
                 light_strength=1):
        super(Star, self).__init__(name, orbit_radius, model, year_scale, day_scale, rotation_cw, system_center)
        self.__light_strength = light_strength


class OrbModel(object):
    def __init__(self, texture, size=1, model="../models/planet_sphere"):
        self.model = loader.loadModel(model)
        self.texture = loader.loadTexture(texture)
        self.size = size
        self.model.setTexture(self.texture, 1)
        self.model.setScale(size)

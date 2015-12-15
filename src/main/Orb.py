from abc import *
from panda3d.core import Vec3

__author__ = 'Klaus'


class Orb:
    __metaclass__ = ABCMeta

    def __init__(self, name, orbit_radius, orb_model, year_scale, day_scale, rotation_cw=True, system_center=None):

        print ("init " + name)

        self.system = []

        self.name = name
        self.orbit_radius = orbit_radius
        self.orb_model = orb_model
        self.year_scale = year_scale
        self.day_scale = day_scale
        self.rotation_cw = rotation_cw

        self.year_period = None
        self.day_period = None
        self.orbit_root = None

        self.system_center = system_center
        self.set_system_center(system_center)

        self.orb_model = orb_model

        self.is_moving = True

    def add_orb(self, orb):

        if isinstance(orb, Orb):
            self.system.append(orb)
        else:
            raise Exception

    def get_orb(self, orb_name):
        for orb in self.system:
            if orb.name == orb_name:
                return orb

    def show_tex(self, show=True, orb_name=None):
        if orb_name is None or orb_name == self.name:
            if show:
                self.orb_model.model.setTexture(self.orb_model.texture)
            else:
                self.orb_model.model.clearTexture()

        for orb in self.system:
            orb.show_tex(show, orb_name)

    # def pause(self, keytext, orb_name=None):
    #     if orb_name is None or orb_name == self.name:
    #         self.toggleOrb(self.name, self.day_period, self.year_period, keytext)
    #
    #     for orb in self.system:
    #         orb.pause(keytext, orb_name)

    # def toggleOrb(self, planet, day, orbit=None, text=None):
    #     if day.isPlaying():
    #         print "Stoppen von " + planet
    #         state = " [PAUSED]"
    #     else:
    #         print "Weiterlaufen von " + planet
    #         state = " [RUNNING]"
    #
    #     if text:
    #         old = text.getText()
    #         text.setText(old[0:old.rfind(' ')] + state)
    #
    #     self.toggleInterval(day)
    #     if orbit: self.toggleInterval(orbit)

    # def toggleInterval(self, interval):
    #     if interval.isPlaying():
    #         interval.pause()
    #     else:
    #         interval.resume()

    def toggle_moving(self, orb_name=None):
        if orb_name is None or orb_name == self.name:
            if self.is_moving:
                self.move(False)
            else:
                self.move(True)

        for orb in self.system:
            orb.toggle_moving(orb_name)

    def move(self, move=True, orb_name=None):
        if orb_name is None or orb_name == self.name:
            if move:
                self.day_period.resume()
                self.year_period.resume()
                self.is_moving = True
            else:
                self.day_period.pause()
                self.year_period.pause()
                self.is_moving = False

        for orb in self.system:
            orb.move(move, orb_name)

    # def rotate(self, rotate=True):
    #     self.is_moving = True
    #     self.day_period.loop()
    #     self.year_period.loop()
    #
    #     for orb in self.system:
    #         orb.rotate(rotate)

    def rotate(self, rotate=True):  # Unschoen, sollte wie oben sein, funktioniert aber nicht
        self.day_period.loop()

        for orb in self.system:
            orb.day_period.loop()
            orb.year_period.loop()


    def set_system_center(self, orb):

        if orb is None:
            self.system_center = None
            self.orbit_root = render.attachNewNode('orbit_root_' + self.name)
            self.orb_model.model.reparentTo(self.orbit_root)
            self.orb_model.model.setPos(self.orbit_radius, 0, 0)

            self.year_period = self.orbit_root.hprInterval(self.year_scale, Vec3(360, 0, 0))
            self.day_period = self.orb_model.model.hprInterval(self.day_scale, Vec3(360, 0, 0))
            print "set pos to " + str(self.orbit_radius)

        elif isinstance(orb, Orb):
            self.system_center = orb
            self.orbit_root = orb.orbit_root.attachNewNode('orbit_root_' + self.name)
            self.orb_model.model.reparentTo(self.orbit_root)
            self.orb_model.model.setPos(self.orbit_radius, 0, 0)

            self.year_period = self.orbit_root.hprInterval((self.year_scale), Vec3(360, 0, 0))
            self.day_period = self.orb_model.model.hprInterval((self.day_scale), Vec3(360, 0, 0))

            print "set pos to " + str(self.orbit_radius + self.orb_model.size)

            orb.add_orb(self)

        else:
            raise Exception

    def change_speed(self, factor, orb_name=None):

        if orb_name is None or orb_name == self.name:
            self.day_scale *= factor
            self.year_scale *= factor

        for orb in self.system:
            orb.change_speed(factor, orb_name)

    def speed_up(self):
        self.year_period.setPlayRate(self.year_period.getPlayRate() + 2)
        for orb in self.system:
            orb.speed_up()

    def slow_down(self):
        self.year_period.setPlayRate(self.year_period.getPlayRate() - 2)
        for orb in self.system:
            orb.slow_down()

    def __repr__(self):
        return self.name + (str(self.system) if len(self.system) != 0 else "")


class Planet(Orb):
    def __init__(self, name, orbit_radius, orb_model, year_scale=1, day_scale=1, rotation_cw=True, system_center=None):
        super(Planet, self).__init__(name, orbit_radius, orb_model, year_scale, day_scale, rotation_cw, system_center)


class Star(Orb):
    def __init__(self, name, orbit_radius, orb_model, year_scale=1, day_scale=1, rotation_cw=True, system_center=None,
                 light_strength=1):
        super(Star, self).__init__(name, orbit_radius, orb_model, year_scale, day_scale, rotation_cw, system_center)
        self.__light_strength = light_strength


class OrbModel(object):
    def __init__(self, texture, size=1, model="../models/planet_sphere"):
        self.model = loader.loadModel(model)
        self.texture = loader.loadTexture(texture)
        self.size = size
        self.model.setTexture(self.texture, 1)
        self.model.setScale(size)

import direct.directbase.DirectStart
from direct.showbase import DirectObject
from panda3d.core import TextNode, Vec3, Vec4
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
import sys

from src.main.Orb import *


class SolarSystem(DirectObject):
    def genLabelText(self, text, i):
        return OnscreenText(text=text, pos=(-1.3, .95 - .05 * i), fg=(1, 1, 1, 1), align=TextNode.ALeft, scale=.05, mayChange=1)

    def __init__(self):
        DirectObject.__init__(self)

        base.setBackgroundColor(0, 0, 0)
        camera.setPos(0, 0, 95)
        camera.setHpr(0, -90, 0)

        self.yearscale = 60
        self.dayscale = self.yearscale / 365.0 * 5
        self.orbitscale = 10
        self.sizescale = 0.6

        self.loadPlanets()

        self.sun.rotate()

        self.show_textures = True

        self.accept("t", self.showTexture)

# end __init__

    def loadPlanets(self):
        self.sky = loader.loadModel("../models/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("../models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(100)

        self.sun = Star("sun", 0, OrbModel("../models/sun_1k_tex.jpg", self.sizescale), 1/0.5, 1, True, None, 1)
        self.earth = Planet("earth", 5, OrbModel("../models/earth_1k_tex.jpg", self.sizescale), 1/0.3, 1, True, self.sun)
        self.moon = Planet("moon", 3, OrbModel("../models/moon_1k_tex.jpg", 0.1 * self.sizescal), 1/0.2, 1, True, self.earth)
        self.mercury = Planet("mercury", 15, OrbModel("../models/mercury_1k_tex.jpg", 0.385 * self.sizescale), 1/0.15, 1, True, self.sun)
        self.venus = Planet("venus", 20, OrbModel("../models/venus_1k_tex.jpg", 0.923 * self.sizescale), 1/0.1, 1, True, self.sun)
        self.mars = Planet("mars", 25, OrbModel("../models/mars_1k_tex.jpg", 0.5 * self.sizescale), 1/0.08, 1, True, self.sun)
        self.jupiter = Planet("juptier", 30, OrbModel("../models/jupiter.jpg", 1.3 * self.sizescale), 1/0.05, 1, True, self.sun)
        self.saturn = Planet("saturn", 35, OrbModel("../models/saturn.jpg", 0.7 * self.sizescale), 1/0.04, 1, True, self.sun)
        self.mercury = Planet("uranus", 40, OrbModel("../models/uranus.jpg", 0.8 * self.sizescale), 1/0.03, 1, True, self.sun)
        self.neptune = Planet("neptune", 45, OrbModel("../models/neptun.jpg", 0.6 * self.sizescale), 1/0.02, 1, True, self.sun)

        print self.sun

    def showTexture(self):
            self.sun.show_tex(not self.show_textures)
            self.show_textures = not self.show_textures

w = SolarSystem()

run()

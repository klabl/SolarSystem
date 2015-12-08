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
        # self.texture = False
        # self.legendFull = True
        self.loadPlanets()
        # self.rotatePlanets()

    # end __init__

    def loadPlanets(self):
        self.sky = loader.loadModel("../models/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("../models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(100)

        self.sun_model = OrbModel("../models/sun_1k_tex.jpg")
        self.sun = Star("sun", 0, self.sun_model, 1, 1, True, None, 1)

        self.earth_model = OrbModel("../models/earth_1k_tex.jpg")
        self.earth = Planet("earth", 3, self.earth_model, 1, 1, True, self.sun)

        self.moon_model = OrbModel("../models/moon_1k_tex.jpg")
        self.moon = Planet("moon", 3, self.moon_model, 1, 1, True, self.earth)

        self.mercury_model = OrbModel("../models/mercury_1k_tex.jpg")
        self.mercury = Planet("mercury", 3, self.mercury_model, 1, 1, True, self.sun)

        self.venus_model = OrbModel("../models/venus_1k_tex.jpg")
        self.venus = Planet("venus", 3, self.venus_model, 1, 1, True, self.sun)

        self.mars_model = OrbModel("../models/mars_1k_tex.jpg")
        self.mars = Planet("mars", 3, self.mars_model, 1, 1, True, self.sun)

        self.jupiter_model = OrbModel("../models/jupiter.jpg")
        self.jupiter = Planet("juptier", 3, self.jupiter_model, 1, 1, True, self.sun)

        self.saturn_model = OrbModel("../models/saturn.jpg")
        self.saturn = Planet("saturn", 3, self.saturn_model, 1, 1, True, self.sun)

        self.uranus_model = OrbModel("../models/uranus.jpg")
        self.mercury = Planet("uranus", 3, self.uranus_model, 1, 1, True, self.sun)

        self.neptune_model = OrbModel("../models/neptun.jpg")
        self.neptune = Planet("neptune", 3, self.neptune_model, 1, 1, True, self.sun)



w = SolarSystem()

run()

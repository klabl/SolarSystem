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
        self.is_paused = False

        self.spacekeyText = self.genLabelText("Leertaste: Stoppen des gesamten Solar Systems [LAUFEND]", 0)

        self.accept("t", self.showTextures)
        self.accept("space", self.togglePause)

    # end __init__

    def loadPlanets(self):
        self.sky = loader.loadModel("../models/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("../models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(100)

        self.sun = Star("sun", 0, OrbModel("../models/sun_1k_tex.jpg", 2 * self.sizescale), 1, 20, True, None, 1)
        self.earth = Planet("earth", self.orbitscale, OrbModel("../models/earth_1k_tex.jpg", self.sizescale), self.yearscale, self.dayscale, True, self.sun)
        self.moon = Planet("moon",  1.1 * self.orbitscale, OrbModel("../models/moon_1k_tex.jpg", 0.1 * self.sizescale), .0749 * self.yearscale, .0749 * self.yearscale, True, self.earth)
        self.mercury = Planet("mercury", 0.38 * self.orbitscale, OrbModel("../models/mercury_1k_tex.jpg", 0.385 * self.sizescale), 0.241 * self.yearscale, 59 * self.dayscale, True, self.sun)
        self.venus = Planet("venus", 0.62 * self.orbitscale, OrbModel("../models/venus_1k_tex.jpg", 0.923 * self.sizescale), 0.615 * self.yearscale, 243 * self.dayscale, True, self.sun)
        self.mars = Planet("mars", 1.37 * self.orbitscale, OrbModel("../models/mars_1k_tex.jpg", 0.5 * self.sizescale), 1.881 * self.yearscale, 1.03 * self.dayscale, True, self.sun)
        self.jupiter = Planet("juptier", 1.75 * self.orbitscale, OrbModel("../models/jupiter.jpg", 1.3 * self.sizescale), 2 * self.yearscale, 1.2 * self.dayscale, True, self.sun)
        self.saturn = Planet("saturn", 2.1 * self.orbitscale, OrbModel("../models/saturn.jpg", 0.7 * self.sizescale), 2.2 * self.yearscale, 5 * self.dayscale, True, self.sun)
        self.uranus = Planet("uranus", 2.43 * self.orbitscale, OrbModel("../models/uranus.jpg", 0.8 * self.sizescale), 3 * self.yearscale, 10 * self.dayscale, True, self.sun)
        self.neptune = Planet("neptune", 2.87 * self.orbitscale, OrbModel("../models/neptun.jpg", 0.6 * self.sizescale), 10 * self.yearscale, 20 * self.dayscale, True, self.sun)

    def showTextures(self):
        self.sun.show_tex(not self.show_textures)
        self.show_textures = not self.show_textures

    def togglePause(self):
        self.sun.move(self.is_paused)
        self.is_paused = not self.is_paused




w = SolarSystem()

run()

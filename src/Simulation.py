import direct.directbase.DirectStart
from direct.showbase import DirectObject
from panda3d.core import TextNode, Vec3, Vec4, PointLight, VBase4, AmbientLight
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

        self.load_planets()

        self.sun.rotate()

        self.show_textures = True
        self.is_paused = False
        self.legend_full = True
        self.light_on = False
        self.year_counter = 0

        self.title = OnscreenText(text="Solar System",
                                  style=1, fg=(1,1,1,1),
                                  pos=(0.9,-0.95), scale = .07)
        self.spacekeyText = self.genLabelText("Leertaste: Stoppen des gesamten Solar Systems [LAUFEND]", 0)
        self.skeyEventText = self.genLabelText("[S]: Sonne Stoppen [LAUFEND]", 1)
        self.ykeyEventText = self.genLabelText("[Y]: Merkur Stoppen [LAUFEND]", 2)
        self.vkeyEventText = self.genLabelText("[V]: Venus Stoppen [LAUFEND]", 3)
        self.ekeyEventText = self.genLabelText("[E]: Erde Stoppen [LAUFEND]", 4)
        self.mkeyEventText = self.genLabelText("[M]: Mars Stoppen [LAUFEND]", 5)
        self.jkeyEventText = self.genLabelText("[J]: Jupiter Stoppen [LAUFEND]", 6)
        self.akeyEventText = self.genLabelText("[A]: Saturn Stoppen [LAUFEND]", 7)
        self.ukeyEventText = self.genLabelText("[U]: Uranus Stoppen [LAUFEND]", 8)
        self.nkeyEventText = self.genLabelText("[N]: Neptun Stoppen [LAUFEND]", 9)
        self.tkeyEventText = self.genLabelText("[T]: Textur an/aus", 10)
        self.lkeyEventText = self.genLabelText("[L]: Licht", 11)
        self.ikeyEventText = self.genLabelText("[I]: Legende ausblenden", 12)
        self.upkeyText = self.genLabelText("[Pfeil Up] Geschwindigkeit erhoehen", 13)
        self.downkeyText = self.genLabelText("[Pfeil Down] Geschwindigkeit verringern", 14)
        # self.yearCounterText = self.genLabelText("0 Erdenjahre vergangen", 15)
        self.text1 = self.genLabelText("Linke Maustaste: Kamera verschieben", 16)
        self.text2 = self.genLabelText("Rechte Maustaste: Kamera rein- und rauszoomen", 17)
        self.text3 = self.genLabelText("Mausrad: Kamerawinkel veraendern", 18)
        self.text4 = ""

        self.accept("t", self.showTextures)
        self.accept("space", self.togglePause)

        # self.accept("newYear", self.incYear)
        self.accept("arrow_up", self.speedUp)
        self.accept("arrow_down", self.slowDown)
        self.accept("escape", sys.exit)
        self.accept("l", self.light)
        self.accept("i", self.legend)

        self.accept("e", self.togglePlanet, ["Earth", self.skeyEventText])
        self.accept("s", self.togglePlanet, ["Sun", self.skeyEventText])
        self.accept("y", self.togglePlanet, ["Mercury", self.ykeyEventText])
        self.accept("v", self.togglePlanet, ["Venus", self.vkeyEventText])
        self.accept("m", self.togglePlanet, ["Mars", self.mkeyEventText])
        self.accept("j", self.togglePlanet, ["Jupiter",  self.jkeyEventText])
        self.accept("a", self.togglePlanet, ["Saturn", self.akeyEventText])
        self.accept("u", self.togglePlanet, ["Uranus", self.ukeyEventText])
        self.accept("n", self.togglePlanet, ["Neptun", self.ukeyEventText])

    # end __init__

    def load_planets(self):
        self.sky = loader.loadModel("../models/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("../models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(100)

        self.sun = Star("Sun", 0, OrbModel("../models/sun_1k_tex.jpg", 2 * self.sizescale), 0, 20, True, None, 1)
        self.earth = Planet("Earth", self.orbitscale, OrbModel("../models/earth_1k_tex.jpg", self.sizescale), self.yearscale, self.dayscale, True, self.sun)
        self.moon = Planet("Moon",  1.1 * self.orbitscale, OrbModel("../models/moon_1k_tex.jpg", 0.1 * self.sizescale), .0749 * self.yearscale, .0749 * self.yearscale, True, self.earth)
        self.mercury = Planet("Mercury", 0.38 * self.orbitscale, OrbModel("../models/mercury_1k_tex.jpg", 0.385 * self.sizescale), 0.241 * self.yearscale, 59 * self.dayscale, True, self.sun)
        self.venus = Planet("Venus", 0.62 * self.orbitscale, OrbModel("../models/venus_1k_tex.jpg", 0.923 * self.sizescale), 0.615 * self.yearscale, 243 * self.dayscale, True, self.sun)
        self.mars = Planet("Mars", 1.37 * self.orbitscale, OrbModel("../models/mars_1k_tex.jpg", 0.5 * self.sizescale), 1.881 * self.yearscale, 1.03 * self.dayscale, True, self.sun)
        self.jupiter = Planet("Juptier", 1.75 * self.orbitscale, OrbModel("../models/jupiter.jpg", 1.3 * self.sizescale), 2 * self.yearscale, 1.2 * self.dayscale, True, self.sun)
        self.saturn = Planet("Saturn", 2.1 * self.orbitscale, OrbModel("../models/saturn.jpg", 0.7 * self.sizescale), 2.2 * self.yearscale, 5 * self.dayscale, True, self.sun)
        self.uranus = Planet("Uranus", 2.43 * self.orbitscale, OrbModel("../models/uranus.jpg", 0.8 * self.sizescale), 3 * self.yearscale, 10 * self.dayscale, True, self.sun)
        self.neptune = Planet("Neptune", 2.87 * self.orbitscale, OrbModel("../models/neptun.jpg", 0.6 * self.sizescale), 10 * self.yearscale, 20 * self.dayscale, True, self.sun)


    def showTextures(self):
        self.sun.show_tex(not self.show_textures)
        self.show_textures = not self.show_textures


    def togglePause(self, name=None, text=None):
        if name is None and text is None:
            self.sun.move(self.is_paused)
            self.is_paused = not self.is_paused


    def togglePlanet(self, planet_name, text=None):
        if self.sun.get_orb(planet_name).is_moving:
            print "Stoppen von " + planet_name
            state = " [PAUSE]"
        else:
            print "Weiterlaufen von " + planet_name
            state = " [LAUFEND]"

        if text is not None:
            old = text.getText()
            text.setText(old[0:old.rfind(' ')] + state)

        self.sun.toggle_moving(planet_name)


    def speedUp(self):
        self.sun.speed_up()


    def slowDown(self):
        self.sun.slow_down()


    def legend(self):
        if self.legend_full:
            self.spacekeyText.clearText()
            self.skeyEventText.clearText()
            self.ykeyEventText.clearText()
            self.ekeyEventText.clearText()
            self.vkeyEventText.clearText()
            self.mkeyEventText.clearText()
            self.jkeyEventText.clearText()
            self.akeyEventText.clearText()
            self.ukeyEventText.clearText()
            self.nkeyEventText.clearText()
            self.tkeyEventText.clearText()
            # self.yearCounterText.clearText()
            self.lkeyEventText.clearText()
            self.upkeyText.clearText()
            self.downkeyText.clearText()
            self.ikeyEventText.clearText()
            self.text1.destroy()
            self.text2.destroy()
            self.text3.destroy()
            self.text4 = self.genLabelText("[I]: Legende einblenden", 0)
            # self.yearCounterText = self.genLabelText(str(self.year_counter) + " Erdenjahre vergangen", 1)
            self.legend_full = False
        else:
            self.text4.destroy()
            # self.yearCounterText.destroy()
            self.spacekeyText = self.genLabelText("Leertaste: Stoppen des gesamten Solar Systems [LAUFEND]", 0)
            self.skeyEventText = self.genLabelText("[S]: Sonne Stoppen [LAUFEND]", 1)
            self.ykeyEventText = self.genLabelText("[Y]: Merkur Stoppen [LAUFEND]", 2)
            self.vkeyEventText = self.genLabelText("[V]: Venus Stoppen [LAUFEND]", 3)
            self.ekeyEventText = self.genLabelText("[E]: Erde Stoppen [LAUFEND]", 4)
            self.mkeyEventText = self.genLabelText("[M]: Mars Stoppen [LAUFEND]", 5)
            self.jkeyEventText = self.genLabelText("[J]: Jupiter Stoppen [LAUFEND]", 6)
            self.akeyEventText = self.genLabelText("[A]: Saturn Stoppen [LAUFEND]", 7)
            self.ukeyEventText = self.genLabelText("[U]: Uranus Stoppen [LAUFEND]", 8)
            self.nkeyEventText = self.genLabelText("[N]: Neptun Stoppen [LAUFEND]", 9)
            self.tkeyEventText = self.genLabelText("[T]: Textur an/aus", 10)
            self.lkeyEventText = self.genLabelText("[L]: Licht", 11)
            self.ikeyEventText = self.genLabelText("[I]: Legende ausblenden", 12)
            self.upkeyText = self.genLabelText("[Pfeil Up] Geschwindigkeit erhoehen",13)
            self.downkeyText = self.genLabelText("[Pfeil Down] Geschwindigkeit verringern",14)
            # self.yearCounterText = self.genLabelText(str(self.year_counter) + " Erdenjahre vergangen", 15)
            self.text1 = self.genLabelText("Linke Maustaste: Kamera verschieben",16)
            self.text2 = self.genLabelText("Rechte Maustaste: Kamera rein- und rauszoomen",17)
            self.text3 = self.genLabelText("Mausrad: Kamerawinkel veraendern",18)
            self.legend_full = True

    # def incYear(self):
    #     self.year_counter += 1
    #     self.yearCounterText.setText(str(self.year_counter) + " Erdenjahre vollendet")

    def light(self):
        if not self.light_on:
            plight1 = PointLight('plight1')
            plight1.setColor(VBase4(255, 255, 255, 0))
            plnp1 = render.attachNewNode(plight1)
            plnp1.setPos(0, 0, 0)
            render.setLight(plnp1)

            alight = AmbientLight('alight')
            alight.setColor(VBase4(0.2, 0.2, 0.2, 1))
            alnp = render.attachNewNode(alight)
            render.setLight(alnp)
            self.light_on = True
        else:
            render.setLightOff()
            self.light_on = False

w = SolarSystem()

base.run()

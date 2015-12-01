import direct.directbase.DirectStart
from direct.showbase import DirectObject
from panda3d.core import TextNode, Vec3, Vec4
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
import sys

class SolarSystem(DirectObject):

  def genLabelText(self, text, i):
    return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),
                       align = TextNode.ALeft, scale = .05, mayChange = 1)

  def __init__(self):

    base.setBackgroundColor(0, 0, 0)
    camera.setPos ( 0, 0, 95)
    camera.setHpr ( 0, -90, 0 )


    self.yearscale = 60
    self.dayscale = self.yearscale / 365.0 * 5
    self.orbitscale = 10
    self.sizescale = 0.6
    self.texture = False
    self.legendFull = True
    self.loadPlanets()
    self.rotatePlanets()

    self.title = OnscreenText(text="Solar System",
                              style=1, fg=(1,1,1,1),
                              pos=(0.9,-0.95), scale = .07)
    self.spacekeyText = self.genLabelText(
      "Leertaste: Stoppen des gesamten Solar Systems [LAUFEND]", 0)
    self.skeyEventText = self.genLabelText("[S]: Sonne Stoppen [LAUFEND]", 1)
    self.ykeyEventText = self.genLabelText("[Y]: Merkur Stoppen [LAUFEND]", 2)
    self.vkeyEventText = self.genLabelText("[V]: Venus Stoppen [LAUFEND]", 3)
    self.ekeyEventText = self.genLabelText("[E]: Erde Stoppen [LAUFEND]", 4)
    self.mkeyEventText = self.genLabelText("[M]: Mars Stoppen [LAUFEND]", 5)
    self.jkeyEventText = self.genLabelText("[J]: Jupiter Stoppen [LAUFEND]", 6)
    self.akeyEventText = self.genLabelText("[A]: Saturn Stoppen [LAUFEND]", 7)
    self.ukeyEventText = self.genLabelText("[U]: Uranus Stoppen [LAUFEND]", 8)
    self.nkeyEventText = self.genLabelText("[N]: Neptun Stoppen [LAUFEND]", 9)
    self.gkeyEventText = self.genLabelText("[G]: Geschwindigkeit", 10)
    self.tkeyEventText = self.genLabelText("[T]: Textur an/aus", 11)
    self.yearCounterText = self.genLabelText("0 Erdenjahre vergangen", 12)
    self.text1 = self.genLabelText("Linke Maustaste: Kamera verschieben",13)
    self.text2 = self.genLabelText("Rechte Maustaste: Kamera rein- und rauszoomen",14)
    self.text3 = self.genLabelText("Mausrad: Kamerawinkel veraendern",15)
    self.lkeyEventText = self.genLabelText("[L]: Legende ausblenden", 16)
    self.text4 = ""
    self.yearCounter = 0
    self.simRunning = True

    self.accept("space", self.handleSpace)
    self.accept("escape", sys.exit)
    self.accept("e", self.handleEarth)
    self.accept("s",
          self.togglePlanet,
          [ "Sun",


            self.day_period_sun,
            None, 
            self.skeyEventText])
    self.accept("y", self.togglePlanet,
          ["Mercury", self.day_period_mercury,
           self.orbit_period_mercury, self.ykeyEventText])
    self.accept("v", self.togglePlanet,
          ["Venus", self.day_period_venus,
           self.orbit_period_venus, self.vkeyEventText])
    self.accept("m", self.togglePlanet,
          ["Mars", self.day_period_mars,
           self.orbit_period_mars, self.mkeyEventText])
    self.accept("j", self.togglePlanet,
          ["Jupiter", self.day_period_jupiter,
           self.orbit_period_jupiter, self.jkeyEventText])
    self.accept("a", self.togglePlanet,
          ["Saturn", self.day_period_saturn,
           self.orbit_period_saturn, self.akeyEventText])
    self.accept("u", self.togglePlanet,
          ["Uranus", self.day_period_uranus,
           self.orbit_period_uranus, self.ukeyEventText])
    self.accept("n", self.togglePlanet,
          ["Neptun", self.day_period_neptun,
           self.orbit_period_neptun, self.ukeyEventText])


    self.accept("t", self.showTexture)
    self.accept("newYear", self.incYear)
    self.accept("l", self.legend)
    self.accept("+",self.speedUp)
    self.accept("-",self.slowDown)
  #end __init__




  def legend(self):
    if (self.legendFull == True):
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
      self.gkeyEventText.clearText()
      self.tkeyEventText.clearText()
      self.genLabelText().clearText()
      self.text1.destroy()
      self.text2.destroy()
      self.text3.destroy()
      self.text4 = self.genLabelText("[L]: Legende einblenden", 1)
      self.legendFull = False


  def showTexture(self):
    if(self.texture == False):
        self.sun.clearTexture()
        self.mercury.clearTexture()
        self.earth.clearTexture()
        self.moon.clearTexture()
        self.venus.clearTexture()
        self.mars.clearTexture()
        self.jupiter.clearTexture()
        self.saturn.clearTexture()
        self.uranus.clearTexture()
        self.neptun.clearTexture()
        self.texture = True
    elif(self.texture == True):
        self.sun.setTexture(self.sun_tex, 1)
        self.mercury.setTexture(self.mercury_tex, 1)
        self.venus.setTexture(self.venus_tex, 1)
        self.mars.setTexture(self.mars_tex, 1)
        self.jupiter.setTexture(self.jupiter_tex, 1)
        self.saturn.setTexture(self.saturn_tex, 1)
        self.uranus.setTexture(self.uranus_tex, 1)
        self.neptun.setTexture(self.neptun_tex, 1)
        self.earth.setTexture(self.earth_tex, 1)
        self.moon.setTexture(self.moon_tex, 1)
        self.texture = False

  def speedUp(self):
     self.day_period_sun.setPlayRate(self.day_period_sun.getPlayRate()+2)
     self.orbit_period_mercury.setPlayRate(self.orbit_period_mercury.getPlayRate()+2)
     self.day_period_mercury.setPlayRate(self.day_period_mercury.getPlayRate()+2)
     self.orbit_period_venus.setPlayRate(self.orbit_period_venus.getPlayRate()+2)
     self.day_period_venus.setPlayRate(self.day_period_venus.getPlayRate()+2)
     self.orbit_period_earth.setPlayRate(self.orbit_period_earth.getPlayRate()+2)
     self.day_period_earth.setPlayRate(self.day_period_earth.getPlayRate()+2)
     self.orbit_period_moon.setPlayRate(self.orbit_period_moon.getPlayRate()+2)
     self.day_period_moon.setPlayRate(self.day_period_moon.getPlayRate()+2)
     self.orbit_period_mars.setPlayRate(self.orbit_period_mars.getPlayRate()+2)
     self.day_period_mars.setPlayRate(self.day_period_mars.getPlayRate()+2)
     self.orbit_period_jupiter.setPlayRate(self.orbit_period_jupiter.getPlayRate()+2)
     self.day_period_jupiter.setPlayRate(self.day_period_jupiter.getPlayRate()+2)
     self.orbit_period_saturn.setPlayRate(self.orbit_period_saturn.getPlayRate()+2)
     self.day_period_saturn.setPlayRate(self.day_period_saturn.getPlayRate()+2)
     self.orbit_period_uranus.setPlayRate(self.orbit_period_uranus.getPlayRate()+2)
     self.day_period_uranus.setPlayRate(self.day_period_uranus.getPlayRate()+2)
     self.orbit_period_neptun.setPlayRate(self.orbit_period_neptun.getPlayRate()+2)
     self.day_period_neptun.setPlayRate(self.day_period_neptun.getPlayRate()+2)

  def slowDown(self):
     self.day_period_sun.setPlayRate(self.day_period_sun.getPlayRate()-2)
     self.orbit_period_mercury.setPlayRate(self.orbit_period_mercury.getPlayRate()-2)
     self.day_period_mercury.setPlayRate(self.day_period_mercury.getPlayRate()-2)
     self.orbit_period_venus.setPlayRate(self.orbit_period_venus.getPlayRate()-2)
     self.day_period_venus.setPlayRate(self.day_period_venus.getPlayRate()-2)
     self.orbit_period_earth.setPlayRate(self.orbit_period_earth.getPlayRate()-2)
     self.day_period_earth.setPlayRate(self.day_period_earth.getPlayRate()-2)
     self.orbit_period_moon.setPlayRate(self.orbit_period_moon.getPlayRate()-2)
     self.day_period_moon.setPlayRate(self.day_period_moon.getPlayRate()-2)
     self.orbit_period_mars.setPlayRate(self.orbit_period_mars.getPlayRate()-2)
     self.day_period_mars.setPlayRate(self.day_period_mars.getPlayRate()-2)
     self.orbit_period_jupiter.setPlayRate(self.orbit_period_jupiter.getPlayRate()-2)
     self.day_period_jupiter.setPlayRate(self.day_period_jupiter.getPlayRate()-2)
     self.orbit_period_saturn.setPlayRate(self.orbit_period_saturn.getPlayRate()-2)
     self.day_period_saturn.setPlayRate(self.day_period_saturn.getPlayRate()-2)
     self.orbit_period_uranus.setPlayRate(self.orbit_period_uranus.getPlayRate()-2)
     self.day_period_uranus.setPlayRate(self.day_period_uranus.getPlayRate()-2)
     self.orbit_period_neptun.setPlayRate(self.orbit_period_neptun.getPlayRate()-2)
     self.day_period_neptun.setPlayRate(self.day_period_neptun.getPlayRate()-2)

  def handleSpace(self):
    if self.simRunning:
      print "Pausing Simulation"
      self.spacekeyText.setText(
        "Leertaste: Stoppen des gesamten Solar Systems [PAUSE]")

      if self.day_period_sun.isPlaying():
        self.togglePlanet("Sun", self.day_period_sun, None,
                  self.skeyEventText)

      if self.day_period_mercury.isPlaying():
        self.togglePlanet("Mercury", self.day_period_mercury,
                  self.orbit_period_mercury, self.ykeyEventText)

      if self.day_period_venus.isPlaying():
        self.togglePlanet("Venus", self.day_period_venus,
                  self.orbit_period_venus, self.vkeyEventText)

      if self.day_period_earth.isPlaying():
        self.togglePlanet("Earth", self.day_period_earth,
                  self.orbit_period_earth, self.ekeyEventText)
        self.togglePlanet("Moon", self.day_period_moon,
                  self.orbit_period_moon)

      if self.day_period_mars.isPlaying():
        self.togglePlanet("Mars", self.day_period_mars,
                  self.orbit_period_mars, self.mkeyEventText)

      if self.day_period_jupiter.isPlaying():
        self.togglePlanet("Jupiter", self.day_period_jupiter,
                  self.orbit_period_jupiter, self.jkeyEventText)

      if self.day_period_saturn.isPlaying():
        self.togglePlanet("Saturn", self.day_period_saturn,
                  self.orbit_period_saturn, self.akeyEventText)

      if self.day_period_uranus.isPlaying():
        self.togglePlanet("Uranus", self.day_period_uranus,
                  self.orbit_period_uranus, self.ukeyEventText)
      if self.day_period_neptun.isPlaying():
        self.togglePlanet("Neptun", self.day_period_neptun,
                  self.orbit_period_neptun, self.nkeyEventText)

    else:
      print "Resuming Simulation"
      self.spacekeyText.setText(
        "Leertaste: Stoppen des gesamten Solar Systems [LAUFEND]")
      if not self.day_period_sun.isPlaying():
        self.togglePlanet("Sun", self.day_period_sun, None,
                  self.skeyEventText)
      if not self.day_period_mercury.isPlaying():
        self.togglePlanet("Mercury", self.day_period_mercury,
                  self.orbit_period_mercury, self.ykeyEventText)
      if not self.day_period_venus.isPlaying():
        self.togglePlanet("Venus", self.day_period_venus,
                  self.orbit_period_venus, self.vkeyEventText)
      if not self.day_period_earth.isPlaying():
        self.togglePlanet("Earth", self.day_period_earth,
                  self.orbit_period_earth, self.ekeyEventText)
        self.togglePlanet("Moon", self.day_period_moon,
                  self.orbit_period_moon)
      if not self.day_period_mars.isPlaying():
        self.togglePlanet("Mars", self.day_period_mars,
                  self.orbit_period_mars, self.mkeyEventText)
      if not self.day_period_jupiter.isPlaying():
        self.togglePlanet("Jupiter", self.day_period_jupiter,
                  self.orbit_period_jupiter, self.jkeyEventText)
      if not self.day_period_saturn.isPlaying():
        self.togglePlanet("Saturn", self.day_period_saturn,
                  self.orbit_period_saturn, self.akeyEventText)
      if not self.day_period_uranus.isPlaying():
        self.togglePlanet("Uranus", self.day_period_uranus,
                  self.orbit_period_uranus, self.ukeyEventText)
      if not self.day_period_neptun.isPlaying():
        self.togglePlanet("Neptun", self.day_period_neptun,
                  self.orbit_period_neptun, self.nkeyEventText)
    self.simRunning = not self.simRunning

  def togglePlanet(self, planet, day, orbit = None, text = None):
    if day.isPlaying():
      print "Stoppen von " + planet
      state = " [PAUSED]"
    else:
      print "Weiterlaufen von " + planet
      state = " [RUNNING]"

    if text:
      old = text.getText()
      text.setText(old[0:old.rfind(' ')] + state)

    self.toggleInterval(day)
    if orbit: self.toggleInterval(orbit)

  def toggleInterval(self, interval):
    if interval.isPlaying(): interval.pause()
    else: interval.resume()

  def handleEarth(self):
    self.togglePlanet("Earth", self.day_period_earth,
              self.orbit_period_earth, self.ekeyEventText)
    self.togglePlanet("Moon", self.day_period_moon,
              self.orbit_period_moon)

  def incYear(self):
    self.yearCounter += 1
    self.yearCounterText.setText(str(self.yearCounter) + " Erdenjahre vollendet")
  
  def loadPlanets(self):
    self.orbit_root_mercury = render.attachNewNode('orbit_root_mercury')
    self.orbit_root_venus = render.attachNewNode('orbit_root_venus')
    self.orbit_root_mars = render.attachNewNode('orbit_root_mars')
    self.orbit_root_earth = render.attachNewNode('orbit_root_earth')
    self.orbit_root_jupiter= render.attachNewNode('orbit_root_jupiter')
    self.orbit_root_saturn= render.attachNewNode('orbit_root_saturn')
    self.orbit_root_uranus= render.attachNewNode('orbit_root_uranus')
    self.orbit_root_neptun= render.attachNewNode('orbit_root_neptun')

    self.orbit_root_moon = (
      self.orbit_root_earth.attachNewNode('orbit_root_moon'))


    self.sky = loader.loadModel("../models/solar_sky_sphere")

    self.sky_tex = loader.loadTexture("../models/stars_1k_tex.jpg")
    self.sky.setTexture(self.sky_tex, 1)
    self.sky.reparentTo(render)
    self.sky.setScale(100)

    self.sun = loader.loadModel("../models/planet_sphere")
    self.sun_tex = loader.loadTexture("../models/sun_1k_tex.jpg")
    self.sun.setTexture(self.sun_tex, 1)
    self.sun.reparentTo(render)
    self.sun.setScale(2 * self.sizescale)

    self.mercury = loader.loadModel("../models/planet_sphere")
    self.mercury_tex = loader.loadTexture("../models/mercury_1k_tex.jpg")
    self.mercury.setTexture(self.mercury_tex, 1)
    self.mercury.reparentTo(self.orbit_root_mercury)
    self.mercury.setPos( 0.38 * self.orbitscale, 0, 0)
    self.mercury.setScale(0.385 * self.sizescale)

    self.venus = loader.loadModel("../models/planet_sphere")
    self.venus_tex = loader.loadTexture("../models/venus_1k_tex.jpg")
    self.venus.setTexture(self.venus_tex, 1)
    self.venus.reparentTo(self.orbit_root_venus)
    self.venus.setPos( 0.72 * self.orbitscale, 0, 0)
    self.venus.setScale(0.923 * self.sizescale)

    self.mars = loader.loadModel("../models/planet_sphere")
    self.mars_tex = loader.loadTexture("../models/mars_1k_tex.jpg")
    self.mars.setTexture(self.mars_tex, 1)
    self.mars.reparentTo(self.orbit_root_mars)
    self.mars.setPos( 1.52 * self.orbitscale, 0, 0)
    self.mars.setScale(0.5 * self.sizescale)

    self.jupiter = loader.loadModel("../models/planet_sphere")
    self.jupiter_tex = loader.loadTexture("../models/jupiter.jpg")
    self.jupiter.setTexture(self.jupiter_tex, 1)
    self.jupiter.reparentTo(self.orbit_root_jupiter)
    self.jupiter.setPos( 1.9 * self.orbitscale, 0, 0)
    self.jupiter.setScale(1.3 * self.sizescale)

    self.saturn = loader.loadModel("../models/planet_sphere")
    self.saturn_tex = loader.loadTexture("../models/saturn.jpg")
    self.saturn.setTexture(self.saturn_tex, 1)
    self.saturn.reparentTo(self.orbit_root_saturn)
    self.saturn.setPos( 2.4 * self.orbitscale, 0, 0)
    self.saturn.setScale(0.7 * self.sizescale)

    self.uranus = loader.loadModel("../models/planet_sphere")
    self.uranus_tex = loader.loadTexture("../models/uranus.jpg")
    self.uranus.setTexture(self.uranus_tex, 1)
    self.uranus.reparentTo(self.orbit_root_uranus)
    self.uranus.setPos( 2.8 * self.orbitscale, 0, 0)
    self.uranus.setScale(0.8 * self.sizescale)

    self.neptun = loader.loadModel("../models/planet_sphere")
    self.neptun_tex = loader.loadTexture("../models/neptun.jpg")
    self.neptun.setTexture(self.neptun_tex, 1)
    self.neptun.reparentTo(self.orbit_root_neptun)
    self.neptun.setPos( 3.2 * self.orbitscale, 0, 0)
    self.neptun.setScale(0.6 * self.sizescale)

    self.earth = loader.loadModel("../models/planet_sphere")
    self.earth_tex = loader.loadTexture("../models/earth_1k_tex.jpg")
    self.earth.setTexture(self.earth_tex, 1)
    self.earth.reparentTo(self.orbit_root_earth)
    self.earth.setScale(self.sizescale)
    self.earth.setPos( self.orbitscale, 0, 0)

    self.orbit_root_moon.setPos( self.orbitscale, 0, 0)

    self.moon = loader.loadModel("../models/planet_sphere")
    self.moon_tex = loader.loadTexture("../models/moon_1k_tex.jpg")
    self.moon.setTexture(self.moon_tex, 1)
    self.moon.reparentTo(self.orbit_root_moon)
    self.moon.setScale(0.1 * self.sizescale)
    self.moon.setPos(0.1 * self.orbitscale, 0, 0)


  def rotatePlanets(self):
    self.day_period_sun = self.sun.hprInterval(20, Vec3(360, 0, 0))

    self.orbit_period_mercury = self.orbit_root_mercury.hprInterval(
      (0.241 * self.yearscale), Vec3(360, 0, 0))
    self.day_period_mercury = self.mercury.hprInterval(
      (59 * self.dayscale), Vec3(360, 0, 0))

    self.orbit_period_venus = self.orbit_root_venus.hprInterval(
      (0.615 * self.yearscale), Vec3(360, 0, 0))
    self.day_period_venus = self.venus.hprInterval(
      (243 * self.dayscale), Vec3(360,0,0))

    self.orbit_period_earth = Sequence(
      self.orbit_root_earth.hprInterval(self.yearscale, Vec3(360, 0, 0)),
      Func(messenger.send, "newYear"))
    self.day_period_earth = self.earth.hprInterval(
      self.dayscale, Vec3(360, 0, 0))

    self.orbit_period_moon = self.orbit_root_moon.hprInterval(
      (.0749 * self.yearscale), Vec3(360, 0, 0))
    self.day_period_moon = self.moon.hprInterval(
      (.0749 * self.yearscale), Vec3(360, 0, 0))

    self.orbit_period_mars = self.orbit_root_mars.hprInterval(
      (1.881 * self.yearscale), Vec3(360, 0, 0))
    self.day_period_mars = self.mars.hprInterval(
      (1.03 * self.dayscale), Vec3(360, 0, 0))

    self.orbit_period_jupiter = self.orbit_root_jupiter.hprInterval(
      (2 * self.yearscale), Vec3(360, 0, 0))
    self.day_period_jupiter = self.jupiter.hprInterval(
      (1.2 * self.dayscale), Vec3(360, 0, 0))

    self.orbit_period_saturn = self.orbit_root_saturn.hprInterval(
      (2.2 * self.yearscale), Vec3(360, 0, 0))
    self.day_period_saturn = self.saturn.hprInterval(
      (5 * self.dayscale), Vec3(360, 0, 0))

    self.orbit_period_uranus = self.orbit_root_uranus.hprInterval(
      (3 * self.yearscale), Vec3(360, 0, 0))
    self.day_period_uranus = self.uranus.hprInterval(
      (10 * self.dayscale), Vec3(360, 0, 0))

    self.orbit_period_neptun = self.orbit_root_neptun.hprInterval(
      (10 * self.yearscale), Vec3(360, 0, 0))
    self.day_period_neptun = self.neptun.hprInterval(
      (20 * self.dayscale), Vec3(360, 0, 0))
    self.day_period_sun.loop()
    self.orbit_period_mercury.loop()
    self.day_period_mercury.loop()
    self.orbit_period_venus.loop()
    self.day_period_venus.loop()
    self.orbit_period_earth.loop()
    self.day_period_earth.loop()
    self.orbit_period_moon.loop()
    self.day_period_moon.loop()
    self.orbit_period_mars.loop()
    self.day_period_mars.loop()
    self.orbit_period_jupiter.loop()
    self.day_period_jupiter.loop()
    self.orbit_period_saturn.loop()
    self.day_period_saturn.loop()
    self.orbit_period_uranus.loop()
    self.day_period_uranus.loop()
    self.orbit_period_neptun.loop()
    self.day_period_neptun.loop()

w = SolarSystem()

run()


import pyglet
from pyglet.gl.glu import *
from pyglet.gl.gl import *

from src.main.Orb import Planet

__author__ = 'mreilaender'

# asd

window = pyglet.window.Window(resizable=False, fullscreen=True)


def init():
    # Initialize planets
    pass


@window.event
def on_draw():
    window.clear()

    # 3r Projektion einstellen
    glEnable(GL_DEPTH_TEST)
    # Kamera auf Fenstergroesse einstellen
    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, window.width, window.height)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLoadIdentity()

    # Lege Perspektive fest
    gluPerspective(45, window.width/window.height, 0.1, 100.0)

    #
    gluLookAt(
            0, 60, 0,
            0, 0, 0,
            0, 0, 1
            )

    # Lade ModelView Matrix
    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()
    glRotatef(45, 1, 0, 0)
    planet1.draw()

    glLoadIdentity()
    # Transliert das Objekt um 10 in die positive x Richtung
    planet2.pos_x = 10
    glRotatef(-45, 1, 0, 0)
    planet2.draw()


def update(time):
    """
    Update Method - hier wird nur berechnet nicht gezeichnet, bzw die update Methoden der Planeten aufgerufen
    :param time: Time which has past during the last call of this method. Pyglet calculates this automatically
    :return:
    """
    # TODO evtl Liste aller Planeten -> dann muss man nurmehr mit einer for durchgehen und die update Methode aufrufen
    # print("Time: %s" % time)
    planet1.update(time)
    planet2.update(time)
    # print("x: %s y: %s z: %s" % (planet2.pos_x, planet2.pos_y, planet2.pos_z))


def set_speed(speed):
    pass


def accelerate():
    # which parameters?
    pass


def deccelerate():
    pass


def show_textures(show=True):
    pass


def pause(pause=True):
    pass


# Initialize planets
# gluNewQuadrtic ist die standard textur
planet1 = Planet("Test Planet", 3, gluNewQuadric())
planet2 = Planet("Test Planet2", 1, gluNewQuadric(), day_scale=0.5)

# Setting update method
pyglet.clock.schedule(update)
pyglet.app.run()

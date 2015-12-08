import pyglet
from pyglet.gl import *
from pyglet.window import key

from src.tmp.Planet import *
from src.tmp.Planet2 import *
from src.main.Camera import *

__author__ = "Manuel"

# pl = ExamplePlanet("Example Planet", 2, 2, 2, 2, 2)

# while True:
#    pass

window = pyglet.window.Window(resizable=False)
window.set_size(800, 600)

planet = Planet()
planet2 = Planet2()
camera = Camera()





def update(time):
    global planet, planet2
    planet.update()
    planet2.update()


@window.event
def on_draw():
    window.clear()

    # glMatrixMode(GL_PROJECTION)

    # 3r Projektion einstellen
    glEnable(GL_DEPTH_TEST)
    # Kamera auf Fenstergroesse einstellen
    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, window.width, window.height)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLoadIdentity()

    # Lege Perspektive fest
    gluPerspective(45, window.width/window.height, 0.1, 100.0)

    global camera
    camera.eyey = 10
    camera.upz = 1
    camera.draw()

    # Lade ModelView Matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_lines()

    global planet, planet2
    planet.draw()
    planet2.draw()


def draw_lines():
    # TODO Transparenter machen mit glColor4ui
    glLoadIdentity()
    # Rote Achse -- X-Achse
    glLineWidth(2.5)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(100, 0, 0)
    glEnd()

    glLoadIdentity()
    # Gruene Achse -- Y-Achse
    glLineWidth(2.5)
    glColor3f(1, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 100, 0)
    glEnd()

    glLoadIdentity()
    # Weisse Achse -- Z-Achse
    glLineWidth(2.5)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 100)
    glEnd()

pyglet.clock.schedule_interval(update, 1/144)
pyglet.app.run()

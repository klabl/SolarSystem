from pyglet.gl.glu import *
from pyglet.gl.gl import *


class Planet(object):

    def __init__(self, velocity=1):
        self.velocity = velocity
        self.rotate = 0

        self.r = 0.10
        self.g = 0.98
        self.b = 0.46

    def draw(self):
        glLoadIdentity()

        glColor3f(self.r, self.g, self.b)
        glRotatef(self.rotate, 1, 1, 0)
        # glTranslatef(0.01, 0.01, 0.01)
        gluSphere(gluNewQuadric(), 1, 20, 12)

    def update(self):
        self.rotate += self.velocity

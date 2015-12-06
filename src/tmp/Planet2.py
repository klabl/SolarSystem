from pyglet.gl.glu import *
from pyglet.gl.gl import *


class Planet2(object):

    def __init__(self, velocity=1):
        self.velocity = velocity
        self.rotate = 0

        self.r = 0.10
        self.g = 0.98
        self.b = 0.46

    def draw(self):
        self.rotate += self.velocity
        glLoadIdentity()

        glColor3f(self.r, self.g, self.b)
        glTranslatef(10, 10, 0)
        glRotatef(self.rotate, 0, 1, 0)
        gluSphere(gluNewQuadric(), 1, 20, 12)

    def update(self):
        self.rotate += self.velocity

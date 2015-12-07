from pyglet.gl import glTranslatef, glRotatef
from pyglet.gl.glu import gluLookAt

from src.tmp.Drawable import Drawable


class Camera(Drawable):

    def update(self):
        pass

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.angle = 0
        self.rotatex = 0
        self.rotatey = 0
        self.rotatez = 0

    def draw(self):
        glTranslatef(-self.x, -self.y, -self.z)
        if self.rotatex != 0 or self.rotatey != 0 or self.rotatez != 0:
            glRotatef(self.angle, self.rotatex, self.rotatey, self.rotatez)

    def reset(self):
        self.rotatex, self.rotatey, self.rotatez = 0, 0, 0

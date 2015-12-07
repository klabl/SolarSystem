from pyglet.gl.glu import gluLookAt

from src.tmp.Drawable import Drawable


class Camera(Drawable):

    def update(self):
        pass

    def __init__(self, eyex=0, eyey=0, eyez=0, centerx=0, centery=0, centerz=0, upx=0, upy=0, upz=0):
        self.eyex = eyex
        self.eyey = eyey
        self.eyez = eyez

        self.centerx = centerx
        self.centery = centery
        self.centerz = centerz

        self.upx = upx
        self.upy = upy
        self.upz = upz

    def draw(self):
        gluLookAt(
            self.eyex, self.eyey, self.eyez,
            self.centerx, self.centery, self.centerz,
            self.upx, self.upy, self.upz
        )

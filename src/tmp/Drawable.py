from abc import ABCMeta


class Drawable:
    __metaclass__ = ABCMeta

    def draw(self):
        raise NotImplementedError("Abstract Method not implemented yet")

    def update(self):
        raise NotImplementedError("Abstract Method not implemented yet")

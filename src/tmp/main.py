import pyglet
from pyglet.gl import *
from pyglet.gl.glu import *
from pyglet.window import key
__author__ = "Manuel"


window = pyglet.window.Window(resizable=False)
window.set_size(800, 600)

# r ist die Geschwindgkeit mit der sich die Kugel dreht
r = 3

# Translateion in x, y oder z Richtung
tx = 0.01
ty = 0.01
tz = 0.01

# Die Startwerte der verschiedenen Farben
colorR = 0
colorG = 1.0
colorB = 0.5

# Geschwindigkeit mit der sich die Farbe ändert
colorChangeSpeed = 0.01

# Other usefull variables
inventR = False
inventG = False
inventB = False

# stop
stop = False


@window.event()
def on_key_press(symbol, modifier):
    if symbol == key.SPACE:
        global stop
        stop = not stop
        print("Stop: ", stop)


def update(time):
    if not stop:
        # In der Update funktion berechnet man immer nur werte, die man dann in der on_draw verwendet
        global r, tx, ty, tz
        r += 1
        tx -= 0.001
        ty -= 0.001
        tz += 0.01
        color_change()


def color_change():
    global colorR, colorG, colorB, colorChangeSpeed, inventR, inventG, inventB
    # Color Change wird für R, G und B jedes mal, abhängig von der frequenz geändert
    if colorR <= 1.0 and not inventR:
        if colorR >= 0.99:
            inventR = True
        colorR += colorChangeSpeed
    elif colorR >= 0.0 or inventR:
        if colorR <= 0.001:
            inventR = False
        colorR -= colorChangeSpeed

    if colorG <= 1.0 and not inventG:
        if colorG >= 0.99:
            inventG = True
        colorG += colorChangeSpeed
    elif colorG >= 0.0 or inventG:
        if colorG <= 0.001:
            inventG = False
        colorG -= colorChangeSpeed

    if colorB <= 1.0 and not inventB:
        if colorB >= 0.99:
            inventB = True
        colorB += colorChangeSpeed
    elif colorB >= 0.0 or inventB:
        if colorB <= 0.001:
            inventB = False
        colorB -= colorChangeSpeed


@window.event
def on_draw():
    window.clear()

    # 3r Projektion einstellen
    glEnable(GL_DEPTH_TEST)
    # Kamera auf Fenstergröße einstellen
    glViewport(0, 0, window.width, window.height)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Lege Perspektive fest
    gluPerspective(65, window.width/window.height, 0.1, 100.0)

    # Lade ModelView Matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Verschiebt die Modelle nach vorne, sodass man sie sieht
    glTranslatef(0, 0, -5.0)

    q = gluNewQuadric()

    global colorR, colorG, colorB, tx, ty, tz
    glColor3f(colorR, colorG, colorB)
    glTranslatef(tx, ty, tz)
    glRotatef(r, 1, 1, 1)
    # glTranslatef(0, 0, -5.0)
    gluSphere(q, 0.3, 20, 12)

    glLoadIdentity()
    q = gluNewQuadric()
    glRotatef(r, 0, 1, 0)
    gluSphere(q, 0.5, 20, 12)



pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()

import pyglet
from pyglet.window import key
from random import randint

class Wall():
    def __init__(self, placement):
        self.x,self.y = 0,0
        self.img = pyglet.image.load("img/wall/wall.jpg")
        self.wall = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)
        if placement == "top":
            self.x = 628
            self.y = 0
            self.wall = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)
        elif placement == "bottom":
            self.x = 628
            self.y = 480
class Background():
    def __init__(self):
        self.img = pyglet.image.load("img/background/borderPatrol.jpg")
        self.background = pyglet.sprite.Sprite(self.img, x=0, y=0)
class Laser():
    def __init__(self, xx, yy):
        self.width = 50
        self.x = xx
        self.y = yy
        self.left = False
        self.right = False
        self.img = [pyglet.image.load("img/lasers/right.jpg"), pyglet.image.load("img/lasers/left.jpg")]
        self.lasers = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
    def move(self):
        if self.left == True:
            self.lasers = pyglet.sprite.Sprite(self.img[1], x=self.x, y=self.y)
            self.x = self.x - 5
            self.lasers.x = self.x
        if self.right == True:
            self.lasers = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
            self.x = self.x + 5
            self.lasers.x = self.x
        if self.x == 578:
            lasers.remove(self)
def moveLaser(dt):
    if lasers:
        for laser in lasers:
            laser.move()
class Character():
    def __init__(self, xx, yy, types, player):
        self.x = xx
        self.y = yy
        self.velocity = 5
        # Directions
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        if types == "user":
            self.width = 100
            self.img = [pyglet.image.load("img/mexico/right.jpg"), pyglet.image.load("img/mexico/left.jpg")]
            self.character = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
        elif types == "enemy":
            self.width = 50
            self.img = [pyglet.image.load("img/trump/right.jpg"), pyglet.image.load("img/trump/left.jpg")]
            self.character = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
    def move(self, dt):
        if self.up == True:
            self.y = self.y + self.velocity
            self.character.y = self.y
        if self.down == True:
            self.y = self.y - self.velocity
            self.character.y = self.y
        if self.left == True:
            self.character = pyglet.sprite.Sprite(self.img[1], x=self.x, y=self.y)
            self.x = self.x - self.velocity
            self.character.x = self.x
        if self.right == True:
            self.character = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
            self.x = self.x + self.velocity
            self.character.x = self.x

window = pyglet.window.Window(1280, 480)
window.set_caption("Backslash")

choices = ["up", "down", "left", "right"]

background = Background()
char = Character(50, 50, "user", "mexico")
enemy = Character(50,50, "enemy", None)
wall = Wall("top")
keys = key.KeyStateHandler()
window.push_handlers(keys)
lasers = []

@window.event
def on_draw():
    window.clear()
    background.background.draw()
    char.character.draw()
    wall.wall.draw()
    x = randint(0,3)
    if choices[x] == "up":
        enemy.up = True
    if choices[x] == "down":
        enemy.down = True
    if choices[x] == "left":
        enemy.left = True
    if choices[x] == "right":
        enemy.right = True
    enemy.character.draw()
    for x in range(len(lasers)):
        lasers[x].lasers.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.W:
        char.up = True
    if symbol == key.S:
        char.down = True
    if symbol == key.A:
        char.left = True
    if symbol == key.D:
        char.right = True
    if symbol == key.SPACE:
        laser = Laser(char.x, char.y)
        if not(char.left or char.right):
            pass
        elif char.left == True:
            laser.left = True
            laser.x -= laser.width
        elif char.right == True:
            laser.right = True
            laser.x += char.width
        if laser.left or laser.right:
            lasers.append(laser)
@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.W:
        char.up = False
    if symbol == key.S:
        char.down = False
    if symbol == key.A:
        char.left = False
    if symbol == key.D:
        char.right = False
pyglet.clock.schedule_interval(moveLaser, 1/60.0)
pyglet.clock.schedule_interval(char.move, 1/60.0)
pyglet.clock.schedule_interval(enemy.move, 1/60.0)
pyglet.app.run()
import pyglet
from pyglet.window import key
from random import randint

class Wall():
    def __init__(self, placement):
        self.x,self.y = 0,0
        self.img = pyglet.image.load("img\\wall\\wall.jpg")
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
        self.img = pyglet.image.load("img\\background\\borderPatrol.jpg")
        self.background = pyglet.sprite.Sprite(self.img, x=0, y=0)

class Character():
    def __init__(self, xx, yy, types, player):
        self.x = xx
        self.y = yy
        if types == "user":
            if player == "animae":
                self.img = [pyglet.image.load("img\\animae\\right.jpg"), pyglet.image.load("img\\animae\\left.jpg")]
                self.character = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
            elif player == "mexico":
                self.img = [pyglet.image.load("img\\mexico\\right.jpg"), pyglet.image.load("img\\mexico\\left.jpg")]
                self.character = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
        elif types == "enemy":
            self.img = [pyglet.image.load("img\\trump\\right.jpg"), pyglet.image.load("img\\trump\\left.jpg")]
            self.character = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
    def up(self, velocity):
        self.y = self.y + velocity
        self.character.y = self.y
    def down(self, velocity):
        self.y = self.y - velocity
        self.character.y = self.y
    def left(self, velocity):
        self.character = pyglet.sprite.Sprite(self.img[1], x=self.x, y=self.y)
        self.x = self.x - velocity
        self.character.x = self.x
    def right(self, velocity):
        self.character = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
        self.x = self.x + velocity
        self.character.x = self.x

window = pyglet.window.Window(1280, 480)
window.set_caption("Death")

choices = ["up", "down", "left", "right"]

background = Background()
char = Character(50, 50, "user", "mexico")
enemy = Character(50,50, "enemy", None)
wall = Wall("top")
keys = key.KeyStateHandler()
window.push_handlers(keys)

@window.event
def on_draw():
    window.clear()
    background.background.draw()
    char.character.draw()
    wall.wall.draw()

    x = randint(0,3)
    if choices[x] == "up":
        enemy.up(15)
    elif choices[x] == "down":
        enemy.down(15)
    elif choices[x] == "left":
        enemy.left(15)
    elif choices[x] == "right":
        enemy.right(15)
        
    enemy.character.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.W:    
        char.up(5)
    elif symbol == key.S:
        char.down(5)
    elif symbol == key.A:
        char.left(5)
    elif symbol == key.D:
        char.right(5)

@window.event
def on_key_release(symbol, modifiers):
    pass

pyglet.app.run()
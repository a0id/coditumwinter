import pyglet
from pyglet.window import key

class Character():
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy
        self.img = pyglet.image.load("guy.png")
        self.character = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)
    def up(self, velocity):
        self.y = self.y + velocity
        self.character.y = self.y
        
window = pyglet.window.Window()

char = Character(50, 50)

keys = key.KeyStateHandler()
window.push_handlers(keys)

@window.event
def on_draw():
    window.clear()
    char.character.draw()
    
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.W:
        char.up(20)
        
@window.event
def on_key_release(symbol, modifiers):
    pass

pyglet.app.run()
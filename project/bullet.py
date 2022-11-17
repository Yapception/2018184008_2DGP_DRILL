import random
from pico2d import *
import game_world


class Bullet:
    image = None

    def __init__(self, xPos, yPos, dir):
        if Bullet.image == None:
            Bullet.image = load_image('Character/Peashooter2.png')
        self.x, self.y, self.fall_speed, self.dir = xPos, yPos, 20 , dir

        self.frame = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 200, 100, 200, 100, self.x, self.y)
        else:
            self.image.clip_composite_draw(self.frame * 200, 100, 200, 100,
                                           3.141592 , '', self.x, self.y, 200, 100)

    def update(self):
        if self.dir == 1:
            self.x += self.fall_speed
        else:
            self.x -= self.fall_speed
        self.frame += (self.frame + 1) % 4
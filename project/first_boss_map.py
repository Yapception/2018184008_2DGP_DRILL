from pico2d import *

class First_boss_map:
    def __init__(self):
        self.image = load_image('Map/First_Map/ruse_of_an_ooze_background.png')

    def draw(self):
        self.image.draw(1280 // 2, 720 // 2)
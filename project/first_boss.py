from pico2d import *
import game_world
import game_framework

import math

t = 0
timer = 0

# Cuphead Run Speed
PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel = 30 cm
RUN_SPEED_KMPH = 15.0           # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Cuphead Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

RD, LD, RU, LU, Z, X = range(6)
event_name = ['RD', 'LD', 'RU', 'LU', 'Z', 'X']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_z): Z,
    (SDL_KEYDOWN, SDLK_x): X
}

class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 27

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(int(self.frame) * 393, 350 * 0, 393, 350, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * 393, 350 * 0, 393, 350, self.x, self.y)

next_state = {
    IDLE: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, Z: IDLE, X: IDLE}
}

import random

class Boss1:
    def __init__(self):
        self.x, self.y = 800, 200
        self.frame = random.randint(0, 5)
        self.dir, self.face_dir = 0, -1
        self.image = load_image('Boss/Goopy Le Grande/Phase 1/Intro/slime_intro_spritesheet2.png')
        self.font = load_font('font/ENCR10B.TTF', 16)

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.hp = 60

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f}),    dir: {self.dir}', (255, 255, 0))
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def handle_collision(self, other, group):
        if group == 'bullet:boss1':
            self.hp -= 1

    def get_bb(self):
        return self.x - 197, self.y - 175, self.x + 197, self.y + 175

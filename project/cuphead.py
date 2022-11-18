from pico2d import *
import game_world
import game_framework
from bullet import Bullet
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
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(int(self.frame) * 100, 150 * 1, 100, 150, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * 100, 150 * 0, 100, 150, self.x, self.y)

RunWav = None

class RUN:
    @staticmethod
    def enter(self, event):
        global RunWav
        print('ENTER RUN')
        # 방향을 결정해야 하는데, 뭘 근거로? 어떤 키가 눌렸기 때문에?
        # 키 이벤트 정보가 필요
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

        RunWav = load_wav('Sound/Player/player_land_ground_01.wav')
        RunWav.play()
    @staticmethod
    def exit(self, event):
        global RunWav
        print('EXIT RUN')
        self.face_dir = self.dir

        del RunWav

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        # x 좌표 변경, 달리기
        self.x += 10 * self.dir
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1280)
        delay(0.05)

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame) * 100, 150 * 3, 100, 150, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame) * 100, 150 * 2, 100, 150, self.x, self.y)


JumpWav = None


class JUMP:
    @staticmethod
    def enter(self, event):
        global JumpWav
        print('ENTER JUMP')
        # 방향을 결정해야 하는데, 뭘 근거로? 어떤 키가 눌렸기 때문에?
        # 키 이벤트 정보가 필요
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        else:
            self.dir = 0
        JumpWav = load_wav('Sound/Player/player_jump_01.wav')

    @staticmethod
    def exit(self, event):
        global JumpWav
        print('EXIT JUMP')
        del JumpWav

    @staticmethod
    def do(self):
        global t
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        # x 좌표 변경, 달리기

        self.x += 10 * self.dir
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        self.y = 200 + 80 * math.sin(math.pi * ((22.5 * t)/180))

        t = t + 1

        if t > 9:
            t = 0
            self.add_event(Z)

        JumpWav.play()
        delay(0.02)

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(int(self.frame) * 100, 150 * 7, 100, 150, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * 100, 150 * 6, 100, 150, self.x, self.y)

ShootSound = None

class SHOOT:
    @staticmethod
    def enter(self, event):
        global ShootSound
        print('ENTER Shoot')
        # 방향을 결정해야 하는데, 뭘 근거로? 어떤 키가 눌렸기 때문에?
        # 키 이벤트 정보가 필요
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        else:
            self.dir = 0
        ShootSound = load_wav('Sound/Player/player_default_fire_loop_01.wav')

    @staticmethod
    def exit(self, event):
        global ShootSound
        print('EXIT Shoot')
        del ShootSound

    @staticmethod
    def do(self):
        global timer
        global ShootSound
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        timer += 1
        if timer >= 3:
            timer = 0
            self.add_event(X)
            self.fire_bullet(self.x, self.y, self.face_dir)
        ShootSound.play()
        delay(0.03)

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(int(self.frame) * 100, 150 * 11, 100, 150, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * 100, 150 * 10, 100, 150, self.x, self.y)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, Z: JUMP, X: SHOOT},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, Z: JUMP, X: SHOOT},
    JUMP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, Z: IDLE},
    SHOOT: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, X: IDLE}
}

import random

class Cuphead:
    def __init__(self):
        self.x, self.y = 200, 200
        self.frame = random.randint(0, 5)
        self.dir, self.face_dir = 0, 1
        self.image = load_image('Character/character.png')
        self.font = load_font('font/ENCR10B.TTF', 16)

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.hp = 2

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
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f}),    dir: {self.dir} , (hp: {self.hp:.2f})', (255, 255, 0))
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 50, self.y - 75, self.x + 50, self.y + 75

    def handle_collision(self, other, group):
        if group == 'cuphead:boss1':
            self.hp -= 1

    def fire_bullet(self, xPos, yPos, dir):
        print('FIRE Bullet')
        bullet = Bullet(xPos, yPos, dir)
        game_world.add_object(bullet, 1)
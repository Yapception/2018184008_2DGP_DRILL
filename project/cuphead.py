from pico2d import *
import math

t = 0

RD, LD, RU, LU, Z = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_z): Z
}


class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0

    @staticmethod
    def exit(self):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 5
        delay(0.05)

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(self.frame * 100, 150 * 1, 100, 150, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 150 * 0, 100, 150, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
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

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        print('self.dir = ', self.dir)
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 16
        # x 좌표 변경, 달리기
        self.x += 10 * self.dir
        self.x = clamp(0, self.x, 1280)
        delay(0.05)

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 150 * 3, 100, 150, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 150 * 2, 100, 150, self.x, self.y)


class JUMP:
    @staticmethod
    def enter(self, event):
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

    @staticmethod
    def exit(self):
        print('EXIT JUMP')
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        global t
        self.frame = (self.frame + 1) % 8
        # x 좌표 변경, 달리기

        self.y = 200 + 80 * math.sin(math.pi * ((22.5 * t)/180))

        if self.dir != 0:
            self.x += 10 * self.dir
            self.x = clamp(0, self.x, 1280)

        t = t+1

        if t > 9:
            t = 0
            self.add_event(Z)

        delay(0.03)

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(self.frame * 100, 150 * 7, 100, 150, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 150 * 6, 100, 150, self.x, self.y)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, Z: JUMP},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, Z: JUMP},
    JUMP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, Z: IDLE},
}


class Cuphead:
    def __init__(self):
        self.x, self.y = 200, 200
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('Character/character.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
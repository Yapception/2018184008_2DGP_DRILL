from pico2d import *


WINDOW_WIDTH, WINDOW_HEIGHT = 1024, 576

def handle_events():
    global running
    global dir
    global state
    global BulletCount

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_z:
                state = 'JUMP'
            if event.key == SDLK_x:
                state = 'SHOOT'
                BulletCount += 1
            if event.key == SDLK_RIGHT:
                dir = 'RIGHT'
                state = 'STAND'
            elif event.key == SDLK_LEFT:
                dir = 'LEFT'
                state = 'STAND'
            elif event.key == SDLK_UP:
                dir = 'UP'
            elif event.key == SDLK_DOWN:
                state = 'DUCK'
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_x:
                state = 'IDLE'
            if event.key == SDLK_RIGHT:
                state = 'IDLE'
            elif event.key == SDLK_LEFT:
                state = 'IDLE'
            elif event.key == SDLK_UP:
                state = 'IDLE'
            elif event.key == SDLK_DOWN:
                state = 'IDLE'


class Tutorial:
    def __init__(self):
        self.image = load_image('Map/Tutorial/Drawing/tutorial_room_back_layer_0001.png')

    def draw(self):
        self.image.draw(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)


class Cuphead:
    def __init__(self):
        self.x, self.y = 200,200
        self.frame = 0
        self.image = load_image('Character/character.png')

    def update(self):
        global FirePosX, FirePosY
        global BulletCount
        if state == 'IDLE':
            self.frame = (self.frame + 1) % 5
            delay(0.1)
        elif state == 'STAND':
            self.frame = (self.frame + 1) % 16
            if dir == 'RIGHT':
                self.x += 10
            else:
                self.x -= 10
            delay(0.07)
        elif state == 'JUMP':
            if self.frame == 8:
                self.state = 'IDLE'
            self.frame = (self.frame + 1) % 8
            if dir == 'RIGHT':
                self.x += 3
                if self.frame < 4:
                    self.y += 30
                else:
                    self.y -= 30
            else:
                self.x -= 3
                if self.frame < 4:
                    self.y += 30
                else:
                    self.y -= 30
            delay(0.08)
        elif state == 'DUCK':
            self.frame = (self.frame + 1) % 7
            delay(0.08)
        elif state == 'SHOOT':
            FirePosX = self.x + 40
            FirePosY = self.y + 10
            print("[", BulletCount, "]FirePos - (x,y):",FirePosX,FirePosY)
            self.frame = (self.frame + 1) % 3
            delay(0.05)
    def draw(self):
        if dir == 'RIGHT':
            if state == 'IDLE':
                self.image.clip_draw(self.frame * 100, 150 * 0, 100, 150, self.x, self.y)
            elif state == 'STAND':
                self.image.clip_draw(self.frame * 100, 150 * 2, 100, 150, self.x, self.y)
            elif state == 'JUMP':
                self.image.clip_draw(self.frame * 100, 150 * 6, 100, 150, self.x, self.y)
            elif state == 'DUCK':
                self.image.clip_draw(self.frame * 130, 150 * 8, 130, 150, self.x, self.y)
            elif state == "SHOOT":
                self.image.clip_draw(self.frame * 100, 150 * 10, 100, 150, self.x, self.y)
        else:
            if state == 'IDLE':
                self.image.clip_draw(self.frame * 100, 150 * 1, 100, 150, self.x, self.y)
            elif state == 'STAND':
                self.image.clip_draw(self.frame * 100, 150 * 3, 100, 150, self.x, self.y)
            elif state == 'JUMP':
                self.image.clip_draw(self.frame * 100, 150 * 7, 100, 150, self.x, self.y)
            elif state == 'DUCK':
                self.image.clip_draw(self.frame * 130, 150 * 9, 130, 150, self.x, self.y)
            elif state == "SHOOT":
                self.image.clip_draw(self.frame * 100, 150 * 11, 100, 150, self.x, self.y)

class Bullet:
    def __init__(self):
        global FirePosX, FirePosY
        self.x, self.y = FirePosX, FirePosY
        self.BulletX, self.BulletY = 300, 200
        self.frame = 0
        self.frame2 = 0
        self.image = load_image('Character/Peashooter2.png')

    def update(self):
        if state == 'SHOOT':
            self.x, self.y = FirePosX, FirePosY
            print("Bullet - (x,y):", self.BulletX, self.BulletY)
            self.frame = (self.frame + 1)
            self.frame2 = (self.frame2 + 1) % 8
            self.BulletX += 50
            delay(0.05)

    def draw(self):
        if state == "SHOOT":
            self.image.clip_draw(self.frame * 100, 100 * 0, 100, 100, self.x, self.y)
            self.image.clip_draw(self.frame2 * 200, 100 * 1, 200, 100, self.BulletX, self.BulletY)


sx, sy = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
FirePosX, FirePosY = 0, 0
frame = 0
dir = 'RIGHT'
state = 'IDLE'
BulletCount = 0

cup = None
map = None
bullet = None
running = None

# 초기화
def enter():
    global cup, map, bullet, running
    cup = Cuphead()
    map = Tutorial()
    bullet = Bullet()
    # bullets = [Bullet() for n in range(1, BulletCount)]
    running = True
# 종료
def exit():
    # global cup, map, bullets
    global cup, map, bullet
    del cup
    del map
    del bullet
    # del bullets
def update():
    cup.update()
    # for bullet in bullets:
    #     bullet.update()
    bullet.update()
def draw():
    clear_canvas()
    map.draw()
    cup.draw()
    # for bullet in bullets:
    #     bullet.draw()
    bullet.draw()
    update_canvas()

pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)

enter()

while running:
    handle_events()
    update()
    draw()

exit()
close_canvas()
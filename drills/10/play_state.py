from boy_grass_object import *
import game_framework
import logo_state
import title_state
import item_state
import boy_adjust_state

# boy = None
# grass = None
# running = None

n = 1

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('run_animation.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 300, 0, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 200, 0, 100, 100, self.x, self.y)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x+10, self.y+50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x+10, self.y+50)

# 초기화
def enter():
    global boy, grass, running
    boy = Boy()
    global n

    # boy = [Boy() for n in range(1, n)]
    grass = Grass()
    running = True

# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.change_state(title_state)
                case pico2d.SDLK_i:
                    game_framework.push_state(item_state)
                case pico2d.SDLK_LEFT:
                    boy.dir -= 1
                case pico2d.SDLK_RIGHT:
                    boy.dir += 1
                case pico2d.SDLK_b:
                    game_framework.push_state(boy_adjust_state)

    delay(0.02)

def pause():
    pass

def resume():
    pass
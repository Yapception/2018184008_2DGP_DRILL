from pico2d import *
import random

# 잔디를 만드려면, 잔디 클래스가 필요
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



# 소년을 만드려면, 소년 클래스가 필요.
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

open_canvas()

grass = Grass() # 잔디 객체 생성
# boy = Boy() # 소년 객체 생성
team = [Boy() for i in range(11)] # 11명의 소년으로 구성된 팀.

running = True
while running:

    handle_events()

    # 시뮬레이션
    for boy in team:
        boy.update()

    # 렌더링 : 보여준다.
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)

del team
del grass

close_canvas()


# game main loop code

# finalization code
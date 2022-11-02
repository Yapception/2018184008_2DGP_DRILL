from pico2d import *
import game_framework
from grass import Grass
from boy import Boy

boy = None
grass = None

def handle_events():
    global boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_events(event)

# 초기화
def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw_world():
    grass.draw()
    boy.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

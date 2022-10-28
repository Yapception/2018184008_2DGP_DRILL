import pico2d

from boy_grass_object import *
import game_framework
import play_state

# 초기화
def enter():
    global boy, grass, running
    boy = Boy()
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
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    play_state.boy.item = None
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    play_state.boy.item = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    play_state.boy.item = 'BigBall'
                    game_framework.pop_state()

    delay(0.02)

def pause():
    pass

def resume():
    pass

def test_self():
    import item_state
    pico2d.open_canvas()
    game_framework.fill_states(play_state)
    game_framework.run(item_state)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()
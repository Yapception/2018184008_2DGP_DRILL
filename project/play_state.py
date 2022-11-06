from pico2d import *
import game_framework
from cuphead import Cuphead
from first_boss_map import First_boss_map

cuphead = None
first_boss_map = None


def enter():
    global cuphead, first_boss_map
    cuphead = Cuphead()
    first_boss_map = First_boss_map()


def exit():
    global cuphead, first_boss_map
    del cuphead
    del first_boss_map


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
        else:
            cuphead.handle_events(event)


def draw():
    clear_canvas()
    first_boss_map.draw()
    cuphead.draw()
    update_canvas()


def update():
    cuphead.update()
    pass


def pause():
    pass


def resume():
    pass

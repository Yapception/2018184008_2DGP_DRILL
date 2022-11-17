from pico2d import *
import game_framework
import game_world

from cuphead import Cuphead
from first_boss_map import First_boss_map
from bullet import Bullet

cuphead = None
first_boss_map = None

bullets = []

def enter():
    global cuphead, first_boss_map
    cuphead = Cuphead()
    first_boss_map = First_boss_map()

    game_world.add_object(first_boss_map, 0)
    game_world.add_object(cuphead, 1)

    # global bullets
    # bullets = [Bullet() for i in range(10)]
    # game_world.add_objects(bullets, 1)

def exit():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            cuphead.handle_events(event)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    pass


def pause():
    pass


def resume():
    pass

from pico2d import *
import game_framework
import game_world

import pause_state
from cuphead import Cuphead
from first_boss import FirstBoss
from first_boss_map import First_boss_map
from bullet import Bullet


cuphead = None
first_boss = None

first_boss_map = None

bullets = []

bgm = None

def enter():
    global cuphead, first_boss_map, first_boss
    cuphead = Cuphead()
    first_boss = FirstBoss()
    first_boss_map = First_boss_map()

    game_world.add_object(first_boss_map, 0)
    game_world.add_object(cuphead, 1)
    game_world.add_object(first_boss, 1)


    game_world.add_collision_pairs(cuphead, first_boss, 'cuphead:first_boss')
    game_world.add_collision_pairs(bullets, first_boss, 'bullet:first_boss')

    global bgm

    bgm = load_music('Sound/Goopy le Grande/Ruse Of An Ooze.mp3')
    bgm.repeat_play()
    bgm.set_volume(10)

    print("enter play_state")

    # global bullets
    # bullets = [Bullet() for i in range(10)]
    # game_world.add_objects(bullets, 1)


def exit():
    global bgm
    game_world.clear()
    print("exit play_state")
    del bgm


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            game_framework.push_state(pause_state)
        else:
            cuphead.handle_events(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


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

    if collide(cuphead, first_boss):
        print("COLLISION cuphead:first_boss")

    for a, b, group in game_world.all_collision_pair():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)
    pass


def pause():
    global bgm
    bgm.pause()
    print("pause")
    pass


def resume():
    global bgm
    bgm.resume()
    print("resume")
    pass

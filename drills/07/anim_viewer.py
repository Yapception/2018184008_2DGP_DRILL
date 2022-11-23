from pico2d import *
import math

open_canvas(1240,600)

grass = load_image('world1_large_island_main_01.png')
character = load_image('character.png')


def up_walk():
    frame = 0
    y = 0
    while (y < 600):
        clear_canvas()
        grass.draw(620, 0)
        character.clip_draw(frame * 103, 113*7, 103, 113, 300, y)
        update_canvas()
        frame = (frame + 1) % 16
        y += 5
        delay(0.05)
        get_events()

def right_up_walk():
    frame = 0
    x = 0
    y = 0
    while(x <800 and y < 600):
        clear_canvas()
        grass.draw(620, 0)
        character.clip_draw(frame * 103, 113*6, 103, 113, x, y)
        update_canvas()
        frame = (frame + 1) % 15
        x += 5
        y += 5
        delay(0.05)
        get_events()


def emotion():
    frame = 0
    for cnt in range(0,24,1):
        clear_canvas()
        grass.draw(620, 0)
        character.clip_draw(frame * 103, 113*5, 103, 113, 400, 300)
        update_canvas()
        frame = (frame + 1) % 6
        delay(0.1)
        get_events()

def right_walk():
    frame = 0
    x = 0
    while(x <800):
        clear_canvas()
        grass.draw(620, 0)
        character.clip_draw(frame * 103, 113*4, 103, 113, x, 50)
        update_canvas()
        frame = (frame + 1) % 14
        x += 5
        delay(0.05)
        get_events()

def right_down_walk():
    frame = 0
    x = 0
    y = 600
    while (x < 800 and y > 0):
        clear_canvas()
        grass.draw(620, 0)
        character.clip_draw(frame * 103, 113 * 3, 103, 113, x, y)
        update_canvas()
        frame = (frame + 1) % 15
        x += 5
        y -= 5
        delay(0.05)
        get_events()

def emotion2():
    frame = 0
    for cnt in range(0,32,1):
        clear_canvas()
        grass.draw(620, 0)
        character.clip_draw(frame * 103, 113 * 2, 103, 113, 400,300)
        update_canvas()
        frame = (frame + 1) % 9
        delay(0.1)
        get_events()

def down_walk():
    frame = 0
    y = 600
    while(y > 0):
        clear_canvas()
        grass.draw(620, 0)
        character.clip_draw(frame * 103, 113 * 1, 103, 113, 400, y)
        update_canvas()
        frame = (frame + 1) % 13
        y -= 5
        delay(0.05)
        get_events()

def emotion3():
    frame = 0
    for cnt in range(0, 40, 1):
        clear_canvas()
        grass.draw(620,0)
        character.clip_draw(frame * 103, 113 * 0, 103, 113, 400, 300)
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.1)
        get_events()



while True:
    up_walk()
    right_up_walk()
    emotion()
    right_walk()
    right_down_walk()
    emotion2()
    down_walk()
    emotion3()


close_canvas()
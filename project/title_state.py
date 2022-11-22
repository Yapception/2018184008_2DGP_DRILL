from pico2d import *
import game_framework

import play_state

image = None
title_music = None

title_frame = 0


def enter():
    global image
    global title_music
    image = load_image('title_screen/Background/Title_SpriteSheet.png')
    title_music = load_music('Sound/MainTheme/MainTheme.mp3')

    title_music.play()


def exit():
    global image, title_music

    del image
    del title_music


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(play_state)


def draw():
    global title_frame

    clear_canvas()
    image.clip_draw(title_frame* 498, 0, 498, 278, 1280//2, 720//2, 1280, 720)
    update_canvas()


def update():
    global title_frame

    image.clip_draw(title_frame* 498, 0, 498, 278, 1280//2, 720//2, 1280, 720)

    title_frame += 1

    if title_frame >= 21:
        title_frame = 0

    delay(0.056)
    pass


def pause():
    pass


def resume():
    pass

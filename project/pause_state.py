from pico2d import *
import game_framework

import play_state

image = None
PauseSound = None


def enter():
    global image
    global PauseSound
    image = load_image('UI/pause.png')
    PauseSound = load_music('Sound/MainTheme/MainTheme.mp3')

    PauseSound.play()


def exit():
    global image, PauseSound

    del image
    del PauseSound


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                game_framework.pop_state()


def draw():
    image.draw(1280 // 2, 720 // 2)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass

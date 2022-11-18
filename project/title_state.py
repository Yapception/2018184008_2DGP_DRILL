from pico2d import *
import game_framework

import play_state

image = None
titleSound = None

title_time = 0

def enter():
    global image
    global titleSound
    # image = load_image('title_screen/Background/title_sheet.png')
    image = load_image('title_screen/Background/title_screen_background.png')
    titleSound = load_music('Sound/MainTheme/MainTheme.mp3')

    titleSound.play()


def exit():
    global image, titleSound

    del image
    del titleSound


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
    global title_time

    clear_canvas()
    # image.clip_draw(title_time * 100 * 1280, 0, 1280, 720, 0, 0)
    image.draw(1280 // 2, 720 // 2)
    update_canvas()


def update():
    # global title_time
    # if title_time > 0.21:
    #     title_time = 0
    # delay(0.1)
    # title_time += 0.1
    pass


def pause():
    pass


def resume():
    pass

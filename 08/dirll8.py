from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir
    global temp

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir = 'RIGHT'
                temp = dir
            elif event.key == SDLK_LEFT:
                dir = 'LEFT'
                temp = dir
            elif event.key == SDLK_UP:
                dir = 'UP'
            elif event.key == SDLK_DOWN:
                dir = 'DOWN'
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir = 'IDLE'
            elif event.key == SDLK_LEFT:
                dir = 'IDLE'
            elif event.key == SDLK_UP:
                dir = 'IDLE'
            elif event.key == SDLK_DOWN:
                dir = 'IDLE'

open_canvas(TUK_WIDTH, TUK_HEIGHT)

# fill here
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = 'IDLE'
temp = 'LEFT'

while running:
    clear_canvas()
    kpu_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir == 'LEFT':
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        if 0 < x <= TUK_WIDTH and 0 <= y <= TUK_HEIGHT:
            x -= 5
    elif dir == 'RIGHT':
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        if 0 <= x < TUK_WIDTH and 0 <= y <= TUK_HEIGHT:
            x += 5
    elif dir == 'UP':
        if temp == 'LEFT':
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        elif temp == 'RIGHT':
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        if 0 <= x <= TUK_WIDTH and 0 <= y < TUK_HEIGHT:
            y += 5
    elif dir == 'DOWN':
        if temp == 'LEFT':
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        elif temp == 'RIGHT':
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        if 0 <= x <= TUK_WIDTH and 0 < y <= TUK_HEIGHT:
            y -= 5
    elif dir == 'IDLE':
        if temp == 'LEFT':
            character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
        elif temp == 'RIGHT':
            character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.01)

close_canvas()





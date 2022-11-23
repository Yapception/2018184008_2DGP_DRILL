from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(True):
    x = 400
    y = 90
    r = -90

    while (400 <= x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)
    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y)
        y = y + 2
        delay(0.01)
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x = x - 2
        delay(0.01)
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y = y - 2
        delay(0.01)
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)
        
    while (r < 270):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        
        x = 400 + 400 * math.cos(2 * math.pi * r/ 360)
        y = 300 + 210 * math.sin(2 * math.pi * r/ 360)
        r += 1
        delay(0.01)    
 
# fill here

close_canvas()

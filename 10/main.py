import pico2d
import logo_state

start_state = logo_state

pico2d.open_canvas()

start_state.enter()
while start_state.running:
    start_state.handle_events()
    start_state.update()
    start_state.draw()
exit()

pico2d.close_canvas()